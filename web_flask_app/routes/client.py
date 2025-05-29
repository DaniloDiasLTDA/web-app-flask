from flask import Blueprint, render_template, request
from data.client_data import CLIENTS

client_route = Blueprint('cliente', __name__)


@client_route.route('/')
def list_client():
   return render_template('client_list.html', clientes=CLIENTS)


@client_route.route('/', methods=['POST'])
def insert_client():

    data = request.json

    new_user = {
        "id":len(CLIENTS) + 1,
        "nome": data['nome'],
        "email": data['email'],
    }

    CLIENTS.append(new_user)

    return render_template('item_client.html', cliente=new_user)


@client_route.route('/new')
def form_client():
    """ Formulario para cadastrar cliente """
    return render_template('form_client.html')

   
@client_route.route('/<int:client_id>')
def client_info(client_id):
    """ Exibir detalher do cliente"""
    return render_template('info_client.html')


@client_route.route('/<int:client_id>/edit')
def form_edit_client(client_id):
    """Formulario para editar um cliente"""
    cliente = None
    for c in CLIENTS:
        if c['id'] == client_id:
            cliente = c

    return render_template('form_client.html', cliente=cliente)

@client_route.route('/<int:client_id>/update', methods=['PUT'])
def update_client(client_id):
    """Atualizar informações do cliente"""
    cliente_editado = None

    data = request.json

    for c in CLIENTS:
        if c['id'] == client_id:
            c['nome'] = data['nome']
            c['email'] = data['email']
            
            cliente_editado = c
            
    return render_template('item_cliente.html', cliente=cliente_editado)


@client_route.route('/<int:client_id>/delete', methods=['DELETE'])
def delete_client(client_id):
    global CLIENTS
    CLIENTS = [ c for c in CLIENTS if c['id'] != client_id]
    return {'deleted': 'ok'}