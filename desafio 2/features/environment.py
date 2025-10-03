"""
Configuração do ambiente de testes com Behave para automação web
"""
import random
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from pages.main_page import MainPage
from pages.practice_form_page import PracticeFormPage
from pages.AFW_main_page import AFWMainPage
from pages.browser_windows_page import BrowserWindowsPage
from pages.elements_main_page import ElementsMainPage
from pages.web_tables_page import WebTablesPage
from pages.widgets_main_page import WidgetsMainPage
from pages.progress_bar_page import ProgressBarPage
from pages.interactions_main_page import InteractionsMainPage
from pages.sortable_page import SortablePage
from config.config import DRIVER_CONFIG
from config.AFW_config import DRIVER_CONFIG as AFW_DRIVER_CONFIG


def generate_random_person():
    """Gera dados pessoais aleatórios (nome, sobrenome, email, idade)"""
    first_names = ["Ana", "Joao", "Maria", "Pedro", "Carla", "Lucas", "Fernanda", "Rafael", "Camila", "Diego"]
    last_names = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", "Pereira", "Lima", "Gomes"]
    
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    
    # Gera email único com número aleatório
    random_number = random.randint(1, 999)
    email = f"{first_name.lower()}.{last_name.lower()}{random_number}@test.com"
    
    # Gera idade aleatória
    age = random.randint(20, 60)
    
    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "age": age
    }


def generate_random_data():
    """Gera dados aleatórios completos para o formulário Practice Form"""
    person = generate_random_person()
    
    # Gera número de telefone aleatório (limite de 10 dígitos)
    phone = f"{random.randint(1000000000, 9999999999)}"
    
    # Gera data de nascimento aleatória (entre 18 e 65 anos)
    current_year = 2025
    birth_year = random.randint(current_year - 65, current_year - 18)
    birth_month = random.randint(1, 12)
    birth_day = random.randint(1, 28)
    
    # Gera endereço aleatório
    streets = ["Rua das Flores", "Avenida Central", "Rua do Comércio", "Avenida Paulista", "Rua da Paz"]
    street = random.choice(streets)
    number = random.randint(1, 9999)
    address = f"{street}, {number}"
    
    # Gera dados aleatórios para hobbies e subjects
    hobbies_options = ["sports", "reading", "music"]
    selected_hobbies = random.sample(hobbies_options, random.randint(1, 3))
    
    subjects_options = ["English", "Physics", "Chemistry", "Maths", "Accounting", "Arts"]
    selected_subjects = random.sample(subjects_options, random.randint(1, 3))
    
    gender_options = ["male", "female", "other"]
    selected_gender = random.choice(gender_options)
    
    return {
        "first_name": person["first_name"],
        "last_name": person["last_name"],
        "email": person["email"],
        "phone": phone,
        "birth_year": birth_year,
        "birth_month": birth_month,
        "birth_day": birth_day,
        "address": address,
        "hobbies": selected_hobbies,
        "subjects": selected_subjects,
        "gender": selected_gender
    }


def generate_random_record():
    """Gera dados aleatórios para um registro da Web Table"""
    person = generate_random_person()
    
    departments = ["Engineering", "Sales", "Marketing", "HR", "IT", "Finance", "Operations", "Legal", "Support", "Research"]
    salary = random.randint(3000, 15000)
    department = random.choice(departments)
    
    return {
        "first_name": person["first_name"],
        "last_name": person["last_name"],
        "email": person["email"],
        "age": person["age"],
        "salary": salary,
        "department": department
    }


def before_all(context):
    """Configuração inicial antes de todos os testes"""
    # Configuração do driver
    options = Options()
    # options.add_argument("--headless")  # modo sem interface gráfica
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    context.driver = webdriver.Firefox(options=options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(DRIVER_CONFIG["implicit_wait"])
    context.driver.set_page_load_timeout(DRIVER_CONFIG["page_load_timeout"])
    
    # Inicializar page objects - Forms
    context.main_page = MainPage(context.driver)
    context.practice_form_page = PracticeFormPage(context.driver)
    
    # Inicializar page objects - AFW
    context.afw_main_page = AFWMainPage(context.driver)
    context.browser_windows_page = BrowserWindowsPage(context.driver)
    
    # Inicializar page objects - Elements
    context.elements_main_page = ElementsMainPage(context.driver)
    context.web_tables_page = WebTablesPage(context.driver)
    
    # Inicializar page objects - Widgets
    context.widgets_main_page = WidgetsMainPage(context.driver)
    context.progress_bar_page = ProgressBarPage(context.driver)
    
    # Inicializar page objects - Interactions
    context.interactions_main_page = InteractionsMainPage(context.driver)
    context.sortable_page = SortablePage(context.driver)
    
    # Gerar dados aleatórios (apenas para teste de formulário)
    context.form_data = generate_random_data()
    
    print(f"Dados gerados: {context.form_data['first_name']} {context.form_data['last_name']} - {context.form_data['email']}")


def after_step(context, step):
    """Executado após cada step - útil para debug"""
    if step.status == "failed":
        print(f"ERRO no step: {step.name}")
        print(f"URL atual: {context.driver.current_url}")
        # Salvar screenshot em caso de erro
        try:
            context.driver.save_screenshot(f"erro_step_{step.name.replace(' ', '_')}.png")
            print("Screenshot salvo para debug")
        except:
            pass


def before_scenario(context, scenario):
    """Configuração antes de cada cenário"""
    print(f"\n> Cenario: {scenario.name}")


def after_scenario(context, scenario):
    """Configuração após cada cenário"""
    if scenario.status == "passed":
        print(f"[PASS] {scenario.name}")
    else:
        print(f"[FAIL] {scenario.name}")


def after_all(context):
    """Limpeza final após todos os testes"""
    if hasattr(context, 'driver'):
        context.driver.quit()
    print("\nExecucao dos testes finalizada!")
