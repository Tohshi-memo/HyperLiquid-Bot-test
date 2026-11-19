# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T06:07:26.414257+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2462`

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

- `market_context_high->unknown_1h` score `4204.1237` n `110` status `ready` deltaP `0.7567` edge `350.3584` maxDD `-0.9174`
- `market_context_high->unknown_24h` score `39.5931` n `98` status `ready` deltaP `5.2083` edge `3.2647` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `12.8787` n `98` status `ready` deltaP `39.594` edge `1.7142` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `10.8723` n `98` status `ready` deltaP `23.5722` edge `1.4491` maxDD `-13.3222`
- `market_context_high->metal_24h` score `-0.2329` n `98` status `ready` deltaP `15.3557` edge `0.2007` maxDD `-15.7982`
- `market_context_high->metal_1h` score `-0.3615` n `110` status `ready` deltaP `3.4431` edge `0.0134` maxDD `-2.6517`
- `market_context_high->metal_4h` score `-0.7028` n `98` status `ready` deltaP `10.5525` edge `0.0018` maxDD `-6.1238`
- `market_context_high->index_1h` score `-0.8231` n `110` status `ready` deltaP `-1.4126` edge `0.0026` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.8683` n `110` status `ready` deltaP `2.2346` edge `0.0605` maxDD `-10.2705`
- `market_context_high->crypto_alt_1h` score `-1.0736` n `110` status `ready` deltaP `-2.0006` edge `0.026` maxDD `-7.6911`
- `market_context_high->crypto_alt_4h` score `-1.1833` n `98` status `ready` deltaP `-2.3239` edge `0.1448` maxDD `-17.1476`
- `market_context_high->fx_1h` score `-1.3513` n `110` status `ready` deltaP `-8.5357` edge `-0.0008` maxDD `-0.392`
- `market_context_high->crypto_major_4h` score `-1.4326` n `98` status `ready` deltaP `-4.6696` edge `0.2057` maxDD `-22.3259`
- `market_context_high->commodity_1h` score `-2.6593` n `110` status `ready` deltaP `-12.5994` edge `-0.0298` maxDD `-3.9584`
- `market_context_high->index_4h` score `-2.8124` n `98` status `ready` deltaP `-11.2836` edge `-0.0248` maxDD `-4.7471`
- `market_context_high->equity_1h` score `-2.8845` n `110` status `ready` deltaP `0.5661` edge `-0.0264` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.563` n `98` status `ready` deltaP `-24.692` edge `-0.0114` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7137` n `98` status `ready` deltaP `-18.6402` edge `-0.0043` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.4522` n `98` status `ready` deltaP `-24.6671` edge `-0.1105` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.0937` n `98` status `ready` deltaP `-16.4222` edge `-0.1061` maxDD `-20.7114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
