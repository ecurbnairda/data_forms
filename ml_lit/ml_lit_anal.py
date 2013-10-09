# %load_ext autoreload
# %autoreload 2


import pandas as pd
import re
import os
import networkx as nx
import numpy as np
import operator
import collections
import math
import itertools
import matplotlib.pyplot as plt    

def load_records(data_dir):
    """Return dataframe of all records, 
    with new column of cited references as list"""

    # I saved all the WoS full records for 'machine learning'
    files = os.listdir(data_dir)
    wos_df  = pd.concat([pd.read_table(wos_df, sep='\t', index_col = False) 
        for wos_df in [data_dir+f for f in files if f.count('.txt')>0]])
    wos_df  =  wos_df.drop_duplicates()

    #fix index
    index = range(0, wos_df.shape[0])
    wos_df.index = index

    #to get all cited refs
    if wos_df.columns.tolist().count('CR') > 0:
        cited_refs = [list(re.split(pattern='; ', 
            string=str(ref).lower().lstrip().rstrip())) for ref in wos_df.CR]
        # add as column to dataframe
        wos_df['cited_refs'] = cited_refs

    # normalise authors
    if wos_df.columns.tolist().count('AF') > 0:
        wos_df.au = [str(au).lower().lstrip().rstrip() for au in wos_df.AF]

    return wos_df

def clean_fields(wos_df):

    """ Returns dataframe with a new field 'field' that lists
    the fields for each reference"""

    wos_df['fields'] = wos_df.SC.dropna().str.lower().str.split('; ')
    return wos_df

def clean_topics(wos_df):
    
    """Wos.DE field has a mixture of topics and techniques.
    -------------------------------------
    Returns a cleaned-up, de-pluralised list version of all the topics and techniques
    """

    wos_df['topics'] = wos_df.DE.dropna().str.lower().str.strip().str.replace('\(\w+ \)', '').str.replace('($  )|(  )', ' ')
    # wos_df['topics'] = wos_df.topics.str.replace("[\(\](\w+ ?)+[\)\]]\W*",  '')
    wos_df.topics  = wos_df.topics.str.replace('svm', 'support vector machine')
    wos_df.topics  = wos_df.topics.str.replace('support vector machine(\w*)', 
        'support vector machine')
    wos_df.topics = wos_df.topics.str.replace('(artificial neural network)|(neural networks)|(neural net\b)', 
        'neural network')
    wos_df.topics = wos_df.topics.str.replace('decision tree(.*)', 'decision tree')
    wos_df.topics = wos_df.topics.str.replace('random forest(\w+)', 'random forest')
    # Web of science topics often have  a bracket expansion
    wos_df['topics'] = wos_df.topics.str.replace("(\w+)\W*[\[\(].+[\)\]]\W*", '\\1 ')
    wos_df.topics = wos_df.topics.str.split('; ')
    return wos_df

def keyword_counts(wos_df):

    """ Returns a dictionary with keyword counts"""
    
    de_all = [d for de in wos_df.topics.dropna() for d in de]
    key_counts = collections.Counter(de_all)
    return key_counts

def citation_counts(wos_df):

    """Returns a dictionary with citations in the cited references counted"""

    all_refs = [ref for refs in wos_df.cited_refs for ref in refs]
    ref_collection = collections.Counter(all_refs)
    return ref_collection


def manual_topic_classifier(wos_df, existing_topic_classes, topic_counts_sorted, start = 0, count=100, ):
    
    """Returns a dictionary with topics classified as techniques
    or not. Asks the user to classify them by hand, starting with the most frequent
    Parameters
    ------------------
    count: how many to classify
    start: where in the list to start
    """

    if existing_topic_classes is None:
        existing_topic_classes = dict()
    if topic_counts_sorted is None:
        de_all = [d for de in wos_df.topics.dropna() for d in de]
        de_set = set(de_all)
        de_counts = {de:de_all.count(de) for de in de_set}
        topic_counts_sorted = sorted(de_counts.iteritems(), 
            key = operator.itemgetter(1), reverse=True)
    topic_classes = {t:raw_input('\n' + t+ ' is technique? ')  for t, v in 
        topic_counts_sorted[start:start+count] if not existing_topic_classes.has_key(t)}
    existing_topic_classes.update(topic_classes)
    return existing_topic_classes


