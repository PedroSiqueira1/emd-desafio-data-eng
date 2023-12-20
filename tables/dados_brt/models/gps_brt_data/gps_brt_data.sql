{{ config(materialized='view')}}

SELECT
  id,
  codigo,
  latitude,
  longitude,
  velocidade

FROM transporte_rodoviario_gps.dados_brt