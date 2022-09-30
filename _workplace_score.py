import imp
from flask import Flask, render_template, jsonify, request, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///score_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route("/", methods=["GET", "POST"])
def workplace_score():
    if request.method == "POST":
        data = request.get_json().split(':')
        # print(data)
        data_team_1 = eval(data[0].replace('{', '')).strip()
        # print(data_team_1)
        data_team_2 = eval(data[1].replace('}', '')).strip()

        from _create_json_db_score import Score
        s = Score()
        s.update_team_1_now(data_team_1, data_team_2)
        
        # db.session.commit()

    from _create_json_db_score import Team_name
    t = Team_name()
    return render_template("_workplace_score.html", list_team = t.get_team_1_name())


@app.route("/control_score", methods=["GET", 'POST'])
def control_score():
    return render_template("_control_score.html")


@app.route('/get_team_score', methods=['GET'])
def remout():   
    from _create_json_db_score import Score
    c = Score()
    return jsonify(team_1 = c.get_score_team_1(), team_2 = c.get_score_team_2())


@app.route('/add_score_team_1', methods=['GET'])
def add_score_team_1():   
    from _create_json_db_score import Score
    c = Score()
    return jsonify(c.add_score_team_1())


@app.route('/add_score_team_2', methods=['GET'])
def add_score_team_2():   
    from _create_json_db_score import Score
    c = Score()
    return jsonify(c.add_score_team_2())


@app.route('/put_score_team_1', methods=['GET'])
def put_score_team_1():   
    from _create_json_db_score import Score
    c = Score()
    return jsonify(c.put_score_team_1())


@app.route('/put_score_team_2', methods=['GET'])
def put_score_team_2():   
    from _create_json_db_score import Score
    c = Score()
    return jsonify(c.put_score_team_2())


@app.route('/reset_score', methods=['GET'])
def reset_score():   
    from _create_json_db_score import Score
    c = Score()
    return jsonify(c.reset_score())

@app.route('/get_team_name', methods=['GET', 'POST'])
def get_team_name():   
    data = request.get_json()
    print(data)
    return jsonify(data)


@app.route('/get_team_1_now', methods=['GET', 'POST'])
def get_team_1_now1():
    from _create_json_db_score import Score
    c = Score()
    team_1 = c.get_team_1_now()
    print(team_1)
    return jsonify(team_1)

@app.route('/get_team_2_now', methods=['GET', 'POST'])
def get_team_2_now2():
    from _create_json_db_score import Score
    c = Score()
    team_2 = c.get_team_2_now()
    print(team_2)
    return jsonify(team_2)



# @sio.on('vmix_socet', namespace='/test')
# def input_pgm_vmix(pgm_vmix):   
#     global Team_1
#     global Tema_2
#     return sio.emit(pgm_vmix, namespace='/test')

    # sio.emit('Team_1', Team_1, namespace = '/test')
    # sio.emit('Team_2', Tema_2, namespace = '/test')
    # sio.emit(pgm_vmix)
    # print('client connected!')

if __name__ == '__main__':
   app.run(host = '127.0.0.1', port=5050, debug = True)