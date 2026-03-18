from flask import Flask, render_template, jsonify
import numpy as np
import os

app = Flask(__name__)

GRID = 5
gamma = 0.9
theta = 0.001

start = (0,0)
goal = (4,4)

blocks = [(1,1),(2,2),(3,3)]

actions = {
    "↑":(-1,0),
    "↓":(1,0),
    "←":(0,-1),
    "→":(0,1)
}

step_reward = -1
goal_reward = 10
wall_reward = -5

def valid(x,y):
    if x<0 or y<0 or x>=GRID or y>=GRID:
        return False
    if (x,y) in blocks:
        return False
    return True


def value_iteration():

    V = np.zeros((GRID,GRID))

    history = []

    while True:

        delta = 0
        newV = V.copy()

        for i in range(GRID):
            for j in range(GRID):

                if (i,j)==goal or (i,j) in blocks:
                    continue

                values = []

                for a in actions:

                    dx,dy = actions[a]
                    nx,ny = i+dx , j+dy

                    if not valid(nx,ny):
                        nx,ny = i,j
                        r = wall_reward
                    else:
                        r = goal_reward if (nx,ny)==goal else step_reward

                    values.append(r + gamma*V[nx][ny])

                newV[i][j] = max(values)

                delta = max(delta,abs(newV[i][j]-V[i][j]))

        V = newV

        history.append(V.copy())

        if delta < theta:
            break

    return history,V

def extract_policy(V):

    policy = [["" for _ in range(GRID)] for _ in range(GRID)]

    for i in range(GRID):
        for j in range(GRID):

            if (i,j)==goal:
                policy[i][j] = "End"
                continue

            if (i,j) in blocks:
                policy[i][j] = "X"
                continue

            best=None
            best_v=-999

            for a in actions:

                dx,dy = actions[a]
                nx,ny = i+dx , j+dy

                if not valid(nx,ny):
                    nx,ny=i,j
                    r=wall_reward
                else:
                    r=goal_reward if (nx,ny)==goal else step_reward

                val=r+gamma*V[nx][ny]

                if val>best_v:
                    best_v=val
                    best=a

            policy[i][j]=best

    return policy

def extract_path(policy):

    path=[]
    x,y=start

    visited=set()

    while (x,y)!=goal:

        path.append((x,y))
        visited.add((x,y))

        a=policy[x][y]

        dx,dy=actions[a]

        x+=dx
        y+=dy

        if (x,y) in visited:
            break

    path.append(goal)

    return path

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/run")
def run():

    history,V=value_iteration()

    policy=extract_policy(V)

    path=extract_path(policy)

    hist=[]

    for h in history:

        grid=[]

        for i in range(GRID):

            row=[]

            for j in range(GRID):

                row.append(round(float(h[i][j]),2))

            grid.append(row)

        hist.append(grid)

    return jsonify({
        "history":hist,
        "policy":policy,
        "path":path
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # 讀取環境變數 PORT，Render 會給一個
    app.run(host="0.0.0.0", port=port, debug=True)
