import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Translation
from django.conf import settings
from .pipeline import slm_file
from .pipeline.file_highlighted_keyword import translate_file
from .config.parameters import update_target_language, update_target_language_filepath
from .config.path import input_txt_path, kannada_file_path, tamil_file_path


# Define a view for translation
def translate(request):
    if request.method == 'POST':
        # Get data from the form
        source_lang = request.POST.get('source_language')
        des_lang = request.POST.get('destination_language')
        content_type = request.POST.get('content_type')
        pipeline_choice = request.POST.get('pipeline_choice') # Get the pipeline choice from the POST data

        # Create a new translation object and save it to the database
        translation = Translation.objects.create(source_language=source_lang,
                                                 destination_language=des_lang,
                                                 content_type=content_type,
                                                 pipeline_choice=pipeline_choice)
        # Update the language settings
        if des_lang == 'ta':
            update_target_language('ta')
            update_target_language_filepath(tamil_file_path)
        elif des_lang == 'kn':
            update_target_language('kn')
            update_target_language_filepath(kannada_file_path)

        # Check the selected pipeline and content type
        if (content_type == 'file') and (pipeline_choice == 'slm'):
            # Handle the file translation using the slm package

            input_file_object = request.FILES.get('input_file')
            translation.input_file = input_file_object
            destination_folder_path = os.path.join(settings.MEDIA_ROOT, 'translated_files')
            translated_content_file_path = os.path.join(settings.MEDIA_ROOT, 'translated_files',
                                                        f'{translation.id}_translated.docx')

            # Create the translated file before passing it to slm_translate_content
            with open(translated_content_file_path, 'w') as file:
                pass

            # function call to invoke slm_translate_content
            slm_file.slm_translate_content(input_file_object, translated_content_file_path)
            translation.translated_file.name = translated_content_file_path
            translation.save()
            return redirect('success_page')  # Redirect to a success page

        elif (content_type == 'file') and (pipeline_choice == 'translate_file'):
            # Handle the file translation using the 'translate_file' pipeline
            input_file_object = request.FILES.get('input_file') # uploaded file object
            translation.input_file = input_file_object
            destination_file_path = os.path.join(settings.MEDIA_ROOT, 'translated_files')
            print("The Input File path is ", destination_file_path)

            # passing the input_file object instead of input_file
            destination_file_path = translate_file.translate_file(input_file_object,
                                                                  input_txt_path,
                                                                  destination_file_path)
            
            translation.translated_file.name = destination_file_path
            translation.save()
            print("outside the function")
            return redirect('success_page')  # Redirect to a success page

    context = {'translation': Translation}
    return render(request, 'translation_form.html', context)  # Render your template for the translation form


def success_page(request):
    return render(request, 'success_page.html')