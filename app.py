from flask import Flask, render_template
from webscryp import obtener_final_df  # Importa la función desde main.py

app = Flask(__name__)

# Llamada a la función para obtener el DataFrame final_df
final_df = obtener_final_df()

@app.route('/')
def mostrar_tabla():
    html_table = final_df.to_html(classes='table table-striped table-bordered table-hover')
    return render_template('index.html', html_table=html_table)

if __name__ == '__main__':
    app.run(debug=True)
