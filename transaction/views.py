from django.shortcuts import render


def upload(require):
    return render(require, 'upload.html')
