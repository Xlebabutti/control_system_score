from flask import Blueprint, render_template, request, jsonify

from website.models import Score, Team_name

# from website.view_score import view_score
# from website.view_team import view_team
# from website.view_time import view_time


views = Blueprint('views', __name__)

c = Score()
t = Team_name()

@views.route("/", methods=['GET', 'POST'])
def workplace_score():
    # if request.method == "POST":
    #     das = request.get_json()
    #     print(das[1])
    #     data = das[0].split(':')
    #     print(data)
        
    #     data_team_1 = eval(data[0].replace('{', '')).strip()
    #     data_team_2 = eval(data[1].replace('}', '')).strip()

    #     c.update_team_1_now(data_team_1, data_team_2)
    #     c.update_time(das[1], das[2])

    return render_template("mauk.html", list_team = t.get_team_1_name())


@views.route("/output_view")
def control_score():
    return render_template("_output_view.html")

