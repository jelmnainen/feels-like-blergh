from django.shortcuts import render
import datetime

from .models import Stomach, Edible, Feeding

def get_default_context():
    return {
        "consistency_choices": Stomach._meta.get_field("consistency").choices,
        "bloodiness_choices": Stomach._meta.get_field("bloodiness").choices,
        "edibles": Edible.objects.all(),
    }

def home(request):
    return render(request, 'home.html', get_default_context())

def create_stomach_record(request):
    context = get_default_context()
    time = parseAgoTime(request)
    stomach = Stomach(
        time=time,
        consistency=request.POST["consistency"],
        bloodiness=request.POST["bloodiness"],
        comment=request.POST["comment"],
        user=request.user
        )
    if stomach.save():
        context["message"] = "Creation successful!"
    else:
        context["message"] = "Creation unsuccesful!"
    return render(request, 'home.html', context)

def create_edible_record(request):
    edible = Edible(name=request.POST['name'])
    context = get_default_context()
    try:
        edible.save()
        if 'ingredients' in request.POST:
            edible.ingredients.set(request.POST.getlist('ingredients'))
        context["message"] =  "Edible created!"
    except:
        context["message"] = "Edible creation unsuccessful"
    return render(request, 'home.html', context)

def create_feeding_record(request):
    context = get_default_context()
    if (set(['food', 'timestamp', 'ago-hours', 'ago-minutes']).issubset(request.POST)):
        time = parseAgoTime(request)
        food = request.POST.getlist('food')
        feeding = Feeding(timestamp=time, user=request.user)
        try:
            feeding.save()
            feeding.food.set(food)
            context["message"] = "New feeding created!"
        except:
            context["message"] = "Feeding creation unsuccesful"
    else:
        context["message"] = "Fill all fields!"
    return render(request, 'home.html', context)

def parseAgoTime(request):
        timestamp = (int)(request.POST['timestamp'])
        hours = (int)(request.POST['ago-hours'])
        minutes = (int)(request.POST['ago-minutes'])
        return (datetime.datetime.utcfromtimestamp(calculate_time(timestamp, hours, minutes)))

def calculate_time(timestamp, hours, minutes):
    min_ms = minutes * 60 * 1000
    hours_ms = hours * 60 *  60 * 1000
    return (timestamp - (min_ms + hours_ms))
