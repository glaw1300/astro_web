from flask import Flask, render_template, jsonify
import mysql.connector
import os

app = Flask(__name__)

def connect_db():
    os.system("mysql.server start")
    conn = mysql.connector.connect(user='root', database='astronomy')
    cur = conn.cursor(buffered=True)

    return conn, cur

def close_connection(cur, conn):
    cur.close()
    conn.close()

@app.route('/')
def splash_page():
    return render_template("index.html")

@app.route('/image_query')
def image_query():
    conn, cur = connect_db()

    close_connection(cur, conn)
    return render_template("image_query.html")#, headers=headers, data=data)

@app.route('/bodies')
def bodies():
    conn, cur = connect_db()

    close_connection(cur, conn)
    return render_template("bodies.html")#, headers=headers, data=data)

@app.route('/body')
def body():
    conn, cur = connect_db()

    close_connection(cur, conn)
    return render_template("body.html")#, headers=headers, data=data)

@app.route('/night')
def night():
    conn, cur = connect_db()

    close_connection(cur, conn)
    return render_template("night.html")#, headers=headers, data=data)

@app.route('/nights')
def nights():
    conn, cur = connect_db()

    close_connection(cur, conn)
    return render_template("nights.html")#, headers=headers, data=data)

@app.route('/observatory_stats')
def obs_stats():
    conn, cur = connect_db()

    close_connection(cur, conn)
    return render_template("observatory_stats.html")#, headers=headers, data=data)

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    conn, cur = connect_db()

    cur.execute("SELECT name FROM bodies")
    suggestion = cur.fetchall()
    map(lambda x: x[0], bodies)

    return jsonify(json_list=suggestion)

if __name__ == '__main__':
    app.run(debug=True)
