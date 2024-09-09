# Databricks notebook source
# Jesse St. John

# COMMAND ----------

# set up file directory
# dbutils.fs.mkdirs("FileStore/tables/assign2")
# file location and type
file_location = "/FileStore/tables/rawHT.csv"
file_type = 'csv'
# move file to new directory
dbutils.fs.mv(file_location, "FileStore/tables/assign2/")

# COMMAND ----------

# check file moved over
dbutils.fs.ls("FileStore/tables/assign2")

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType

# set up schema
humanTraffickingSchema = StructType(\
    [StructField('yearOfRegistration', IntegerType(), True), \
     StructField('Datasource', StringType(), True), \
     StructField('gender', StringType(), True), \
     StructField('ageBroad', StringType(), True), \
     StructField('majorityStatus', StringType(), True), \
     StructField('majorityStatusAtExploit', StringType(), True), \
     StructField('majorityEntry', StringType(), True), \
     StructField('citizenship', StringType(), True), \
     StructField('meansOfControlDebtBondage', IntegerType(), True), \
     StructField('meansOfControlTakesEarnings', IntegerType(), True), \
     StructField('meansOfControlRestrictsFinancialAccess', IntegerType(), True), \
     StructField('meansOfControlThreats', IntegerType(), True), \
     StructField('meansOfControlPsychologicalAbuse', IntegerType(), True), \
     StructField('meansOfControlPhysicalAbuse', IntegerType(), True), \
     StructField('meansOfControlSexualAbuse', IntegerType(), True), \
     StructField('meansOfControlFalsePromises', IntegerType(), True), \
     StructField('meansOfControlPsychoactiveSubstances', IntegerType(), True), \
     StructField('meansOfControlRestrictsMovement', IntegerType(), True), \
     StructField('meansOfControlRestrictsMedicalCare', IntegerType(), True), \
     StructField('meansOfControlExcessiveWorkingHours', IntegerType(), True), \
     StructField('meansOfControlUsesChildren', IntegerType(), True), \
     StructField('meansOfControlThreatOfLawEnforcement', IntegerType(), True), \
     StructField('meansOfControlWithholdsNecessities', IntegerType(), True), \
     StructField('meansOfControlWithholdsDocuments', IntegerType(), True), \
     StructField('meansOfControlOther', IntegerType(), True), \
     StructField('meansOfControlNotSpecified', IntegerType(), True), \
     StructField('meansOfControlConcatenated', StringType(), True), \
     StructField('isForcedLabour', IntegerType(), True), \
     StructField('isSexualExploit', IntegerType(), True), \
     StructField('isOtherExploit', IntegerType(), True), \
     StructField('isSexAndLabour', IntegerType(), True), \
     StructField('isForcedMarriage', IntegerType(), True), \
     StructField('isForcedMilitary', IntegerType(), True), \
     StructField('isOrganRemoval', IntegerType(), True), \
     StructField('isSlaveryAndPractices', IntegerType(), True), \
     StructField('typeOfExploitConcatenated', StringType(), True), \
     StructField('typeOfLabourAgriculture', IntegerType(), True), \
     StructField('typeOfLabourAquafarming', IntegerType(), True), \
     StructField('typeOfLabourBegging', IntegerType(), True), \
     StructField('typeOfLabourConstruction', IntegerType(), True), \
     StructField('typeOfLabourDomesticWork', IntegerType(), True), \
     StructField('typeOfLabourIllicitActivities', IntegerType(), True), \
     StructField('typeOfLabourHospitality', IntegerType(), True), \
     StructField('typeOfLabourManufacturing', IntegerType(), True), \
     StructField('typeOfLabourMiningOrDrilling', IntegerType(), True), \
     StructField('typeOfLabourPeddling', IntegerType(), True), \
     StructField('typeOfLabourTransportation', IntegerType(), True), \
     StructField('typeOfLabourOther', IntegerType(), True), \
     StructField('typeOfLabourNotSpecified', IntegerType(), True), \
     StructField('typeOfLabourConcatenated', StringType(), True), \
     StructField('typeOfSexProstitution', IntegerType(), True), \
     StructField('typeOfSexPornography', IntegerType(), True), \
     StructField('typeOfSexRemoteInteractiveServices', IntegerType(), True), \
     StructField('typeOfSexPrivateSexualServices', IntegerType(), True), \
     StructField('typeOfSexConcatenated', StringType(), True), \
     StructField('isAbduction', IntegerType(), True), \
     StructField('RecruiterRelationship', StringType(), True), \
     StructField('CountryOfExploition', StringType(), True), \
     StructField('recruiterRelationIntimatePartner', IntegerType(), True), \
     StructField('recruiterRelationFriend', IntegerType(), True), \
     StructField('recruiterRelationFamily', IntegerType(), True), \
     StructField('recruiterRelationOther', IntegerType(), True), \
     StructField('recruiterRelationUknown', IntegerType(), True), \
    ])

