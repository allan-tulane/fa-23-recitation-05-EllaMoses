import math, queue
from collections import Counter
import tabulate 

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))
    
def get_frequencies(fname):
    ## This function is done.
    ## Given any file name, this function reads line by line to count the frequency per character. 
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return(dict(C.most_common()))

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    # construct heap from frequencies, the initial items should be
    # the leaves of the final tree
    for c in f.keys():
        p.put(TreeNode(None,None,(f[c], c)))
    # greedily remove the two nodes x and y with lowest frequency,
    # create a new node z with x and y as children,
    # insert z into the priority queue (using an empty character "")
    while (p.qsize() > 1):
        min1 = p.get() #get the element with the smallest frequency and remove it from the queue
        min2= p.get() #get the element with the second smalled frequency and remove it from the queue
        sum = min1.data[0] + min2.data[0] #get the sum of the frequencies
        z = TreeNode(min1, min2, (sum, "")); #create a new node with these two nodes as children. This node's frequency will be equal to the sum of its children's frequency and it will be labeled ""
        p.put(z) #add this new node to the priority queue

    # return root of the tree
    return p.get()


# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code={}):  
    if node.left != None: #if the node has a left child, traverse down the left side of the tree and add a 0 to the current prefix
        get_code(node.left, prefix + '0', code)
    if node.right != None:  #if the node has a right child, traverse down the right side of the tree and add a 1 to the current prefix
        get_code(node.right, prefix + '1', code)
    if node.right == None and node.left == None: #if the node is a leaf node, stop traversing and add the current prefix for that node to the dictionary code, the key is the node's character
        code[node.data[1]] = prefix
    return code #return the dictionary of character prefix pairs


        
        

# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(f):
    #the cost of an encoding is equal to the sum of the frequency per character times the length of the encoding per character
    #for fixed length coding, we need to represent each character with the same number of bits
    num_characters = len(f) #number of different characters
    num_bits = math.ceil(math.log2(num_characters)) #number of bits needed to represent the number of characters
    total = (sum(f.values())) #number of characters
    return total*num_bits #number of characters * number of bits per character = how many bits are needed to ecode the text

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    cost = 0 #cost starts at zero
    for key in f: #for each character in the file
        count = f[key] #get the count of the character
        code = C[key] #get the encoding of the character
        bits = count * len(code) #the number of bits needed to represent all instances of that character is equal to the length of the encoding times the frequency of the character
        cost += bits #add the number of bits needed to the total cost
                
    return cost #after all keys have been accounted for, return total cost



#compare_methods and print results functions are adapted from previous labs
def compare_methods(files): #input is a list of files
    result = []
    for file in files: #for every file
        f = get_frequencies(file) #get the character frequencies
        fixed_cost = fixed_length_cost(f) #calculate the fixed_cost
        T = make_huffman_tree(f) #make the huffman tree
        C = get_code(T) #get the character encodings
        huff_cost = huffman_cost(C, f) #calculate the huffman cost
        ratio = fixed_cost/huff_cost #compute a ration of fixed-length-cost/huffman-cost to get the compression ratio
        result.append([file, fixed_cost, huff_cost, ratio]) #add to results
    return result #return results for all files

#print the results for all files
def print_results(results):
    print(tabulate.tabulate(results,
                            headers=['filename', 'fixed-length-cost', 'huffman-cost', 'ratio'],
                            floatfmt=".3f",
                            tablefmt="github"))
 
files = ['alice29.txt', 'asyoulik.txt', 'f1.txt', 'fields.c', 'grammar.lsp'] 
print_results(compare_methods(files))
