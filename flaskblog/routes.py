from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog import app, db, hashing, mail
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, RequestResetForm, ResetPasswordForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
from PIL import Image
from flask_mail import Message

db.create_all()
# Such JSON data needs to be retrieved from database, or through APIs
