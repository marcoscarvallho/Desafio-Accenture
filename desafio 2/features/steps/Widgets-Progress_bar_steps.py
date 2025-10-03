"""
Steps do BDD para Widgets - Progress Bar
"""
from behave import when, then
from config.widgets_config import VALIDATION


@when('eu clico no card "Widgets"')
def step_clico_widgets_card(context):
    """Clica no card Widgets"""
    context.widgets_main_page.click_widgets_card()


@then('devo ser redirecionado para a página de Widgets')
def step_redirecionado_widgets(context):
    """Verifica se foi redirecionado para a página de Widgets"""
    current_url = context.driver.current_url
    assert "widgets" in current_url.lower() or "progress-bar" in current_url.lower()


@when('eu clico no menu "Progress Bar"')
def step_clico_progress_bar(context):
    """Clica no menu Progress Bar"""
    context.widgets_main_page.click_progress_bar_menu()


@then('devo ser redirecionado para a página de Progress Bar')
def step_redirecionado_progress_bar(context):
    """Verifica se foi redirecionado para a página de Progress Bar"""
    current_url = context.driver.current_url
    assert "progress-bar" in current_url.lower()


@when('eu inicio e paro a barra antes de chegar aos 25%')
def step_inicio_e_paro_antes_25(context):
    """Para a barra antes de chegar aos 25%"""
    target = VALIDATION.get("target_stop_percentage", 20)
    max_percentage = VALIDATION["max_percentage_before_stop"]
    context.stopped_value = context.progress_bar_page.start_and_stop_before(
        target_percentage=target,
        max_percentage=max_percentage
    )


@then('o valor da progress bar deve ser menor ou igual a 25%')
def step_validar_menor_25(context):
    """Valida que o valor é menor ou igual a 25%"""
    max_percentage = VALIDATION["max_percentage_before_stop"]
    target = VALIDATION.get("target_stop_percentage", 20)
    
    # Valida que está dentro do limite máximo
    assert context.stopped_value <= max_percentage, \
        f"Progress bar parou em {context.stopped_value}%, esperado <= {max_percentage}%"
    
    # Certifica que realmente parou
    import time
    time.sleep(0.5)
    value_after_wait = context.progress_bar_page.get_progress_value()
    assert value_after_wait == context.stopped_value, \
        f"Progress bar não parou! Era {context.stopped_value}%, agora está {value_after_wait}%"
    
    # Verifica se ficou próximo do target (margem de erro de ±5%)
    if abs(context.stopped_value - target) <= 5:
        print(f"✅ PERFEITO: Parou em {context.stopped_value}% (target era {target}%)")
    else:
        print(f"⚠️  Parou em {context.stopped_value}% (target era {target}%, diferença de {abs(context.stopped_value - target)}%)")
    
    print(f"✅ Certificado: Barra realmente parou (não está andando)")


@when('eu clico no botão Start novamente')
def step_clico_start_novamente(context):
    """Clica no botão Start novamente (continua de onde parou)"""
    # Apenas armazena que vai continuar
    pass


@when('aguardo a barra chegar aos 100%')
def step_aguardo_100(context):
    """Aguarda a barra chegar aos 100%"""
    # Passa o valor de onde parou para validar que continuou
    context.final_value = context.progress_bar_page.start_and_wait_completion(
        continue_from_value=context.stopped_value
    )


@then('o valor da progress bar deve ser 100%')
def step_validar_100(context):
    """Valida que o valor é 100%"""
    assert context.final_value == 100, \
        f"Progress bar completou em {context.final_value}%, esperado 100%"
    
    # Valida também que a classe mudou para success
    progress_class = context.progress_bar_page.get_progress_class()
    assert "bg-success" in progress_class, \
        f"Progress bar não está com classe 'bg-success', classe atual: {progress_class}"
    
    print(f"✅ Progress bar completou em 100% com classe 'bg-success'")


@when('eu clico no botão Reset')
def step_clico_reset(context):
    """Clica no botão Reset"""
    context.progress_bar_page.click_reset()
    import time
    time.sleep(0.5)


@then('a progress bar deve voltar para 0%')
def step_validar_reset(context):
    """Valida que a barra voltou para 0%"""
    reset_value = context.progress_bar_page.get_progress_value()
    assert reset_value == 0, \
        f"Progress bar após reset: {reset_value}%, esperado 0%"
    
    # Valida que voltou para classe info
    progress_class = context.progress_bar_page.get_progress_class()
    assert "bg-info" in progress_class, \
        f"Progress bar não está com classe 'bg-info', classe atual: {progress_class}"
