import streamlit as st
import os
os.system('python rom.py')
if not hasattr(st, 'already_started_server'):
    st.already_started_server = True

    st.write('''
        The first time this script executes it will run forever because it's
        running a Flask server.

        Just close this browser tab and open a new one to see your Streamlit
        app.
    ''')

    from flask import Flask

    app = Flask(__name__)

    @app.route('/foo')
    def serve_foo():
        return 'This page is served via Flask!'

    app.run(port = 8880)

x = st.slider('Pick a number')
st.write('You picked:', x)
