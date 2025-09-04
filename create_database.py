import duckdb

def create_db():
    #creating duckdb data base
    my_conn = duckdb.connect(database="credible_domains.duckdb")

    #this will currently be a small sample set that contains some website domains that we will determine
    # the relative credibility for
    #create table
    my_conn.execute("CREATE table domains (id INTEGER, url VARCHAR, rank INTEGER)")

    #ADD IN OUR RELATIVE DOMAINS AND THEIR CREDIBILITIES FOR A TEST/TRAINING SET, IF THIS WAS LARGER WE WOULD ADD MORE
    my_conn.execute("INSERT into domains VALUES (1, 'quora.com', 1), (2, 'reddit.com', 1), (3, 'mayoclinic.org', 5), (4, 'britannica.com', 5), (5, 'en.wikipedia.org', 3), (6, 'yahoo.com', 3), (7, 'quoradigest.com', 1), (8, 'webmd.com', 4), (9, 'medicinenet.com', 3), (10, 'nutritionsource.hsph.harvard.edu', 5), (11, 'mealmastermind.com', 2), (12, 'ucfhealth.com', 4), (13, 'pmc.ncbi.nlm.nih.gov', 5), (14, 'psychiatry.org', 5), (15, 'my.clevelandclinic.org', 5), (16, 'sciencedirect.com', 3), (17, 'inquisicook.com', 1), (18, 'mediterraneantaste.com', 1), (19, 'twopeasandtheirpod.com', 1), (20, 'facebook.com', 1)")

    my_conn.close()
if __name__ == "__main__":
    create_db()