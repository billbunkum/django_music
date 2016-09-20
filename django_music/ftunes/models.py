from django.db import models

# Create your models here.
class Album(model.Models):
	name = models.CharField(max_length=50)
	artist = models.ForeignKey('Artist')
	genre = models.ForeignKey('Genre')

	def __str__(self):
		return "{}, {}, {}".format(self.name, self.artist, self.genre)

class Track(model.Models):
	name = models.CharField(max_length=50)
	album = models.ForeignKey('Album')

	def __str__(self):
		return self.name

class Artist(model.Models):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Genre(model.Models):
	CATEGORY_CHOICES = (
		('ALTERNATIVE', 'alternative'),
		('DISCO', 'disco'),
		('JAM_BAND', 'jam band'),
		('ROCK', 'rock'),
		('POP', 'pop'),
		('BAD', 'bad'),
		('GOOD', 'good'),
	)

	name = models.CharField(max_length=50, default=ALTERNATIVE, choices=CATEGORY_CHOICES)

	def __str__(self):
		return self.name