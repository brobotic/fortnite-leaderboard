from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class StatsFour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.String(64), index=True)
    s4_solo_wins = db.Column(db.Integer, index=True)
    s4_solo_kills = db.Column(db.Integer, index=True)
    s4_solo_killsmax = db.Column(db.Integer, index=True)
    s4_solo_kd = db.Column(db.Float, index=True)
    s4_solo_wr = db.Column(db.Float, index=True)
    s4_solo_matches = db.Column(db.Integer, index=True)
    s4_duo_wins = db.Column(db.Integer, index=True)
    s4_duo_kills = db.Column(db.Integer, index=True)
    s4_duo_killsmax = db.Column(db.Integer, index=True)
    s4_duo_kd = db.Column(db.Float, index=True)
    s4_duo_wr = db.Column(db.Float, index=True)
    s4_duo_matches = db.Column(db.Integer, index=True)
    s4_squad_wins = db.Column(db.Integer, index=True)
    s4_squad_kills = db.Column(db.Integer, index=True)
    s4_squad_killsmax = db.Column(db.Integer, index=True)
    s4_squad_kpm = db.Column(db.Float, index=True)
    s4_squad_kd = db.Column(db.Float, index=True)
    s4_squad_wr = db.Column(db.Float, index=True)
    s4_squad_matches = db.Column(db.Integer, index=True)
    s4_total_wins = db.Column(db.Integer, index=True)
    s4_total_kills = db.Column(db.Integer, index=True)
    s4_total_matches = db.Column(db.Integer, index=True)

class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.String(64), index=True)
    solo_wins = db.Column(db.Integer, index=True)
    solo_kills = db.Column(db.Integer, index=True)
    solo_kpm = db.Column(db.Float, index=True)
    solo_kd = db.Column(db.Float, index=True)
    solo_wr = db.Column(db.Float, index=True)
    solo_matches = db.Column(db.Integer, index=True)
    duo_wins = db.Column(db.Integer, index=True)
    duo_kills = db.Column(db.Integer, index=True)
    duo_kpm = db.Column(db.Float, index=True)
    duo_kd = db.Column(db.Float, index=True)
    duo_wr = db.Column(db.Float, index=True)
    duo_matches = db.Column(db.Integer, index=True)
    squad_wins = db.Column(db.Integer, index=True)
    squad_kills = db.Column(db.Integer, index=True)
    squad_kpm = db.Column(db.Float, index=True)
    squad_kd = db.Column(db.Float, index=True)
    squad_wr = db.Column(db.Float, index=True)
    squad_matches = db.Column(db.Integer, index=True)
    life_wins = db.Column(db.Integer, index=True)
    life_kills = db.Column(db.Integer, index=True)
    life_kpm = db.Column(db.Float, index=True)
    life_kd = db.Column(db.Float, index=True)
    life_wr = db.Column(db.Float, index=True)
    life_matches = db.Column(db.Integer, index=True)
    life_solo_wins = db.Column(db.Integer, index=True)
    life_solo_kills = db.Column(db.Integer, index=True)
    life_solo_kd = db.Column(db.Float, index=True)
    life_solo_wr = db.Column(db.Float, index=True)
    life_solo_matches = db.Column(db.Integer, index=True)
    life_duo_wins = db.Column(db.Integer, index=True)
    life_duo_kills = db.Column(db.Integer, index=True)
    life_duo_kd = db.Column(db.Float, index=True)
    life_duo_wr = db.Column(db.Float, index=True)
    life_duo_matches = db.Column(db.Integer, index=True)
    life_squad_wins = db.Column(db.Integer, index=True)
    life_squad_kills = db.Column(db.Integer, index=True)
    life_squad_kd = db.Column(db.Float, index=True)
    life_squad_wr = db.Column(db.Float, index=True)
    life_squad_matches = db.Column(db.Integer, index=True)
    s3_total_wins = db.Column(db.Integer, index=True)
    s3_total_kills = db.Column(db.Integer, index=True)
    s3_total_kd = db.Column(db.Float, index=True)
    s3_total_matches = db.Column(db.Integer, index=True)
    s3_total_matchesnew = db.Column(db.Integer, index=True)
    s4_solo_wins = db.Column(db.Integer, index=True)
    s4_solo_kills = db.Column(db.Integer, index=True)
    s4_solo_kd = db.Column(db.Float, index=True)
    s4_solo_wr = db.Column(db.Float, index=True)
    s4_solo_matches = db.Column(db.Integer, index=True)
    s4_duo_wins = db.Column(db.Integer, index=True)
    s4_duo_kills = db.Column(db.Integer, index=True)
    s4_duo_kd = db.Column(db.Float, index=True)
    s4_duo_wr = db.Column(db.Float, index=True)
    s4_duo_matches = db.Column(db.Integer, index=True)
    s4_squad_wins = db.Column(db.Integer, index=True)
    s4_squad_kills = db.Column(db.Integer, index=True)
    s4_squad_kpm = db.Column(db.Float, index=True)
    s4_squad_kd = db.Column(db.Float, index=True)
    s4_squad_wr = db.Column(db.Float, index=True)
    s4_squad_matches = db.Column(db.Integer, index=True)
    pic = db.Column(db.String(128), index=True)

class StatsLifetime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.String(64), index=True)
    life_wins = db.Column(db.Integer, index=True)
    life_kills = db.Column(db.Integer, index=True)
    life_kpm = db.Column(db.Float, index=True)
    life_kd = db.Column(db.Float, index=True)
    life_wr = db.Column(db.Float, index=True)
    life_matches = db.Column(db.Integer, index=True)
    life_solo_wins = db.Column(db.Integer, index=True)
    life_solo_kills = db.Column(db.Integer, index=True)
    life_solo_kd = db.Column(db.Float, index=True)
    life_solo_wr = db.Column(db.Float, index=True)
    life_solo_matches = db.Column(db.Integer, index=True)
    life_duo_wins = db.Column(db.Integer, index=True)
    life_duo_kills = db.Column(db.Integer, index=True)
    life_duo_kd = db.Column(db.Float, index=True)
    life_duo_wr = db.Column(db.Float, index=True)
    life_duo_matches = db.Column(db.Integer, index=True)
    life_squad_wins = db.Column(db.Integer, index=True)
    life_squad_kills = db.Column(db.Integer, index=True)
    life_squad_kd = db.Column(db.Float, index=True)
    life_squad_wr = db.Column(db.Float, index=True)
    life_squad_matches = db.Column(db.Integer, index=True)

class WinFeed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    log = db.Column(db.String(128), index=True)

if __name__ == '__main__':
    manager.run()