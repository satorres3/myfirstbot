"""Core data models for the hub application."""

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify


class Department(models.Model):
    """A simple department representation.

    This is a placeholder for the richer department model described in the
    project requirements. It can be extended via JSON schema definitions and
    related AI configuration.
    """

    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        get_user_model(), on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

