from django.db import models


class Translation(models.Model):
    # Choices for source language (e.g., English)
    SOURCE_CHOICES = (
        ('en', 'English'),
        # Add more languages as needed
    )

    # Choice for destination languages (e.g., Tamil, Kannada)
    DESTINATION_CHOICES = (
        ('ta', 'Tamil'),
        ('kn', 'Kannada')
        # Add more languages as needed
    )

    # Choices for content types (e.g., text, Youtube URL, file)
    TYPE_CHOICES = (
        ('file', 'File'),
        # Add more choices as needed
    )

    # Choice for pipelines (e.g,. SLM, Translate File Highlighted Keywords, Translate Folder Highlighted
    PIPELINE_CHOICES = (
        ('slm', 'SLM'),
        ('translate_file', 'Translate File Highlighted Keywords'),
        # Add more pipeline choices as needed
    )

    source_language = models.CharField(max_length=2, choices=SOURCE_CHOICES)
    destination_language = models.CharField(max_length=2, choices=DESTINATION_CHOICES)
    content_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    input_file = models.FileField(upload_to='input_files/', null=True, blank=False)  # Store input files here
    translated_file = models.FileField(upload_to='translated_files/',
                                       blank=True, null=True)  # Store translated files here
    pipeline_choice = models.CharField(max_length=20, choices=PIPELINE_CHOICES,
                                       default='slm')  # New pipeline choice field

    # Add other fields as necessary, e.g., for uploaded files

    def __str__(self):
        return f'{self.get_content_type_display()} - {self.source_language} to {self.destination_language}'
