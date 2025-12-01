from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# The database of posts
posts = [
    {
        "id": 1,
        "name": "Pyin Oo Lwin Vlog Post",
        "thumbnail": "/static/pol.jpg",
        "text": "Welcome to my vlog about Pyin Oo Lwin! Known for its cool climate and stunning botanical gardens."
    },
    {
        "id": 2,
        "name": "Kalaw Vlog Post",
        "thumbnail": "/static/kalaw.jpg",
        "text": "Kalaw is a paradise for trekkers and nature lovers. I'll take you through some of the best trekking routes."
    },
    {
        "id": 3,
        "name": "Inle Lake Vlog Post",
        "thumbnail": "/static/inle.jpg",
        "text": "Inle Lake is famous for its floating villages and gardens. Join me as I explore the unique lifestyle."
    }
]


@app.route('/')
def home():
    query = request.args.get('q')

    if query:
        filtered_posts = [p for p in posts if query.lower()
                          in p['name'].lower()]
        return render_template('index.html', posts=filtered_posts)

    return render_template('index.html', posts=posts)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        new_post = {
            "id": len(posts) + 1,
            "name": request.form["name"],
            "thumbnail": request.form["thumbnail"],
            "text": request.form["text"]
        }
        posts.append(new_post)
        return redirect(url_for('home'))
    return render_template('create.html')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    post = next((p for p in posts if p['id'] == id), None)
    if request.method == 'POST':
        post['name'] = request.form['name']
        post['text'] = request.form['text']
        post['thumbnail'] = request.form['thumbnail']
        return redirect(url_for('home'))
    return render_template('create.html', post=post)


if __name__ == '__main__':
    app.run(debug=True)