# read in data
rawHumanTraffickingDF = spark.read.format("csv").option("header", True).schema(humanTraffickingSchema).load("dbfs:/FileStore/tables/assign2/rawHT.csv").persist()
rawHumanTraffickingDF.show()

# COMMAND ----------

# select needed/desired columns for analysis
humanTraffickingDF = rawHumanTraffickingDF.select('yearOfRegistration', 'gender', 'ageBroad', 'majorityStatus', 'majorityStatusAtExploit', 'majorityEntry', 'citizenship', 'meansOfControlDebtBondage', 'meansOfControlTakesEarnings', 'meansOfControlRestrictsFinancialAccess', 'meansOfControlThreats', 'meansOfControlPsychologicalAbuse', 'meansOfControlPhysicalAbuse', 'meansOfControlSexualAbuse', 'meansOfControlFalsePromises', 'meansOfControlPsychoactiveSubstances', 'meansOfControlRestrictsMovement', 'meansOfControlRestrictsMedicalCare', 'meansOfControlExcessiveWorkingHours', 'meansOfControlUsesChildren', 'meansOfControlThreatOfLawEnforcement', 'meansOfControlWithholdsNecessities', 'meansOfControlWithholdsDocuments', 'meansOfControlOther', 'meansOfControlNotSpecified', 'typeOfExploitConcatenated', 'typeOfLabourConcatenated', 'typeOfSexConcatenated', 'isAbduction', 'RecruiterRelationship', 'CountryOfExploition')
humanTraffickingDF.show()

# COMMAND ----------

    #  StructField('meansOfControlDebtBondage', IntegerType(), True), \               # monetary    DONE
    #  StructField('meansOfControlTakesEarnings', IntegerType(), True), \             # monetary    DONE
    #  StructField('meansOfControlRestrictsFinancialAccess', IntegerType(), True), \  # monetary    DONE
    #  StructField('meansOfControlThreats', IntegerType(), True), \                   # manipulation  DONE
    #  StructField('meansOfControlPsychologicalAbuse', IntegerType(), True), \        # manipulation  DONE
    #  StructField('meansOfControlPhysicalAbuse', IntegerType(), True), \             # physical harm   DONE
    #  StructField('meansOfControlSexualAbuse', IntegerType(), True), \               # sexual abuse    DONE
    #  StructField('meansOfControlFalsePromises', IntegerType(), True), \             # manipulation    DONE
    #  StructField('meansOfControlPsychoactiveSubstances', IntegerType(), True), \    # drugs           DONE
    #  StructField('meansOfControlRestrictsMovement', IntegerType(), True), \         # manipulation    DONE
    #  StructField('meansOfControlRestrictsMedicalCare', IntegerType(), True), \      # withholding     DONE
    #  StructField('meansOfControlExcessiveWorkingHours', IntegerType(), True), \     # manipulation   DONE 
    #  StructField('meansOfControlUsesChildren', IntegerType(), True), \              # manipulation    DONE
    #  StructField('meansOfControlThreatOfLawEnforcement', IntegerType(), True), \    # manipulation    DONE
    #  StructField('meansOfControlWithholdsNecessities', IntegerType(), True), \      # withholding DONE
    #  StructField('meansOfControlWithholdsDocuments', IntegerType(), True), \        # withholding
    #  StructField('meansOfControlOther', IntegerType(), True), \                     # other   DONE
    #  StructField('meansOfControlNotSpecified', IntegerType(), True), \              # not specified   DONE

