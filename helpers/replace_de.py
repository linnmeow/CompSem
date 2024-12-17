import pandas as pd
import random


# # initialize counters for specific tokens 
# token_count_NOW = 0
# ist_count_NOW = 0
# sind_count_NOW = 0
# werden_count_NOW = 0
# wird_count_NOW = 0
# hat_count_NOW = 0
# haben_count_NOW = 0

# token_count_PST = 0
# war_count_PST = 0
# waren_count_PST = 0
# wurde_count_PST = 0
# wurden_count_PST = 0
# hatte_count_PST = 0
# hatten_count_PST = 0

# token_count_ENS = 0
# ist_count_ENS = 0
# sind_count_ENS = 0 
# werden_count_ENS = 0
# wird_count_ENS = 0
# hat_count_ENS = 0
# haben_count_ENS = 0

# token_count_EPS = 0
# war_count_EPS = 0
# waren_count_EPS = 0
# wurde_count_EPS = 0
# wurden_count_EPS = 0
# hatte_count_EPS = 0
# hatten_count_EPS = 0

# for line in lines:
#     line = line.strip().split('\t')

#     # make sure the label is "NOW"
#     if line[-1] == "NOW":
#         token_count_NOW += 1

#         if line[0] == "ist": # check whether "ist" is in the sent
#             ist_count_NOW += 1
#         if line[0] == "sind": # check whether "sind" is in the sent
#             sind_count_NOW += 1
#         if line[0] == "werden": # check whether "werden" is in the sent
#             werden_count_NOW += 1
#         if line[0] == "wird": # check whether "wird" is in the sent
#             wird_count_NOW += 1
#         if line[0] == 'hat': # check whether "hat" is in the sent
#             hat_count_NOW +=1
#         if line[0] == "haben": # check whether "haben" is in the sent
#             haben_count_NOW += 1
    
#     # make sure the label is "PST"
#     if line[-1] == "PST":
#         token_count_PST += 1

#         if line[0] == "war": # check whether "war" is in the sent
#             war_count_PST += 1
#         if line[0] == "waren": # check whether "waren" is in the sent
#             waren_count_PST += 1
#         if line[0] == "wurden": # check whether "wurden" is in the sent
#             wurden_count_PST += 1
#         if line[0] == "wurde": # check whether "wurde" is in the sent
#             wurde_count_PST += 1
#         if line[0] == 'hatte': # check whether "hatte" is in the sent
#             hatte_count_PST +=1
#         if line[0] == "hatten": # check whether "hatten" is in the sent
#             hatten_count_PST += 1

    
#     # make sure the label is "ENS"
#     if line[-1] == "ENS":
#         token_count_ENS += 1  

#         if line[0] == "ist": # check whether "ist" is in the sent
#             ist_count_ENS += 1
#         if line[0] == "sind":
#             sind_count_ENS += 1
#         if line[0] == "werden": # check whether "werden" is in the sent
#             werden_count_ENS += 1 
#         if line[0] == "wird": # check whether "wird" is in the sent
#             wird_count_ENS += 1
#         if line[0] == 'hat': # check whether "hat" is in the sent
#             hat_count_ENS +=1
#         if line[0] == "haben": # check whether "haben" is in the sent
#             haben_count_ENS += 1

#     # make sure the label is "EPS"
#     if line[-1] == "EPS":
#         token_count_EPS += 1

#         if line[0] == "war": # check whether "war" is in the sent
#             war_count_EPS += 1
#         if line[0] == "waren": # check whether "waren" is in the sent
#             waren_count_EPS += 1
#         if line[0] == "wurden": # check whether "wurden" is in the sent
#             wurden_count_EPS += 1
#         if line[0] == "wurde": # check whether "wurde" is in the sent
#             wurde_count_EPS += 1
#         if line[0] == 'hatte': # check whether "hatte" is in the sent
#             hatte_count_EPS +=1
#         if line[0] == "hatten": # check whether "hatten" is in the sent
#             hatten_count_EPS += 1



