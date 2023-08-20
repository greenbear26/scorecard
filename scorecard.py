class Scorecard:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.inning = 1
        self.inning_half = "Top"
        self.outs = 0
        self.strikes = 0
        self.balls = 0

    def _batter(self):
        return input("Who is the batter? ")

    def _record_hit(self, batter):
        hit_type = input("What type of hit was it? (1B, 2B, 3B, HR) ")
        hit_description = ""
        if hit_type == "1B":
            hit_description = batter + " singles."
        elif hit_type == "2B":
            hit_description = batter + " doubles."
        elif hit_type == "3B":
            hit_description = batter + " triples."
        elif hit_type == "HR":
            hit_description = batter + " homers."
        return hit_description

    def _record_out(self, batter):
        person = input("Who got out? Batter(B), Runner(R) ")
        if person == "B":
            return self._record_batter_out(batter)
        elif person == "R":
            runner = input("Who is the runner? ")
            return self._record_runner_out(runner)

    def _record_batter_out(self, batter):
        out_type = input("What type of out was it? (Groundout(G), Flyout(F), Fielder's Choice(FC), Double Play(DP), Triple Play(TP)) ")
        out_description = ""
        if out_type == "G":
            out_description = batter + " grounds out."
        elif out_type == "F":
            out_description = batter + " flies out."
        elif out_type == "FC":
            out_description = batter + " reaches on a fielder's choice."
        elif out_type == "DP":
            out_description = batter + " hits into a double play."
        elif out_type == "TP":
            out_description = batter + " hits into a triple play."
        return out_description

    def _record_runner_out(self, runner):
        out_type = input("What type of out was it? (Caught Stealing(CS), Forced Out(FO), Tagged Out(TO)) ")
        base = input("What base was the runner out at? (1B, 2B, 3B, Home) ")
        out_description = ""
        if out_type == "CS":
            out_description = runner + " is caught stealing " + base + "."
        elif out_type == "FO":
            out_description = runner + " is forced out at " + base + "."
        elif out_type == "TO":
            out_description = runner + " is tagged out at " + base + "."
        return out_description

    def _record_error(self):
        fielder = input("Who made the error? ")
        error_type = input("What type of error was it? (Fielding(F), Throwing(T)) ")
        error_description = ""
        if error_type == "F":
            error_description = fielder + " commits a fielding error."
        elif error_type == "T":
            error_description = fielder + " commits a throwing error."
        return error_description

    def _record_run(self):
        run_scorer = input("Who scored? ")
        run_description = run_scorer + " scores."
        return run_description

    def _check_outs(self):
        if self.outs == 3:
            if self.inning_half == "Top":
                self.inning_half = "Bottom"
            elif self.inning_half == "Bottom":
                self.inning_half = "Top"
                self.inning += 1
            self.outs = 0

    def _record_play(self):
        hit_play = ""
        outs = [""]
        errors = [""]
        runs = [""]

        batter = self._batter()

        hit = input("Did the batter get a hit? Y/N ")
        if hit == "Y":
            hit_play = self._record_hit(batter)

        out = input("Did someone get out? Y/N ")
        while out == "Y":
            outs.append(self._record_out(batter))
            out = input("Did someone else get out? Y/N ")

        error = input("Did someone make an error? Y/N ")
        while error == "Y":
            errors.append(self._record_error())
            error = input("Did someone else make an error? Y/N ")

        run = input("Did someone score? Y/N ")
        while run == "Y":
            runs.append(self._record_run())
            run = input("Did someone else score? Y/N ")

        play = ""
        team = None
        if self.inning_half == "Top":
            team = self.away_team
        elif self.inning_half == "Bottom":
            team = self.home_team


        if hit == "Y":
            play += "\n" + hit_play
            team.add_hit()

        for out in outs:
            play += "\n" + out
            self.outs += 1

        for error in errors:
            play += "\n" + error
            team.add_error()

        for run in runs:
            play += "\n" + run
            team.add_run()
        
        self._check_outs()

        state = input("Do you want to see the current game state? Y/N ")
        if state == "Y":
            play += "\n\n" + self.return_game_state()

        return play

    def record_pitch(self):
        pitch = input("What is the pitch result? (Strike/Foul(S), Ball(B), In Play(P)) ")

        if pitch == "S":
            self.strikes += 1
            if self.strikes == 4:
                self.strikes = 0
                self.balls = 0
                self.outs += 1
                return "Strikeout!"
            else:
                return "Strike!"
        elif pitch == "B":
            self.balls += 1
            if self.balls == 4:
                self.strikes = 0
                self.balls = 0
                return "Walk!"
            else:
                return "Ball!"
        elif pitch == "P":
            self.strikes = 0
            self.balls = 0
            return self._record_play()

    def return_game_state(self):
        state = ""
        state += "Inning: " + self.inning_half + " " + str(self.inning) + "\n"
        state += "Outs: " + str(self.outs) + "\n"
        state += "Strikes: " + str(self.strikes) + "\n"
        state += "Balls: " + str(self.balls) + "\n"
        state += "Score: " + "Home: " + str(self.home_team.runs) + " - " + "Away: " + str(self.away_team.runs)
        return state
