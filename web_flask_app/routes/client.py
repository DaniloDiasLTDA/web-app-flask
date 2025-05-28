from flask import Blueprint, render_template, request
from data.client_data import CLIENTS

client_route = Blueprint('cliente', __name__)


@client_route.route('/')
def list_client():
   return render_template('client_list.html', clientes=CLIENTS)


@client_route.route('/', methods=['POST'])
def insert_client():

    print(request.json)
    return {'ok': 'ok'}


@client_route.route('/new')
def customer_form():
    return render_template('form_client.html')


@client_route.route('/<id>:client_id')
def client_info(client_id):
    return render_template('info_client.html')


@client_route.route('/<id>:client_id/edit')
def form_edit_client(client_id):
    return render_template('form_edit_client.html')


@client_route.route('/<id>:client_id/update', methods=['PUT'])
def update_client(client_id):
    pass


@client_route.route('/<id>:client_id/delete', methods=['DELETE'])
def delete_client(client_id):
    pass
