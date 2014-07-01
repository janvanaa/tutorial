"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import RequestFactory
from django.test import LiveServerTestCase
from contacts.models import Contact
from selenium.webdriver.firefox.webdriver import WebDriver
from .views import ContactListView
class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
        
class ContactTests(TestCase):
    def test_str(self):
        c = Contact(first_name = 'John', last_name = 'Smith')
        self.assertEqual(str(c), 'John Smith')
    

class ContactListViewTests(TestCase):    
    def test_no_ontacts_in_context(self):
        factory = RequestFactory()
        request = factory.get('/') 
        response = ContactListView.as_view()(request)
        self.assertEquals(
            list(response.context_data['object_list']),
            [],
        )
        
    def test_contacts_in_context(self):
        factory = RequestFactory()
        request = factory.get('/')
        c = Contact.objects.create(first_name='John',last_name='Smith',email='john@smith.com')
        response = ContactListView.as_view()(request)
        self.assertEquals(
            list(response.context_data['object_list']),
            [c],
        )
        
class CreateContactIntegrationTest(LiveServerTestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(CreateContactIntegrationTest, cls).setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(CreateContactIntegrationTest, cls).tearDownClass()
    
    def test_add_contact(self):
        self.selenium.get('%s/new' % (self.live_server_url,))
        self.selenium.find_element_by_id('id_first_name').send_keys('John')
        self.selenium.find_element_by_id('id_last_name').send_keys('Smith')
        self.selenium.find_element_by_id('id_email').send_keys('john@smith.nl')
        self.selenium.find_element_by_xpath("//input[@type='submit']").click()
        self.assertEqual(Contact.objects.all()[0].first_name, 'John')