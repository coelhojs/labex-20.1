import requests
from json import dump
from json import loads
from pathlib import Path

def run_query(json, headers):
    request = requests.post('https://api.github.com/graphql', json=json, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}. {}"
                        .format(request.status_code, json['query'],
                                json['variables']))

query = """
query example{
  search(query:"stars:100..{STARS}", type:REPOSITORY, first:50{AFTER}){
    pageInfo{
        hasNextPage
        endCursor
    }
    nodes{
      ... on Repository{
        nameWithOwner
        url
        stargazers {
          totalCount
        }
        createdAt
        forks{
          totalCount
        }
        releases{
          totalCount
        }
        primaryLanguage{
          name
        }
      }
    }
  }
  rateLimit{
    remaining
    resetAt
  }
}
"""

first_query = query.replace("{STARS}", "*")
final_query = first_query.replace("{AFTER}", "")

json = {
    "query":final_query, "variables":{}
}

token = 'eebd3fc5d3ddded0864ea8ce8a9313ced18de9fa' #insert your token
headers = {"Authorization": "Bearer " + token} 
total_pages = 1 #GiHutb restricts queries to 100 pages (1k repositories)

print("[REPORT]: STARTING QUERIES ")
print("[REPORT]: QUERYING PAGE:" + str(total_pages))

result = run_query(json, headers)
nodes = result['data']['search']['nodes']
next_page  = result["data"]["search"]["pageInfo"]["hasNextPage"]

while (next_page and total_pages < 100):
    if(result['data']['rateLimit']['remaining'] == 0):
        print("[REPORT]: CHANGING TOKEN")
        token = '95e3bd95f13ca07fe89bf4609794765c157adca5' #due to query limits
    
    total_pages += 1

    print("[REPORT]: QUERYING PAGE:" + str(total_pages))
    
    cursor = result["data"]["search"]["pageInfo"]["endCursor"]

    next_query = first_query.replace("{AFTER}", ", after: \"%s\"" % cursor)
    
    json["query"] = next_query
    result = run_query(json, headers)
    nodes += result['data']['search']['nodes']
    next_page  = result["data"]["search"]["pageInfo"]["hasNextPage"]

    #for each block of 100 pages, qe have to make a new query (based on the number of stars)
    if(total_pages % 10 == 0): 
        if(total_pages == 100): #some workaround
            continue

        total_pages += 1
        print("[REPORT]: QUERYING PAGE:" + str(total_pages))

        first_query = query.replace("{STARS}", str(nodes[-1]['stargazers']['totalCount']))
        final_query = first_query.replace("{AFTER}", "")
        json["query"] = final_query

        result = run_query(json, headers)
        nodes += result['data']['search']['nodes']
        next_page  = result["data"]["search"]["pageInfo"]["hasNextPage"]

print("[REPORT]: END OF REQUESTS")

for node in nodes:
    output = Path(__file__).parent / "./github_5k_repositories.csv"
    with open(output, 'a') as the_file:
        the_file.write(node['nameWithOwner'] + ";" + node['url'] + ";" + str(node['stargazers']['totalCount']) + ";" +
        node['createdAt'] + ";" + str(node['forks']['totalCount']) + ";" + str(node['releases']['totalCount']) + "\n") 
