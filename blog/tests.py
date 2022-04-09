from django.test import TestCase
from django.test import SimpleTestCase
from .models import Project
import datetime
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
class SimpleUrlTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class ProjectModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', email='test@email.com', password='secret')
        self.project = Project.objects.create(title='just a test', date=datetime.date.today(), description='Dummy Description',
                                body='sample body', author=self.user )
        

    def test_text_content(self): # test if title in db matches the text
        project=Project.objects.get(id=1)
        expected_object_name = f'{project.title}'
        self.assertEqual(expected_object_name, 'just a test')

    def test_project_content(self): # test the contents of db
        self.assertEqual(f'{self.project.title}', 'just a test')
        self.assertEqual(f'{self.project.author}', 'testuser')
        self.assertEqual(f'{self.project.body}', 'sample body')
        self.assertEqual(f'{self.project.date}', f'{datetime.date.today()}')
        self.assertEqual(f'{self.project.description}', 'Dummy Description')

    def test_project_list_view(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dummy Description') # check if project actually displays on page body by checking for desc
        self.assertTemplateUsed(response, 'projects.html')

    def test_project_detail_view(self):
        response = self.client.get('/projects/1/')
        no_response = self.client.get('/projects/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'just a test')
        self.assertTemplateUsed(response, 'project_detail.html')

    def test_get_absolute_url(self): 
        self.assertEqual(self.project.get_absolute_url(), '/projects/1/')

    def test_project_create_view(self): 
        response = self.client.post(reverse('new_project'), {
        'title': 'New title',
        'body': 'New text',
        'description': 'Some Caption',
        'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302) # ensure that create operation results in a redirect (to new project)
        self.assertEqual(Project.objects.last().title, 'New title')
        self.assertEqual(Project.objects.last().body, 'New text')

    def test_project_update_view(self): 
        response = self.client.post(reverse('edit_project', args='1'), {
        'title': 'Updated title',
        'description': 'Updated description',
        'body': 'Updated text',
        })
        self.assertEqual(response.status_code, 302) # ensure that update operation results in a redirect (to updated project)

    def test_project_delete_view(self): 
        response = self.client.post(
        reverse('delete_project', args='1'))
        self.assertEqual(response.status_code, 302) # ensure that delete operation results in a redirect (to existing projects page)