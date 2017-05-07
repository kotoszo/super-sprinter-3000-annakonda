from flask import Flask, request, render_template
import file_minator


app = Flask(__name__)


@app.route('/')
@app.route('/home', methods=['DELETE'])
def homepage():
    if request.method == "DELETE":
        print(True)
    csv_loader = file_minator.csv_loader("stories.csv")
    return render_template('index.html', stories=csv_loader)


@app.route('/story')
@app.route('/story/<story_id>')
def story(story_id=None):
    csv_loader = file_minator.csv_loader("stories.csv")
    return render_template("story.html", story_id=story_id, stories=csv_loader)


def delete(id_to_delete):
    file_minator.csv_remover("stories.csv", id_to_delete)
    return homepage()


@app.route('/list', methods=['POST', 'GET', "DELETE"])
def post(story_id=None, id_to_delete=None):
    if request.method == "DELETE":
        delete_info = request.form['delete']
        print(True)
    loaded_infos = file_minator.csv_loader("stories.csv")
    info1 = request.form['story_title']
    info2 = request.form['user_story'].replace("\r", ' ').replace("\n", ' ')
    info3 = request.form['accept_crit'].replace("\r", " ").replace("\n", ' ')
    info4 = request.form['business_value']
    info5 = request.form['estimation']
    info6 = request.form['status']
    bunch_of_new_info = [info1, info2, info3, info4, info5, info6]
    for item in range(len(loaded_infos)):
        if info1 in loaded_infos[item][0]:
            file_minator.csv_remover("stories.csv", loaded_infos[item][0])
    file_minator.csv_saver("stories.csv", bunch_of_new_info)
    return homepage()


@app.route('/lofasz')
def lofasz():
    return render_template("post_story.html")


if __name__ == '__main__':
    app.run(debug=True)
