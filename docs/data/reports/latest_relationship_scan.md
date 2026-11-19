# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T01:52:38.056706+00:00`
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

- `market_context_high->unknown_24h` score `1367.5479` n `98` status `ready` deltaP `5.2083` edge `113.9276` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.3038` n `98` status `ready` deltaP `39.594` edge `1.7687` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.3309` n `98` status `ready` deltaP `24.4402` edge `1.5021` maxDD `-13.3222`
- `market_context_high->metal_24h` score `-0.2833` n `98` status `ready` deltaP `15.3557` edge `0.1965` maxDD `-15.7982`
- `market_context_high->metal_1h` score `-0.3714` n `98` status `ready` deltaP `0.831` edge `0.007` maxDD `-2.1461`
- `market_context_high->metal_4h` score `-0.6454` n `98` status `ready` deltaP `11.3147` edge `0.0015` maxDD `-6.1238`
- `market_context_high->crypto_alt_4h` score `-0.8457` n `98` status `ready` deltaP `0.2675` edge `0.1708` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.9686` n `98` status `ready` deltaP `-3.6723` edge `-0.001` maxDD `-1.2295`
- `market_context_high->crypto_major_4h` score `-1.1252` n `98` status `ready` deltaP `-2.6879` edge `0.2319` maxDD `-22.3259`
- `market_context_high->crypto_alt_1h` score `-1.2461` n `98` status `ready` deltaP `-2.2577` edge `0.0056` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.4406` n `98` status `ready` deltaP `-9.645` edge `-0.0011` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-2.0206` n `98` status `ready` deltaP `-0.0397` edge `0.0186` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.6216` n `98` status `ready` deltaP `-9.4543` edge `-0.0211` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9486` n `98` status `ready` deltaP `-15.9721` edge `-0.0345` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.1874` n `98` status `ready` deltaP `-0.0397` edge `-0.0476` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.6252` n `98` status `ready` deltaP `-25.4542` edge `-0.0115` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7444` n `98` status `ready` deltaP `-18.8138` edge `-0.0057` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.5004` n `98` status `ready` deltaP `-24.8195` edge `-0.1135` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.0158` n `98` status `ready` deltaP `-15.5541` edge `-0.1054` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.4397` n `98` status `ready` deltaP `-15.3435` edge `-0.2523` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
