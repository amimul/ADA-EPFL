import pyLDAvis
import re
pos_re = re.compile(r'/(NOUN|ADJ|VERB|ADV)')

import numpy as np
def extract_dists(model, finalDf,corpus, dictionary):
    data = pyLDAvis.gensim._extract_data(model,corpus,dictionary)
    vocab = data['vocab'] = [pos_re.sub('', t).replace('_', ' ') for t in data['vocab']]
    vis_data = pyLDAvis.prepare(**data)
    vis_topic_order = vis_data.topic_order
    new_order = np.array(vis_topic_order) - 1
    topic_ids = range(1, len(new_order) + 1)
    data['topic_term_dists'] = pd.DataFrame(data['topic_term_dists'].T, index=vocab)[new_order]
    data['topic_term_dists'].columns = topic_ids
    data['doc_topic_dists'] = pd.DataFrame(data['doc_topic_dists'], index=finalDf.index)[new_order]
    data['doc_topic_dists'].columns = topic_ids
    if vis_data:
        data['vis'] = vis_data
    return data



def topics_for(doc_name, model_data):
    doc_dist = model_data['doc_topic_dists']
    return doc_dist.ix[doc_name].sort_values(ascending=False)

def _sort_cols(df, cols):
    res = df[cols].apply(lambda probs: probs.sort_values(ascending=False).index)
    return res.reset_index(drop=True)

def top_topic_terms(topic_ids,model_data):
    topic_term_dists = model_data['topic_term_dists']
    return _sort_cols(topic_term_dists, topic_ids)

def top_docs(topic_ids,model_data):
    doc_topic_dists = model_data['doc_topic_dists']
    return _sort_cols(doc_topic_dists, topic_ids)

def top_term_topics(term,model_data,sort=True):
    topic_term_dists = model_data['topic_term_dists']
    if sort:
        df = topic_term_dists.T[term].sort_values(ascending=False)
    else:
        df = topic_term_dists.T[term]
    return df#.reset_index(drop=True)

def all_top_terms(model_data):
    topic_term_dists=model_data['topic_term_dists']
    return top_topic_terms(topic_term_dists.columns)

def topic_docs(topic_id,model_data):
    doc_topic_dists = model_data['doc_topic_dists']
    return doc_topic_dists[topic_id].sort_values(ascending=False)

import collections
from collections import OrderedDict
def create_mapping_dict(lda_data,finalDf,lda,dictionary):
    input_categories = lda_data['doc_topic_dists']


    compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
    L = len(lda_data['doc_topic_dists'].columns)
    matchDict = OrderedDict(zip(list(range(0, L)), list([None for i in range(0, L)])))
    to_match = list(matchDict.keys())
    nb_wrong = 0
    nb_right = 0
    for ind, row in input_categories.iterrows():
        r_list = list(row.values)
        r_list = list(np.around(np.array(r_list), decimals=4))

        row = pd.Series(r_list, row.index)

        match_row = list(OrderedDict(
            lda.get_document_topics(dictionary.doc2bow(list(eval(finalDf.finalIngredients[ind]))),
                                    minimum_probability=0)).values())
        match_row = list(np.around(np.array(match_row), decimals=4))
        for indm, m in enumerate(match_row):
            if r_list.count(m) == 1:
                key = indm
                index_match = row[row == m].keys()[0]
                if matchDict[key] != None:

                    if matchDict[key] != index_match:

                        nb_wrong = nb_wrong + 1
                    else:
                        nb_right = nb_right + 1

                else:

                    matchDict[key] = index_match

                break
    print("misses: " + str(nb_wrong / (nb_right + nb_wrong)))

    return matchDict

import pandas as pd
def map_series(s,correspond_dict):
    #s has keys from gensim
    #set these to the ones from pyLDA vis
    new = pd.Series(list(s.values),list(correspond_dict.values()))
    return new




