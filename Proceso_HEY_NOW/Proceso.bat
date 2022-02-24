set rutaDescarga= C:\API_HEY_NOW\Descargas_Online
set rutaProceso= C:\API_HEY_NOW\Proceso_HEY_NOW
set ruta1= gs://niubiz-pe/Hey_Now/Hey_Now_Data/*%date:~-4,4%%date:~-10,2%%date:~-7,2%*
set ruta2= gs://niubiz-pe/Hey_Now/Hey_Now_data_chat/*%date:~-4,4%%date:~-10,2%%date:~-7,2%*
set ruta3= gs://niubiz-pe/Hey_Now/Hey_Now_step/*%date:~-4,4%%date:~-10,2%%date:~-7,2%*



del %rutaDescarga%\*.csv

cd %rutaProceso%
Call python ConsumirArchivoScroll1.py
Call python ConsumirArchivoScroll2.py
Call python ConsumirArchivoScroll3.py


::Borrar Archivos 
::Call gsutil rm -r %ruta1%
::Call gsutil rm -r %ruta2% 
::Call gsutil rm -r %ruta3% 

::Cargar storage archivos en el storage
cd %rutaDescarga%
::Call gsutil -m cp -r "datosArchivo1"*.csv gs://niubiz-pe/Hey_Now/Hey_Now_Data/
::Call gsutil -m cp -r "datosArchivo2"*.csv gs://niubiz-pe/Hey_Now/Hey_Now_data_chat/
::Call gsutil -m cp -r "datosArchivo3"*.csv gs://niubiz-pe/Hey_Now/Hey_Now_step/


Call bq load --max_bad_records=0 --source_format=CSV  --allow_jagged_rows --allow_quoted_newlines --replace=false --skip_leading_rows=1 --ignore_unknown_values --field_delimiter=, niubiz-pe:Hey_Now.Hey_Now_data C:\API_HEY_NOW\Descargas_Online\datosArchivo1.csv C:\API_HEY_NOW\Proceso_HEY_NOW\Hey_now_data_1.json
Call bq load --max_bad_records=0 --source_format=CSV  --allow_jagged_rows --allow_quoted_newlines --replace=false --skip_leading_rows=1 --ignore_unknown_values --field_delimiter=; niubiz-pe:Hey_Now.Hey_now_data_source_chat  C:\API_HEY_NOW\Descargas_Online\datosArchivo2.csv C:\API_HEY_NOW\Proceso_HEY_NOW\Hey_now_data_source_chat2.json
Call bq load --max_bad_records=0 --source_format=CSV  --allow_jagged_rows --allow_quoted_newlines --replace=false --skip_leading_rows=1 --ignore_unknown_values --field_delimiter=; niubiz-pe:Hey_Now.Hey_now_data_source_step  C:\API_HEY_NOW\Descargas_Online\datosArchivo3.csv C:\API_HEY_NOW\Proceso_HEY_NOW\ESQUEMA_STEPS_HEY.json


Call bq query --use_legacy_sql=false "CREATE OR REPLACE TABLE `niubiz-pe.Hey_Now.Hey_Now_data` AS SELECT * EXCEPT(rn) FROM (SELECT *, ROW_NUMBER() OVER(PARTITION BY data_id ORDER BY data_id) rn FROM `niubiz-pe.Hey_Now.Hey_Now_data`) WHERE rn = 1"
Call bq query --use_legacy_sql=false "CREATE OR REPLACE TABLE `niubiz-pe.Hey_Now.Hey_now_data_source_chat` AS SELECT * EXCEPT(rn) FROM (SELECT *, ROW_NUMBER() OVER(PARTITION BY id ORDER BY ID) rn FROM `niubiz-pe.Hey_Now.Hey_now_data_source_chat`) WHERE rn = 1"
Call bq query --use_legacy_sql=false "CREATE OR REPLACE TABLE `niubiz-pe.Hey_Now.Hey_now_data_source_step` AS SELECT * EXCEPT(rn) FROM (SELECT *, ROW_NUMBER() OVER(PARTITION BY key ORDER BY key) rn FROM `niubiz-pe.Hey_Now.Hey_now_data_source_step`) WHERE rn = 1"
