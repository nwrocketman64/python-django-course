from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat",
    "february": "Walk fir at least 20 minutes",
    "march": "Learn Django",
    "april": "Eat no meat",
    "may": "Walk fir at least 20 minutes",
    "june": "Learn Django",
    "july": "Eat no meat",
    "august": "Walk fir at least 20 minutes",
    "september": "Learn Django",
    "october": "Eat no meat",
    "november": "Walk fir at least 20 minutes",
    "december": "Learn Django",
}


# Create your views here.
def index(request):
    list_item = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_item += f"<li><a href=\"{month_path}\">{capitalized_month}</li>"

    response_data = "<ul>" + list_item + "</ul>"
    return HttpResponse(response_data)


def monthly_challege_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Month is not found")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
    except:
        return HttpResponseNotFound("Month is not found")
    return HttpResponse(response_data)
