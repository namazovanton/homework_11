from flask import Flask, render_template

import utils

app = Flask(__name__)


@app.route("/")
def general_page():
    candidate_names = utils.get_all()
    return f"<h1>Все кандидаты</h1>{render_template('list.html', candidate_names=candidate_names)}"


@app.route("/candidate/<int:uid>/")
def search_by_id(uid):
    candidate_name, candidate_position, candidate_pic, candidate_skills = utils.get_by_id(uid)
    return render_template('single.html', candidate_name=candidate_name, candidate_position=candidate_position,
                           candidate_pic=candidate_pic, candidate_skills=candidate_skills)


@app.route("/search/<candidate_name>/")
def search_by_name(candidate_name):
    candidates_by_name = utils.get_by_name(candidate_name)
    page_content = render_template('search.html', candidates_by_name=candidates_by_name)
    return f"""<h1>Найдено со кандидатов "{candidate_name}": {len(candidates_by_name)}</h1>{page_content}"""


@app.route("/skills/<skill>/")
def search_by_skill(skill):
    candidates_by_skills = utils.get_by_skill(skill)
    page_content = render_template('skill.html', candidates_by_skills=candidates_by_skills)
    return f"""<h1>Найдено со скиллом "{skill}": {len(candidates_by_skills)}</h1>{page_content}"""


@app.route("/alexander/")
def alexander_page():
    page_content = render_template('alexander.html')
    return page_content


@app.errorhandler(404)
def page_not_found(e):
    return "Страница не найдена", 404


@app.errorhandler(500)
def page_server_error(e):
    return "Ошибка на сервере", 500


app.run()
