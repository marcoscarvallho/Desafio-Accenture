"""
Steps do BDD para Interactions - Sortable
"""
from behave import when, then
from config.interactions_config import EXPECTED_ORDER


@when('eu clico no card "Interactions"')
def step_clico_interactions_card(context):
    """Clica no card Interactions"""
    context.interactions_main_page.click_interactions_card()


@then('devo ser redirecionado para a página de Interactions')
def step_redirecionado_interactions(context):
    """Verifica se foi redirecionado para a página de Interactions"""
    current_url = context.driver.current_url
    assert "interaction" in current_url.lower() or "sortable" in current_url.lower()


@when('eu clico no menu "Sortable"')
def step_clico_sortable(context):
    """Clica no menu Sortable"""
    context.interactions_main_page.click_sortable_menu()


@then('devo ser redirecionado para a página de Sortable')
def step_redirecionado_sortable(context):
    """Verifica se foi redirecionado para a página de Sortable"""
    current_url = context.driver.current_url
    assert "sortable" in current_url.lower()


@when('eu ordeno os elementos em ordem decrescente')
def step_ordeno_elementos(context):
    """Ordena os elementos em ordem decrescente usando drag and drop"""
    # Captura a ordem inicial
    initial_order = context.sortable_page.get_current_order()
    print(f"\n📋 Ordem inicial: {', '.join(initial_order)}")
    
    # Executa a ordenação
    success = context.sortable_page.sort_to_descending_order()
    
    assert success, "Falha ao ordenar os elementos"


@then('os elementos devem estar na ordem: Six, Five, Four, Three, Two, One')
def step_validar_ordem(context):
    """Valida que os elementos estão na ordem esperada (decrescente)"""
    import time
    time.sleep(0.5)  # Aguarda estabilizar
    
    current_order = context.sortable_page.get_current_order()
    expected = EXPECTED_ORDER
    
    print(f"\n✅ Ordem final: {', '.join(current_order)}")
    print(f"🎯 Esperado: {', '.join(expected)}")
    
    # Valida cada posição
    for i, (current, exp) in enumerate(zip(current_order, expected)):
        assert current == exp, \
            f"Posição {i}: esperado '{exp}', encontrado '{current}'"
    
    print("✅ Todos os elementos estão na ordem decrescente correta!")
