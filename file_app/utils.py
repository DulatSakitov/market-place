from . import models


def save_file(file_object, file_type, product=None):
    instance = models.File.objects.create(file=file_object,
                                          type=file_type,
                                          product=product
                                          )
    return instance.id

