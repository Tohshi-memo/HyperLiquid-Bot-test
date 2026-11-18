# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T21:07:32.332463+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2262`

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

- `market_context_high->unknown_24h` score `1368.2992` n `98` status `ready` deltaP `4.3403` edge `113.996` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.3881` n `98` status `ready` deltaP `39.594` edge `1.7795` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.4533` n `98` status `ready` deltaP `24.4402` edge `1.5178` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.3302` n `98` status `ready` deltaP `1.4298` edge `0.0083` maxDD `-2.1461`
- `market_context_high->metal_24h` score `-0.4105` n `98` status `ready` deltaP `15.3557` edge `0.1859` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.5838` n `98` status `ready` deltaP `11.6196` edge `0.0046` maxDD `-6.1238`
- `market_context_high->crypto_alt_4h` score `-0.6329` n `98` status `ready` deltaP `1.0297` edge `0.193` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.8853` n `98` status `ready` deltaP `-2.325` edge `0.0007` maxDD `-1.2295`
- `market_context_high->crypto_major_4h` score `-0.9622` n `98` status `ready` deltaP `-1.7733` edge `0.2467` maxDD `-22.3259`
- `market_context_high->crypto_alt_1h` score `-1.1292` n `98` status `ready` deltaP `-1.5092` edge `0.0156` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3676` n `98` status `ready` deltaP `-8.7468` edge `-0.001` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-1.879` n `98` status `ready` deltaP `0.4094` edge `0.0274` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.5186` n `98` status `ready` deltaP `-8.6921` edge `-0.0176` maxDD `-4.7471`
- `market_context_high->equity_1h` score `-2.8696` n `98` status `ready` deltaP `1.4573` edge `-0.0311` maxDD `-11.0868`
- `market_context_high->commodity_1h` score `-2.9438` n `98` status `ready` deltaP `-15.9721` edge `-0.0341` maxDD `-3.7125`
- `market_context_high->fx_4h` score `-4.5194` n `98` status `ready` deltaP `-24.3871` edge `-0.0098` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7528` n `98` status `ready` deltaP `-18.8138` edge `-0.0064` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.4046` n `98` status `ready` deltaP `-24.0573` edge `-0.1106` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.0906` n `98` status `ready` deltaP `-16.2486` edge `-0.107` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-11.9595` n `98` status `ready` deltaP `-14.2764` edge `-0.2194` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