# print(f"Total 'NOW' tokens: {token_count_NOW}") # 2254  # 917

# print(f"'ist' count as NOW: {ist_count_NOW}") # 644  # 388
# print(f"'sind' count as NOW : {sind_count_NOW}") # 118  # 41
# print(f"'werden' count as NOW: {werden_count_NOW}") # 75  # 2
# print(f"'wird' count as NOW: {wird_count_NOW}") # 69  # 4
# print(f"'hat' count as NOW: {hat_count_NOW}") # 385  # 168
# print(f"'haben' count as NOW: {haben_count_NOW}") # 125  # 27
# print('\n')

# print(f"Total 'PST' tokens: {token_count_PST}") # 618   # 250

# print(f"'war' count as PST: {war_count_PST}") # 173   # 58
# print(f"'waren' count as PST : {waren_count_PST}") # 28  #7
# print(f"'wurden' count as PST: {wurden_count_PST}") # 36  # 19
# print(f"'wurde' count as PST: {wurde_count_PST}") # 163  # 114
# print(f"'hatte' count as PST: {hatte_count_PST}") # 33   # 8
# print(f"'hatten' count as PST: {hatten_count_PST}") # 23   # 2
# print('\n')

# print(f"Total 'ENS' tokens: {token_count_ENS}") # 2477   # 839

# print(f"'ist' count as ENS: {ist_count_ENS}") # 210  # 126
# print(f"'sind' count as ENS: {sind_count_ENS}") # 32  # 12
# print(f"'werden' count as ENS: {werden_count_ENS}") # 0  # 0
# print(f"'wird' count as ENS: {wird_count_ENS}") # 1  # 0
# print(f"'hat' count as ENS: {hat_count_ENS}") # 71  # 38
# print(f"'haben' count as ENS: {haben_count_ENS}") # 26   # 4
# print('\n')

# print(f"Total 'EPS' tokens: {token_count_EPS}") # 2466  # 803

# print(f"'war' count as EPS: {war_count_EPS}") # 97  # 25
# print(f"'waren' count as EPS : {waren_count_EPS}") # 15  # 2
# print(f"'wurden' count as EPS: {wurden_count_EPS}") # 0  # 0
# print(f"'wurde' count as EPS: {wurde_count_EPS}") # 3  # 1
# print(f"'hatte' count as EPS: {hatte_count_EPS}") # 37  # 6
# print(f"'hatten' count as PST: {hatten_count_EPS}") # 0  #0
# print('\n')


def txt_to_data(file_path):

    with open(file_path, "rt", encoding="utf-8") as file:
        lines = file.readlines()

    sentences = []  # list of dictionaries
    current_sentence_tokens = []  # initialize the list
    current_sentence_labels = []  # initialize the list
    current_sentence = {'sentence': [], 'labels': []}  # dictionary for each sentence specifying the tokens and the labels

    for line in lines:
        line = line.strip().split('\t')
        if len(line) == 1:
            if current_sentence_tokens:
                sentences.append({
                    'sentence': current_sentence_tokens,
                    'labels': current_sentence_labels
                })
                current_sentence_tokens = []  # reset the list for the next sentence
                current_sentence_labels = []  # reset the list for the next sentence
        else:
            current_sentence_tokens.append(line[0])
            current_sentence_labels.append(line[-1])

    # add the last sentence if not empty
    if current_sentence_tokens:
        sentences.append({
            'sentence': current_sentence_tokens,
            'labels': current_sentence_labels
        })

    return sentences

data_gold_de = txt_to_data('data_pmb.4.0.0/de_gold.txt')   # 2844
data_gold_de_new = txt_to_data('data_sem.0.2.0/de_gold.txt')   # 2935
data_silver_de = txt_to_data('data_pmb.4.0.0/de_silver.txt')   # 6338
data_silver_de_new = txt_to_data('data_sem.0.2.0/de_silver.txt')  #1339

