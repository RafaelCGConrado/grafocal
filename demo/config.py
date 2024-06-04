from sqlalchemy import create_engine


# data
df_query_all_tables = None
df_query_result = None
df_tgraph_features = None

available_features = None 
NxGraph = None 

df_query_supervision = None 
df_tgraph_features_supervision = None


#flag
flag_data_loaded = None
flag_use_prefix_in_graph = False


#Graph config
opt_source = None
opt_destination = None 
opt_timestamp = None
opt_measure = None

#io
feature_file_path = None

#plot
cmap = "rainbow"
cmap_colorshade = "jet"
plotly_width = "100%"
plotly_height = 800

columns_matrix_lasso = []
selected_points_lasso = []
df_selected = None

opt_logx_hexbin = False
opt_logy_hexbin = False

opt_logx_scatter_matrix = False
opt_logy_scatter_matrix = False



NODE_ID = "node_ID"

engine = create_engine('postgresql://rafael:rafael@localhost:5432/incordb') 
connection = engine.connect()

#SELECT * FROM OMOP5.death LIMIT 100

#pegar duas tabelas e criar semantica
