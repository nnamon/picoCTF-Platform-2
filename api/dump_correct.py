import api.problem
import json
from bson import json_util
import time
import api.team

while True:
	l = api.problem.get_submissions(correctness=True)	
	for i in l:
		i['key'] = None
		i['team_name'] = api.team.get_team(tid=i['tid'])['team_name']
		i['problem_name'] = api.problem.get_problem(pid=i['pid'])['name']
	data = json.dumps(l, default=json_util.default)
	open("/srv/http/ctf/score.json", 'w').write(data)
	time.sleep(3)

