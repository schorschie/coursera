# python3
#from math import dist
import sys


def compute_min_refills(distance, tank, stops):
    
    refills = 0
    
    while distance > tank:
        reachable_stops = sum([(tank-s)>=0 for s in stops])
        if reachable_stops == 0 and distance > tank:
            return -1  # There are no more stops on the way
                
        # what is the distance left, at the last gas station?
        distance = distance - stops[reachable_stops-1]
        
        # recumpute the stops at the last reachable gas station
        stops = [s-stops[reachable_stops-1] for s in stops]

        # drop the gas stations which are in the past
        for i in sorted(range(reachable_stops), reverse=True):
            del stops[i]
        
        refills+=1
        
    return refills

    

if __name__ == '__main__':
    DEBUG = False
    
    if not DEBUG:
        d, m, _, *stops = map(int, sys.stdin.read().split())
    else:
        d = 950
        m = 400
        stops = [200, 375, 550, 750]
        d = 10
        m = 3
        stops = [1, 2, 5, 9]
        d = 200
        m = 250
        stops = [100, 150]

    
    print(compute_min_refills(d, m, stops))
