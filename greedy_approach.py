"""
Greedy Algorithm Assignment - Greedy Approach Implementation

You should implement greedy algorithms in this file.
"""

from typing import List, Tuple
from main import Node, Edge, get_neighbors, calculate_travel_cost, print_route_summary


# ============================================================================
# PART A: COMPANY'S GREEDY ALGORITHM 
# ============================================================================

def greedy_company_route(nodes: List[Node], depot: Node, edges: List[Edge]) -> Tuple[List[Node], float]:
    """
    Part A: Implement the company's greedy algorithm.
    
    Goal: Maximize company profit (delivery_fee - travel_cost)
    
    Algorithm Steps:
    1. Start at the depot
    2. Look at all unvisited neighboring customer nodes (connected by roads)
    3. Calculate profit for each: delivery_fee - travel_cost to reach it
    4. Choose the neighbor with highest profit
    5. Repeat until all customers visited
    6. Return to depot
    
    Args:
        nodes (List[Node]): All delivery locations including depot
        depot (Node): The starting depot location
        edges (List[Edge]): All road connections between cities
        
    Returns:
        Tuple[List[Node], float]: (route as list of nodes, total profit)
        
    TODO: Students implement this function
    """
    # START YOUR IMPLEMENTATION HERE
    
    # Hints:
    # - Use get_neighbors(current_node, edges) to find connected cities
    # - Use current_node.distance_to(neighbor) to get distance
    # - Use calculate_travel_cost(distance) to get travel cost
    # - Keep track of visited customers using a set of IDs
    # - Calculate profit = neighbor.delivery_fee - travel_cost
    # - Choose the neighbor with the highest profit at each step
    # - Only consider unvisited customer neighbors (not depot, not already visited)
    # - Don't forget to return to the depot at the end
    depot_id = depot.id
    visited = set()
    route: List[Node] = [depot]
    total_profit = 0.0
    current_node = depot

    while True: 
        neighbors = get_neighbors(current_node, edges)
        candidates = []
        for n in neighbors:
            if n.id != depot_id and n.id not in visited:
                candidates.append(n)
        if not candidates:
            break

        best = None
        best_profit = float('-inf')
        for n in candidates:
            distance = current_node.distance_to(n)
            travel_cost = calculate_travel_cost(distance)
            profit = n.delivery_fee - travel_cost
            if profit > best_profit:
                best_profit = profit
                best = n
        
        move_distance = current_node.distance_to(best)
        move_cost = calculate_travel_cost(move_distance)
        total_profit += best.delivery_fee - move_cost
        visited.add(best.id)
        route.append(best)
        current_node = best

    if current_node.id != depot_id:
        return_distance = current_node.distance_to(depot)
        return_cost = calculate_travel_cost(return_distance)
        total_profit -= return_cost
        route.append(depot)
    
    return route, total_profit

        
    # END YOUR IMPLEMENTATION


# ============================================================================
# PART B: DRIVER'S GREEDY ALGORITHM - STUDENT IMPLEMENTATION
# ============================================================================

