# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T17:37:45.952937+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2298`

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

- `market_context_high->unknown_24h` score `1365.689` n `98` status `ready` deltaP `2.7778` edge `113.7889` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.944` n `98` status `ready` deltaP `40.1148` edge `1.8473` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.1761` n `98` status `ready` deltaP `25.8291` edge `1.6012` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.2671` n `98` status `ready` deltaP `2.4777` edge `0.0094` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.4858` n `98` status `ready` deltaP `1.6395` edge `0.2078` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.4945` n `98` status `ready` deltaP `15.3557` edge `0.1789` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.539` n `98` status `ready` deltaP `11.9245` edge `0.0063` maxDD `-6.1238`
- `market_context_high->crypto_major_4h` score `-0.8909` n `98` status `ready` deltaP `-1.316` edge `0.2528` maxDD `-22.3259`
- `market_context_high->index_1h` score `-0.8939` n `98` status `ready` deltaP `-2.4747` edge `0.0006` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.0879` n `98` status `ready` deltaP `-1.2098` edge `0.0189` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3304` n `98` status `ready` deltaP `-8.2977` edge `-0.0009` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-1.9246` n `98` status `ready` deltaP `-0.0397` edge `0.0266` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.4105` n `98` status `ready` deltaP `-7.6251` edge `-0.0157` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.7809` n `98` status `ready` deltaP `-14.6248` edge `-0.0295` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-2.8253` n `98` status `ready` deltaP `1.607` edge `-0.0284` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.4939` n `98` status `ready` deltaP `-24.0823` edge `-0.0097` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7648` n `98` status `ready` deltaP `-18.8138` edge `-0.0074` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.2167` n `98` status `ready` deltaP `-22.5329` edge `-0.1051` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.8536` n `98` status `ready` deltaP `-13.9916` edge `-0.1023` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-11.6005` n `98` status `ready` deltaP `-13.2093` edge `-0.1966` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
