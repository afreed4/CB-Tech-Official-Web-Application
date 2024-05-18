from django.shortcuts import render
from typing import Any, Dict

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import reverse
from django.views import generic


# Create your views here.
