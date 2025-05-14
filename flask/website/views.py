games = [
        {
            'game_id': 100,
            'title': 'Chess',
            'description': 'A classic game of strategy and wisdom.',
            'players': '2 players',
            'rating': 99,
            'image_url': 'chess.jpg',  # The image file should be in the 'static/images/' folder
            'rules_pdf': 'Chess.pdf'  # The PDF file should be in 'static/pdfs/' folder
        },
        {
            'game_id': 200,
            'title': 'Monopoly',
            'description': 'A game of real estate and business.',
            'players': '2-6 players',
            'rating': 97,
            'image_url': 'monopoly.jpg',
            'rules_pdf': 'Monopoly.pdf'
        },
        {
            'game_id': 300,
            'title': 'Scrabble',
            'description': 'Form words with letter tiles on a board. Highest score wins.',
            'players': '2-4 players',
            'rating': 75,
            'image_url': 'scrabble.jpeg',
            'rules_pdf': 'Scrabble.pdf'
        },
        {
            'game_id': 400,
            'title': 'Checkers',
            'description': 'Move pieces diagonally to jump and capture opponent’s pieces.',
            'players': '2 players',
            'rating': 90,
            'image_url': 'checkers.jpeg',
            'rules_pdf': 'Checkers.pdf'
        },
        {
            'game_id': 500,
            'title': 'Ludo',
            'description': 'Race your four tokens around the board to reach home first.',
            'players': '2-4 players',
            'rating': 90,
            'image_url': 'Ludo.jpeg',
            'rules_pdf': 'Ludo.pdf'
        },
        {
            'game_id': 600,
            'title': 'Catan',
            'description': 'Collect resources, build settlements, and trade to reach 10 points.',
            'players': '3-4 players',
            'rating': 85,
            'image_url': 'Catan.jpeg',
            'rules_pdf': 'Catan.pdf'
        },
        {
            'game_id': 700,
            'title': 'Carcassonne',
            'description': 'Place tiles to build roads, cities, and farms. Score by placing meeples.',
            'players': '2-5 players',
            'rating': 70,
            'image_url': 'Carcassonne.jpeg',
            'rules_pdf': 'Carcassonne.pdf'
        },
        {
            'game_id': 800,
            'title': 'Azul',
            'description': 'Draft colorful tiles and arrange them to complete patterns and score.',
            'players': '2-4 players',
            'rating': 90,
            'image_url': 'Azul.jpeg',
            'rules_pdf': 'Azul.pdf'
        },
        {
            'game_id': 900,
            'title': 'Pandemic',
            'description': 'Work together to stop 4 diseases from spreading worldwide.',
            'players': '2-4 players',
            'rating': 90,
            'image_url': 'Pandemic.jpeg',
            'rules_pdf': 'Pandemic.pdf'
        },
        {
            'game_id': 1000,
            'title': 'Dominion',
            'description': 'Build a deck of cards to gain the most victory points.',
            'players': '2-4 players',
            'rating': 80,
            'image_url': 'Dominion.jpeg',
            'rules_pdf': 'Dominion.pdf'
        }
    ]


from flask import Blueprint, render_template, request
from flask_login import login_user, login_required, current_user
from flask import Blueprint, render_template, session, redirect, url_for
from flask import redirect, url_for, session

from flask import Flask, render_template, redirect, url_for, request, flash
from .models import db, User, Game, UserGame
from flask import session

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from datetime import datetime
from .models import db, Session  # assuming you have models set up
from flask import send_from_directory

import os
from flask import send_from_directory


views = Blueprint('views', __name__)

@views.route('/login')
def login():
    return render_template('login.html', user=current_user)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home(): 
    games = [
        {
            'game_id': 100,
            'title': 'Chess',
            'description': 'A classic game of strategy and wisdom.',
            'players': '2 players',
            'rating': 99,
            'image_url': 'chess.jpg',  # The image file should be in the 'static/images/' folder
            'rules_pdf': 'Chess.pdf'  # The PDF file should be in 'static/pdfs/' folder
        },
        {
            'game_id': 200,
            'title': 'Monopoly',
            'description': 'A game of real estate and business.',
            'players': '2-6 players',
            'rating': 97,
            'image_url': 'monopoly.jpg',
            'rules_pdf': 'Monopoly.pdf'
        },
        {
            'game_id': 300,
            'title': 'Scrabble',
            'description': 'Form words with letter tiles on a board. Highest score wins.',
            'players': '2-4 players',
            'rating': 75,
            'image_url': 'scrabble.jpeg',
            'rules_pdf': 'Scrabble.pdf'
        },
        {
            'game_id': 400,
            'title': 'Checkers',
            'description': 'Move pieces diagonally to jump and capture opponent’s pieces.',
            'players': '2 players',
            'rating': 90,
            'image_url': 'checkers.jpeg',
            'rules_pdf': 'Checkers.pdf'
        },
        {
            'game_id': 500,
            'title': 'Ludo',
            'description': 'Race your four tokens around the board to reach home first.',
            'players': '2-4 players',
            'rating': 90,
            'image_url': 'Ludo.jpeg',
            'rules_pdf': 'Ludo.pdf'
        },
        {
            'game_id': 600,
            'title': 'Catan',
            'description': 'Collect resources, build settlements, and trade to reach 10 points.',
            'players': '3-4 players',
            'rating': 85,
            'image_url': 'Catan.jpeg',
            'rules_pdf': 'Catan.pdf'
        },
        {
            'game_id': 700,
            'title': 'Carcassonne',
            'description': 'Place tiles to build roads, cities, and farms. Score by placing meeples.',
            'players': '2-5 players',
            'rating': 70,
            'image_url': 'Carcassonne.jpeg',
            'rules_pdf': 'Carcassonne.pdf'
        },
        {
            'game_id': 800,
            'title': 'Azul',
            'description': 'Draft colorful tiles and arrange them to complete patterns and score.',
            'players': '2-4 players',
            'rating': 90,
            'image_url': 'Azul.jpeg',
            'rules_pdf': 'Azul.pdf'
        },
        {
            'game_id': 900,
            'title': 'Pandemic',
            'description': 'Work together to stop 4 diseases from spreading worldwide.',
            'players': '2-4 players',
            'rating': 90,
            'image_url': 'Pandemic.jpeg',
            'rules_pdf': 'Pandemic.pdf'
        },
        {
            'game_id': 1000,
            'title': 'Dominion',
            'description': 'Build a deck of cards to gain the most victory points.',
            'players': '2-4 players',
            'rating': 80,
            'image_url': 'Dominion.jpeg',
            'rules_pdf': 'Dominion.pdf'
        }
    ]

    session['games'] = games

    search_query = request.args.get('q', '').lower()
    
    if search_query:
        filtered_games = [game for game in games if search_query in game["title"].lower()]
    else:
        filtered_games = games

    return render_template("home.html", user=current_user, games=filtered_games,)  


