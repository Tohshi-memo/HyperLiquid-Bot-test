# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T03:22:42.113192+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2450`

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

- `market_context_high->unknown_24h` score `1364.6067` n `98` status `ready` deltaP `5.2083` edge `113.6825` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.2976` n `98` status `ready` deltaP `39.594` edge `1.7679` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.3075` n `98` status `ready` deltaP `24.4402` edge `1.4991` maxDD `-13.3222`
- `market_context_high->metal_24h` score `-0.2641` n `98` status `ready` deltaP `15.3557` edge `0.1981` maxDD `-15.7982`
- `market_context_high->metal_1h` score `-0.428` n `99` status `ready` deltaP `0.5065` edge `0.0052` maxDD `-2.4092`
- `market_context_high->metal_4h` score `-0.6868` n `98` status `ready` deltaP `10.8574` edge `0.0011` maxDD `-6.1238`
- `market_context_high->index_1h` score `-0.9564` n `99` status `ready` deltaP `-3.4961` edge `-0.0006` maxDD `-1.2295`
- `market_context_high->crypto_alt_4h` score `-0.958` n `98` status `ready` deltaP `-0.6471` edge `0.1625` maxDD `-17.1476`
- `market_context_high->crypto_major_4h` score `-1.1983` n `98` status `ready` deltaP `-3.2977` edge `0.2266` maxDD `-22.3259`
- `market_context_high->fx_1h` score `-1.4483` n `99` status `ready` deltaP `-9.7064` edge `-0.0013` maxDD `-0.3743`
- `market_context_high->crypto_alt_1h` score `-1.9414` n `99` status `ready` deltaP `-2.5616` edge `0.0056` maxDD `-7.6911`
- `market_context_high->crypto_major_1h` score `-2.0085` n `99` status `ready` deltaP `-0.0545` edge `0.0197` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.6824` n `98` status `ready` deltaP `-10.0641` edge `-0.0221` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9488` n `99` status `ready` deltaP `-15.8426` edge `-0.0342` maxDD `-3.8069`
- `market_context_high->equity_1h` score `-3.173` n `99` status `ready` deltaP `-0.2042` edge `-0.0453` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.6324` n `98` status `ready` deltaP `-25.4542` edge `-0.0121` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7444` n `98` status `ready` deltaP `-18.8138` edge `-0.0057` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.5624` n `98` status `ready` deltaP `-25.4293` edge `-0.1146` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.0062` n `98` status `ready` deltaP `-15.5541` edge `-0.1046` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.6542` n `98` status `ready` deltaP `-16.1057` edge `-0.2651` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
