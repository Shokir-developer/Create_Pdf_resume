from django.shortcuts import render, redirect

from .models import PdfModel
from .forms import PdfForm

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def formFill(request):
    form = PdfForm()
    if request.method == 'POST':
        form = PdfForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('pdf/')

    context = {'form': form}
    return render(request, 'index.html', context)


def render_pdf_view(request):

    template_path = 'base.html'
    person = PdfModel.objects.latest('id')
    skills = str(person.skills)
    skillar = skills.split(",")

    

    title = str(person)
    context = {'person': person, 'skillar':skillar}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    #yuklab oladi
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    #agar attachmentni o'chirsak brauzerda ko'rsatadi
    response['Content-Disposition'] = f'filename="{title}.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response