from causallearn.search.ConstraintBased.PC import pc
from causallearn.search.ScoreBased.GES import ges
from causallearn.search.ScoreBased.ExactSearch import bic_exact_search
from causallearn.utils.GraphUtils import GraphUtils
from SCORE.stein import *
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

import io
import numpy as np

#maybe
#from causallearn.utils.Dataset import load_dataset
#data, labels = load_dataset(dataset_name)


#----------------------------------------------------------
# Scroll down to uncomment the disired functions
#----------------------------------------------------------

#----------------------------------------------------------
# Defining important Variables for all Datasets
#----------------------------------------------------------
# Define Numer of iterations by String length. 
# Each letter/number will be used for naming the result
iteratorString = '123'

#----------------------------------------------------------
# Preparing Sachs Data
#----------------------------------------------------------
# Define Data Path
sachs_file_path = 'Data/sachs.data.txt'
# Load the Data
sachs_data = np.genfromtxt(sachs_file_path, skip_header=1)
# Save the node names
sachs_node_names=['Raf', 'Mek', 'Plcg', 'PIP2', 'PIP3', 'Erk', 'Akt', 'PKA', 'PKC', 'P38', 'Jnk']
# Save the dataset name 
sachs_name = 'Sachs'



#----------------------------------------------------------
# PC Algorithm 
#----------------------------------------------------------
def runpc(iteratorString, dataset_name, data, dataset_nodes, prior):
    pydot_graph_array = []
    for x in iteratorString:
        # Use the algorithm to estimate the causal graph
        causal_graph = pc(data, background_knowledge = prior, show_progress=False)
        # Convert the Graph
        pydot_graph = GraphUtils.to_pydot(causal_graph.G, title = dataset_name + x, labels = dataset_nodes)
        # Save the graph
        pydot_graph.write_pdf('Results/' + dataset_name + '_PC' + x + '.pdf')
        # Put the generated graph into an arry
        pydot_graph_array.append(pydot_graph)

    else:
        print('Finished ' + dataset_name + ' PC')

    # Return an array of all generated graphs
    return pydot_graph_array

#----------------------------------------------------------
# Bic Score Algorithm !!! DOES NOT TAKE PRIOR KNOWLEDGE!!!
#----------------------------------------------------------
def runbicscore(iteratorString, dataset_name, data, dataset_nodes):
    pydot_graph_array = []
    for x in iteratorString:
        # Use the algorithm to estimate the causal graph
        result = ges(data)
        causal_graph = result['G']
        # Convert the Graph
        pydot_graph = GraphUtils.to_pydot(causal_graph, title = dataset_name + x, labels = dataset_nodes)
        # Save the graph
        pydot_graph.write_pdf('Results/' + dataset_name + '_BIC_score' + x + '.pdf')
        # Put the generated graph into an arry
        pydot_graph_array.append(pydot_graph)

    else:
        print('Finished ' + dataset_name + ' BIC score')

    # Return an array of all generated graphs
    return pydot_graph_array

#----------------------------------------------------------
# SCORE Algorithm taken from https://github.com/paulrolland1307/SCORE
#----------------------------------------------------------
def runscore(iteratorString, dataset_name, data, dataset_nodes, prior):
    pydot_graph_array = []
    for x in iteratorString:
        # Use the algorithm to estimate the causal graph
        result = SCORE(data, include_graph=prior)
        causal_graph = result[0]
        print(result)
        # Convert the Graph
        pydot_graph = GraphUtils.to_pydot(causal_graph, title = dataset_name + x, labels = dataset_nodes )
        # Save the graph
        pydot_graph.write_pdf('Results/' + dataset_name + '_Exact' + x + '.pdf')
        # Put the generated graph into an arry
        pydot_graph_array.append(pydot_graph)

    else:
        print('Finished ' + dataset_name + ' Exact')

    # Return an array of all generated graphs
    return pydot_graph_array


#----------------------------------------------------------
# Exact Search Algorithm 
#----------------------------------------------------------
def runexact(iteratorString, dataset_name, data, dataset_nodes, prior):
    pydot_graph_array = []
    for x in iteratorString:
        # Use the algorithm to estimate the causal graph
        exact_result = bic_exact_search(data, include_graph=prior)
        causal_graph = exact_result[0]
        print(exact_result)
        # Convert the Graph
        pydot_graph = GraphUtils.to_pydot(causal_graph, title = dataset_name + x, labels = dataset_nodes )
        # Save the graph
        pydot_graph.write_pdf('Results/' + dataset_name + '_Exact' + x + '.pdf')
        # Put the generated graph into an arry
        pydot_graph_array.append(pydot_graph)

    else:
        print('Finished ' + dataset_name + ' Exact')

    # Return an array of all generated graphs
    return pydot_graph_array


#----------------------------------------------------------
# Calling all the functions
#----------------------------------------------------------


# BIC score !!!only possible without priors!!!
graphs_sachs_bicscore_normal = runbicscore(iteratorString, sachs_name, sachs_data, sachs_node_names)



# PC without prior knowledge
graphs_sachs_pc_normal = runpc(iteratorString, sachs_name, sachs_data, sachs_node_names, None)

# SCORE without prior knowledge 
#graphs_sachs_score_normal = runscore(iteratorString, sachs_name, sachs_data, sachs_node_names, None)


# Exact Search without prior knowledge
#graphs_sachs_exact_normal = runexact(iteratorString, sachs_name, sachs_data, sachs_node_names, None)
