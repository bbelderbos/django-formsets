from django.forms.models import modelformset_factory
from django.shortcuts import render

from .forms import BookForm
from .models import Book


def home(request):
    BookFormSet = modelformset_factory(
        Book, BookForm, extra=3)
    formset = BookFormSet(request.POST or None)

    # print formset data if it is valid
    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)
        formset.save()

    context = {'formset': formset}
    return render(request, "home.html", context)
