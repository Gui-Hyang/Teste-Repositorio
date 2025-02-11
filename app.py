from flask import Flask, jsonify, request

app = Flask (__name__)


usuarios = [

 {
    'id': 1,
    'nome': 'Obi Wan',
    'idade': 34

 },
{
    'id': 2,
    'nome': 'Han Solo',
    'idade': 28

 },
{
    'id': 3,
    'nome': 'Luke Skywalker',
    'idade': 21

 },
]

@app.route('/usuarios', methods= ['GET'])
def consultar_usuarios():
    return jsonify(usuarios)

@app.route('/usuarios/<int:id>', methods=['GET'])

def consultar_usuario_por_id(id):
    for usuario in usuarios:
     if usuario.get('id') == id:
      return jsonify (usuario)

@app.route ('/usuarios', methods=['POST'])
def cadastrar_usuario():
    novo_usuario = request.get_json()
    usuarios.append (novo_usuario)
    return jsonify (usuarios)

@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_por_id(id):
 usuarios_atualizado = request.get_json()
 for indice, usuario in enumerate (usuarios):
    if usuario.get('id') == id:
        usuarios[indice].update(usuarios_atualizado)
        return jsonify (usuarios[indice])

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def excluir_usuario_por_id(id):
    for indice,usuario in enumerate(usuarios):
        if usuario.get('id') == id:
            del usuarios[indice]
    return jsonify (usuarios)

app.run(port=8080,host='localhost',debug=True)