def greedy_driver_route(nodes: List[Node], depot: Node, edges: List[Edge]) -> Tuple[List[Node], float]:
    """
    Part B: Implement the driver's greedy algorithm.
    
    Goal: Maximize driver earnings (delivery_fee + estimated_tip - travel_cost)
    
    Algorithm Steps:
    1. Start at the depot
    2. Look at all unvisited neighboring customer nodes (connected by roads)
    3. Calculate earnings for each: delivery_fee + tip - travel_cost
    4. Choose the neighbor with highest earnings
    5. Repeat until all customers visited
    6. Return to depot
    
    Args:
        nodes (List[Node]): All delivery locations including depot
        depot (Node): The starting depot location
        edges (List[Edge]): All road connections between cities
        
    Returns:
        Tuple[List[Node], float]: (route as list of nodes, total earnings)
        
    TODO: Students implement this function
    """
    # START YOUR IMPLEMENTATION HERE
    
    # Hints:
    # - Similar to Part A, but now consider tips too
    # - Use get_neighbors(current_node, edges) to find connected cities
    # - Calculate earnings = neighbor.delivery_fee + neighbor.estimated_tip - travel_cost
    # - Choose the neighbor with the highest earnings at each step
    # - Keep track of total earnings (fees + tips - costs)
    
    # Example modification from Part A:
    # earnings = neighbor.delivery_fee + neighbor.estimated_tip - travel_cost
    
    current_city = depot
    visited = set()
    route = [depot]
    total_earnings = 0.0

    while True:
        neighbors = get_neighbors(current_city, edges)

        # only unvisited customers (not the depot)
        candidates = []
        for city in neighbors:
            if city.id != depot.id and city.id not in visited:
                candidates.append(city)

        if len(candidates) == 0:
            break

        best = None
        best_earnings = float('-inf')

        for city in candidates:
            distance = current_city.distance_to(city)
            move_cost = calculate_travel_cost(distance)
            earnings = city.delivery_fee + city.estimated_tip - move_cost
            if earnings > best_earnings:
                best_earnings = earnings
                best = city

        if best is None:
            break  # safety

        # move to best and update totals
        move_distance = current_city.distance_to(best)
        move_cost = calculate_travel_cost(move_distance)
        total_earnings += best.delivery_fee + best.estimated_tip - move_cost

        route.append(best)
        visited.add(best.id)      
        current_city = best

    # return to depot
    if current_city != depot:
        return_distance = current_city.distance_to(depot)
        return_cost = calculate_travel_cost(return_distance)
        total_earnings -= return_cost
        route.append(depot)

    return route, total_earnings

    
    
    # END YOUR IMPLEMENTATION


# ============================================================================
# PART C: ETHICAL GREEDY ALGORITHM - STUDENT IMPLEMENTATION
# ============================================================================

def greedy_ethical_route(nodes: List["Node"], depot: "Node", edges: List["Edge"], long_hop_threshold: float = 6.0, short_hop_limit: float = 3.0 ) -> Tuple[List["Node"], float]:
    """
    Part C: Implement an ethically-modified greedy algorithm.
    
    Modify either the company or driver algorithm to incorporate ethical considerations.
    
    Possible ethical rules:
    - "fairness": Alternate between high-tip and low-tip regions
    - "fatigue": Limit consecutive long-distance drives
    - "priority": Consider delivery priority levels
    - "balance": Ensure all regions get early service
    
    Args:
        nodes (List[Node]): All delivery locations including depot
        depot (Node): The starting depot location
        edges (List[Edge]): All road connections between cities
        ethical_rule (str): Which ethical rule to apply
        
    Returns:
        Tuple[List[Node], float]: (route as list of nodes, total profit/earnings)
        
    TODO: Students implement this function with ethical modifications
    """
    # START YOUR IMPLEMENTATION HERE
    
    # Hints:
    # - Start with either your Part A or Part B algorithm as a base
    # - Add ethical considerations to the greedy selection process
    # - Use get_neighbors(current_node, edges) to find connected cities
    # - Examples:
    #   * Fairness: Give bonus/penalty based on tip equity
    #   * Fatigue: Penalize long consecutive drives
    #   * Balance: Encourage visiting different regions early
    # - You can modify the scoring function to include ethical factors
    # - Compare results with and without ethical modifications
 
   
    current_city = depot
    visited_ids = set()
    route: List["Node"] = [depot]
    total_earnings = 0.0

    last_hop_distance = 0.0  # track distance of last move

    def score(next_city: "Node") -> float:
        """Calculate driver's immediate earnings for visiting next_city."""
        d = current_city.distance_to(next_city)
        cost = calculate_travel_cost(d)
        return next_city.delivery_fee + next_city.estimated_tip - cost

    while True:
        # Gather unvisited neighboring customers (not the depot)
        neighbors = get_neighbors(current_city, edges)
        candidates: List["Node"] = []
        for city in neighbors:
            if city.id != depot.id and city.id not in visited_ids:
                candidates.append(city)

        if len(candidates) == 0:
            break  # no unvisited neighbors

        # Apply fatigue rule if last hop was long
        restricted = candidates
        if last_hop_distance > long_hop_threshold:
            short_neighbors: List["Node"] = []
            for city in candidates:
                d = current_city.distance_to(city)
                if d <= short_hop_limit:
                    short_neighbors.append(city)
            if len(short_neighbors) > 0:
                restricted = short_neighbors

        # Pick neighbor with highest earnings
        best_city = None
        best_gain = float("-inf")
        for city in restricted:
            gain = score(city)
            if gain > best_gain:
                best_gain = gain
                best_city = city

        if best_city is None:
            break 

        # Move to the best city and update totals
        move_distance = current_city.distance_to(best_city)
        move_cost = calculate_travel_cost(move_distance)
        total_earnings += best_city.delivery_fee + best_city.estimated_tip - move_cost

        route.append(best_city)
        visited_ids.add(best_city.id)
        current_city = best_city
        last_hop_distance = move_distance  

    # Return to depot and subtract the travel cost
    if current_city != depot:
        back_distance = current_city.distance_to(depot)
        back_cost = calculate_travel_cost(back_distance)
        total_earnings -= back_cost
        route.append(depot)

    return route, total_earnings
    
    # END YOUR IMPLEMENTATION


