# ML_model flow 
import pandas as pd 
import numpy as np 


def modelflow(data):
    sample_size = len(data)  
    if sample_size <50 : 
        return('Your sample size looks insufficient. Gather more data')
    else: 
        response = input("Enter 'Y' either 'N': Are you predicting categorical variable?")
        if response.upper() in ['Y','YES'] :
            print("For predicting categorical variable, there are two branches: Clustering | Classification ")

            response_a1 = input("Enter 'Y'or 'N': Do you have labeled response?" ) 
            #  Y:Classification 
            if response_a1.upper() in ['Y','YES'] : 
                print("For classification : \n" ,
                      "1) large sample size >= 100k -> SGD \n", 
                      "2) sample size < 100k -> SVC, NaiveBayes, KNN \n") 
                if sample_size >= 100000 :
                    #SGD classificer -> Kernel Approximation  
                    return("Try Stochastic Gradient Descent(SGD) classifier. If it still not working, try Kernel Approximation")
                else : 
                    #Linear SVC  -> (text)Naive Bayes | (non-text) KNN -> SVC or Ensemble 
                    return("Linear Support Vector Classifier(SVC) is recommended. If it does not work and if you are working with text data, try Naive Bayes. If you are not dealing with text data then try KNN classifier. If still does not work well, try SVC or Ensemble classifiers ")
            else : # N: Clustering 
                response_a2 = input("Enter 'Y'or 'N': Is Number of categories known?")   
                print("For clustering : \n", 
                      "If you have predefined # of cluster: \n",
                      " 1) large sample size >= 100k -> KMeans, Spectral, GMM \n" ,
                      " 2) size <100k -> MiniBatch-Kmeans \n",
                      "If you don't have predefined # of cluster:\n ",
                      " 1) size >= 100k -> No recommendable model. You should find the fit model by yourself. \n",
                      " 2) size < 100k -> MeanShift, VBGMM \n"  )
                if response_a2.upper() in ['Y','YES'] :
                    if sample_size >=100000: 
                        
                        return('Try Kmeans clustering. If it does not work, try Spectral clustering or GMM')     
                    else :
                        return('Try MiniBatch Kmeans clustering')
                
                else : # Case when the # of cluster is not predefined.  
                    if sample_size >= 100000: 
                        return('Tough luck...')
                    else: 
                        return('Try MeanShift or VBGMM.') 

            
        elif response.upper() in ['N','NO'] : 
            print("Now your model is heading to: Regression | Dimension Reduction.") 

            response_b1 = input("Enter 'Y' or 'N': Are you predicting quantitative values?") #Y: Regression / N: Dim Reduction
            if response_b1.upper() in ['Y','YES']:  
                print("For regression: \n", 
                      "1) Sample size >= 100k -> SGD \n", 
                      "2) size < 100k -> Allow regularization has feature selection effect? \n",
                        " Yes --> L1-reg, Elastic net \n", 
                        " No --> L2-reg, SVR, Ensemble. \n")
                if sample_size >= 100000: 
                    return("Try SGD regressor") 
                else : 
                    response_b1_a = input("Enter 'N' or 'Y': Do you want to allow feature selection through Regularization?")
                    if response_b1_a.upper() in ['Y','YES']: 
                        return('Try regression with L1(Lasso)-regularization or Elsatic Net.')
                    else : 
                        return('Try regression with L2(Ridge)-regularization or Support Vector Regression(SVR) with linear kernel. If still not working, try Ensemble Regressor or SVR with rbf kernel.')

            else : 
                response_b2 = input("Enter 'Y' or 'N': Are you running dimensionality reduction?")  
                if response_b2 in ['Y','YES']: 
                    print("For Dimensionality reduction: \n", 
                          "1) Sample size >= 10k -> PCA, Kernel Approximation \n", 
                          "2) size < 10k -> PCA, Spectral Embedding, IsoMap, LLE \n")
                    if sample_size >= 10000 :
                        return('Try Randomized PCA first. If it does not work, try Kernel Approximiation') 
                    else : 
                        return('Try Randomized PCA first. If it does not work, try Spectral Embedding, IsoMap, or LLE')

                else : 
                    return('Hmm, maybe it is time to imagine the fit structure. Tough luck... ') 


def read_multi_extension(path:list ):  
    directories = path 
    data_dic = {i:None for i in range(len(path))} 
    key = 0 
    for directory in directories:
        delim = check_delimiters(directory)
        extension = directory[directory.rfind('.')+1:]
        if extension in ['xlsx','xls','xlsb','xlsm']: 
            extension = 'excel' 
            data_dic[key] = eval(f'pd.read_{extension}("{directory}")')
        else: 
            extension = 'csv'
            data_dic[key] = eval(f'pd.read_{extension}("{directory}",delimiter={delim})')
        key+= 1   
    return data_dic 


# Function to read and display the file with different delimiters
def check_delimiters(file_path):
    delimiters = [',', ';', '\t', '|']
    print(f"Checking file: {file_path}")
    for delimiter in delimiters:
        try:
            df = pd.read_csv(file_path, delimiter=delimiter)
            print(f"Delimiter '{delimiter}' seems to work. Here are the first few rows:")
            print(df.head())
            print("\n")
            return delimiter
        except Exception as e:
            pass 
            #print(f"Delimiter '{delimiter}' did not work.")
    print(f"Could not find a suitable delimiter for {file_path}\n")
    return None



