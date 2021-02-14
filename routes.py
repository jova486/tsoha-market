from app import app
import messages, users

from flask import Flask, render_template, request, flash, redirect, make_response
from forms import RegistrationForm, LoginForm, new_adForm, new_mesageForm, search_Form


@app.route("/")
def index():
    lists = messages.get_list()
    return render_template('index.html', lists=lists)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/new_message/<int:to_id>", methods=['GET', 'POST'])
def new_message(to_id):
    user_id = users.user_id()
    if user_id == 0:
        flash(f'Kirjaudu jotta voit voit lähettää viestin', 'danger')
        return redirect("/")
    form = new_mesageForm()
    if form.validate_on_submit():
        content = form.message.data
        if messages.send(content, to_id):
            flash(f'Viesti lähetetty {form.message.data}!', 'success')
            return redirect("/")
        else:
            flash('Voi hitsi! Viestin lähettäminen ei onnistunut', 'danger')

    return render_template('message.html', title='Lähetä viesti', form=form)

@app.route("/show_messages")
def show_messages():
    m = messages.get_messages()
    if m: 
        return render_template('show_messages.html', messages=m)
    else:
        return redirect("/")

@app.route("/my_ads")
def my_ads():
    ads = messages.get_my_list()
    if ads != False:
        return render_template('my_ads.html', lists=ads)
    else:
        flash(f'Kirjaudu jotta voit nähdä omat ilmoituksesi', 'danger')
        return redirect("/")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if users.register(form.username.data,form.password.data):
            flash(f'Tili luotu käyttäjälle {form.username.data}!', 'success')
            return redirect("/")
        else:
            flash('Kirjautuminen epäonnistui. Tarkista käyttäjätunnus ja salasana', 'danger')

    return render_template('register.html', title='Luo tili', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if users.login(form.username.data,form.password.data):
            flash(f'Kirjautunut {form.username.data}!', 'success')
            return redirect("/")
        else:
            flash('Kirjautuminen epäonnistui. Ole hyvä ja tarkista käyttäjätunnus ja salasana', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    user_id = users.user_id()
    if user_id == 0:
        flash(f'Kirjaudu jotta voit kirjautua ulos', 'danger')
        return redirect("/")
    users.logout()
    flash(f'Ulos kirjautuminen onnistui!', 'success')
    return redirect("/")

@app.route("/new_ad", methods=['GET', 'POST'])
def new_ad():
    user_id = users.user_id()
    if user_id == 0:
        flash(f'Kirjaudu jotta voit jättää ilmoituksen', 'danger')
        return redirect("/")
    form = new_adForm()
    result = messages.get_cat()
    form.cat.choices = [(r['id'],r['cat_name'] ) for r in result]
    if form.validate_on_submit():
        cat_id = form.cat.data
        ad_type = 1
        valid = 30
        item = form.item.data
        ad_text = form.ad.data
        image = form.image.data
        if messages.new_ad(cat_id, ad_type, valid, item, ad_text, image):
            flash(f'new_ad done {form.item.data}!', 'success')
            return redirect("/")
        else:
            flash('new_ad Unsuccessful. Please check username and password', 'danger')
    return render_template('new_ad.html', title='new_ad', form=form)

@app.route("/search", methods=['GET', 'POST'])
def search():
    form = search_Form()
    result = messages.get_cat()
    form.cat.choices = [(r['id'],r['cat_name'] ) for r in result]
    if form.validate_on_submit():
        cat_id = int(form.cat.data)
        ad_type = int(form.radios.data)
        item = form.item.data
        ad_text = form.ad.data
        ads = messages.search(cat_id, ad_type, item, ad_text)
        if ads != False:
            return render_template('index.html', lists=ads)
        else:
            flash(f'Haku ei tuottanut tulosta', 'danger')
            return redirect("/")
    return render_template('search.html', title='Haku', form=form)


@app.route("/delete_ad/<int:id>")
def delete_ad(id):
    
    messages.delete_ad(id)
  
    return redirect("/my_ads")

@app.route("/ad/<int:id>")
def ad(id):
    
    a = messages.get_ad(id)
    return render_template('ad.html', ad=a)

@app.route("/ad_photo/<int:id>")
def ad_photo(id):
    
    image = messages.get_image(id)
  
    return image
    
    
