subject_dict = {}


number_of_subject = int(input("Enter the number of subjects: "))

for i in range(number_of_subject):
    u = 0
    name_of_subject = input(f"\nEnter name of subject {i + 1}: ")
    while u == 0:
        score = int(input(f"Enter the score for {name_of_subject}: "))
        if score < 0 or score > 100:
            print(f"Invalid input for score of {name_of_subject}, score must be within (0 - 100).")
        else:
            subject_dict[name_of_subject] = score
            u += 1

subject = list(subject_dict.keys())
scores = list(subject_dict.values())

total = 0

for score in scores:
    total += score

mean_value = total / len(subject)

print(f"\nThe mean score is {mean_value: .2f}")

# Mode
nums = []
for i in range(len(subject_dict)):
    num = scores.count(scores[i])
    nums.append(num)

highest_num = max(nums)

values = []
for index, count in enumerate(nums):
    if count == highest_num:
        values.append(index)

modal_scores = []
for i in range(len(values)):
    mod = scores[values[i]]
    modal_scores.append(mod)

modal_scores = set(modal_scores)
modal_scores = list(modal_scores)

for i in range(len(modal_scores)):
    print(f"The modal score is {modal_scores[i]}")

#Q3.Calculating median

scores = sorted(scores)

if len(subject_dict) % 2 != 0:
    place_holder =int((len(subject_dict) + 1) / 2)
    median_score = scores[(place_holder - 1)]
    print(f"The median score is {median_score}")
elif len(subject_dict) % 2 == 0:
    place_holder = int(len(subject_dict) / 2)
    score1 = int(scores[place_holder - 1])
    score2 = int(scores[place_holder])
    median_score = ((score1 + score2) / 2)
    print(f"The median score is {median_score}")

#Q4 Variance
diffs = []
for score in scores:
    dif = round(score - mean_value, 4)
    diffs.append(dif)

summation = 0
for diff in diffs:
    diff = pow(diff, 2)
    summation += diff

variance = summation / len(subject_dict)

print(f"The variance is{variance: .2f}")

standard_deviation = pow(variance, 1/2)
print(f"The standard deviation is{standard_deviation: .2f}")


























