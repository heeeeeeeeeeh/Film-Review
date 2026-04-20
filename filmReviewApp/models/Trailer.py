from django.db.models import CharField, IntegerField, Model


class Trailer(Model):
    trailer_url = CharField(max_length=200)
    img_src = CharField(max_length=200)
    img_alt = CharField(max_length=100)
    img_width = IntegerField()
    img_height = IntegerField()
    description = CharField()
    duration = CharField(10)
