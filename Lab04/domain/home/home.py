from flask import Blueprint, render_template


def create_podcasts():
    list_of_podcasts = [{
        'title': 'D-Hour Radio Network',
        'img_url': 'http://is3.mzstatic.com/image/thumb/Music118/v4/b9/ed/86/b9ed8603-d94b-28c5-5f95-8b7061bf22fa/source/600x600bb.jpg',
        'id': 1,
        'author': 'D Hour Radio Network',
        'language': 'English',
        'about': 'The D-Hour Radio Network is the home of real entertainment radio and "THE" premiere online radio network. We showcase dynamically dynamite radio shows for the sole purpose of entertaining your listening ear. Here on the D-hour Show Radio network we take pride in providing an outlet for Celebrity Artists, Underground Artists, Indie Artists, Producers, Entertainers, Entrepreneurs, Internet Stars and future business owners. We discuss topics of all forms and have a great time while doing so. We play all your favorite hits in the forms of Celebrity, Indie, Hip Hop, Soul/R&B, Pop, and everything else you want and consider popular. If you would like yourself and or your music to be showcased on our radio network submit email requests for music airplay, interviews and etc.. to: dhourshow@gmail.com and we will get back to you promptly. Here at the D-Hour Radio Network we are Family and all of our guests, listeners and loyal fans are family too. So tune into the D-Hour Radio Network and join the Family!	',
        'categories': 'Society & Culture | Personal Journals',
        'website': 'http://www.blogtalkradio.com/dhourshow',
        'itunes_id': '538283940'
    },
        {
            'title': 'Brian Denny Radio',
            'img_url': 'http://is5.mzstatic.com/image/thumb/Music111/v4/49/c8/19/49c8190a-ca0f-f32c-c089-d7ae502d2cb8/source/600x600bb.jpg',
            'id': 2,
            'author': 'Brian Denny',
            'language': 'English',
            'about': '5-in-1: Brian Denny Radio is the fastest podcast in all the land. Each episode is 5 minutes and done in 1 take. Brian covers news, politics, sports, pro wrestling, life & more! No one does it faster or better, probably. #BDR	',
            'categories': 'Professional | News & Politics | Sports & Recreation | Comedy',
            'website': 'http://thebdshow.libsyn.com/podcast	',
            'itunes_id': '1132261215'
        },
        {
            'title': 'Onde Road - Radio Popolare',
            'img_url': 'http://is2.mzstatic.com/image/thumb/Music62/v4/a5/44/ce/a544ce1f-3250-7147-1e8a-6316a161900c/source/600x600bb.jpg',
            'id': 3,
            'author': 'Radio Popolare',
            'language': 'Italian',
            'about': 'Il podcast la trasmissione Onde Road di Radio Popolare',
            'categories': 'Society & Culture',
            'website': 'http://www.radiopopolare.it',
            'itunes_id': '568005832'
        }
    ]
    return list_of_podcasts


home_blueprint = Blueprint('home_bp', __name__)


@home_blueprint.route('/', methods=['GE`'])
def home():
    list_of_podcasts = create_podcasts()

    return render_template('/layout.html', podcasts=list_of_podcasts)