def coword_matrix_years(wos_df, start_year, end_year, keys):

    """
    Return the coword matrix for a year range for the given set of keys

    Parameters
    ---------------------------------
    wos_df: references dataframe
    start_year: include references starting from this year
    end_year: references up to but including this year
    keys: list of keys to include in the matrix

    """
    wos_df_delim = wos_df[(wos_df.PY>= start_year) & (wos_df.PY <end_year)]
    coword_m = coword_matrix(wos_df_delim, keys)
    return coword_m

def coword_matrix(wos_df, keys):

    """ Implementation of Callon style co-word analysis of  the keywords field
    
    Parameters
    ------------------------------------------------
    wos_df: the  literature DataFrame -- doesn't need to be WoS, as long as it has the right fields
    keys: list of keys to count
    """

    # create reference-topic matrix
    topics = wos_df.topics
    #drop references that have no topics
    topics = topics.dropna()
    doc_count = len(topics)
    dtm = np.zeros((doc_count, len(keys)))

    #nested loops here but 
    #I couldn't get the list comprehensions working properly
    
    for row in range(0, doc_count):
        top = topics.iget(row)
        for topic in top:
            if keys.count(topic) >0:
                # set all the topics found for this reference to 1
                dtm[row, keys.index(topic)] = 1

    #to create coword matrix, use matrix dot product
    cow_m = np.dot(np.transpose(dtm), dtm)
    cow_wos_df = pd.DataFrame(cow_m, columns=keys, index=keys)
    return cow_wos_df

def coword_network(mesh_df, start, end,topic_count=0): 
        """
        constructs a coword network for the years supplied; nodes have an attribute 'topic'
        
        Parameters
        ----------------
        mesh_df: a dataframe with at least the topics and years columns
        start: start year
        end: end year
        topic_count: the number of the topics to use (not too big, otherwise coword matrix will be huge
        """

        # determine the number of topics to count
        all_topics = [t for top in mesh_df.topics.dropna() for t in top]
        topic_collection = collections.Counter(all_topics)
        if topic_count > 0 and topic_count < len(topic_collection):
            common_topics = [k[0] for k in topic_collection.most_common(topic_count)]
        else:
            common_topics = sorted(topic_collection.keys())

        cow_df = coword_matrix_years(mesh_df, start, end, common_topics)
        cow_nx = nx.from_numpy_matrix(cow_df.as_matrix())
        col_names = cow_df.columns.tolist()
        labels = {col_names.index(l):l for l in col_names}

        nx.set_node_attributes(cow_nx, 'topic', labels)
        return cow_nx


def cofield_matrix(wos_df, fields):

    """ Implementation of Callon style co-word analysis of  the 
    Wos DE field -- the keywords field in the database
    
    Parameters
    ------------------------------------------------
    wos_df: the WoS literature DataFrame
    fields: fields to use
    """

    fields_all = wos_df.fields
    # create document term matrix of keywords
    fields_all = fields_all.dropna()
    cofield = np.zeros((len(fields_all), len(fields)))

    # hate doing these nested for loops but 
    #I couldn't get the list comprehensions working properly
    
    for row in range(0, len(fields_all)):
        top = fields_all.iget(row)
        for topic in top:
            if fields.count(topic) >0:
               cofield[row, fields.index(topic)] = 1
    
    #to create cofieldord matrix, use matrix dot product
    print('finished matrix ... ')
    cofield_m = np.dot(np.transpose(cofield), cofield)
    np.fill_diagonal(cofield_m, 0)
    cofield_wos_df = pd.DataFrame(cofield_m, columns=fields, index=fields)
    return cofield_wos_df


