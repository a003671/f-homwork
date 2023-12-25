from typing import Any, Callable
import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, ** kwargs)
    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, ** kwargs)
    return factory


# проверка получения первого курса
@pytest.mark.django_db
def test_get_course(client: APIClient, course_factory: Callable[..., Any]):
    #arrange
    course = course_factory(_quantity=10)
    #act
    response = client.get('/api/v1/courses/')
    #assert
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == course[0].id
   

# проверка получения списка курсов.
@pytest.mark.django_db
def test_list_get_course(client: APIClient, course_factory: Callable[..., Any]):
    course = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(course)
  

# проверка фильтрации списка курсов по id.
@pytest.mark.django_db
def test_filterid_list_course(client: APIClient, course_factory: Callable[..., Any]):
    course = course_factory(_quantity=10)[5].id
    response = client.get('/api/v1/courses/', {'id': F'{course}'})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['id'] == course



# проверка фильтрации списка курсов по name.
@pytest.mark.django_db
def test_filtername_list_course(client: APIClient, course_factory: Callable[..., Any]):
    course = course_factory(_quantity=10)[3].name
    response = client.get('/api/v1/courses/', {'name': F'{course}'})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['name'] == course


# тест успешного создания курса
@pytest.mark.django_db
def test_create_course(client: APIClient):
    response = client.post('/api/v1/courses/', data={'name': 'SQL Postgres'})
    assert response.status_code == 201
    data = response.json()
    assert data['name'] == 'SQL Postgres'


# тест успешного обновления курса
@pytest.mark.django_db
def test_update_course(client: APIClient, course_factory: Callable[..., Any]):
    course = course_factory(_quantity=1)
    response = client.patch(F'/api/v1/courses/{course[0].id}/', data={'name': 'SQL Postgres'})
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'SQL Postgres'


# тест успешного удаления курса
@pytest.mark.django_db
def test_del_course(client: APIClient, course_factory: Callable[..., Any]):
    course = course_factory(_quantity=1)
    response = client.delete(F'/api/v1/courses/{course[0].id}/')
    assert response.status_code == 204


# проверка успешного добавления студентов на курс.
@pytest.mark.django_db
def test_student_course(client: APIClient, course_factory: Callable[..., Any], student_factory: Callable[..., Any]):
    course = course_factory(_quantity=1)[0]
    students = student_factory(_quantity=10)
    course.students.add(*students)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data[0]['students']) == 10