# COMMAND ----------

import pyspark.sql.functions as f

# COMMAND ----------

# create monetaryControl column
humanTraffickingDF = humanTraffickingDF.withColumn('monetaryControl',
                                                   f.when((f.col('meansOfControlDebtBondage') == 1) | (f.col('meansOfControlTakesEarnings') == 1) | (f.col('meansOfControlRestrictsFinancialAccess') == 1), 1)\
                                                    .when((f.col('meansOfControlDebtBondage') == 0) & (f.col('meansOfControlTakesEarnings') == 0) & (f.col('meansOfControlRestrictsFinancialAccess') == 0), 0)\
                                                    .otherwise(0)
)

# create manipulation control column
humanTraffickingDF = humanTraffickingDF.withColumn('manipulationControl',
                                                   f.when((f.col('meansOfControlFalsePromises') == 1) | (f.col('meansOfControlRestrictsMovement') == 1) | (f.col('meansOfControlExcessiveWorkingHours') == 1) | (f.col('meansOfControlUsesChildren') == 1) | (f.col('meansOfControlThreatOfLawEnforcement') == 1) | (f.col('meansOfControlPsychologicalAbuse') == 1) | (f.col('meansOfControlThreats') == 1), 1)\
                                                    .when((f.col('meansOfControlFalsePromises') == 0) & (f.col('meansOfControlRestrictsMovement') == 0) & (f.col('meansOfControlExcessiveWorkingHours') == 0) & (f.col('meansOfControlUsesChildren') == 0) & (f.col('meansOfControlThreatOfLawEnforcement') == 0) & (f.col('meansOfControlPsychologicalAbuse') == 0) & (f.col('meansOfControlThreats') == 0), 0)\
                                                    .otherwise(0)
)

# create withholding control column
humanTraffickingDF = humanTraffickingDF.withColumn('withholdingControl',
                                                   f.when((f.col('meansOfControlRestrictsMedicalCare') == 1) | (f.col('meansOfControlWithholdsNecessities') == 1) | (f.col('meansOfControlWithholdsDocuments') == 1), 1)\
                                                    .when((f.col('meansOfControlRestrictsMedicalCare') == 0) & (f.col('meansOfControlWithholdsNecessities') == 0) & (f.col('meansOfControlWithholdsDocuments') == 0), 0)\
                                                    .otherwise(0)
)

# create bodilyHarmControl column
humanTraffickingDF = humanTraffickingDF.withColumn('bodilyHarmControl',
                                                   f.when((f.col('meansOfControlPhysicalAbuse') == 1) | (f.col('meansOfControlSexualAbuse') == 1) | (f.col('meansOfControlPsychoactiveSubstances') == 1), 1)\
                                                    .when((f.col('meansOfControlPhysicalAbuse') == 0) & (f.col('meansOfControlSexualAbuse') == 0) & (f.col('meansOfControlPsychoactiveSubstances') == 0), 0)\
                                                    .otherwise(0)
)

# create otherControl column
humanTraffickingDF = humanTraffickingDF.withColumn('otherControl',
                                                   f.when((f.col('meansOfControlOther') == 1) | (f.col('meansOfControlNotSpecified') == 1), 1)\
                                                    .when((f.col('meansOfControlOther') == 0) & (f.col('meansOfControlNotSpecified') == 0), 0)\
                                                    .otherwise(0)
)

humanTraffickingDF.show()

# COMMAND ----------

