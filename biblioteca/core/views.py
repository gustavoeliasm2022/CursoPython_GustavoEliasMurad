import json

from django.core.serializers import serialize
from django.http import HttpResponse
from rest_framework.status import *
from rest_framework.views import APIView
from datetime import datetime
from django.db import IntegrityError


from core.models import *


class AuthorView(APIView):

    def get(self, request, author_id=None):
        if author_id:
            if Author.objects.filter(pk=author_id).exists():
                author_response = Author.objects.filter(pk=author_id)  # QuerySet
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Author no Encontrado found'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            author_response = Author.objects.all()
        author_response = serialize('json', author_response)
        return HttpResponse(content_type='application/json',
                            content=author_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        author, created = Author.objects.get_or_create(**body)  # (director, created)
        if created:
            author.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Author creado con éxito',
                                                    'data': body}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Author ya existe'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, author_id):
        author = Author.objects.filter(pk=author_id)
        if not author.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Author no encontrado'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.datetime.now()
        # body['last_update'] = datetime.now()
        author.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Author actualizado con éxito'}),
                            status=HTTP_200_OK)

    def delete(self, request, author_id):
        author = Author.objects.filter(pk=author_id)
        if not author.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Author no encontrado'}),
                                status=HTTP_404_NOT_FOUND)
        author.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Author eliminado con exito'}),
                            status=HTTP_200_OK)


class PartnerView(APIView):

    def get(self, request, partner_id=None):
        if partner_id:
            if Partner.objects.filter(pk=partner_id).exists():
                partner_response = Partner.objects.filter(pk=partner_id)  # QuerySet
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Socio no Encontrado'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            partner_response = Partner.objects.all()
        partner_response = serialize('json', partner_response)
        return HttpResponse(content_type='application/json',
                            content=partner_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        partner, created = Partner.objects.get_or_create(**body)  # (partner, created)
        if created:
            partner.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Socio creado con éxito',
                                                    'data': body}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Socio ya existe'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, partner_id):
        partner = Partner.objects.filter(pk=partner_id)
        if not partner.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Socio no encontrado'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.datetime.now()
        # body['last_update'] = datetime.now()
        partner.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Socio actualizado con éxito'}),
                            status=HTTP_200_OK)

    def delete(self, request, partner_id):
        partner = Partner.objects.filter(pk=partner_id)
        if not partner.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Socio no encontrado'}),
                                status=HTTP_404_NOT_FOUND)
        partner.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Socio eliminado con exito'}),
                            status=HTTP_200_OK)


class AuthorViewWithOrm(APIView):

    def get(self, request):
        # Obtener registros cuyo nombre sea exactamente de alguna Autor existente
        # author = Author.objects.filter(last_name=author_last_name)
        # queryset_exact_field = list(Author.objects.filter(last_name=author))
        queryset_exact_field = list(Author.objects.filter(last_name="Alfaro"))
        queryset_exact_field = serialize('json', queryset_exact_field)
        # print(author_last_name)
        # print(author)
        response = {
            'exact_field': queryset_exact_field
        }
        return HttpResponse(content_type='application/json',
                            # content=json.dumps(response),
                            content=queryset_exact_field,
                            status=HTTP_200_OK)

class CatogoryViewWithOrm(APIView):

    def get(self, request):
        # Obtener registros cuyo nombre sea exactamente de alguna Categoria existente
        queryset_exact_field = list(Category.objects.filter(name="Novela"))
        queryset_exact_field = serialize('json', queryset_exact_field)
        response = {
            'exact_field': queryset_exact_field
        }
        return HttpResponse(content_type='application/json',
                            # content=json.dumps(response),
                            content=queryset_exact_field,
                            status=HTTP_200_OK)


class PartnerViewWithOrm(APIView):

    def get(self, request):
        # Obtener registros cuyo dni sea exactamente de algun Socio existente
        queryset_exact_field = list(Partner.objects.filter(dni="24217436"))
        queryset_exact_field = serialize('json', queryset_exact_field)
        response = {
            'exact_field': queryset_exact_field
        }
        return HttpResponse(content_type='application/json',
                            # content=json.dumps(response),
                            content=queryset_exact_field,
                            status=HTTP_200_OK)


class BookLoanView(APIView):

    def get(self, request, bookloan_id=None):
        if bookloan_id:
            if BookLoan.objects.filter(pk=bookloan_id).exists():
                bookloan_response = BookLoan.objects.filter(pk=bookloan_id)  # QuerySet
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Prestamo no encontrado'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            bookloan_response = BookLoan.objects.all()
        bookloan_response = serialize('json', bookloan_response)
        return HttpResponse(content_type='application/json',
                            content=bookloan_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        try:
            bookloan, created = BookLoan.objects.get_or_create(**body)
        except IntegrityError:
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Error actor_id/movie_id'}),
                                status=HTTP_400_BAD_REQUEST)
        if created:
            bookloan.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Prestamo creado con exito',
                                                    'data': body}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Prestamo ya existe'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, bookloan_id):
        bookloan = BookLoan.objects.filter(pk=bookloan_id)
        if not bookloan.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Prestamo no encontrado'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.datetime.now()
        bookloan.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Prestamo modificado con exito'}),
                            status=HTTP_200_OK)

    def delete(self, request, bookloan_id):
        bookloan = BookLoan.objects.filter(pk=bookloan_id)
        if not bookloan.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Prestamo no encontrado'}),
                                status=HTTP_404_NOT_FOUND)
        bookloan.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Prestamo eliminado con exito'}),
                            status=HTTP_200_OK)


