# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T02:52:26.737321+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4173`

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

- `market_context_high->unknown_24h` score `1489.7346` n `98` status `ready` deltaP `3.4722` edge `124.1214` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.378` n `98` status `ready` deltaP `46.0176` edge `1.9918` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.2214` n `98` status `ready` deltaP `31.0374` edge `1.8287` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.4143` n `98` status `ready` deltaP `0.2322` edge `0.0055` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.7972` n `98` status `ready` deltaP `-0.4947` edge `0.1821` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.8665` n `98` status `ready` deltaP `15.3557` edge `0.1479` maxDD `-15.7982`
- `market_context_high->index_1h` score `-0.9928` n `98` status `ready` deltaP `-4.1214` edge `-0.0011` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-1.1235` n `98` status `ready` deltaP `7.1989` edge `-0.0109` maxDD `-6.1238`
- `market_context_high->crypto_alt_1h` score `-1.1588` n `98` status `ready` deltaP `-1.5092` edge `0.0118` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.2933` n `98` status `ready` deltaP `-7.8486` edge `-0.0008` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.5411` n `98` status `ready` deltaP `-3.755` edge `0.1857` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.2519` n `98` status `ready` deltaP `-1.8361` edge `0.0113` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.8184` n `98` status `ready` deltaP `-11.2836` edge `-0.0253` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9786` n `98` status `ready` deltaP `-16.2715` edge `-0.035` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.3091` n `98` status `ready` deltaP `-0.3391` edge `-0.0549` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6096` n `98` status `ready` deltaP `-25.4542` edge `-0.0102` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7564` n `98` status `ready` deltaP `-18.8138` edge `-0.0067` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.7357` n `98` status `ready` deltaP `-26.8012` edge `-0.1199` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.42` n `98` status `ready` deltaP `-9.6514` edge `-0.0951` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-13.5161` n `98` status `ready` deltaP `-18.2398` edge `-0.3193` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
