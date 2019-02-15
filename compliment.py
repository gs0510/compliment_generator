import random
from flask import Flask, Response


app = Flask(__name__)
ADJECTIVES_FN = 'data/adjectives.txt'
NOUNS_FN = 'data/nouns.txt'


def construct_compliment():
    compliment = ""

    with open(ADJECTIVES_FN, 'r') as f:
        adjectives = f.readlines()
        adjectives = [x.strip() for x in adjectives]

        num_compliments = random.randint(2, 4)
        compliment = ", ".join(random.sample(adjectives, num_compliments))

    with open(NOUNS_FN, 'r') as f:
        nouns = f.readlines()
        nouns = [x.strip() for x in nouns]

        compliment = compliment + " " + random.sample(nouns, 1)[0]

    return compliment


@app.route("/sms", methods=["GET", "POST"])
def sms():
    compliment = construct_compliment()

    resp = """
    <Response>
        <Message>
            Thank you, you {}!
        </Message>
    </Response>""".format(compliment)

    return Response(resp, mimetype="text/xml")


if __name__ == '__main__':
    app.run(debug=True)
