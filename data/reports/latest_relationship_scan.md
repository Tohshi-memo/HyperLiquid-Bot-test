# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T04:52:37.540350+00:00`
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

- `market_context_high->unknown_24h` score `1353.3027` n `98` status `ready` deltaP `5.2083` edge `112.7405` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.1213` n `98` status `ready` deltaP `39.594` edge `1.7453` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `11.0912` n `98` status `ready` deltaP `23.7458` edge `1.476` maxDD `-13.3222`
- `market_context_high->metal_24h` score `-0.2377` n `98` status `ready` deltaP `15.3557` edge `0.2003` maxDD `-15.7982`
- `market_context_high->metal_1h` score `-0.5569` n `105` status `ready` deltaP `1.5112` edge `0.01` maxDD `-2.6517`
- `market_context_high->metal_4h` score `-0.6748` n `98` status `ready` deltaP `10.8574` edge `0.0021` maxDD `-6.1238`
- `market_context_high->index_1h` score `-0.8333` n `105` status `ready` deltaP `-1.6995` edge `0.0032` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.8626` n `105` status `ready` deltaP `2.1642` edge `0.0617` maxDD `-10.2705`
- `market_context_high->crypto_alt_1h` score `-0.8628` n `105` status `ready` deltaP `0.0142` edge `0.0396` maxDD `-7.6911`
- `market_context_high->crypto_alt_4h` score `-1.0883` n `98` status `ready` deltaP `-1.5617` edge `0.1519` maxDD `-17.1476`
- `market_context_high->crypto_major_4h` score `-1.3119` n `98` status `ready` deltaP `-3.9074` edge `0.2161` maxDD `-22.3259`
- `market_context_high->fx_1h` score `-1.3497` n `105` status `ready` deltaP `-8.5158` edge `-0.0008` maxDD `-0.392`
- `market_context_high->index_4h` score `-2.7492` n `98` status `ready` deltaP `-10.6738` edge `-0.0236` maxDD `-4.7471`
- `market_context_high->equity_1h` score `-2.7741` n `105` status `ready` deltaP `1.2118` edge `-0.0215` maxDD `-11.0868`
- `market_context_high->commodity_1h` score `-2.8351` n `105` status `ready` deltaP `-14.4212` edge `-0.0323` maxDD `-3.9584`
- `market_context_high->fx_4h` score `-4.6202` n `98` status `ready` deltaP `-25.3018` edge `-0.0121` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7372` n `98` status `ready` deltaP `-18.8138` edge `-0.0051` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.5382` n `98` status `ready` deltaP `-25.2768` edge `-0.1136` maxDD `-14.6855`
- `market_context_high->index_24h` score `-9.0273` n `98` status `ready` deltaP `-15.7278` edge `-0.1052` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.8338` n `98` status `ready` deltaP `-16.7154` edge `-0.276` maxDD `-44.2305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
