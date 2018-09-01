from django.shortcuts import render
import datetime

from .models import Stomach

def get_default_context():
    return {
        "consistency_choices": Stomach._meta.get_field("consistency").choices,
        "bloodiness_choices": Stomach._meta.get_field("bloodiness").choices,
    }

def home(request):

    return render(request, 'home.html', get_default_context())

def create_stomach_record(request):
    context = get_default_context()
    timestamp = (int)(request.POST['timestamp'])
    hours = (int)(request.POST['ago-hours'])
    minutes = (int)(request.POST['ago-minutes'])
    print(hours, minutes, timestamp, calculate_time(timestamp, hours, minutes))
    time = datetime.datetime.utcfromtimestamp(calculate_time(timestamp, hours, minutes))
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


def calculate_time(timestamp, hours, minutes):
    min_ms = minutes * 60 * 1000
    hours_ms = hours * 60 *  60 * 1000
    return (timestamp - (min_ms + hours_ms))
