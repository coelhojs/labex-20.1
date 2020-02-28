import requests
from json import dump
from json import loads

def run_query(json, headers): # A simple function to use requests.post to make the API call. 

    request = requests.post('https://api.github.com/graphql', json=json, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}. {}"
                        .format(request.status_code, json['query'],
                                json['variables']))

query = """
query example{
  search(query:"stars:>100", type:REPOSITORY, first:10{AFTER}){
    pageInfo{
        hasNextPage
        endCursor
    }
    nodes{
      ... on Repository{
        nameWithOwner
      }
    }
  }
}
"""

finalQuery = query.replace("{AFTER}", "")

json = {
    "query":finalQuery, "variables":{}
}

token = '' #insert your token
headers = {"Authorization": "Bearer " + token} 

total_pages = 1

result = run_query(json, headers)

nodes = result['data']['search']['nodes']
next_page  = result["data"]["search"]["pageInfo"]["hasNextPage"]

#paginating
while (next_page and total_pages < 3):
    total_pages += 1
    cursor = result["data"]["search"]["pageInfo"]["endCursor"]
    next_query = query.replace("{AFTER}", ", after: \"%s\"" % cursor)
    json["query"] = next_query
    result = run_query(json, headers)
    nodes += result['data']['search']['nodes']
    next_page  = result["data"]["search"]["pageInfo"]["hasNextPage"]

#saving data
for node in nodes:
    with open("/home/laertexavier/Repositories/repos.csv", 'a') as the_file:
        the_file.write(node['nameWithOwner'] + "\n") 
