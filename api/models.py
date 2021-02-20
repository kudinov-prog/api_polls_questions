from django.db import models
from django.contrib.auth import get_user_model
import datetime


User = get_user_model()


class Choice(models.Model):
    question = models.ForeignKey(
        'Question', related_name='choices_question',on_delete=models.CASCADE
    )
    text = models.CharField(
        max_length=256
    )


class Question(models.Model):
    TEXT = 'TEXT'
    CHOICE = 'CHOICE'
    MULTICHOICE = 'MULTICHOICE'

    CHOICES = (
        (TEXT, 'TEXT'),
        (CHOICE, 'CHOICE'),
        (MULTICHOICE, 'MULTICHOICE'),
    )

    text = models.CharField(
        max_length=1024
    )
    question_type = models.CharField(
        max_length=32, choices=CHOICES
    )

    def __str__(self):
        return self.text


class Poll(models.Model):
    name = models.CharField(
        max_length=200
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    finished = models.DateTimeField(
        blank=True
    )
    description = models.TextField(
        max_length=4096
    )
    #questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name


class Vote(models.Model):
    poll = models.ForeignKey(
        Poll, related_name='votes_poll', on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, related_name='votes_user', on_delete=models.CASCADE,
        blank=True, null=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )


class Answer(models.Model):
    question = models.ForeignKey(
        Question, related_name='answers_question', on_delete=models.CASCADE
    )
    vote = models.ForeignKey(
        Vote, related_name='answers_vote', on_delete=models.CASCADE
    )
    choice = models.ForeignKey(
        Choice, related_name='answers_choice', on_delete=models.CASCADE
    )
    value = models.CharField(
        max_length=512, blank=True, null=True
    )

    def __str__(self):
        return self.value
