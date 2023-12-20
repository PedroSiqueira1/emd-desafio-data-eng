{{ config(materialized='view')}}


WITH dados_brt AS (

    SELECT *
    FROM transporte_rodoviario_gps.dados_brt
)

SELECT
  id,
  codigo,
  latitude,
  longitude,
  velocidade

FROM dados_brt