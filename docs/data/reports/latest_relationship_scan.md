# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T05:07:30.736207+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2452`

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

- `market_context_high->unknown_24h` score `1350.7839` n `98` status `ready` deltaP `5.2083` edge `112.5306` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.0651` n `98` status `ready` deltaP `39.594` edge `1.7381` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.0268` n `98` status `ready` deltaP `23.5722` edge `1.4689` maxDD `-13.3222`
- `market_context_high->metal_24h` score `-0.2377` n `98` status `ready` deltaP `15.3557` edge `0.2003` maxDD `-15.7982`
- `market_context_high->metal_1h` score `-0.5221` n `106` status `ready` deltaP `1.8557` edge `0.0106` maxDD `-2.6517`
- `market_context_high->metal_4h` score `-0.6736` n `98` status `ready` deltaP `10.8574` edge `0.0022` maxDD `-6.1238`
- `market_context_high->crypto_major_1h` score `-0.8381` n `106` status `ready` deltaP `2.4997` edge `0.0626` maxDD `-10.2705`
- `market_context_high->index_1h` score `-0.8579` n `106` status `ready` deltaP `-2.1128` edge `0.0028` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-0.9087` n `106` status `ready` deltaP `-0.435` edge `0.0367` maxDD `-7.6911`
- `market_context_high->crypto_alt_4h` score `-1.1056` n `98` status `ready` deltaP `-1.7142` edge `0.1507` maxDD `-17.1476`
- `market_context_high->fx_1h` score `-1.2998` n `106` status `ready` deltaP `-7.9229` edge `-0.0006` maxDD `-0.392`
- `market_context_high->crypto_major_4h` score `-1.3315` n `98` status `ready` deltaP `-4.0599` edge `0.2146` maxDD `-22.3259`
- `market_context_high->index_4h` score `-2.7504` n `98` status `ready` deltaP `-10.6738` edge `-0.0237` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.7907` n `106` status `ready` deltaP `-13.9419` edge `-0.0318` maxDD `-3.9584`
- `market_context_high->equity_1h` score `-2.8328` n `106` status `ready` deltaP `0.7626` edge `-0.0234` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.619` n `98` status `ready` deltaP `-25.3018` edge `-0.012` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.736` n `98` status `ready` deltaP `-18.8138` edge `-0.005` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.5346` n `98` status `ready` deltaP `-25.2768` edge `-0.1133` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.0436` n `98` status `ready` deltaP `-15.9014` edge `-0.1054` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.8398` n `98` status `ready` deltaP `-16.7154` edge `-0.2765` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
