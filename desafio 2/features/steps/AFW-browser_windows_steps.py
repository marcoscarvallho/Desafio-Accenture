"""
Steps do BDD para Alerts, Frame & Windows - Browser Windows
"""
from behave import when, then
from config.AFW_config import TEST_DATA


@when('eu clico no card "Alerts, Frame & Windows"')
def step_clico_afw_card(context):
    """Clica no card Alerts, Frame & Windows"""
    context.afw_main_page.click_afw_card()


@then('devo ser redirecionado para a página de AFW')
def step_redirecionado_afw(context):
    """Verifica se foi redirecionado para a página de AFW"""
    current_url = context.driver.current_url
    assert "alertsWindows" in current_url or "browser-windows" in current_url


@when('eu clico no menu "Browser Windows"')
def step_clico_browser_windows(context):
    """Clica no menu Browser Windows"""
    context.afw_main_page.click_browser_windows_menu()


@then('devo ser redirecionado para a página de Browser Windows')
def step_redirecionado_browser_windows(context):
    """Verifica se foi redirecionado para a página de Browser Windows"""
    current_url = context.driver.current_url
    assert "browser-windows" in current_url


@when('eu clico no botão "New Window"')
def step_clico_new_window(context):
    """Clica no botão New Window"""
    context.initial_window_count = context.browser_windows_page.get_window_count()
    context.browser_windows_page.click_new_window()


@then('uma nova janela deve ser aberta')
def step_nova_janela_aberta(context):
    """Verifica se uma nova janela foi aberta"""
    import time
    time.sleep(1)  # Aguarda a janela abrir
    
    current_window_count = context.browser_windows_page.get_window_count()
    assert current_window_count > context.initial_window_count, \
        f"Esperado mais de {context.initial_window_count} janelas, mas encontrado {current_window_count}"


@when('eu mudo para a nova janela')
def step_mudo_para_nova_janela(context):
    """Muda para a nova janela"""
    context.original_window = context.browser_windows_page.switch_to_new_window()


@then('devo ver a mensagem "This is a sample page"')
def step_ver_mensagem_sample(context):
    """Verifica se a mensagem correta está presente na nova janela"""
    message = context.browser_windows_page.get_sample_message()
    expected_message = TEST_DATA["expected_message"]
    
    assert message == expected_message, \
        f"Esperado '{expected_message}', mas encontrado '{message}'"


@when('eu fecho a nova janela')
def step_fecho_nova_janela(context):
    """Fecha a nova janela"""
    context.browser_windows_page.close_current_window()


@when('volto para a janela original')
def step_volto_janela_original(context):
    """Volta para a janela original"""
    context.browser_windows_page.switch_to_window(context.original_window)


@then('devo estar de volta na página de Browser Windows')
def step_volta_browser_windows(context):
    """Verifica se está de volta na página de Browser Windows"""
    current_url = context.driver.current_url
    assert "browser-windows" in current_url
    
    # Verifica se está na janela original
    window_count = context.browser_windows_page.get_window_count()
    assert window_count == context.initial_window_count, \
        f"Esperado {context.initial_window_count} janela(s), mas encontrado {window_count}"