def inclusion_score(cow_wos_df, key1, key2, key_counts):
    """ Calculates  the inclusion score (conditional probability?) of key1
    given the presence of key2 (or vice versa)"""

    c_ij = cow_wos_df[key1][key2]
    I_ij = c_ij/min(key_counts[key1],  key_counts[key2])
    return I_ij

def inclusion_matrix(cow_m):
    """ Calculates  the inclusion matrix for a coword matrix. 
    Inclusion score is conditional probability of key1
    given the presence of key2 (or vice versa)"""

    keycounts = cow_m.diagonal().tolist()[0]
    # print(len(keycounts))
    # print(cow_m.shape)
    minimum_matrix = [min(p,q) for p,q in itertools.product(keycounts,repeat=2)]
    print(len(minimum_matrix))
    minimum_matrix = np.array(minimum_matrix, dtype=np.float16).reshape(cow_m.shape)
    I_ij = cow_m/minimum_matrix
    return I_ij

def inclusion_matrix_to_edge_weights(I_ij):
    """ Reshapes an inclusion matrix to 
    the tuple-value dictionary needed by networkx
    """
    return {(x,y):I_ij[x,y]   for x in range(0,I_ij.shape[0]) for y in range(0, I_ij.shape[1]) if I_ij[x,y] > 0}

def proximity_score(cow_wos_df, key1, key2, key_counts, article_count):
    """ Calculates  the proximity score  of key1
    given the presence of key2 (or vice versa); 
    The mediator and peripheral keywords pulled
    out by Pg represent minor but potentially growing areas."""

    c_ij = cow_wos_df[key1][key2]
    p_ij = c_ij/(key_counts[key1] * key_counts[key2]) * article_count
    return p_ij

def proximity_matrix(cow_m):
    """ Calculates  the proximity score  of key1
    given the presence of key2 (or vice versa); 
    The mediator and peripheral keywords pulled
    out by Pg represent minor but potentially growing areas."""

    return 'tba'

def equivalence_score(cow_wos_df, key1, key2, key_counts):
    """ Calculates  the equivalence score (mutual inclusion) of key1
    given the presence of key2 (or vice versa); Eghas a value between 0 and 1. Similar to ( l ) E
    measures the probability of word i appearing 
    simultaneously in a document set indexed by word j
    and, inversely, the probability of word j ifword i appears, given the respec-
    tive collection frequencies of the two words."""   

    c_ij = cow_wos_df[key1][key2]
    Equiv_ij  = c_ij**2/(key_counts[key1] * key_counts[key2])
    return Equiv_ij

def fast_equivalence_matrix(cow_m):
    """ Constructs the equivalence matrix for all combinations of key words; 
    This is following (Callon, 1991).

    Parameters
    ---------------------------------------------------------------- 
    cow_m: the matrix of co-word counts
"""

    ecow = cow_m**2
    colsums = cow_m.diagonal()
    for i in range(0,cow_m.shape[0]):
        for j in range(0, cow_m.shape[1]):
            ecow[i,j] = ecow[i,j]/(colsums[i]*colsums[j])
   
    # replace NaN with zero -- this happens because all topics are used in topic list, 
    # but particular years may not have that topic
    isnan = np.isnan(ecow)
    ecow[isnan] = 0

    return ecow       


def equivalence_matrix(cow_wos_df, key_counts):
    """ Constructs the equivalence matrix for all combinations of key words; 
    This is following (Callon, 1991).

    Parameters
    ---------------------------------------------------------------- 
    cow_wos_df: the matrix of co-word counts
    key_counts: the list of keyword counts
    """

    keys = cow_wos_df.columns.tolist()
    key_combinations = [(k1, k2) for k1 in 
        cow_wos_df.columns for k2 in cow_wos_df.index if k1 != k2]
    ecow = np.zeros(cow_wos_df.shape)
    for key1_key2 in key_combinations:
        key1, key2 = key1_key2
        if (keys.count(key1) > 0)  & (keys.count(key2)> 0):
            index1 = keys.index(key1)
            index2 = keys.index(key2)
            escore = equivalence_score(cow_wos_df, key1, key2, key_counts)
            ecow[index1, index2] = escore

    eqcow_wos_df = pd.DataFrame(ecow, 
        columns=cow_wos_df.columns, index = cow_wos_df.index)
    return eqcow_wos_df

