from collections import defaultdict

# Global variables

# main key/value data structure
KV_STORE = dict()
# dict that stores every word among the values of KV_STORE, along with their corresponsing frequencies
VF_STORE = defaultdict(int)


# Methods
def ds_set(keys, value, d=KV_STORE):
    """
    List, String/Dict, Dict -> None

    Given: a list of key/s, a value and a dict to store the key/s and value in

    Effect: sets key = value in KV_STORE. cleans up keys in VF_STORE if the value of an existing key is being replaced
    """
    key = keys[0]
    if len(keys) > 1:
        if key in d:
            if isinstance(d.get(key), str):
                decrement_vf_store(d.get(key))
                d[key] = {}
        else:
            d[key] = {}
        ds_set(keys[1:], value, d.get(key))
    else:
        if key in d:
            decrement_vf_store(d.get(key))
        d[key] = value
        increment_vf_store(value)


def ds_delete(keys, d=KV_STORE):
    """
    List, Dict -> None

    Given: a list of key/s

    Effect: removes given key from KV_STORE. Reduces the frequency of keys in VF_STORE for the corresponding value being
            deleted
    """
    key = keys[0]
    if key in d:
        if len(keys) > 1:
            ds_delete(keys[1:], d.get(key))
        else:
            decrement_vf_store(d.get(key))
            d.pop(key, None)
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
        print 'No values in the dictionary'


# Helper functions
def decrement_vf_store(value):
    """
    String/Dict -> None

    Given: a 'value' string

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


def increment_vf_store(value):
    """
    String/Dict -> None

    Given: a 'value' string

    Effect: Tokenizes the given value and increases the frequency of each token in VF_STORE by one
    """
    global VF_STORE
    if isinstance(value, dict):
        for k, v in value.iteritems():
            increment_vf_store(v)
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
