from flask import Flask, render_template, url_for, request, redirect
import pickle

app = Flask(__name__)