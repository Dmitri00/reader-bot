import json
import atexit
import os

class Datamodel:
    def __init__(self, database_fname):
        try:
            with open(database_fname, 'r') as f:
                self.ds = json.load(f)
        except IOError:
            self.ds = self.new_ds_dict()
        self.database_fname = database_fname
        self.store()
        atexit.register(self.store)

    def new_ds_dict(self):
        return {'users': []}

    def add_user(self, user_id):
        print(user_id)
        if user_id not in self.ds['users']:
            self.ds['users'].append(user_id)
    def remove_user(self, user_id):
        if user_id  in self.ds['users']:
            self.ds['users'].remove(user_id)
    def get_users(self):
        return self.ds['users']
    def store(self):
        print('dumping ds files')
        with open(self.database_fname, 'w') as f:
            json.dump(self.ds, f)