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
        min1 = p.get()
        min2= p.get()
        sum = min1.data[0] + min2.data[0]
        if min1.data[1] == '':
            z = TreeNode(min2, min1, (sum, ""))
        else:
            z = TreeNode(min1, min2, (sum, ""))
        p.put(z)
        #print(z.data)

        
    # return root of the tree
    return p.get()


# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code={}):  
    if node.left != None:
        get_code(node.left, prefix + '0', code)
    if node.right != None:
        get_code(node.right, prefix + '1', code)
    else:
        code[node.data[1]] = prefix
    return code


        
        

# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(f):
    #for fixed length coding, we need to represent each character with the same number of bits
    num_characters = len(f) #number of different characters
    num_bits = math.ceil(math.log(num_characters, 2)) #number of bits needed to represent the number of characters
    total = (sum(f.values())) #number of characters
    return total*num_bits #number of characters * number of bits per character = how many bits are needed to ecode the text

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    sum = 0
    for key in f:
        count = f[key]
        code = C[key]
        bits = count * len(code)
        sum += bits
                
    return sum

'''
f = get_frequencies('f1.txt')
print("Fixed-length cost:  %d" % fixed_length_cost(f))
T = make_huffman_tree(f)
C = get_code(T)
print("Huffman cost:  %d" % huffman_cost(C, f))
'''

def compare_methods(files):
    result = []
    for file in files:
        f = get_frequencies(file)
        print(f)
        print(len(f))
        fixed_cost = fixed_length_cost(f)
        T = make_huffman_tree(f)
        C = get_code(T)
        #print(C)
        huff_cost = huffman_cost(C, f)
        ratio = huff_cost/fixed_cost
        result.append([file, fixed_cost, huff_cost, ratio])
    return result

def print_results(results):
    print(tabulate.tabulate(results,
                            headers=['filename', 'fixed-length-cost', 'huffman-cost', 'ratio'],
                            floatfmt=".3f",
                            tablefmt="github"))
 
files = ['alice29.txt', 'asyoulik.txt', 'f1.txt', 'fields.c', 'grammar.lsp'] 
files2 = ['f1.txt'] 
print_results(compare_methods(files))
