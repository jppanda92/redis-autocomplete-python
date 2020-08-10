# redis client ofr python
import redis
# flask to expose api's to outside world
from flask import Flask, request, jsonify

app = Flask("auto-complete-redis")

# creating a redis connection
r = redis.StrictRedis(host='api_redis_1', port=6379, db=0)

# route to add a value to autocomplete list
'''
FORMAT:
localhost:5000/add_word?word=<word>
'''

@app.route('/add_word')
def add_to_dict():
    try:
        name = request.args.get('word')
        n = name.strip()
        for l in range(1, len(n)):
            prefix = n[0:l]
            r.zadd('compl', {prefix: 0})
        r.zadd('compl', {n + "*": 0})
        return "Added"
    except:
        return "Addition failed"


# route to get the autocomplete suggestion
'''
FORMAT:
localhost:5000/autocomplete?query=<query you want to match>
'''


@app.route('/autocomplete')
def get_suggestions():
    prefix = request.args.get('query')
    results = []
    rangelen = 50  # This is not random, try to get replies < MTU size
    count = 5
    start = r.zrank('compl', prefix)
    if not start:
        return "[]"
    while (len(results) != count):
        range = r.zrange('compl', start, start + rangelen - 1)
        start += rangelen
        if not range or len(range) == 0:
            break
        for entry in range:
            entry = entry.decode('utf-8')
            minlen = min(len(entry), len(prefix))
            if entry[0:minlen] != prefix[0:minlen]:
                count = len(results)
                break
            if entry[-1] == "*" and len(results) != count:
                results.append(entry[0:-1])

    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
'''
Start the Application through cmd:
export FLASK_APP=/Users/jyopanda/PycharmProjects/redis-auto-complete/auto-complete-redis.py
flask run
'''