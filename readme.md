# Very good flask template
## contains:
### sqlalchemy
### CORS
# simple example

##### live site
# on netlify
https://63f3a5385cefb50460ddd502--graceful-paprenjak-cc08d0.netlify.app/
# on github
https://narnav.github.io/flask_sqlachemy_cors_render/


# Update DB create 
    with app.app_context():
        db.create_all()
        app.run(debug=True)

# Run:
    create a virtual enviroment
    py -m virtualenv env
# activate:
    env\script\activate
# prepare the environment
    pip install -r .\requirements.txt
    flask run