def discipline_techniques_graph(wos_df):

    """ Constructs a bipartite graph from techniques 
    to discipline_techniques_graph.
    It assumes that dataframe already has a cleaned up topics field.
    Preferably it has already been cut down just to techniques
    ------------------------------
    Returns graph
    """

    wos_df['SC_l'] = wos_df.SC.str.lower()
    techn_graph = nx.DiGraph()
    [techn_graph.add_edge(te, f) for t,f in zip(wos_df.topics, wos_df.SC_l) if t is not np.nan  for te in t]
    return techn_graph

def trim_degrees(graph, degree=1):

    """ Trims all nodes with degree less than the parameter.
    Returns the trimmed graph 
    """
    graph_trimmed = graph.copy()
    degrees = nx.degree(graph_trimmed)
    [graph_trimmed.remove_node(n) for n in graph_trimmed.nodes() if degrees[n] <= degree]
    return graph_trimmed

def sorted_map(keyval): 

    """ Takes a key-value dictionary and 
    sorts it according to value counts
    Returns a list of key-value tuples
    """
    map_sorted = sorted(keyval.iteritems(), key=lambda (k, v): (-v, k))
    return map_sorted

def trim_edges(graph, weight=1):

    """ Trims all edges with degree less than the parameter.
    Parameters
    -----------------------------
    graph: this graph will have edges taken from it
    weight: remove edges with weight less than this
    """

    [graph.remove_edge(f,to) for f, to, edata in graph.edges(data=True) if edata['weight']<weight]
    return graph

def island_method(graph, iterations=5):
    """ 
    This comes the SNA book -- a way to show only those bits of the network
    that are strongly connected

    """

    weights = [edata['weight'] for f, to, edata in graph.edges(data=True)]
    mn = int(min(weights))
    mx = int(max(weights))
    step = int((mx-mn)/iterations)
    return [[threshold, trim_edges(graph, threshold)] for threshold in range(mn, mx, step)]

def keyword_years(wos_df, keyword):

    """ Returns a DataFrame with publication years and 
    records containing the keyword
    
    Parameters
    -------------------------------
    wos_df: WoS references
    keyword: the one sought

    """
    keyword = keyword + '(s)?'
    top_py_wos_df = wos_df[['topics', 'PY', 'DE']].dropna()
    key_wos_df = top_py_wos_df[top_py_wos_df.DE.str.contains(keyword, 
        case=False)]
    return key_wos_df

def find_author(wos_df, author):

    """ Return WoS records that include that author somewhere
    in the author field.

    Parameters
    -------------------------------
   wos_df: WoS references
   author:
    """
    au = wos_df.AU.dropna()
    found= au[au.str.contains(author, case=False)==True].index
    return wos_df.ix[found]


def find_citation(wos_df, ref):
    
    """ Returns all the records that cite the reference

    Parameters
    -------------------------
    wos_df: WoS references
    ref: the cited reference expected in 'author year' format
    """
    
    ref = ref.lower()
    ref_parts = ref.split(' ')
    ref_auth  = ref_parts[0]
    ref_year  = ref_parts[1]
    ref_other = ''
    if len(ref_parts)  > 2:
        ref_other = ref_parts[2]
    citing_refs = [ut for (refs,ut) in zip(wos_df['cited_refs'], wos_df.index.tolist()) for r in refs if  (ref_auth in r) & (ref_year in r) & (ref_other in r) ]
    return wos_df.ix[citing_refs]