# drop unneeded columns
humanTraffickingDF = humanTraffickingDF.drop('meansOfControlDebtBondage', 'meansOfControlTakesEarnings', 'meansOfControlRestrictsFinancialAccess', 'meansOfControlFalsePromises', 'meansOfControlRestrictsMovement', 'meansOfControlExcessiveWorkingHours', 'meansOfControlUsesChildren', 'meansOfControlThreatOfLawEnforcement', 'meansOfControlRestrictsMedicalCare', 'meansOfControlWithholdsNecessities', 'meansOfControlWithholdsDocuments', 'meansOfControlPhysicalAbuse', 'meansOfControlSexualAbuse', 'meansOfControlPsychoactiveSubstances', 'meansOfControlThreats', 'meansOfControlPsychologicalAbuse', 'meansOfControlOther', 'meansOfControlNotSpecified')
humanTraffickingDF.show()

# COMMAND ----------

humanTraffickingDF.count()

# COMMAND ----------

#check number of missing values in each col
df_cols = humanTraffickingDF.columns
nullCnts = []

for currCol in df_cols:
    nullCnt = humanTraffickingDF.filter(f.col(currCol).isNull()).count()
    nullCnts.append(nullCnt)

nullDict = dict(zip(df_cols, nullCnts))
print(nullDict)

# COMMAND ----------

# handling of null values
# yearOfRegistration: drop rows
# gender: drop rows
# ageBroad: drop column, keep majorityStatus since there are less missing values
# majorityStatus: drop rows
# majorityStatusAtExploit: drop column
# majorityEntry: drop column
# citizenship: replace with 0
# typeOfExploitConcatenated: check again after initial null handling
# typeOfLabourConcatenated: check again after initial null handling
# typeOfSexConcatenated: check again after initial null handling
# isAbduction: drop column
# RecruiterRelationship: check again after initial null handling
# CountryOfExploition: check again after initial null handling

# drop columns with large amounts of missing values
humanTraffickingDF = humanTraffickingDF.drop('ageBroad', 'majorityStatusAtExploit', 'majorityEntry', 'isAbduction')
humanTraffickingDF.show()

# COMMAND ----------

# drop specific rows with null values
humanTraffickingDF = humanTraffickingDF.dropna(subset= ['yearOfRegistration', 'gender', 'majorityStatus'])
humanTraffickingDF.count()

# COMMAND ----------

# replace null with 0 for citizenship
humanTraffickingDF = humanTraffickingDF.fillna('0', subset= 'citizenship')
humanTraffickingDF.filter(f.col('citizenship').isNull()).count()

# COMMAND ----------

# humanTraffickingDF.count()

# COMMAND ----------

# check other columns after initial null cleaning
exploitCnts = humanTraffickingDF.filter(f.col('typeOfExploitConcatenated').isNull()).count()
labourCnts = humanTraffickingDF.filter(f.col('typeOfLabourConcatenated').isNull()).count()
sexCnts = humanTraffickingDF.filter(f.col('typeOfSexConcatenated').isNull()).count()
recruiterCnts = humanTraffickingDF.filter(f.col('RecruiterRelationship').isNull()).count()
countryCnts = humanTraffickingDF.filter(f.col('CountryOfExploition').isNull()).count()
exploitCnts, labourCnts, sexCnts, recruiterCnts, countryCnts

# COMMAND ----------

humanTraffickingDF.columns

# COMMAND ----------

# further handling of nulls
# drop columns
humanTraffickingDF = humanTraffickingDF.drop('typeOfLabourConcatenated', 'typeOfSexConcatenated')

# drop rows with null values
humanTraffickingDF = humanTraffickingDF.dropna(subset= ['typeOfExploitConcatenated', 'RecruiterRelationship', 'CountryOfExploition'])

humanTraffickingDF.count()

# COMMAND ----------

humanTraffickingDF.show()

# COMMAND ----------

# split the RecruiterRelationship column by ; delimiter and only keep first indicated relationship
from pyspark.sql.functions import split

split_col = split(humanTraffickingDF['RecruiterRelationship'], ';')

# add first split col to the dataframe
humanTraffickingDF = humanTraffickingDF.withColumn('recruiterRelationship', split_col.getItem(0))