# ============================================================================
# TESTING FUNCTIONS
# ============================================================================
def _route_cost(route: List[Node]) -> float:
    """Sum travel cost along the route using calculate_travel_cost."""
    if not route or len(route) < 2:
        return 0.0
    total = 0.0
    for i in range(len(route) - 1):
        d = route[i].distance_to(route[i+1])
        total += calculate_travel_cost(d)
    return total


def test_mn_data():
    """Test implementations with Minnesota data."""
    try:
        from mn_dataset import MN_NODES, MN_DEPOT, MN_EDGES
        
        print("\n" + "="*60)
        print("TESTING WITH MINNESOTA DATA")
        print("="*60)
        
        print(f"Minnesota nodes: {len(MN_NODES)}")
        print(f"Minnesota edges: {len(MN_EDGES)}")
        print(f"Minnesota depot: {MN_DEPOT}")
        
        # Test Part A on larger dataset
        try:
            route_a_mn, profit_a_mn = greedy_company_route(MN_NODES, MN_DEPOT, MN_EDGES)
            print(f"\nCompany algorithm on MN data: ${profit_a_mn:.2f} profit")
            print(f"Route length: {len(route_a_mn)} stops")
        except NotImplementedError:
            print("\nPart A not implemented for MN testing")
        except Exception as e:
            print(f"\nError in Part A on MN data: {e}")

        # Part B: Driver Greedy 
        try:
            route_b_mn, earn_b_mn = greedy_driver_route(MN_NODES, MN_DEPOT, MN_EDGES)
            cost_b = _route_cost(route_b_mn)
            print("\n--- PART B: DRIVER GREEDY ---")
            print_route_summary(route_b_mn, earn_b_mn, cost_b)
        except Exception as e:
            print(f"\nError in Part B on MN data: {e}")

        # Part C: Ethical (Fatigue) 
        try:
            # tweak thresholds if your distances are on a different scale
            route_c_mn, earn_c_mn = greedy_ethical_route(
                MN_NODES, MN_DEPOT, MN_EDGES,
                long_hop_threshold=2.0, short_hop_limit=1.0
            )
            cost_c = _route_cost(route_c_mn)
            print("\n--- PART C: ETHICAL (FATIGUE) ---")
            print_route_summary(route_c_mn, earn_c_mn, cost_c)

            # Quick comparison to Part B
            print(f"Δ earnings (C − B): {round(earn_c_mn - earn_b_mn, 2)}")
            print(f"Stops (B): {len(route_b_mn)} | Stops (C): {len(route_c_mn)}")

        except Exception as e:
            print(f"\nError in Part C on MN data: {e}")

        
            
    except ImportError:
        print("\nMinnesota dataset not available for testing")


def main():
    """Main testing function."""
    test_mn_data()


if __name__ == "__main__":
    main()