# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T14:37:27.080018+00:00`
- Price records: `672`
- Market context records: `8311`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5886`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `news_risk_high->unknown_24h` score `6250.9562` n `52` status `ready` deltaP `35.1896` edge `520.7205` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.667` n `52` status `ready` deltaP `25.1524` edge `0.4476` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.79` n `52` status `ready` deltaP `20.6817` edge `0.1255` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5317` n `52` status `ready` deltaP `21.7988` edge `0.0847` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0375` n `52` status `ready` deltaP `9.674` edge `0.2661` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7934` n `52` status `ready` deltaP `13.6573` edge `0.1018` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6266` n `52` status `ready` deltaP `11.1124` edge `0.1012` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.6235` n `52` status `ready` deltaP `18.0934` edge `0.2267` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.2095` n `52` status `ready` deltaP `10.3776` edge `0.0784` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2516` n `52` status `ready` deltaP `4.8941` edge `0.0172` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.153` n `52` status `ready` deltaP `6.6905` edge `0.0031` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `0.024` n `52` status `ready` deltaP `4.445` edge `0.0127` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4763` n `52` status `ready` deltaP `4.1979` edge `0.0067` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2735` n `52` status `ready` deltaP `-9.7651` edge `-0.0458` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0021` n `52` status `ready` deltaP `-20.2591` edge `-0.0496` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-5.6733` n `52` status `ready` deltaP `-21.5144` edge `-0.0523` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.2018` n `52` status `ready` deltaP `-33.22` edge `-0.2146` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.722` n `52` status `ready` deltaP `-9.3082` edge `-0.3208` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.184` n `52` status `ready` deltaP `-23.9049` edge `-0.3057` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-33.3613` n `52` status `ready` deltaP `-15.0774` edge `-1.2271` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
