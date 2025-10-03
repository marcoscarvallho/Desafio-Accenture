"""
Steps do BDD para o formulário de prática
"""
from behave import when, then
from selenium.webdriver.common.by import By


@when('eu clico no card "Forms"')
def step_clico_forms_card(context):
    """Clica no card Forms"""
    context.main_page.click_forms_card()


@then('devo ser redirecionado para a página de Forms')
def step_redirecionado_forms(context):
    """Verifica se foi redirecionado para a página de Forms"""
    import time
    time.sleep(2)
    current_url = context.driver.current_url
    assert "forms" in current_url.lower() or "practice-form" in current_url.lower()


@when('eu clico no menu "Practice Form"')
def step_clico_practice_form(context):
    """Clica no menu Practice Form"""
    context.main_page.click_practice_form_menu()


@then('devo ser redirecionado para a página do formulário')
def step_redirecionado_formulario(context):
    """Verifica se foi redirecionado para a página do formulário"""
    # Verifica se o campo firstName está presente
    first_name_field = context.practice_form_page.find_element(
        context.practice_form_page.first_name_locator
    )
    assert first_name_field is not None


@when('eu preencho todos os campos do formulário com dados válidos')
def step_preencho_formulario(context):
    """Preenche todos os campos do formulário em ordem linear com scroll otimizado"""
    context.practice_form_page.fill_complete_form(context.form_data)


@then('o formulário deve ser preenchido com sucesso')
def step_formulario_preenchido(context):
    """Verifica se o formulário foi preenchido corretamente"""
    # Verifica se os campos principais foram preenchidos
    first_name_field = context.practice_form_page.find_element(
        context.practice_form_page.first_name_locator
    )
    assert first_name_field.get_attribute("value") == context.form_data["first_name"]
    
    email_field = context.practice_form_page.find_element(
        context.practice_form_page.email_locator
    )
    assert email_field.get_attribute("value") == context.form_data["email"]


@when('eu submeto o formulário')
def step_submeto_formulario(context):
    """Submete o formulário"""
    context.practice_form_page.submit_form()


@then('deve aparecer um modal com os dados preenchidos')
def step_modal_aparece(context):
    """Verifica se o modal de resultado aparece"""
    assert context.practice_form_page.is_modal_open()


@when('eu verifico se os dados no modal estão corretos')
def step_verifico_dados_modal(context):
    """Extrai e armazena os dados do modal para verificação"""
    context.modal_data = context.practice_form_page.get_modal_data()


@then('os dados devem corresponder aos dados inseridos')
def step_dados_corretos(context):
    """Verifica se os dados do modal correspondem aos dados inseridos"""
    modal_data = context.modal_data
    
    # Verificar nome
    expected_name = f"{context.form_data['first_name']} {context.form_data['last_name']}"
    assert modal_data.get("Student Name") == expected_name
    
    # Verificar email
    assert modal_data.get("Student Email") == context.form_data["email"]
    
    # Verificar telefone
    assert modal_data.get("Mobile") == context.form_data["phone"]
    
    # Verificar gênero
    expected_gender = context.form_data["gender"].title()
    assert modal_data.get("Gender") == expected_gender
    
    # Verificar endereço
    assert modal_data.get("Address") == context.form_data["address"]
    
    # Verificar data de nascimento
    months = ["", "January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    expected_date = f"{context.form_data['birth_day']:02d} {months[context.form_data['birth_month']]},{context.form_data['birth_year']}"
    assert modal_data.get("Date of Birth") == expected_date


@when('eu fecho o modal')
def step_fecho_modal(context):
    """Fecha o modal de resultado"""
    context.practice_form_page.close_modal()


@then('o modal deve ser fechado e retornar ao formulário')
def step_modal_fechado(context):
    """Verifica se o modal foi fechado"""
    assert not context.practice_form_page.is_modal_open()
