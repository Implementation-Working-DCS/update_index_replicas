from elasticsearch import Elasticsearch, RequestsHttpConnection
import urllib3
 
# Deshabilitar las advertencias de SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
# Conexión al clúster de Elasticsearch con verificación SSL deshabilitada
es = Elasticsearch(
    ["https://localhost:PORT"],
    http_auth=("USER", "PASS"),
    scheme="https",
    port=PORT,
    connection_class=RequestsHttpConnection,
    verify_certs=False
)
 
# Función para actualizar el número de réplicas
def update_replicas(index_name, replicas):
    try:
        es.indices.put_settings(
            index=index_name,
            body={"index": {"number_of_replicas": replicas}},
        )
        print(f"Updated replicas for index: {index_name}")
    except Exception as e:
        print(f"Failed to update replicas for index: {index_name}. Error: {e}")
 
# Obtener todos los índices
indices = es.indices.get_alias("*")
restricted_indices = ['.kibana_security_session_1', '.apm-custom-link', '.security-profile-8', '.kibana_analytics_8.9.0_001',
                      '.fleet-enrollment-api-keys-7', '.apm-agent-configuration', '.kibana_security_solution_8.9.0_001',
                      '.fleet-policies-7', '.kibana_ingest_8.9.0_001', '.transform-internal-007', '.kibana_alerting_cases_8.9.0_001',
                      '.kibana_8.9.0_001', '.security-7', '.async-search', '.kibana_task_manager_8.9.0_001']
 
for index in indices:
    if index not in restricted_indices:
        update_replicas(index, 1)
 
# Obtener todos los data streams
data_streams = es.indices.get_data_stream(name="*")
for data_stream in data_streams['data_streams']:
    index_name = data_stream['name']
    if index_name not in restricted_indices:
        update_replicas(index_name, 1)
 
print("Replica update completed.")