# print(len(data_gold_de), len(data_gold_de_new), len(data_silver_de), len(data_silver_de_new))

def augment_dataset(data):
    augmented_data = []

    for example in data:
        sentence = example['sentence'].copy()  # Create a copy of the original sentence
        labels = example['labels'].copy()  # Create a copy of the original labels

        # check if 'NOW' label is present and corresponds to 'ist' token
        if 'NOW' in labels and 'ist' in sentence:
            # find the index of 'NOW' label
            index_now = labels.index('NOW')
            
            # find the index of 'ist' token
            index_ist = sentence.index('ist')

            # check if 'NOW' corresponds to 'ist'
            if index_now == index_ist:
                # create a new instance with modified 'labels' and 'sentence'
                augmented_example = {'sentence': sentence.copy(), 'labels': labels.copy()}
                augmented_example['labels'][index_now] = 'PST'
                augmented_example['sentence'][index_ist] = 'war'

                # append augmented example to the list
                augmented_data.append(augmented_example)

        # check if 'NOW' label is present and corresponds to 'sind' token
        if 'NOW' in labels and 'sind' in sentence:
            # find the index of 'NOW' label
            index_now = labels.index('NOW')
            
            # find the index of 'sind' token
            index_sind = sentence.index('sind')

            # check if 'NOW' corresponds to 'sind'
            if index_now == index_sind:
                # create a new instance with modified 'labels' and 'sentence'
                augmented_example = {'sentence': sentence.copy(), 'labels': labels.copy()}
                augmented_example['labels'][index_now] = 'PST'
                augmented_example['sentence'][index_sind] = 'waren'

                # append augmented example to the list
                augmented_data.append(augmented_example)

        # check if 'NOW' label is present and corresponds to 'hat' token
        if 'NOW' in labels and 'hat' in sentence:
            # find the index of 'NOW' label
            index_now = labels.index('NOW')
            
            # find the index of 'hat' token
            index_hat = sentence.index('hat')

            # check if 'NOW' corresponds to 'hat'
            if index_now == index_hat:
                # create a new instance with modified 'labels' and 'sentence'
                augmented_example = {'sentence': sentence.copy(), 'labels': labels.copy()}
                augmented_example['labels'][index_now] = 'PST'
                augmented_example['sentence'][index_hat] = 'hatte'

                # append augmented example to the list
                augmented_data.append(augmented_example)

        # check if 'NOW' label is present and corresponds to 'haben' token
        if 'NOW' in labels and 'haben' in sentence:
            # find the index of 'NOW' label
            index_now = labels.index('NOW')
            
            # find the index of 'haben' token
            index_haben = sentence.index('haben')

            # check if 'NOW' corresponds to 'haben'
            if index_now == index_haben:
                # create a new instance with modified 'labels' and 'sentence'
                augmented_example = {'sentence': sentence.copy(), 'labels': labels.copy()}
                augmented_example['labels'][index_now] = 'PST'
                augmented_example['sentence'][index_haben] = 'hatten'

                # append augmented example to the list
                augmented_data.append(augmented_example)

        # check if 'PST' label is present and corresponds to 'war' token
        if 'PST' in labels and 'war' in sentence:
            # find the index of 'PST' label
            index_pst = labels.index('PST')
            
            # find the index of 'war' token
            index_war = sentence.index('war')

            # check if 'PST' corresponds to 'war'
            if index_pst == index_war:
                # create a new instance with modified 'labels' and 'sentence'
                augmented_example = {'sentence': sentence.copy(), 'labels': labels.copy()}
                augmented_example['labels'][index_pst] = 'NOW'
                augmented_example['sentence'][index_war] = 'ist'

                # append augmented example to the list
                augmented_data.append(augmented_example)

        # check if 'PST' label is present and corresponds to 'wurde' token
        if 'PST' in labels and 'wurde' in sentence:
            # find the index of 'PST' label
            index_pst = labels.index('PST')
            
            # find the index of 'wurde' token
            index_wurde = sentence.index('wurde')

            # check if 'PST' corresponds to 'wurde'
            if index_pst == index_wurde:
                # create a new instance with modified 'labels' and 'sentence'
                augmented_example = {'sentence': sentence.copy(), 'labels': labels.copy()}
                augmented_example['labels'][index_pst] = 'NOW'
                augmented_example['sentence'][index_wurde] = 'wird'

                # append augmented example to the list
                augmented_data.append(augmented_example)

        # check if 'ESN' label is present and corresponds to 'ist' token
        if 'ENS' in labels and 'ist' in sentence:
            # find the index of 'ENS' label
            index_ens = labels.index('ENS')
            
            # find the index of 'ist' token
            index_ist = sentence.index('ist')

            # check if 'ENS' corresponds to 'ist'
            if index_ens == index_ist:
                # create a new instance with modified 'labels' and 'sentence'
                augmented_example = {'sentence': sentence.copy(), 'labels': labels.copy()}
                augmented_example['labels'][index_ens] = 'EPS'
                augmented_example['sentence'][index_ist] = 'war'

                # append augmented example to the list
                augmented_data.append(augmented_example)
        
        # check if 'ENS' label is present and corresponds to 'hat' token
        if 'ENS' in labels and 'hat' in sentence:
            # find the index of 'ENS' label
            index_ens = labels.index('ENS')
            
            # find the index of 'hat' token
            index_hat = sentence.index('hat')

            # check if 'ENS' corresponds to 'hat'
            if index_ens == index_hat:
                # create a new instance with modified 'labels' and 'sentence'
                augmented_example = {'sentence': sentence.copy(), 'labels': labels.copy()}
                augmented_example['labels'][index_ens] = 'EPS'
                augmented_example['sentence'][index_hat] = 'hatte'

                # append augmented example to the list
                augmented_data.append(augmented_example)

        # check if 'EPS' label is present and corresponds to 'war' token
        if 'EPS' in labels and 'war' in sentence:
            # find the index of 'ENS' label
            index_eps = labels.index('EPS')
            
            # find the index of 'war' token
            index_war = sentence.index('war')

            # check if 'EPS' corresponds to 'war'
            if index_eps == index_war:
                # create a new instance with modified 'labels' and 'sentence'
                augmented_example = {'sentence': sentence.copy(), 'labels': labels.copy()}
                augmented_example['labels'][index_eps] = 'ENS'
                augmented_example['sentence'][index_war] = 'ist'

                # append augmented example to the list
                augmented_data.append(augmented_example)

    return augmented_data


# augment the dataset
augmented_dataset_gold = augment_dataset(data_gold_de)   # 978
augmented_dataset_gold_new = augment_dataset(data_gold_de_new)   # 974
augmented_dataset_silver = augment_dataset(data_silver_de)   # 1831
augmented_dataset_silver_new = augment_dataset(data_silver_de_new)   # 416

# print(len(augmented_dataset_gold), len(augmented_dataset_gold_new), len(augmented_dataset_silver), len(augmented_dataset_silver_new))

# putting all datasets together silver gold, original and augmented
original_and_augmented = augmented_dataset_silver + augmented_dataset_gold + data_gold_de + data_silver_de + data_gold_de_new + data_silver_de_new + augmented_dataset_gold_new + augmented_dataset_silver_new

# print(len(original_and_augmented)) # 17655

# ### we don't need to randomly sample anymore
# # # randomly sample 2409 samples from the gold dataset
# # random_sampled_data = random.sample(data_gold_de, 2409)
# # final = original_and_augmented + random_sampled_data

# # print(len(final))

# # write augmented data to a CSV file
# pd.DataFrame(original_and_augmented).to_csv('final_de.csv', index=False)

print(original_and_augmented[:5])