def draw_network_by_years(df, start_year, end_year, draw, trim):

    """ Constructs and draws the co-word networks for the years
    Parameters
    -----------------------------------------
    df: WoS references
    start_year:
    end_year:
    draw: boolean for drawing or not
    trim: degree of nodes to include in the graph

    Returns
    ----------------------------------
    coword networkx object
    """

    df_sub = df[(df.PY> start_year) & (df.PY <= end_year)]
    keys = keyword_counts(df_sub)
    
    print('Calculating co-word matrix')
    coword_df = coword_matrix(df_sub,keys.keys())
    
    coword_array = coword_df.as_matrix()
    np.fill_diagonal(coword_array, 0)
    coword_net  = nx.from_numpy_matrix(coword_array)
    col_names = coword_df.columns.tolist()
    labels = {col_names.index(l):l for l in col_names}
    nx.set_node_attributes(coword_net, 'keyword', labels)
    nx.set_node_attributes(coword_net, 'between_central', nx.betweenness_centrality(coword_net))
    if trim > 0:
        coword_net = trim_degrees(coword_net, trim)
        labels = {n:labels[n] for n in coword_net.nodes()}
   
    return coword_net

def trim_draw_network(coword_net, trim):

    """ Trims and draws the co-word networks for the years
    
    Parameters
    -----------------------------------------
    coword_net: networkx coword Graph
    trim: degree of nodes to include in the graph

    Returns
    ----------------------------------
    coword networkx object
    """
    coword_net = trim_degrees(coword_net, trim)
    labels = nx.get_node_attributes(coword_net, 'keyword')
    pos = nx.spring_layout(coword_net)
    fig = plt.gcf()
    fig.set_size_inches(12.5,12.5)
    print('drawing the network .... ')
    nx.draw(coword_net, pos=pos, alpha=0.5, 
        node_size={n:math.log1p(5000*bc) for n,bc in nx.get_node_attributes(coword_net, 'between_central').iteritems()}, 
        with_labels=True, labels=labels)
    fig.show()
    return coword_net



def plot_co_x(cox, start, end, size = (20,20), title = ''):
        
        """ Plotting function for keyword graphs

        Parameters
        --------------------
        cox: the coword networkx graph; assumes that nodes have attribute 'topic'
        start: start year
        end: end year
        """

        plt.figure(figsize=size)
        plt.title(title +' %s - %s'%(start,end), fontsize=18)
        nx.draw_graphviz(cox, with_labels=True, 
                     alpha = 0.8, width=0.1,
                     labels = nx.get_node_attributes(cox, 'topic'),
                     fontsize=9,
                     node_size = [s*4500 for s in nx.eigenvector_centrality(cox).values()],
                     node_color = [s for s in nx.degree(cox).values()])

def term_year_network(df, topic, start, end, size = (18,18)):

    """ Constructs, plots and returns a network for the given term during the given years

    Parameters
    --------------------------------------
    df: references dataframe with a 'topics' field
    topic: the keyword
    start: start year
    end: end year -- not included
    size: size in inches of the plot
    """
    svm_nx = coword_network(df, start, end)

    svm_cow = nx.to_numpy_matrix(svm_nx)
    topics = nx.get_node_attributes(svm_nx, 'topic')
    eigen = nx.eigenvector_centrality(svm_nx)
    class_nx = nx.ego_graph(svm_nx, nxkey_for_topic(topic, topics), undirected=True, radius=20)

    plot_co_x(class_nx, start, end, size)
    return class_nx

def nxkey_for_topic(topic, topics):

    """ helper function to look up the node number
    for a given topic in the list of topics as ordered
    in a networkx graph
    """

    return [k[0] for k in topics.items() if k[1] == topic][0]

def  pmc_year_column(pmc_df):

    """ Adds a PY - publication year -- column to a EuroPMC dataframe. PMC doesn't return the publication
    year explicitly in the core fields.
    """
    passyears = pmc_df.journalInfo.map(lambda x: x['yearOfPublication'])
    pmc_df['PY'] = years
    return pmc_df