from typing import TypedDict

# loading review
with open('../../Data/review-1.txt') as f:
    lines = f.readlines()
    review = ' '.join(lines)

print(review)