from django.db import models


class Assistant(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    object = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    name = models.CharField(max_length=1024)
    description = models.TextField(null=True)
    model = models.CharField(max_length=1024)
    instructions = models.TextField()
    tools = models.JSONField()
    metadata = models.JSONField()
    top_p = models.FloatField()
    temperature = models.FloatField()
    response_format = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class VectorStore(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    object = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    name = models.CharField(max_length=1024)
    bytes = models.IntegerField()
    file_counts = models.JSONField()

    def __str__(self):
        return self.name
