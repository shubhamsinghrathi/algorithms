'''
Merge a linked list into another linked list at alternate positions
'''

from linkedList import *

ll1 = LinkedList([1,2,3,4]).list
ll2 = LinkedList([5,6,7,8]).list

#val1 == ll1, val2 = ll2["next"]
def mrg(val1, val2):
    if val1 == None and val2 == None:
        return None
    elif val1 == None:
        return {
            "value": val2["value"],
            "next": mrg(None, val2["next"])
        }
    elif val2 == None:
        return {
            "value": val1["value"],
            "next": mrg(val1["next"], None)
        }
    else:
        return {
            "value": val1["value"],
            "next": {
                "value": val2["value"],
                "next": mrg(val1["next"], val2["next"])
            }
        }

def merger(ll1, ll2):
    ll3 = {
        "value": ll2["value"],
        "next": mrg(ll1, ll2["next"])
    }
    print("ll3:", ll3)

merger(ll1, ll2)