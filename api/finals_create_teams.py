import api.team
import api.user
import random
import string
import hashlib

teams = """dlan|DLAN|Nanyang Polytechnic (NYP)
missing|Missing|Nanyang Polytechnic (NYP)
blackshades|Bl@ck$had3s|Nanyang Polytechnic (NYP)
zerooffsec|0x0ffff5ec|Nanyang Technological University (NTU)
oneoffsec|1x0ffff5ec|Nanyang Technological University (NTU)
twooffsec|2x0ffff5ec|Nanyang Technological University (NTU)
xiaoflaggers|Xiia0F1aGGer$|National University of Singapore (NUS)
nevergonnagive|Never Gonna Give|National University of Singapore (NUS)
omegaprime|Ω'|National University of Singapore (NUS)
gandalf|Gandalf the Hacker|Ngee Ann Polytechnic (NP)
ultimatenovices|Ultimate Novices|Ngee Ann Polytechnic (NP)
jnex|J-NEX|Ngee Ann Polytechnic (NP)
fengshui|FengShui|Others (Only Students)
whitehats|Whitehats|Singapore Management University (SMU)
blackcats|Black Cats|Singapore Management University (SMU)
xiaolongbao|小笼包|Singapore Polytechnic (SP)
burdenoverflow|Burden Overflow|Singapore Polytechnic (SP)
append|.append(0);|Singapore Polytechnic (SP)
kopipacket|Kopipacket-Jr|Singapore University of Technology and Design (SUTD)
axiom|Axiom|Temasek Polytechnic (TP)
asdfghjkl|asdfghjkl|Temasek Polytechnic (TP)
teamdoughnut|Team Doughnut|Temasek Polytechnic (TP)"""

def create(user_name, team_name, school):
    random_team_pass = "".join(random.choice(string.ascii_letters) for i in range(10))
    tid = api.team.create_team({"team_name": team_name,
                                "school": school,
                                "password": random_team_pass,
                                "eligible": True})
    password = hashlib.sha384(team_name.encode("utf8")).hexdigest()[:16][::-1]
    api.user.create_user(user_name, team_name, "", "",
                         api.user.hash_password(password), tid)
    return password

def main():
    teams_l = [i.split("|") for i in teams.split("\n")]
    creds = []
    for i in teams_l:
        ps = create(*i)
        creds.append("%s|%s" % (i[0], ps))
    print("\n".join(creds))

if __name__ == "__main__":
    main()
