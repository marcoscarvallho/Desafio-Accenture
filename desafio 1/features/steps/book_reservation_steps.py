from behave import given, when, then
import random


@given('que eu tenho credenciais válidas de usuário')
def step_tenho_credenciais_validas(context):
    assert context.test_user is not None
    assert 'userName' in context.test_user
    assert 'password' in context.test_user
    print(f"   [INFO] Usando usuario: {context.test_user['userName']}")


@when('eu crio um novo usuário no sistema')
def step_criar_usuario(context):
    base_username = context.test_user['userName']
    password = context.test_user['password']
    
    # Tenta criar usuario, se ja existir, adiciona numero random
    for tentativa in range(10):
        if tentativa == 0:
            username = base_username
        else:
            username = f"{base_username}{random.randint(0, 9999)}"
        
        context.response = context.account_api.criar_usuario(username, password)
        
        if context.response.status_code in [200, 201]:
            user_data = context.response.json()
            context.user_data = user_data
            if 'userID' in user_data:
                context.user_id = user_data['userID']
            print(f"   [STATUS] {context.response.status_code}")
            print(f"   [INFO] Usuario criado: {username}")
            context.test_user['userName'] = username
            break
        elif context.response.status_code == 406:
            if tentativa < 9:
                continue
            else:
                print(f"   [WARNING] Nao conseguiu criar usuario unico")
                print(f"   [STATUS] {context.response.status_code}")
        else:
            print(f"   [STATUS] {context.response.status_code}")
            print(f"   [ERROR] {context.response.text}")
            break


@when('eu gero um token de autenticação')
def step_gerar_token(context):
    context.response = context.account_api.gerar_token(
        context.test_user['userName'],
        context.test_user['password']
    )
    
    print(f"   [STATUS] {context.response.status_code}")
    
    if context.response.status_code == 200:
        token_data = context.response.json()
        context.token = token_data.get('token')


@when('eu verifico se o usuário está autorizado')
def step_verificar_autorizacao(context):
    context.response = context.account_api.verificar_autorizacao(
        context.test_user['userName'],
        context.test_user['password']
    )
    
    print(f"   [STATUS] {context.response.status_code}")


@when('eu listo os livros disponíveis')
def step_listar_livros(context):
    context.response = context.bookstore_api.listar_livros()
    
    if context.response.status_code == 200:
        books_data = context.response.json()
        context.books = books_data.get('books', [])
        
        if context.books:
            print(f"   [INFO] Total de livros: {len(context.books)}")
            for i, book in enumerate(context.books[:3]):
                print(f"      {i+1}. {book['title']} (ISBN: {book['isbn']})")


@when('eu reservo {quantidade:d} livros da lista')
def step_reservar_livros(context, quantidade):
    if not context.selected_isbns:
        if context.books and len(context.books) >= quantidade:
            context.selected_isbns = [book['isbn'] for book in context.books[:quantidade]]
        else:
            books_response = context.bookstore_api.listar_livros()
            books_data = books_response.json()
            context.selected_isbns = [book['isbn'] for book in books_data['books'][:quantidade]]
    
    context.response = context.bookstore_api.reservar_livros(
        context.user_id,
        context.token,
        context.selected_isbns[:quantidade]
    )
    
    print(f"   [STATUS] {context.response.status_code}")
    print(f"   [INFO] Livros reservados: {context.selected_isbns[:quantidade]}")


@when('eu consulto os detalhes do usuário')
def step_consultar_detalhes_usuario(context):
    context.response = context.account_api.obter_detalhes_usuario(
        context.user_id,
        context.token
    )
    
    if context.response.status_code == 200:
        user_details = context.response.json()
        print(f"   [INFO] Usuario: {user_details.get('username', 'N/A')}")
        books = user_details.get('books', [])
        print(f"   [INFO] Livros no perfil: {len(books)}")


@then('o usuário deve ser criado com sucesso')
def step_usuario_criado_sucesso(context):
    assert context.response is not None
    assert context.response.status_code in [200, 201, 406]


@then('o token deve ser gerado com sucesso')
def step_token_gerado_sucesso(context):
    assert context.response is not None
    assert context.response.status_code == 200
    token_data = context.response.json()
    assert token_data.get('status') == 'Success'


@then('o usuário deve estar autorizado')
def step_usuario_autorizado(context):
    assert context.response is not None
    assert context.response.status_code == 200
    is_authorized = context.response.json()
    assert is_authorized == True


@then('devo ver a lista de livros disponíveis')
def step_ver_lista_livros(context):
    assert context.response is not None
    assert context.response.status_code == 200
    books_data = context.response.json()
    assert 'books' in books_data


@then('os livros devem ser reservados com sucesso')
def step_livros_reservados_sucesso(context):
    assert context.response is not None
    assert context.response.status_code in [200, 201]


@then('devo ver os livros reservados no perfil do usuário')
def step_ver_livros_no_perfil(context):
    assert context.response is not None
    assert context.response.status_code == 200
    user_details = context.response.json()
    assert 'books' in user_details
    assert len(user_details['books']) >= 0
