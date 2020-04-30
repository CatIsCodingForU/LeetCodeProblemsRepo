def max_price_of_parts(pairs, pack_weight):
    weights = sorted(pairs, key=lambda x: x[0] / x[1], reverse=True)
    sums, current_weight = 0, 0
    while current_weight + weights[0][1] <= pack_weight:
        current_weight += weights[0][1]
        sums += weights[0][0]
        weights.remove(weights[0])
    sums += weights[0][1]/weights[0][0]*(pack_weight-current_weight)
    return sums


def main():
    n, w = [int(i) for i in input().split(' ')]
    pairs = []
    for i in range(n):
        a, b = [int(i) for i in input().split(' ')]
        pairs.append([a, b])
    print(pairs)

    maxPrice = max_price_of_parts(pairs, w)
    print(maxPrice)
    #
    # for i in maxPrice:
    #     print(i, end=" ")


if __name__ == "__main__":
    main()