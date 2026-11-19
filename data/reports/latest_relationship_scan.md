# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T07:22:34.586972+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2638`

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

- `market_context_high->unknown_1h` score `11501.295` n `112` status `ready` deltaP `0.9678` edge `958.4546` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `7893.5176` n `103` status `ready` deltaP `0.0074` edge `657.8215` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `12.6291` n `98` status `ready` deltaP `39.594` edge `1.6822` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `10.6573` n `98` status `ready` deltaP `23.0513` edge `1.425` maxDD `-13.3222`
- `market_context_high->metal_24h` score `-0.2461` n `98` status `ready` deltaP `15.3557` edge `0.1996` maxDD `-15.7982`
- `market_context_high->metal_1h` score `-0.2505` n `112` status `ready` deltaP `3.1437` edge `0.0134` maxDD `-2.6517`
- `market_context_high->metal_4h` score `-0.5171` n `103` status `ready` deltaP `11.5972` edge `0.0106` maxDD `-6.1475`
- `market_context_high->crypto_major_4h` score `-0.7574` n `103` status `ready` deltaP `-2.1548` edge `0.2755` maxDD `-22.3259`
- `market_context_high->crypto_alt_4h` score `-0.7661` n `103` status `ready` deltaP `-0.0607` edge `0.1832` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.7972` n `112` status `ready` deltaP `-1.0212` edge `0.0033` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.8303` n `112` status `ready` deltaP `2.5449` edge `0.0633` maxDD `-10.2705`
- `market_context_high->crypto_alt_1h` score `-1.0323` n `112` status `ready` deltaP `-1.4756` edge `0.0278` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3806` n `112` status `ready` deltaP `-8.9019` edge `-0.0008` maxDD `-0.392`
- `market_context_high->index_4h` score `-2.4529` n `103` status `ready` deltaP `-8.3649` edge `-0.0143` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.5798` n `112` status `ready` deltaP `-11.8905` edge `-0.0279` maxDD `-3.9584`
- `market_context_high->equity_1h` score `-2.7468` n `112` status `ready` deltaP `1.358` edge `-0.0202` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.266` n `103` status `ready` deltaP `-21.3` edge `-0.0092` maxDD `-2.0104`
- `market_context_high->fx_24h` score `-6.6311` n `98` status `ready` deltaP `-17.7721` edge `-0.0032` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.4106` n `103` status `ready` deltaP `-23.3617` edge `-0.1024` maxDD `-14.7522`
- `market_context_high->index_24h` score `-9.1232` n `98` status `ready` deltaP `-16.5958` edge `-0.1074` maxDD `-20.7114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
