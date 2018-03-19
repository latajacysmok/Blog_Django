from django.test import TestCase
from blog.models import Tag
from django.urls import reverse
from selenium import webdriver
from django.urls.exceptions import NoReverseMatch
from selenium.webdriver.support.ui import Select
import time 

# Create your tests here.

WELCOME_TEXT = 'Najnowsze posty na naszej stronie'

class ModelsTest(TestCase):

	def create_tag(self, name):
		return Tag.objects.create(name=name)

	def test_tag_creation(self):
		tag = self.create_tag("Sport")
		self.assertTrue(isinstance(tag, Tag))
		self.assertEqual(tag.name, "Sport")
		self.assertEqual(tag.__str__(), "Sport")

		tag = Tag.objects.get(name="Sport")
		self.assertEqual(tag.name, "Sport")
		

class ViewsTest(TestCase):

	def test_index_view(self):
		url = reverse("index")
		request = self.client.get(url)

		self.assertEqual(request.status_code, 200)
		with self.assertRaises(NoReverseMatch):
			reverse("abba")


class SignupTest(TestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.hostname = "http://127.0.0.1:8000"
		self.successText = 'Account created successfully'
		self.successTextUserAlreadyRegistered = 'Użytkownik o tej nazwie już istnieje.'

	# def test_sign_up(self):
	# 	url = reverse("index")
	# 	self.driver.get(self.hostname + url)
	# 	self.driver.find_element_by_xpath('//div[@id="wrapper"]/div[@id="menu"]/ul/li[3]/a').click()
	# 	self.driver.find_element_by_id('id_username').send_keys('testSelenium')
	# 	self.driver.find_element_by_id('id_email').send_keys('testSelenium@gmail.com')
	# 	self.driver.find_element_by_id('id_password1').send_keys('qwerty12345')
	# 	self.driver.find_element_by_id('id_password2').send_keys('qwerty12345')
	# 	self.driver.find_element_by_id('submit_register').click()
	# 	time.sleep(4)
	# 	page = self.driver.page_source
	# 	self.assertIn(WELCOME_TEXT, page)

	def login(self):
		url = reverse("index")
		self.driver.get(self.hostname + url)
		self.driver.find_element_by_xpath('//div[@id="wrapper"]/div[@id="menu"]/ul/li[2]/a').click()
		self.driver.find_element_by_id('id_username').send_keys('testSelenium')
		self.driver.find_element_by_id('id_password').send_keys('qwerty12345')
		self.driver.find_element_by_id('submit_login').click()

	# def test_login(self):
	# 	self.login()
	# 	time.sleep(4)
	# 	page = self.driver.page_source
	# 	self.assertIn(WELCOME_TEXT, page)

	def test_add_post(self):
		self.login()
		url = reverse("index")
		self.driver.get(self.hostname + url)
		self.driver.find_element_by_xpath('//div[@id="wrapper"]/div[@id="menu"]/ul/li[2]/a').click()
		self.driver.find_element_by_id('id_title').send_keys('Post made by Selenium')
		self.driver.find_element_by_id('id_content').send_keys("czesc, jestem wyslany z selenium!")
		select_tag = Select(self.driver.find_element_by_id('id_tags'))
		select_tag.select_by_value("2");
		self.driver.find_element_by_xpath('//form//button[@type="submit"]').click()
		time.sleep(4)

	def tearDown(self):
		self.driver.quit()