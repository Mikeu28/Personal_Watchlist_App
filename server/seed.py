from models import User, Show, UserShow
from app import app
from config import db

if __name__ == "__main__":
    with app.app_context():
        print("Clearing db...")
        Show.query.delete()
        # User.query.delete()
        # UserShow.query.delete()

        print("Starting seed...")

        def create_shows():
            show_names = [ 'SUITS', 'Breaking Bad' ]
            show_images = [ 
                'https://occ-0-444-448.1.nflxso.net/dnm/api/v6/6gmvu2hxdfnQ55LZZjyzYR4kzGk/AAAABTcWWxzelLQuE_pX3K8UHvGFFFwB9SD80hp2YUvnXpn340jYXn7KGT2y1ndf2rRWlDqe40dnw2fY_bketKSlnB2sABD4cdS_pQQ.webp?r=0a6',
                'https://occ-0-444-448.1.nflxso.net/dnm/api/v6/6gmvu2hxdfnQ55LZZjyzYR4kzGk/AAAABZi_RqpT84KU9PuLqluo8QNslnXT8Hu2_bME3ez2GFxUqc-CdICtULofUMFIpTV_EO1tghUWNSLzXeqhWzYDdSL2ifiUB0eKrn8.webp?r=01d'
            ]
            show_platforms = [ 'Netflix', 'Netflix' ]

            for show_name, show_image, show_platform in zip( show_names, show_images, show_platforms ):
                show = Show(
                    name = show_name,
                    image = show_image,
                    platform = show_platform,
                )

                db.session.add( show )
                db.session.commit()
                
        print( "Seeing shows..." )
        create_shows()

        print( "Done Seeding!" )