# COMMAND ----------

# useful dicts for later use
country_dict = {'0': 'null', 'MX': 'Mexico', 'CN': 'China', 'US': 'United States of America', 'PH': 'Philippines', 'UA': 'Ukraine', 'SV': 'El Salvador', 'UZ': 'Uzbekistan', 'BY': 'Belarus', 'KR': 'Korea (the Republic of)', 'KE': 'Kenya', 'HT': 'Haiti', 'KH': 'Cambodia', 'NG': 'Nigeria', 'MM': 'Myanmar', 'GH': 'Ghana', 'BD': 'Bangladesh', 'ID': 'Indonesia', 'BR': 'Brazil', 'IL': 'Israel', 'JM': 'Jamaica', 'CU': 'Cuba', 'UG': 'Uganda', 'VN': 'Vietnam', 'CI': 'Cote d\'Ivoire', 'SL': 'Sierra Leone', 'GT': 'Guatemala', 'ET': 'Ethiopia', 'KG': 'Kyrgyzstan', 'PL': 'Poland', 'RU': 'Russian Federation', 'HK': 'China', 'LY': 'Libya', 'SA': 'Saudi Arabia', 'KZ': 'Kazakhstan', 'MY': 'Malaysia', 'ML': 'Mali', 'LB': 'Lebanon'}

region_dict = {'0': ['0'], 'Northern America': ['US'], 'Central America': ['MX', 'SV', 'GT'], 'Caribbean': ['HT', 'JM', 'CU'], 'South America': ['BR'], 'Eastern Europe': ['UA', 'BY', 'PL', 'RU'], 'Western Asia': ['IL', 'SA', 'LB'], 'Central Asia': ['UZ', 'KG', 'KZ'], 'Eastern Asia': ['CN', 'KR', 'HK'], 'Southeastern Asia': ['PH', 'KH', 'MM', 'ID', 'VN'], 'Southern Asia': ['BD', 'MY'], 'Northern Africa': ['LY'], 'Western Africa': ['NG', 'GH', 'CI', 'SL', 'ML'], 'Eastern Africa': ['KE', 'UG', 'ET']}

# COMMAND ----------

# def regionMap(search_country, region_dict):
#     for region, country in region_dict.items():
#         if search_country in country:
#             return region
        
# regionMap('UA', region_dict)

# COMMAND ----------

# helper functions to map country to region
regionMap_udf = udf(lambda search_country: regionMap(search_country, region_dict), StringType())
def regionMap(search_country, region_dict):
    for region, country in region_dict.items():
        if search_country in country:
            return region

# create new col for citizenshipRegion
humanTraffickingDF = humanTraffickingDF.withColumn('citizenshipRegion', regionMap_udf(f.col('citizenship')))

# create new col for regionOfExploition
humanTraffickingDF = humanTraffickingDF.withColumn('regionOfExploition', regionMap_udf(f.col('CountryOfExploition')))

# COMMAND ----------

from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.clustering import KMeans
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import ClusteringEvaluator

# COMMAND ----------

humanTraffickingDF.columns

# COMMAND ----------

# create indexers for string data
# prep gender: stringIndexer
genderIndexer = StringIndexer(inputCol= 'gender', outputCol= 'genderIndexer')
# testGenderIndexer = genderIndexer.fit(humanTraffickingDF).transform(humanTraffickingDF)
# testGenderIndexer.select(['gender', 'genderIndexer']).distinct().show()

# prep majoritystatus: stringIndexer (check values first)
majorityStatusIndexer = StringIndexer(inputCol= 'majorityStatus', outputCol= 'majorityStatusIndexer')
# majorityStatusIndexer = majorityStatusIndexer.fit(humanTraffickingDF).transform(humanTraffickingDF)
# majorityStatusIndexer.select(['majorityStatus', 'majorityStatusIndexer']).distinct().show()

