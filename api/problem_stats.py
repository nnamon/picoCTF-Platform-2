import api.common

def main():
    db = api.common.get_conn()
    problems = {}
    for i in db.problems.find():
        problems[i["pid"]] = i

    teams = {}
    for i in db.teams.find():
        teams[i["tid"]] = i

    problems_s = {}
    for i in problems.keys():
        problems_s[i] = {"solvers": [], "count": 0}

    for i in db.submissions.find():
        problems_s[i["pid"]]["count"] += 1
        if i["correct"]:
            problems_s[i["pid"]]["solvers"].append(teams[i["tid"]])

    print("Solved:")
    c = 1
    for i in problems.keys():
        if problems_s[i]["solvers"]:
            solvers = ", ".join(z["team_name"] for z in problems_s[i]["solvers"])
            print("%d. %s [%s] (%d/%d)" % (c, problems[i]["name"], solvers, len(problems_s[i]["solvers"]), problems_s[i]["count"]))
            c += 1

    print("\nUnsolved:")
    c = 1
    for i in problems.keys():
        if not problems_s[i]["solvers"]:
            print("%d. %s (%d)" % (c, problems[i]["name"], problems_s[i]["count"]))
            c += 1

if __name__ == "__main__":
    main()
