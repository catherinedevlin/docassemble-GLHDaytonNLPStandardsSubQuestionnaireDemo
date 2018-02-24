import os
import re
import string

template = string.Template('''
# This sub-questionnaire has not yet been written!
# Please submit a fixed version 
# [here](${github_path}).
---
question: What city do you live in?
field: ${county}_cities
buttons:
  - city 1
  - city 2
  - etc.
---
''')

github_path_template = string.Template('https://github.com/catherinedevlin/docassemble-GLHDaytonNLPStandardsSubQuestionnaireDemo/blob/master/docassemble/GLHDaytonNLPStandardsSubQuestionnaireDemo/data/questions/${county}-cities.yml')

questionnaire_path=os.path.join('..', 'docassemble', 'GLHDaytonNLPStandardsSubQuestionnaireDemo',
                           'data', 'questions')
master_path = os.path.join(questionnaire_path, 'eviction_master.yml')

questionnaire_name_pattern = re.compile(r'  \- (?P<filename>(?P<county>\w+)\-cities.yml)\b')

with open(master_path) as infile:
    for match in questionnaire_name_pattern.finditer(infile.read()):
        subpath = os.path.join(questionnaire_path, match.group('filename'))
        if not os.path.exists(subpath):
            with open(subpath, 'w') as outfile:
                github_path = github_path_template.substitute(county=match.group('county'))
                outfile.write(template.substitute(county=match.group('county'), github_path=github_path))