# views.py

from flask import session, flash, redirect, url_for
from flask_login import login_required, current_user

@views.route('/add_to_collection/<int:game_id>', methods=['POST'])
@login_required
def add_to_collection(game_id):
    user = current_user  # Get the current logged-in user

    # Retrieve games from session
    games = session.get('games', [])  # Get games list from session

    # Find the game in the session list by game_id
    game = next((g for g in games if g['game_id'] == game_id), None)

    if game:
        # Check if the game is already in the user's collection
        existing_game = UserGame.query.filter_by(user_id=user.id, game_id=game_id).first()

        if not existing_game:
            # Add the game to the collection (create a new association in UserGame table)
            new_game = UserGame(user_id=user.id, game_id=game_id)
            db.session.add(new_game)
            db.session.commit()

            flash('Game added to your collection!')
        else:
            flash('This game is already in your collection.')
    else:
        flash('Game not found.')

    return redirect(url_for('views.home'))  # Redirect to the home page


@views.route('/remove-from-collection/<int:game_id>', methods=['POST'])
@login_required
def remove_from_collection(game_id):
    user = current_user  # Get the current logged-in user

    # Find the game in the user's collection
    game_to_remove = UserGame.query.filter_by(user_id=user.id, game_id=game_id).first()

    if game_to_remove:
        db.session.delete(game_to_remove)
        db.session.commit()
        flash('Game removed from your collection.')
    else:
        flash('This game is not in your collection.')

    return redirect(url_for('views.my_collection'))  # Redirect to collection page


@views.route('/my_collection')
@login_required
def my_collection():
    user = current_user
    user_games = UserGame.query.filter_by(user_id=user.id).all()

    games_in_collection = []
    for user_game in user_games:
        game = next((g for g in games if g['game_id'] == user_game.game_id), None)
        if game:
            games_in_collection.append(game)

    return render_template('my_collection.html', user=user, games=games_in_collection)

#sessions 
@views.route('/sessions')
def sessions():
    sessions = Session.query.all()
    games = [
        'Catan', 'Carcassonne', 'Ticket to Ride', 'Pandemic', 'Azul',
        '7 Wonders', 'Dominion', 'Splendor', 'Codenames', 'Terraforming Mars',
        'Wingspan', 'Gloomhaven', 'Scythe', 'Root', 'Betrayal at House on the Hill',
        'Blood Rage', 'Arkham Horror', 'Brass: Birmingham', 'Everdell', 'Quacks of Quedlinburg'
    ]
    return render_template('sessions.html', sessions=sessions, games=games, user=current_user)

@views.route('/save_session', methods=['POST'])
def save_session():
    data = request.json
    new_session = Session(
        name=data['sessionName'],
        game_name=data['gameName'],
        date_played=datetime.strptime(data['datePlayed'], '%Y-%m-%d'),
        num_players=data['numPlayers'],
        duration=data['duration']
    )
    db.session.add(new_session)
    db.session.commit()
    return jsonify({'message': 'Session saved successfully!'})

@views.route('/delete_session/<int:session_id>', methods=['POST'])
def delete_session(session_id):
    session = Session.query.get(session_id)
    if session:
        db.session.delete(session)
        db.session.commit()
        return jsonify({'message': 'Session deleted successfully!'})
    return jsonify({'error': 'Session not found'}), 404

@views.route('/view_rules/<game_name>')
def view_rules(game_name):
    # Clean the game name if needed (handle case sensitivity, spaces, etc.)
    game_name = game_name.strip().lower()
    # Make sure the game name corresponds to a valid PDF file
    try:
        return send_from_directory(os.path.join('static', 'rules'), f'{game_name}.pdf')
    except FileNotFoundError:
        return "PDF not found!", 404
    
@views.route('/chess')
def chess():
    return render_template('chess.html', user=current_user)
