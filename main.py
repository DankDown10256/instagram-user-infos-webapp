from flask import Flask, render_template, request
import instaloader

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/get_info', methods=['GET', 'POST'])
def info():
    if request.method == 'POST':
       username_insta = request.form['username']
       L = instaloader.Instaloader()
       profile = instaloader.Profile.from_username(L.context, username_insta)
       name = profile.full_name
       bio = profile.biography
       followers = profile.followers
       website = profile.external_url
       userid = profile.userid
       publication_number = profile.mediacount
       private = profile.is_private
       if private == True:
           private = "Oui"
       elif private == False:
           private = "Non"
       verified = profile.is_verified
       if verified == True:
           verified = "Oui"
       elif verified == False:
           verified = "Non"
       return render_template('index.html', name=name, bio=bio, followers=followers, website=website, userid=userid, publication_number=publication_number, private=private, verified=verified)
    return render_template('index.html')
    


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=50, debug=True)