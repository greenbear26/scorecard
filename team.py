class Team:
    def __init__(self):
        self.hits = 0
        self.errors = 0
        self.runs = 0

    def get_hits(self):
        return self.hits

    def get_errors(self):
        return self.errors

    def get_runs(self):
        return self.runs

    def add_hit(self):
        self.hits += 1

    def add_error(self):
        self.errors += 1

    def add_run(self):
        self.runs += 1
