from behave import given, when, then
from selenium import webdriver

@given('I have a web browser')
def step_given_web_browser(context):
    context.browser = webdriver.Chrome()

@when('I open a website')
def step_when_open_website(context):
    context.browser.get('http://example.com')

@then('I should see the title')
def step_then_see_title(context):
    assert "Example Domain" in context.browser.title
    context.browser.quit()
