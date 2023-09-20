def can_defeat_all_enemies(N, H, strengths, X):
    for strength in strengths:
        if strength <= X:
            continue
        elif H > strength:
            H -= strength
        else:
            return False
    return True

def find_min_resistance(T, test_cases):
    results = []
    for i in range(T):
        N, H, strengths = test_cases[i]
        left, right = 0, max(strengths)  # Updated left to start from 0
        while left <= right:  # Changed the condition to include equal to
            mid = (left + right) // 2
            if can_defeat_all_enemies(N, H, strengths, mid):
                right = mid - 1  # Updated right to mid - 1
            else:
                left = mid + 1
        results.append(left)
    return results

# Input
T = int(input())
test_cases = []
for _ in range(T):
    N, H = map(int, input().split())
    strengths = list(map(int, input().split()))
    test_cases.append((N, H, strengths))

# Find and print the results
results = find_min_resistance(T, test_cases)
for res in results:
    print(res)
