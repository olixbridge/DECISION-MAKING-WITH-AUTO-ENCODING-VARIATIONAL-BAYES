import pickle
import pprint

#ppca_res4.pkl
#simu_gaussian_res_paper_def_ais.pkl
with open('ppca_res4.pkl', 'rb') as f:
    data = pickle.load(f)

#print(type(data))
print(data.shape)
#print(data.columns)
#pprint.pprint(data)

#data['oliv']
#print(data['oliv'])

#print(data['CUBO'])
#print( (data['eval_encoder_name'])[0:10])



#print((data['oliv'])[0:10])

print((data['oliv'])[0:14])








