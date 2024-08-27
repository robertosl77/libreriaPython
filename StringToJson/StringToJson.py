import json

# La cadena de texto proporcionada
data = """
CIRCUITO 88
Proceso Finalizado en 0 segundos
-*-
Proceso Finalizado en 0 segundos
-*-

CIRCUITO 103
-*-PROCEDIMIENTOS MT-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
MODIFICA_DOCUMENTOS: Finaliza OK
Proceso Finalizado en 46 segundos
-*-
AGREGA_AFECTACIONES: Finaliza OK
-->CT sin numero: 26|Documento no confirmado en idms: 0|Documento con causa incorrecta: 29|Documento con tiempo vencido: 352|Nuevo CT Insertado: 0|CT Agregado: 0|CT Reactivado: 0|CT con agregado desactivado: 0
Proceso Finalizado en 14 segundos
-*-
INSERTA_DOCUMENTOS_GEN: Finaliza OK
Proceso Finalizado en 0 segundos
-*-
INSERTA_DOCUMENTOS_DET: Finaliza OK
-->CT sin numero: 1|Documento no confirmado en idms: 0|Documento con causa incorrecta: 0|Documento con tiempo vencido: 0|Nuevo CT Insertado: 0|CT Agregado: 0|CT Reactivado: 0|CT con agregado desactivado: 0
Proceso Finalizado en 10 segundos
-*-
INSERTA_DOCUMENTOS_DET_PRG: Finaliza OK
-->CT sin numero: 0|Documento no confirmado en idms: 0|Documento con causa incorrecta: 0|Documento con tiempo vencido: 0|Nuevo CT Insertado: 0|CT Agregado: 0|CT Reactivado: 0|CT con agregado desactivado: 0
Proceso Finalizado en 0 segundos
-*-
-*-PROCEDIMIENTOS AT-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
CORTESAT_INSERCION: Finaliza OK
Proceso Finalizado en 0 segundos
-*-
CORTESAT_ACTUALIZACION: Finaliza OK
Proceso Finalizado en 0 segundos
-*-
CORTESAT_NORMALIZACION: Finaliza OK
Proceso Finalizado en 0 segundos
-*-
CORTESAT_INSERTA_DOC_DET: Finaliza OK
Proceso Finalizado en 8 segundos
-*-
DOCUMENT_EXTERNAL_DATA_RUN: Finaliza OK
Proceso Finalizado en 1 segundos
-*-
Tiempo total de ejecución:     81.25 segundos
OK
"""

# Convertir la cadena en líneas
lines = data.split('\n')

# Inicializar variables
procedimientos = {}
estadisticas = {}
current_procedimiento = None
current_details = []

# Procesar cada línea
for line in lines:
    if line in ('','-*-'):
        None
    elif line in ('CIRCUITO 88','CIRCUITO 103'):
        current_procedimiento=line
    elif '-*-' in line:
        if current_procedimiento:
            if current_details:
                procedimientos[current_procedimiento]['details'] = current_details
                current_details = []
            current_procedimiento = None
    elif line.startswith('EJECUTA CIRCUITO'):
        circuit = line.split()[2]
        procedimientos[circuit] = {}
        current_procedimiento = circuit
    elif 'Finaliza OK' in line:
        if current_procedimiento:
            procedure_name = line.split(':')[0]
            procedimientos[current_procedimiento][procedure_name] = 'OK'
    elif '-->' in line:
        if current_procedimiento:
            details = line.split('|')
            detail_dict = {}
            for detail in details:
                key, value = detail.split(':')
                detail_dict[key.strip()] = int(value.strip())
            current_details.append(detail_dict)
    elif 'Tiempo total de ejecución' in line:
        total_time = line.split(':')[1].strip()
        procedimientos['total_execution_time'] = total_time
    elif 'OK' in line or 'ERROR' in line:
        final_status = line.strip()
        procedimientos['final_status'] = final_status

# Convertir a JSON
json_output = json.dumps(procedimientos, indent=4)

# Imprimir el JSON
print(json_output)
