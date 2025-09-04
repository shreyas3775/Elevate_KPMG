from ddgs import DDGS
import duckdb

def search_fact(fact):
    web_results = []

    with DDGS() as ddgs_func:
        results = ddgs_func.text(fact, max_results=5)

        #check through the results and strip the result
    for result in results:
        url = result["href"]
        url_front = url.split("://")[-1]
        url_domain = url_front.split("/")[0]
        web_results.append(url_domain.replace("www.", ""))
    
    #now we will check to see if there is a match for any of the websites in the data base and if there is return its credibility score
    my_conn = duckdb.connect("credible_domains.duckdb")

    #print(web_results)
    cred = []
    for result in web_results:
        rows = (my_conn.execute('SELECT rank FROM domains WHERE url = ?', [result]).fetchall())

        if rows:
            cred.append(rows[0][0])
        else:
            cred.append(0)
    
    #find the average value and if its greater than or equal to 3 say yay for now
    average = sum(cred) / len(cred)

    print("The fact is: " + fact)
    print("The credibility rating is: " + str(average))
    if average >= 3:
        print("The information found appears to be credible.")
    else:
        print("The information appears to be found from a mix of less credible sites, additional research would be beneficial")
    # print(cred)
    
if __name__ == "__main__":
    fact1 = "eating vegetables is really important"
    fact2 = "Electroconvulsive therapy (ETC) can greatly and rapidly improve severe symptoms of severe depression"
    fact3 = "blueberries are peaches"

    search_fact(fact1)
    search_fact(fact2)
    search_fact(fact3)
