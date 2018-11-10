# You are in charge of a display advertising program. Your ads are displayed on websites all over the internet. You have some CSV input data that counts how many times you showed an ad on each individual domain. Every line consists of a count and a domain name. It looks like this:

counts = ["900,google.com",
          "60,mail.yahoo.com",
          "10,mobile.sports.yahoo.com",
          "40,sports.yahoo.com",
          "300,yahoo.com",
          "10,stackoverflow.com",
          "2,en.wikipedia.org",
          "1,es.wikipedia.org",
          "1,mobile.sports"]


# Write a function that takes this input as a parameter and returns a data structure containing the number of hits that were recorded on each domain AND each domain under it. For example, an impression on "mail.yahoo.com" counts for "mail.yahoo.com", "yahoo.com", and "com". (Subdomains are added to the left of their parent domain. So "mail" and "mail.yahoo" are not valid domains.)

# Sample output (in any order):


# getTotalsByDomain(counts)
# 1320    com
#  900    google.com
#  410    yahoo.com
#   60    mail.yahoo.com
#   10    mobile.sports.yahoo.com
#   50    sports.yahoo.com
#   10    stackoverflow.com
#    3    org
#    3    wikipedia.org
#    2    en.wikipedia.org
#    1    es.wikipedia.org
#    1    mobile.sports
#    1    sports


#  "300,yahoo.com",

def getTotalsByDomain(counts):
    domain_hit_mapping = dict()

    for count in counts:
        hit, url = count.split(",")
        if domain_hit_mapping.get(url):
            domain_hit_mapping[url] += int(hit)
        else:
            domain_hit_mapping[url] = int(hit)
        while url:
            tmp = url.split(".", maxsplit=1)
            #             [yahoo, com]
            if len(tmp) <= 1:
                break
            else:
                url = tmp[-1]
            #                 com
            if domain_hit_mapping.get(url):
                domain_hit_mapping[url] += int(hit)
            else:
                domain_hit_mapping[url] = int(hit)

    return domain_hit_mapping

print(getTotalsByDomain(counts))