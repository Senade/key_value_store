from collections import defaultdict
import json

# Global variables

# main key/value data structure
KV_STORE = dict()
# dict that stores every token among the values of KV_STORE, along with their corresponsing frequencies
VF_STORE = defaultdict(int)


# Methods
def set(key, value):
    """
    String, String/Dict -> None

    Given: a key and a value

    Effect: sets key = value in KV_STORE. cleans up keys in VF_STORE if the value of an existing key is being replaced
    """
    global KV_STORE
    if key in KV_STORE:
        decrement_vf_store(KV_STORE.get(key))
    if is_json(value):
        value = json.loads(value)
    KV_STORE[key] = value
    update_vf_store(value)


def delete(key):
    """
    String -> None

    Given: a key

    Effect: removes given key from KV_STORE. Reduces the frequency of keys in VF_STORE for the corresponding value being
            deleted
    """
    global KV_STORE
    if key in KV_STORE:
        decrement_vf_store(KV_STORE[key])
        KV_STORE.pop(key, None)
    else:
        print 'Key doesn\'t exist. Cannot delete'


def display_data_store(d=KV_STORE, indent=1):
    """
    Dict, NonNegInt -> None

    Given: a dict and the number of '+'s to print in the current iteration

    Effect: prints KV_STORE in the required format
    """
    for key, value in d.iteritems():
        if isinstance(value, dict):
            print '+' * indent + ' {}:'.format(key)
            display_data_store(value, indent + 1)
        else:
            print '+' * indent + ' {}:'.format(key),
            print str(value)


def display_max_vf_store():
    """
    None -> None

    Effect: displays the key with the maximum frequency in VF_STORE
    """
    global VF_STORE
    if VF_STORE:
        maximum = max(VF_STORE, key=VF_STORE.get)
        print '\nMost common word: {}'.format(maximum)
    else:
        print 'Dictionary is empty'


# Helper functions
def is_json(s):
    """
    String -> Boolean

    Given: a string

    Returns: returns True iff the given string is a valid JSON string
    """
    try:
        json.loads(s)
    except ValueError:
        return False
    return True


def decrement_vf_store(value):
    """cleanup-> decrement
    String/Dict -> None

    Given: a 'value'

    Effect: Tokenizes the given value and reduces the frequency of each token in VF_STORE by one
    """
    global KV_STORE, VF_STORE
    if isinstance(value, dict):
        for k, v in value.iteritems():
            decrement_vf_store(v)
    else:
        for v in value.strip().split():
            VF_STORE[v] -= 1
            if VF_STORE[v] == 0:
                VF_STORE.pop(v, None)


def update_vf_store(value):
    """update -> increment
    String/Dict -> None

    Given: a 'value'

    Effect: Tokenizes the given value and increses the frequency of each token in VF_STORE by one
    """
    global VF_STORE
    if isinstance(value, dict):
        for k, v in value.iteritems():
            update_vf_store(v)
    else:
        for token in value.strip().split():
            VF_STORE[token] += 1


# Test functions
def get_kv_store():
    """ Test function that returns the global KV_STORE"""
    global KV_STORE
    return KV_STORE


def get_vf_store():
    """ Test function that returns the global VF_STORE"""
    global VF_STORE
    return VF_STORE
