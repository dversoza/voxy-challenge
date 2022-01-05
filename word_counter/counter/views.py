from django.shortcuts import render

from .forms import TextForm

from .services.word_counter import WordCounterService


def index(request):
    context = {"form": TextForm(initial=request.POST)}

    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            form_text = request.POST.get("text_input")
            context["word_count"] = WordCounterService.count_words(form_text)
        else:
            for field, _ in form.errors.items():
                form.fields[field].widget.attrs.update({"class": "invalid"})
            context["form"] = form

    return render(request, "index.html", context)
