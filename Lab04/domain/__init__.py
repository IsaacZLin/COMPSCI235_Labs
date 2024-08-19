from flask import Flask, render_template
from .home.home import create_podcasts

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .home import home
        app.register_blueprint(home.home_blueprint)

    @app.route('/podcasts')
    def podcasts():
        list_of_podcasts = create_podcasts()

        return render_template('catalogue.html', podcasts=list_of_podcasts)

    @app.route('/description/<int:podcast_id>')
    def show_description(podcast_id):
        list_of_podcasts = create_podcasts()
        podcast = list_of_podcasts[podcast_id]
        return render_template('podcastDescription.html', podcast=podcast)

    return app
