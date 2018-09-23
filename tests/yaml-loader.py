
import yaml

with open("tests/fixtures/example.yml", 'r') as stream:
    try:
        data=yaml.load(stream)
        for groupKey, group in data['mqtt'].items():
            for buttons in group:
                for buttonKey, button in buttons.items():
                    print(buttonKey,' Data: ',buttons[buttonKey]['id'],buttons[buttonKey]['title'])
    except yaml.YAMLError as exc:
        print(exc)
