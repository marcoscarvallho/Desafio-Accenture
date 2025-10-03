"""
Steps do BDD para Elements - Web Tables
"""
from behave import when, then
from features.environment import generate_random_record


@when('eu clico no card "Elements"')
def step_clico_elements_card(context):
    """Clica no card Elements"""
    context.elements_main_page.click_elements_card()


@then('devo ser redirecionado para a página de Elements')
def step_redirecionado_elements(context):
    """Verifica se foi redirecionado para a página de Elements"""
    current_url = context.driver.current_url
    assert "elements" in current_url.lower() or "webtables" in current_url.lower()


@when('eu clico no menu "Web Tables"')
def step_clico_web_tables(context):
    """Clica no menu Web Tables"""
    context.elements_main_page.click_web_tables_menu()


@then('devo ser redirecionado para a página de Web Tables')
def step_redirecionado_web_tables(context):
    """Verifica se foi redirecionado para a página de Web Tables"""
    current_url = context.driver.current_url
    assert "webtables" in current_url.lower()


# Steps para criar e deletar 12 registros
@when('eu crio 12 novos registros dinamicamente')
def step_crio_12_registros(context):
    """Cria 12 registros dinamicamente"""
    context.created_records = []
    
    for i in range(12):
        record = generate_random_record()
        context.web_tables_page.create_record(record)
        context.created_records.append(record)


@then('todos os 12 registros devem aparecer na tabela')
def step_12_registros_aparecem(context):
    """Verifica se todos os 12 registros aparecem na tabela"""
    for record in context.created_records:
        is_visible = context.web_tables_page.is_record_visible(record["email"])
        assert is_visible, f"Registro {record['email']} não foi encontrado na tabela"


@when('eu deleto todos os 12 registros criados')
@then('eu deleto todos os 12 registros criados')
def step_deleto_12_registros(context):
    """Deleta todos os 12 registros criados"""
    for record in context.created_records:
        context.web_tables_page.delete_record(record["email"])


@then('nenhum dos 12 registros deve aparecer na tabela')
def step_12_registros_nao_aparecem(context):
    """Verifica se nenhum dos 12 registros aparece na tabela"""
    for record in context.created_records:
        is_visible = context.web_tables_page.is_record_visible(record["email"])
        assert not is_visible, f"Registro {record['email']} ainda está visível na tabela após deletar"
