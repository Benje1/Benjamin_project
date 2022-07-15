from flask import Flask, render_template

from controllers.vet_controller import vets_blueprint
from controllers.pet_controller import pets_blueprint

app = Flask(__name__)

app.register_blueprint(pets_blueprint)
app.register_blueprint(vets_blueprint)


@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
