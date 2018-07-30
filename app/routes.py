from flask import render_template
from app import app, db
from app.models import Stats, WinFeed, StatsFour, StatsLifetime

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
@app.route('/index/<int:page>', methods=["GET", "POST"])
def index(page=1):
    stats = Stats.query.order_by(Stats.id.desc()).limit(5)
    stats_four = StatsFour.query.order_by(StatsFour.id.desc()).limit(5)
    stats_lifetime = StatsLifetime.query.order_by(StatsLifetime.id.desc()).limit(5)

    s3_top_solo_wins = Stats.query.order_by(Stats.solo_wins.desc()).first()
    s3_top_solo_kills = Stats.query.order_by(Stats.solo_kills.desc()).first()
    s3_top_solo_kd = Stats.query.order_by(Stats.solo_kd.desc()).first()
    s3_top_solo_wr = Stats.query.order_by(Stats.solo_wr.desc()).first()

    s3_top_duo_wins = Stats.query.order_by(Stats.duo_wins.desc()).first()
    s3_top_duo_kills = Stats.query.order_by(Stats.duo_kills.desc()).first()
    s3_top_duo_kd = Stats.query.order_by(Stats.duo_kd.desc()).first()
    s3_top_duo_wr = Stats.query.order_by(Stats.duo_wr.desc()).first()

    s3_top_squad_wins = Stats.query.order_by(Stats.squad_wins.desc()).first()
    s3_top_squad_kills = Stats.query.order_by(Stats.squad_kills.desc()).first()
    s3_top_squad_kd = Stats.query.order_by(Stats.squad_kd.desc()).first()
    s3_top_squad_wr = Stats.query.order_by(Stats.squad_wr.desc()).first()

    winpages = WinFeed.query.order_by(WinFeed.log.desc()).paginate(page, 10, False)

    return render_template('index.html', winpages=winpages, scores=stats, scores_four=stats_four, scores_lifetime=stats_lifetime, top_solo_wins=s3_top_solo_wins, top_solo_kills=s3_top_solo_kills, top_solo_kd=s3_top_solo_kd, top_solo_wr=s3_top_solo_wr, top_duo_wins=s3_top_duo_wins, top_duo_kills=s3_top_duo_kills, top_duo_kd=s3_top_duo_kd, top_duo_wr=s3_top_duo_wr, top_squad_wins=s3_top_squad_wins, top_squad_kills=s3_top_squad_kills, top_squad_kd=s3_top_squad_kd, top_squad_wr=s3_top_squad_wr, title="Season 4")

@app.route('/changelog.html')
def changelog():
    return render_template('changelog.html')