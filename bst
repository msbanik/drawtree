#!/usr/bin/python
import drawtree
import sys
import select
import re

#Split space-delimited stream (stdin, file) into list of nodes.
def listify(stream):
    nodes = []

    for line in stream:
        for token in line.strip().split():
            nodes.append(token)        

    return nodes  

# Format a list of nodes into level order format
# i.e. {1,6,3,5,#,9,2}
def format_level_order(nodes):
    nodes = ' '.join(nodes).replace(',', ' ')
    nodes = '{' + nodes.replace('[', '')\
        .replace(']', '')\
        .replace('{', '')\
        .replace('}', '')\
        .strip()\
        .replace(' ', ',') + '}' 
    return nodes     

def usage():
    return """Flags:
 -p, --preorder    (interpet sequence as preorder)    
 -b, --balanced    (auto balance bst)
 -l, --level-order (interpet sequence as level-order)

Print a bst:
$ bst 10 5 8 4 6 
$ bst nodes.txt
$ echo "colin eric dave" | bst
$ cat nodes.txt | sort | uniq | bst

Print a balanced bst:
$ bst -b 10 5 6 9 3
$ bst -b nodes.txt
$ bst -b < nodes.txt

Print a bst from preorder expression:
$ bst -p dave colin dan
$ echo "1 2 3 4 5" | bst -p
$ bst -p nodes.txt  

Print a random bst:
$ bst           (random bst of 10 nodes)
$ bst 5         (random bst of 5 nodes)
$ bst -b 7      (random balanaced bst of 7 nodes)"""

if __name__ == "__main__":
    nodes = []

    #form list of nodes from stdin if available.
    if select.select([sys.stdin,],[],[],0.0)[0]:
        nodes = listify(sys.stdin)

    # $ bst (Draw a BST with 10 random nodes).
    if len(sys.argv) < 2 and not nodes:
        drawtree.draw_random_bst(10)

    # Draw the BST using the nodes from stdin
    elif len(sys.argv) < 2:
        drawtree.draw_bst(nodes)

    # Draw BST using second arg. If 2nd arg is not a flag and not
    # an int it will be treated as a file. When the 2nd arg is 
    # an int, a random BST with n nodes will be constructed.
    elif len(sys.argv) == 2:
        if 'help' in sys.argv[1].strip().lower():
            print(usage())
            exit()

        # bst -p
        elif sys.argv[1] == '-p' or sys.argv[1] == '--preorder':
            drawtree.draw_bst(nodes, preorder=True)

        # bst -b 
        elif sys.argv[1] == '-b' or sys.argv[1] == '--balanced':

            #Draw random 7 node balanced bst.
            if not nodes:
                drawtree.draw_random_bst(7, balanced=True) 

            #Draw balanced tree using stdin
            else:
                drawtree.draw_bst(nodes, balanced=True)    

        # bst -l
        elif sys.argv[1] == '-l' or sys.argv[1] == '--level-order': 
            nodes = format_level_order(nodes)
            drawtree.draw_level_order(nodes)

        # bst 7 (draw random 7 node bst)
        elif re.match('\d+', sys.argv[1]):
            drawtree.draw_random_bst(int(sys.argv[1]))

        # $ bst nodes.txt
        else:
            filename = sys.argv[1]
            nodes = listify(open(filename))
            drawtree.draw_bst(nodes)

    else:
        if sys.argv[1] == '-p' or sys.argv[1] == '--preorder':

            # $ bst -p nodes.txt (load file as preorder traversal)
            if len(sys.argv) == 3 and not re.match("\d+",sys.argv[2]):
                nodes = listify(open(filename))
                drawtree.draw_bst(nodes, preorder=True)               

            # $ bst -p 1 2 3 4 5 (command line args in preorder)
            else:
                nodes = [n for n in list(sys.argv)][2:]
                drawtree.draw_bst(nodes, preorder=True)

        elif sys.argv[1] == '-b' or sys.argv[1] == '--balanced':

            # $ bst -b nodes.txt (flag set followed by 1 string. Treat as file)
            if len(sys.argv) == 3 and not re.match("\d+",sys.argv[2]):
                nodes = listify(open(sys.argv[2]))  
                drawtree.draw_bst(nodes, balanced=True)   

            else:
                nodes = [n for n in list(sys.argv)][2:]

                # $ bst -b 7  (draw random balanaced binary tree with 7 nodes)
                if len(sys.argv) == 3:
                    drawtree.draw_random_bst(int(sys.argv[2]), balanced=True)

                # $ bst -b 1 2 3 (draw balanced bst using args.)
                else:
                    drawtree.draw_bst(nodes, balanced=True)

        elif sys.argv[1] == '-l' or sys.argv[1] == '--level-order':
            arg = sys.argv[2]

            # $ bst -l nodes.txt (draw level order traversal tree from file)
            if len(sys.argv) == 3 and not re.match("\d+",arg) and arg[0] != '[':
                nodes = listify(open(sys.argv[2]))  
                nodes = format_level_order(nodes)
                drawtree.draw_level_order(nodes)

            else:       
                nodes = [n for n in list(sys.argv)][2:]
                nodes = format_level_order(nodes)
                drawtree.draw_level_order(nodes)
        

        # $ bst 10 5 7 (no flags set - use all args as nodes)
        else:
            nodes = [n for n in list(sys.argv)][1:]
            drawtree.draw_bst(nodes)
