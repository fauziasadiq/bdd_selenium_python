
from behave import given, when, then
from pages.login_page import LoginPage
import time

@given("user navigates to login page")
def step_navigate(context):
    context.driver.get(context.config_data["base_url"])
    context.login_page = LoginPage(context.driver)

@when('user enters username "{username}" and password "{password}"')
def step_login(context, username, password):
    context.login_page.login(username, password)


@then("user should see dashboard")
def step_verify(context):
    context.login_page.is_dashboard_visible()

