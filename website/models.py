from .extensions import db


class Score(db.Model):
    # id = db.Column(db.Integer, primary_key = True)
    score_team_1 = db.Column(db.Integer, primary_key = True)
    score_team_2 = db.Column(db.Integer, primary_key = True)
    team_1_now = db.Column(db.String(100), primary_key = True)
    team_2_now = db.Column(db.String(100), primary_key = True)
    time_mm = db.Column(db.String(100), primary_key = True)
    time_ss = db.Column(db.String(100), primary_key = True)
    id = db.Column(db.Integer, primary_key = True)


# Get item table in score_bd------------------------------->

    def get_querry_all_score(self):
        return Score.query.all()

    def get_score_team_1(self):
        score_team_1 = self.get_querry_all_score()
        return score_team_1[0].score_team_1
    
    def get_score_team_2(self):
        score_team_2 = self.get_querry_all_score()
        return score_team_2[0].score_team_2

    def get_team_now(self):
        team_now = self.get_querry_all_score()
        print(team_now[0].team_now)

    def get_time_mm(self):
        time_mm = self.get_querry_all_score()
        return time_mm[0].time_mm

    def get_time_ss(self):
        time_ss = self.get_querry_all_score()
        return time_ss[0].time_ss


# Edit score teams in score_bd------------------------------>
    def update_team_now(self, var):
        score_update = "Update score set team_now = " + str(var)
        db.session.execute(score_update)
        db.session.commit()


    def add_score_team_1(self):
        add_score_team_1 = 1 + self.get_score_team_1()
        score_update = "Update score set score_team_1 = " + str(add_score_team_1)
        db.session.execute(score_update)
        db.session.commit()

    def add_score_team_2(self):
        add_score_team_2 = 1 + self.get_score_team_2()
        score_update = "Update score set score_team_2 = " + str(add_score_team_2)
        db.session.execute(score_update)
        db.session.commit()

    def put_score_team_1(self):
        put_score_team_1 = self.get_score_team_1() - 1
        score_update = "Update score set score_team_1 = " + str(put_score_team_1)
        db.session.execute(score_update)
        db.session.commit()

    def put_score_team_2(self):
        put_score_team_2 = self.get_score_team_2() - 1
        score_update = "Update score set score_team_2 = " + str(put_score_team_2)
        db.session.execute(score_update)
        db.session.commit()

    def reset_score(self):
        update_score_team_1 = "Update score set score_team_1 = 0"
        update_score_team_2 = "Update score set score_team_2 = 0"
        db.session.execute(update_score_team_1)
        db.session.execute(update_score_team_2)
        db.session.commit()

    def update_team_1_now(self, team_1, team_2):
        s = Score.query.filter_by(id=1).first()
        s.team_1_now = team_1
        s.team_2_now = team_2   
        db.session.commit()

    def update_time(self, time_mm, time_ss):
        s = Score.query.filter_by(id=1).first()
        s.time_mm = time_mm
        s.time_ss = time_ss
        db.session.commit()

    def get_team_1_now(self):
        data_team = self.get_querry_all_score()
        print(data_team[0].team_1_now)
        return data_team[0].team_1_now

    def get_team_2_now(self):
        data_team = self.get_querry_all_score()
        return data_team[0].team_2_now

    
class Team_name(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    team_1_name = db.Column(db.String(100))
    team_2_name = db.Column(db.String(100))

    def get_querry_all_team_name(self):
        return Team_name.query.all()

    def get_team_1_name(self):
        list_team_name= []
        score_team_1 = self.get_querry_all_team_name()
        for count in range(0, len(score_team_1)):
            dict_team_name = {score_team_1[count].team_1_name :  score_team_1[count].team_2_name}
            list_team_name.append(dict_team_name)
        return list_team_name