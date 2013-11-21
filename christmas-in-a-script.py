#!/usr/bin/env python

import random, sys

families = [['Kyle', 'Jody'], ['Roberta', 'Jeff'], ['Tim', 'Heidi'], ['Owen'], ['Hillary', 'Jamie']]
individuals = [item for sublist in families for item in sublist]

def in_family(individual1, individual2):
    for family in families:
        if individual1 in family and individual2 in family:
            return True
    return False

max_iterations = 2000
count = len(individuals)
allocated = []
allocations = {}
failed = False

for giver_id, giver in enumerate(individuals):
    recipient_id = random.randint(0, count - 1) #sometimes you just gotta trust the PRNG
    iterations = 0
    #can't give to self, can't give to already allocated recipient, can't give to somebody giving to you
    while (recipient_id == giver_id) or (recipient_id in allocated) or (recipient_id in allocations and allocations[recipient_id] == giver_id):
        iterations += 1
        recipient_id = random.randint(0, count - 1)
        #can't give to somebody in your family
        if in_family(individuals[recipient_id], individuals[giver_id]):
            recipient_id = giver_id
        if iterations >= max_iterations: #lazy avoidance of bad allocation scenarios
            print('Try again, hit max number of attempts ({0})'.format(max_iterations))
            print('\tUnallocated: {0}'.format([individual for individual_id, individual in enumerate(individuals) if individual_id not in allocated]))
            failed = True
            break
    if failed:
        break
    allocated.append(recipient_id)
    allocations[giver_id] = recipient_id

for giver_id in allocations:
    giver_name = individuals[giver_id]
    recipient_name = individuals[allocations[giver_id]]
    print("{0} -> {1}".format(giver_name, recipient_name))

