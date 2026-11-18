# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T19:37:45.999454+00:00`
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

- `market_context_high->unknown_24h` score `1366.6333` n `98` status `ready` deltaP `3.6458` edge `113.8618` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.562` n `98` status `ready` deltaP `39.594` edge `1.8018` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.6616` n `98` status `ready` deltaP `24.4402` edge `1.5445` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.3052` n `98` status `ready` deltaP `1.8789` edge `0.0085` maxDD `-2.1461`
- `market_context_high->metal_24h` score `-0.4537` n `98` status `ready` deltaP `15.3557` edge `0.1823` maxDD `-15.7982`
- `market_context_high->crypto_alt_4h` score `-0.5045` n `98` status `ready` deltaP `1.6395` edge `0.2054` maxDD `-17.1476`
- `market_context_high->metal_4h` score `-0.5486` n `98` status `ready` deltaP `11.9245` edge `0.0055` maxDD `-6.1238`
- `market_context_high->crypto_major_4h` score `-0.8589` n `98` status `ready` deltaP `-1.316` edge `0.2569` maxDD `-22.3259`
- `market_context_high->index_1h` score `-0.8604` n `98` status `ready` deltaP `-1.8759` edge `0.0009` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.1284` n `98` status `ready` deltaP `-1.5092` edge `0.0157` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3676` n `98` status `ready` deltaP `-8.7468` edge `-0.001` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-1.9198` n `98` status `ready` deltaP `0.11` edge `0.026` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.4373` n `98` status `ready` deltaP `-7.9299` edge `-0.0159` maxDD `-4.7471`
- `market_context_high->equity_1h` score `-2.7857` n `98` status `ready` deltaP `1.9064` edge `-0.0271` maxDD `-11.0868`
- `market_context_high->commodity_1h` score `-2.8899` n `98` status `ready` deltaP `-15.523` edge `-0.0326` maxDD `-3.7125`
- `market_context_high->fx_4h` score `-4.4683` n `98` status `ready` deltaP `-23.7774` edge `-0.0096` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7564` n `98` status `ready` deltaP `-18.8138` edge `-0.0067` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.293` n `98` status `ready` deltaP `-23.1427` edge `-0.1074` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.9936` n `98` status `ready` deltaP `-15.3805` edge `-0.1047` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-11.6801` n `98` status `ready` deltaP `-13.5142` edge `-0.2012` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