class BookViewWithOrm(APIView):

    def get(self, request):
         # Trae todos los libros en las que el nombre del Autor sea "Gustavo"
        queryset_foreignkey_field = list(Book.objects.filter(author__first_name="Pili").values("name",
                                                                                              "category__name",
                                                                                              "author__last_name",
                                                                                               "author__first_name"))
        response = {
            'foreignkey_field': queryset_foreignkey_field
        }
        return HttpResponse(content_type='application/json',
                            # content=json.dumps(response),
                            content=queryset_foreignkey_field,
                            status=HTTP_200_OK)


class BookLoanViewWithOrm(APIView):

    def get(self, request):
         # Trae todos los prestamos en las que el estado sea "Prestado"
             queryset_exact_field = list(BookLoan.objects.filter(status="prestado"))
             queryset_exact_field = serialize('json', queryset_exact_field)
             response = {
                 'exact_field': queryset_exact_field
             }
             return HttpResponse(content_type='application/json',
                                 # content=json.dumps(response),
                                 content=queryset_exact_field,
                                 status=HTTP_200_OK)

class BookLoanViewDniSocioWithOrm(APIView):

    def get(self, request):
        # Trae todos los libros de un determinado socio, segun su dni
        queryset_foreignkey_field = list(BookLoan.objects.filter(partner__dni="24454598").values("partner__first_name",
                                                                                              "book__name"))
        response = {
                 'foreignkey_field': queryset_foreignkey_field
             }
        return HttpResponse(content_type='application/json',
                                 # content=json.dumps(response),
                                 content=queryset_foreignkey_field,
                                 status=HTTP_200_OK)


class CategoryView(APIView):

    def get(self, request, category_id=None):
        if category_id:
            if Category.objects.filter(pk=category_id).exists():
                category_response = Category.objects.filter(pk=category_id)  # QuerySet
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Categoria no Encontrada'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            category_response = Category.objects.all()
        category_response = serialize('json', category_response)
        return HttpResponse(content_type='application/json',
                            content=category_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        category, created = Category.objects.get_or_create(**body)  # (director, created)
        if created:
            category.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Categoria creada con éxito',
                                                    'data': body}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Categoria ya existe'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, category_id):
        category = Category.objects.filter(pk=category_id)
        if not category.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Categoria no encontrada'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.datetime.now()
        # body['last_update'] = datetime.now()
        category.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Categoria actualizada con éxito'}),
                            status=HTTP_200_OK)

    def delete(self, request, category_id):
        category = Category.objects.filter(pk=category_id)
        if not category.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Categoria no encontrada'}),
                                status=HTTP_404_NOT_FOUND)
        category.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Categoria eliminada con exito'}),
                            status=HTTP_200_OK)

class BookView(APIView):

    def get(self, request, book_id=None):
        if book_id:
            if Book.objects.filter(pk=book_id).exists():
                # book_response = Book.objects.get(pk=book_id)
                book_response = Book.objects.filter(pk=book_id)
            else:
                return HttpResponse(content_type='application/json',
                                    content=json.dumps({'detail': 'Libro no encontrado'}),
                                    status=HTTP_404_NOT_FOUND)
        else:
            book_response = list(Book.objects.all())
        book_response = serialize('json', book_response)
        return HttpResponse(content_type='application/json',
                            content=book_response,
                            status=HTTP_200_OK)

    def post(self, request):
        body = json.loads(request.body)
        body['author'] = Author.objects.get(pk=body['author'])
        body['category'] = Category.objects.get(pk=body['category'])
        book, created = Book.objects.get_or_create(**body)
        if created:
            book.save()
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Libro creado con exito'}),
                                status=HTTP_201_CREATED)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Libro ya existe'}),
                            status=HTTP_409_CONFLICT)

    def put(self, request, book_id):
        book = Book.objects.filter(pk=book_id)
        if not book.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Libro no encontrado'}),
                                status=HTTP_404_NOT_FOUND)
        body = json.loads(request.body)
        body['last_update'] = datetime.datetime.now()
        book.update(**body)
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Libro actualizado corractamente'}),
                            status=HTTP_200_OK)

    def delete(self, request, book_id):
        book = Book.objects.filter(pk=book_id)
        if not book.exists():
            return HttpResponse(content_type='application/json',
                                content=json.dumps({'detail': 'Libro no encontrado'}),
                                status=HTTP_404_NOT_FOUND)
        book.delete()
        return HttpResponse(content_type='application/json',
                            content=json.dumps({'detail': 'Libro eliminado con exito'}),
                            status=HTTP_200_OK)



