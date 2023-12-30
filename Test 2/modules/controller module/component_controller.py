from component import Component
import sqlite3

class ComponentController:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        
def controleer_component(component):
            componenten = {
                'landmacht': 1,
                'zeemacht': 2,
                'luchtmacht': 3,
                'medisch component': 4
                }

            component = component.lower()
            if component in componenten:
                return componenten[component]
            else:
                print("U kunt enkel kiezen tussen land-, zee-, lucht- of medisch component")
                return None

            