# prep typeOfExploitConcatenated: stringIndexer
typeExploitIndexer = StringIndexer(inputCol= 'typeOfExploitConcatenated', outputCol= 'typeExploitIndexer')
# typeExploitIndexer = typeExploitIndexer.fit(humanTraffickingDF).transform(humanTraffickingDF)
# typeExploitIndexer.select(['typeOfExploitConcatenated', 'typeExploitIndexer']).distinct().show()

# prep recruiterRelationship: stringIndexer
recruiterIndexer = StringIndexer(inputCol= 'recruiterRelationship', outputCol= 'recruiterIndexer')
# recruiterIndexer = recruiterIndexer.fit(humanTraffickingDF).transform(humanTraffickingDF)
# recruiterIndexer.select(['recruiterRelationship', 'recruiterIndexer']).distinct().show()

# prep citizenship: stringIndexer on citizenshipRegion
citizenshipIndexer = StringIndexer(inputCol= 'citizenshipRegion', outputCol= 'citizenshipIndexer')
# citizenshipIndexer = citizenshipIndexer.fit(humanTraffickingDF).transform(humanTraffickingDF)
# citizenshipIndexer.select(['citizenshipRegion', 'citizenshipIndexer']).distinct().show()

# prep countryOfExploition: stringIndexer on regionOfExploition
exploitRegionIndexer = StringIndexer(inputCol= 'regionOfExploition', outputCol= 'regionOfExploitIndexer')
# exploitRegionIndexer = exploitRegionIndexer.fit(humanTraffickingDF).transform(humanTraffickingDF)
# exploitRegionIndexer.select(['regionOfExploition', 'regionOfExploitIndexer']).distinct().show()

# COMMAND ----------

train_df, test_df = humanTraffickingDF.randomSplit(weights= [0.7, 0.3], seed= 42)

# COMMAND ----------

# create vector assembler
vecAssem = VectorAssembler(inputCols= ['yearOfRegistration', 'genderIndexer', 'majorityStatusIndexer', 'typeExploitIndexer', 'recruiterIndexer', 'monetaryControl','manipulationControl', 'withholdingControl', 'bodilyHarmControl', 'otherControl', 'citizenshipIndexer', 'regionOfExploitIndexer'], outputCol= 'features')

# create stages
myStages = [genderIndexer, majorityStatusIndexer, typeExploitIndexer, recruiterIndexer, citizenshipIndexer, exploitRegionIndexer, vecAssem]

# create pipeline
p = Pipeline(stages= myStages)

pModel = p.fit(train_df)

featuresDF_train = pModel.transform(train_df)
featuresDF_test = pModel.transform(test_df)
featuresDF_train.show()

# COMMAND ----------

# finding optimal number of clusters (k)
sil_score = []

# create evaluator
evaluator = ClusteringEvaluator(predictionCol='prediction', 
                                featuresCol='features',
                                metricName='silhouette',  
                                distanceMeasure='squaredEuclidean')

# create kmeans model
for i in range(2, 10):
    km = KMeans(k= i, featuresCol= 'features')
    km_fit = km.fit(featuresDF_train)
    output = km_fit.transform(featuresDF_train)
    score = evaluator.evaluate(output)
    sil_score.append(score)
    print("Silhouette Score:", score)

# COMMAND ----------

# plot silhouette scores
import matplotlib.pyplot as plt

plt.plot(range(1, 9), sil_score)
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Score')
plt.grid()
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC Based on the plot above, the elbow point is at 5. We will move forward with an optimal k value of 5.

# COMMAND ----------

# create vector assembler
vecAssem_optK = VectorAssembler(inputCols= ['yearOfRegistration', 'genderIndexer', 'majorityStatusIndexer', 'typeExploitIndexer', 'recruiterIndexer', 'monetaryControl','manipulationControl', 'withholdingControl', 'bodilyHarmControl', 'otherControl', 'citizenshipIndexer', 'regionOfExploitIndexer'], outputCol= 'features')

# kmeans w/optimal clusters
km_opt = KMeans(featuresCol= 'features', k= 5)

