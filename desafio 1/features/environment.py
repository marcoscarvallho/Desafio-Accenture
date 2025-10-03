"""
Configuração do ambiente de testes com Behave
"""
from pages.account_api import AccountAPI
from pages.bookstore_api import BookStoreAPI
from config.config import TEST_USER


def before_all(context):
    context.account_api = AccountAPI()
    context.bookstore_api = BookStoreAPI()
    context.test_user = TEST_USER.copy()
    print("\nIniciando execucao dos testes...")


def before_scenario(context, scenario):
    context.response = None
    context.user_data = None
    context.token = None
    context.user_id = None
    context.books = None
    context.selected_isbns = []
    print(f"\n> Cenario: {scenario.name}")


def after_scenario(context, scenario):
    if scenario.status == "passed":
        print(f"[PASS] {scenario.name}")
    else:
        print(f"[FAIL] {scenario.name}")


def after_all(context):
    print("\nExecucao dos testes finalizada!")
