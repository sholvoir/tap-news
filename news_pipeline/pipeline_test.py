#!/bin/env python
from optparse import OptionParser
from datetime import datetime

from sklearn.feature_extraction.text import TfidfVectorizer

def get_args():
    parser = OptionParser(usage='news_monitor.py -d -t to')
    parser.add_option('-t', '--times', dest='times', default='-1', type='int')
    parser.add_option('-l', '--last', dest='last', default=datetime.utcnow().isoformat(timespec='seconds'))
    parser.add_option('-s', '--sleep', dest='sleep', action="store_true", default=False)
    return parser.parse_args()

def optparse_test():
    (options, args) = get_args()
    print(options)
    print(args)

def tfidf_test():
    doc1 = "I like apples. I like oranges too"
    doc2 = "I love apples. I hate doctors"
    doc3 = "An apple a day keeps the doctor away"
    doc4 = "Never compare an apple to an orange"
    documents = [doc1, doc2, doc3, doc4]
    tfidf = TfidfVectorizer().fit_transform(documents)
    pairwise_sim = tfidf * tfidf.T
    print(pairwise_sim.shape)

def tfidf_news_test():
    news1 = ' (CNN). A real estate investment startup co-founded by Jared Kushner skirted New York City laws and earned his company more money than expected when they flipped the properties, according to a report by Bloomberg.. In the company\'s first-known deal, according to Bloomberg, Cadre sold three rent-regulated buildings for $59 million in April 2017, about an 80% premium over what it paid a little more than two years earlier.. Kushner Cos., Cadre\'s operating partner at the property, "told the city the buildings had no rent-regulated tenants when applying for construction permits to update the buildings in 2015 but tax records filed later showed almost 100 such residents," . Bloomberg reported. , citing an earlier story by the Associated Press.. Additionally, Kushner, an adviser to his father-in-law, President Donald Trump, had not divested his holdings in Cadre by last December, according to Kushner\'s latest financial disclosure report.. Tax records filed by Cadre with New York City claimed the properties had no residents in rent-controlled units, according to the Associated Press, but later tax filings showed nearly 100 residents living in rent-controlled units, which would have been worth less to prospective buyers.'
    news2 = ' (CNN). Two men were taken to the hospital with serious but non-life threatening injuries after an explosion in southwest Austin, Texas, on Sunday evening, authorities said. . Police were called to the scene at 8:32 p.m., in a city that has been rattled by a series of blasts. . The two injured men were in their 20s and taken to St. David\'s South Austin Medical Center, according to an . Austin-Travis County EMS.  tweet. Both patients are in good condition, a spokesperson at the hospital told CNN. . Police and the FBI responded to the scene Sunday. There was a second item, a backpack that police were clearing, said Austin Police Chief Brian Manley. . "It\'s obvious an explosion has occurred," he said at a late Sunday briefing. . The latest explosion comes less than a week after police said three package explosions that happened over 10 days were connected. Those explosions killed a man and a teenager, and . injured two others. . The victims . in those three explosions were African-American or Hispanic..  Police have not yet discovered a motive, but have not ruled out the possibility the bombs could be hate crimes. . . It\'s not clear if Sunday\'s explosion is related to the previous events.. Manley wasn\'t taking questions, but said another briefing would take place early Monday.. "Do not touch any packages or anything that looks like a package. Do not even go near it at this time," Manley told residents. "Given the darkness we have not had an opportunity to really look at this blast site to determine what has happened.". Resident: \'It\'s concerning\'. Stan Malachowski, who lives about half a mile away, said he heard a loud explosion. . "It was loud enough to hear inside of our house with our windows and door shut. Again, airplanes go by and cars backfire so we didn\'t think much of it," . he told CNN affiliate KXAN. . "This is a quiet neighborhood. It\'s a family neighborhood. It\'s concerning." . The Sunday incident was reported on Dawn Song Drive, with police warning residents in the immediate area to stay inside their homes until morning. Regents School of Austin, a nearby private school, will open two hours late Monday for "a complete security sweep," it said in a statement. . On edge. Many in Austin have been on edge since the bombings, as some residents of color in the Texas capital say . they feel under threat.. The reward for information leading to the arrest of the person or persons responsible for the three explosions increased to a total of $115,000, authorities had announced earlier Sunday. Officials have urged residents to call in with tips to the police department, even if the information is seemingly "inconsequential.". South by Southwest wrapped up Sunday, but received a.  bomb threat Saturday, . that resulted in the cancellation of a concert featuring The Roots. . CNN\'s Janet DiGiacomo and Sheena Jones contributed to this report. '
    documents = [news1, news2]
    tfidf = TfidfVectorizer().fit_transform(documents)
    pairwise_sim = tfidf * tfidf.T
    print(pairwise_sim.A)

if __name__ == "__main__":
    tfidf_test()
