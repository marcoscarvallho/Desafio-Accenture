"""
Steps compartilhados entre diferentes testes
"""
from behave import given
from config.config import BASE_URL


@given('que eu estou na página inicial do DemoQA')
def step_estou_na_pagina_inicial(context):
    """Navega para a página inicial do DemoQA"""
    if hasattr(context, 'interactions_main_page'):
        context.interactions_main_page.navigate_to(BASE_URL)
    elif hasattr(context, 'widgets_main_page'):
        context.widgets_main_page.navigate_to(BASE_URL)
    elif hasattr(context, 'elements_main_page'):
        context.elements_main_page.navigate_to(BASE_URL)
    elif hasattr(context, 'afw_main_page'):
        context.afw_main_page.navigate_to(BASE_URL)
    elif hasattr(context, 'main_page'):
        context.main_page.navigate_to(BASE_URL)
    else:
        context.driver.get(BASE_URL)