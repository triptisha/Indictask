from __future__ import unicode_literals
import frappe, os, json
from frappe.permissions import reset_perms

#Test Api
@frappe.whitelist(allow_guest=True)
def ping():
	return "pong"

#Create Api
@frappe.whitelist(allow_guest=True)
def create_movies(movie_name, popularity=None, director = None, production=None, description=None, imdb_score=None, cast=None, genre=None):
	movies_doc = frappe.new_doc("Movies")
	movies_doc.movie_name = movie_name
	movies_doc.popularity = popularity
	movies_doc.director = director
	movies_doc.production = production
	movies_doc.description = description
	movies_doc.imdb_score = imdb_score
	movies_doc.cast = cast
	movies_doc.genre = genre
	movies_doc.save()
	frappe.db.commit()
	return "movie is created"

#Read Api
@frappe.whitelist(allow_guest=True)
def get_movies():
	movie_list = frappe.db.sql("""select movie_name,popularity from tabMovies """,as_dict=1)
	return movie_list

#Update Api
@frappe.whitelist(allow_guest=True)
def update_movies(docname,movie_name,popularity=None):
	movies_doc = frappe.get_doc("Movies" , docname)
	movies_doc.movie_name = movie_name
	movies_doc.popularity = popularity
	movies_doc.save()
	frappe.db.commit()
	return "movie is updated"

# Delete Api
@frappe.whitelist(allow_guest=True)
def delete_movies(docname):
	movies_doc = frappe.delete_doc("Movies", docname)
	frappe.db.commit()
	return "movie is deleted"


# http://localhost:8080/api/method/movies.api.create_movies?movie_name=tripti
# http://localhost:8080/api/method/movies.api.get_movies
# http://localhost:8080/api/method/movies.api.update_movies?docname=MOV00002&&movie_name=test
# http://localhost:8080/api/method/movies.api.delete_movies?docname=MOV00001


