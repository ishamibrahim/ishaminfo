import datetime

import requests
import graphene
from flask import render_template
from flask_graphql import GraphQLView
from graphene import ObjectType, Int, String, List, Schema, Field

from mutations import Mutation
from queries import Query
from main import app

@app.route('/')
def home_route():
    user = {
        "fname": "Isham",
        "lname": "Ibrahim",
        "email": "eyash.27@gmail.com",
        "phone": "+918970236033",
        "website": "ishamibrahim.info",
        "designation": "Backend Developer/Lead",
        "brief": """I am a Software Developer hailing from India. With over a decade of experience in the industry 
        crafting robust and scalable software, I possess a deep understanding of the working of computer software 
        and excel in architecting and developing complex applications""",
        "subbrief": """Results oriented with a proven track record of crafting high performant, 
        scalable applications using Python and Go. I excel in designing and developing robust backend systems, 
        APIs and microservices. Adept and leveraging strengths of each language and tool to deliver optimal solution.
        """,
        "education": [
            {"from": 2008,
             "to": 2012,
             "degree": "Bachelors in Computer Science Engineering",
             "university": "Visvesvaraya Technological University",
             "place": "Karnataka, India",
             "brief": """Obtained a bachelors degree in Computer Science Engineering with a strong foundation 
             in programming, data structures and algorithms. Gained knowledge on database design and SQL 
             with fundamentals of Object Oriented Programming and software development methodologies such as agile 
             and waterfall."""
             },
        ]
    }


    context = {
        "resumefile": "airesume_202406.pdf",
        "utc_dtnow": datetime.datetime.now().strftime('%d, %b %Y'),
        "skills": ["python", "go","django","django rest framework","mysql/postgres","aws","docker","celery","redis",
                   "mongodb", "dynamodb", "selenium", "github", "jenkins", "virtualization", "agile"],
        "links": [
            {
                "site": "github",
                "bw_logo": "fa-brands fa-github-alt",
                "href": "https://github.com/ishamibrahim"
            },
            {
                "site": "twitter",
                "bw_logo": "fa-brands fa-x-twitter",
                "href": "https://x.com/Eyashuddin"
            },
            {
                "site": "linkedin",
                "bw_logo": "fa-brands fa-linkedin-in",
                "href": "https://www.linkedin.com/in/isham-ibrahim-47963156/"
            },
            {
                "site": "bitbucket",
                "bw_logo": "fa-brands fa-bitbucket",
                "href": "https://bitbucket.org/ishamibrahim"
            },
        ]
    }
    experience = [
        {
            "designation": "Technical Lead",
            "org": "Space Inventive",
            "from": 2024,
            "to": "Present",
            "region": "Hyderabad, India",
        },
        {
            "designation": "Lead developer",
            "org": "Alcor Solutions",
            "from": 2023,
            "to": 2024,
            "region": "Remote",
        },
        {
            "designation": "Software Engineer Senior",
            "org": "Akamai Technologies",
            "from": 2018,
            "to": 2023,
            "region": "Bangalore, India",
        },
        {
            "designation": "Senior Engineer",
            "org": "Accion Labs",
            "from": 2017,
            "to": 2018,
            "region": "Bangalore, India",
        },
        {
            "designation": "Backend Engineer",
            "org": "SignEasy",
            "from": 2016,
            "to": 2017,
            "region": "Bangalore, India",
        },
        {
            "designation": "Software Developer",
            "org": "Unicourt India",
            "from": 2012,
            "to": 2016,
            "region": "Mangalore, India",
        }
    ]
    return render_template('index.html', user=user, context=context, experience=experience)


@app.route('/sections')
def sections():
    return render_template('sections.html')


schema = Schema(query=Query, mutation=Mutation)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Enables GraphQL interface for testing
    )
)

if __name__ == '__main__':
    app.run(debug=True)