# create stages
myStages_optK = [genderIndexer, majorityStatusIndexer, typeExploitIndexer, recruiterIndexer, citizenshipIndexer, exploitRegionIndexer, vecAssem_optK, km_opt]

# create pipeline
p_optK = Pipeline(stages= myStages_optK)

pModel_optK = p_optK.fit(train_df)

featuresDF_train_optK = pModel_optK.transform(train_df)

featuresDF_train_optK.select('features', 'prediction')

# COMMAND ----------

featuresDF_train_optK.show()

# COMMAND ----------

# set up files for streaming
test_df = test_df.repartition(10)
# remove any old contents, just in case
dbutils.fs.rm("FileStore/tables/assign2/stream/", True)

# write out new files, with a different file for each partition
test_df.write.format("csv").option("header", True).save("FileStore/tables/assign2/stream/")

# COMMAND ----------

# set up stream
minTraffickingSchema = StructType(\
    [StructField('yearOfRegistration', IntegerType(), True), \
     StructField('gender', StringType(), True), \
     StructField('majorityStatus', StringType(), True), \
     StructField('citizenship', StringType(), True), \
     StructField('typeOfExploitConcatenated', StringType(), True), \
     StructField('recruiterRelationship', StringType(), True), \
     StructField('CountryOfExploition', StringType(), True), \
     StructField('monetaryControl', IntegerType(), True), \
     StructField('manipulationControl', IntegerType(), True), \
     StructField('withholdingControl', IntegerType(), True), \
     StructField('bodilyHarmControl', IntegerType(), True), \
     StructField('otherControl', IntegerType(), True), \
     StructField('citizenshipRegion', StringType(), True), \
     StructField('regionOfExploition', StringType(), True), \
    ])

sourceStream = spark.readStream.format("csv").option("header", True).schema(minTraffickingSchema).option("maxFilesPerTrigger", 1).load("dbfs:///FileStore/tables/assign2/stream").withColumnRenamed('output', 'label')

streamTrafficking = pModel_optK.transform(sourceStream).select('features', 'prediction')

query = streamTrafficking.writeStream.outputMode("update").format('memory').queryName('cntWin').start()

# COMMAND ----------

current = spark.sql("SELECT * FROM cntWin")
current.show()

# COMMAND ----------

query.stop()

# COMMAND ----------

# optimal kmeans
km_opt = KMeans(featuresCol= 'features', k= 5)
km_model = km_opt.fit(featuresDF_test)
preds = km_model.transform(featuresDF_test)

# print cluster centers
centers = km_model.clusterCenters()
print("Cluster Centers: ")
for center in centers:
    print(center)

# COMMAND ----------

# # assign data points to clusters
# clustered_data = km_model.transform(featuresDF)

# convert to pandas df
clustered_pd = preds.toPandas()

# COMMAND ----------

clustered_pd.head()

# COMMAND ----------

clustered_pd['gender'].value_counts().plot.bar()

# COMMAND ----------

clustered_pd['prediction'].value_counts().plot.bar()

# COMMAND ----------

import pandas as pd
import plotly.express as px

centroids = pd.DataFrame(centers, columns= ['yearOfRegistration', 'genderIndexer', 'majorityStatusIndexer', 'typeExploitIndexer', 'recruiterIndexer', 'monetaryControl','manipulationControl', 'withholdingControl', 'bodilyHarmControl', 'otherControl', 'citizenshipIndexer', 'regionOfExploitIndexer'])
centroids['cluster'] = centroids.index
fig = px.parallel_coordinates(centroids, color="cluster",
                              dimensions=['yearOfRegistration', 'genderIndexer', 'majorityStatusIndexer', 'typeExploitIndexer', 'recruiterIndexer', 'monetaryControl','manipulationControl', 'withholdingControl', 'bodilyHarmControl', 'otherControl', 'citizenshipIndexer', 'regionOfExploitIndexer'],
                              color_continuous_scale=px.colors.diverging.Tealrose,
                              color_continuous_midpoint=2)
fig.show()
