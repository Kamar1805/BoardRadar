from flask import Blueprint, render_template, request
from flask_login import login_user, login_required, current_user
from flask import Blueprint, render_template, session, redirect, url_for


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home(): 
    games = [
        {
            'title': 'Chess',
            'description': 'A classic game of strategy.',
            'players': '2 players',
            'rating': 85,
            'image_url': 'chess.jpg',  # The image file should be in the 'static/images/' folder
            'rules_pdf': 'CHESS.pdf'  # The PDF file should be in 'static/pdfs/' folder
        },
        {
            'title': 'Monopoly',
            'description': 'A game of real estate and business.',
            'players': '2-6 players',
            'rating': 90,
            'image_url': 'monopoly.jpg',
            'rules_pdf': 'monopoly_rules.pdf'
        },
        {
            'title': 'Monopoly',
            'description': 'A game of real estate and business.',
            'players': '2-6 players',
            'rating': 90,
            'image_url': 'monopoly.jpg',
            'rules_pdf': 'monopoly_rules.pdf'
        },
        {
            'title': 'Monopoly',
            'description': 'A game of real estate and business.',
            'players': '2-6 players',
            'rating': 90,
            'image_url': 'monopoly.jpg',
            'rules_pdf': 'monopoly_rules.pdf'
        },
        {
            'title': 'Monopoly',
            'description': 'A game of real estate and business.',
            'players': '2-6 players',
            'rating': 90,
            'image_url': 'monopoly.jpg',
            'rules_pdf': 'monopoly_rules.pdf'
        },
        {
            'title': 'Monopoly',
            'description': 'A game of real estate and business.',
            'players': '2-6 players',
            'rating': 90,
            'image_url': 'monopoly.jpg',
            'rules_pdf': 'monopoly_rules.pdf'
        },
        {
            'title': 'Monopoly',
            'description': 'A game of real estate and business.',
            'players': '2-6 players',
            'rating': 90,
            'image_url': 'monopoly.jpg',
            'rules_pdf': 'monopoly_rules.pdf'
        },
        {
            'title': 'Monopoly',
            'description': 'A game of real estate and business.',
            'players': '2-6 players',
            'rating': 90,
            'image_url': 'monopoly.jpg',
            'rules_pdf': 'monopoly_rules.pdf'
        },
        {
            'title': 'Monopoly',
            'description': 'A game of real estate and business.',
            'players': '2-6 players',
            'rating': 90,
            'image_url': 'monopoly.jpg',
            'rules_pdf': 'monopoly_rules.pdf'
        },
        {
            'title': 'Monopoly',
            'description': 'A game of real estate and business.',
            'players': '2-6 players',
            'rating': 90,
            'image_url': 'monopoly.jpg',
            'rules_pdf': 'monopoly_rules.pdf'
        },
        {
            'title': 'Lebronnnnn',
            'description': 'A game of real estate and business.',
            'players': '2-6 players',
            'rating': 90,
            'image_url': 'monopoly.jpg',
            'rules_pdf': 'monopoly_rules.pdf'
        },
        {
            'title': 'Monopoly',
            'description': 'A game of real estate and business.',
            'players': '2-6 players',
            'rating': 90,
            'image_url': 'monopoly.jpg',
            'rules_pdf': 'monopoly_rules.pdf'
        },
        {
            'title': 'Monopoly',
            'description': 'A game of real estate and business.',
            'players': '2-6 players',
            'rating': 90,
            'image_url': 'monopoly.jpg',
            'rules_pdf': 'monopoly_rules.pdf'
        },
        {
            'title': 'Monopoly',
            'description': 'A game of real estate and business.',
            'players': '2-6 players',
            'rating': 90,
            'image_url': 'monopoly.jpg',
            'rules_pdf': 'monopoly_rules.pdf'
        },
        {
            'title': 'Monopoly',
            'description': 'A game of real estate and business.',
            'players': '2-6 players',
            'rating': 90,
            'image_url': 'monopoly.jpg',
            'rules_pdf': 'monopoly_rules.pdf'
        },
        {
            'title': 'Monopoly',
            'description': 'A game of real estate and business.',
            'players': '2-6 players',
            'rating': 90,
            'image_url': 'monopoly.jpg',
            'rules_pdf': 'monopoly_rules.pdf'
        },
        {
            'title': 'Monopoly',
            'description': 'A game of real estate and business.',
            'players': '2-6 players',
            'rating': 90,
            'image_url': 'monopoly.jpg',
            'rules_pdf': 'monopoly_rules.pdf'
        },
        {
            'title': 'Monopoly',
            'description': 'A game of real estate and business.',
            'players': '2-6 players',
            'rating': 90,
            'image_url': 'monopoly.jpg',
            'rules_pdf': 'monopoly_rules.pdf'
        },
         {
            'title': 'Monopoly',
            'description': 'A game of real estate and business.',
            'players': '2-6 players',
            'rating': 90,
            'image_url': 'monopoly.jpg',
            'rules_pdf': 'monopoly_rules.pdf'
        },
         {
            'title': 'Monopoly',
            'description': 'A game of real estate and business.',
            'players': '2-6 players',
            'rating': 90,
            'image_url': 'monopoly.jpg',
            'rules_pdf': 'monopoly_rules.pdf'
        }      
    ]

    search_query = request.args.get('q', '').lower()
    
    if search_query:
        filtered_games = [game for game in games if search_query in game["title"].lower()]
    else:
        filtered_games = games

    return render_template("home.html", user=current_user, games=filtered_games,)  

@views.route('/collection')
def my_collections():

      # You define this to get user's games
    return render_template('collection.html',user=current_user)
