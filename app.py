from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

clients = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # create
        if 'create' in request.form:
            client_id = request.form.get('client_id')
            company_name = request.form.get('company_name')
            if client_id.isdigit():
                clients.append({'id': int(client_id), 'name': company_name})
                return redirect(url_for('index'))
        
        # delete
        elif 'delete' in request.form:
            client_id_to_delete = request.form.get('delete_id')
            clients[:] = [client for client in clients if str(client['id']) != client_id_to_delete]
            return redirect(url_for('index'))
    return render_template('index.html', clients=clients)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5015)

