import math

def brutef_closest_pair(points_list):

    """
    finds distance between two closest points in the plane by brute force
    input: a list p of n (n ≥ 2) points p 1 (x 1 , y 1 ), . . . , p n (x n , y n )
    output: the distance between the closest pair of points
    """

    dist = math.inf
    for i in range(1,len(points_list)-1):
        for j in range(i + 1, len(points_list)):
            dist = min(dist,math.sqrt((points_list[i][0] - points_list[j][0])**2 + (points_list[i][1] - points_list[j][1])**2))
    return dist 
