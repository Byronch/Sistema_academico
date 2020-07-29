from django.http import HttpResponse
from django.shortcuts import render

# Create your views here

html_base = """
    <h1 class="text-center">Dr. Teodoro Maldonado Carbo</h1>
    <ul>
        <li>   <a href="/">PORTADA</a>              </li>
        <li>   <a href="/asistencia/"> Asistencia </a>   </li>
        <li>   <a href="/notas/"> Notas </a>     </li>
        <li>   <a href="/personal/"> Personal </a>     </li>
        <li>   <a href="/estudiantes/"> Estudiantes </a>     </li>
        <li>   <a href="/materias/"> Materias </a>     </li>
    </ul>
"""


def home(request):
    html_responsde = "<h1>La pagina de portada</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);

def notas(request):
    html_responsde = "<h1>La pagina de notas</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);

def asistencia(request):
    html_responsde = "<h1>la pagina de asistencias</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);

def personal(request):
    html_responsde = "<h1>La pagina de maestros</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);

def estudiantes(request):
    html_responsde = "<h1>La pagina de estudiantes</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);

def cursos(request):
    html_responsde = "<h1>La pagina de los cursos</h1>"
    html_responsde = html_base + html_responsde
    return HttpResponse(html_responsde);

def home(request, template="home.html"):
    return render(request, template);

def asistencia(request, template="asistencias.html"):
    return render(request, template);

def notas(request, template="notas.html"):
    return render(request, template);

def personal(request, template="personal.html"):
    return render(request, template);

def estudiantes(request, template="estudiantes.html"):
    return render(request, template);

def materias(request, template="materias.html"):
    return render(request, template);

def cursos(request, template="cursos.html"):
    return render(request, template);