from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None
}


# Create your views here.
def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })


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
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
