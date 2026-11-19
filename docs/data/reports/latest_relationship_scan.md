# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T06:22:26.190316+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2640`

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

- `market_context_high->unknown_1h` score `7771.9734` n `111` status `ready` deltaP `0.8632` edge `647.6785` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `3782.2181` n `99` status `ready` deltaP `-0.3064` edge `315.2153` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `12.8257` n `98` status `ready` deltaP `39.594` edge `1.7074` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `10.8271` n `98` status `ready` deltaP `23.5722` edge `1.4433` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.2147` n `111` status `ready` deltaP `3.7439` edge `0.014` maxDD `-2.6517`
- `market_context_high->metal_24h` score `-0.2341` n `98` status `ready` deltaP `15.3557` edge `0.2006` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.7434` n `99` status `ready` deltaP `10.0886` edge `0.0018` maxDD `-6.1475`
- `market_context_high->index_1h` score `-0.801` n `111` status `ready` deltaP `-1.0628` edge `0.0031` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.8327` n `111` status `ready` deltaP `2.5435` edge `0.063` maxDD `-10.2705`
- `market_context_high->crypto_alt_1h` score `-1.0434` n `111` status `ready` deltaP `-1.6589` edge `0.0276` maxDD `-7.6911`
- `market_context_high->crypto_alt_4h` score `-1.1243` n `99` status `ready` deltaP `-1.8786` edge `0.1494` maxDD `-17.1476`
- `market_context_high->crypto_major_4h` score `-1.3242` n `99` status `ready` deltaP `-4.2037` edge `0.2165` maxDD `-22.3259`
- `market_context_high->fx_1h` score `-1.3793` n `111` status `ready` deltaP `-8.8715` edge `-0.0009` maxDD `-0.392`
- `market_context_high->commodity_1h` score `-2.6044` n `111` status `ready` deltaP `-12.0179` edge `-0.0291` maxDD `-3.9584`
- `market_context_high->index_4h` score `-2.7566` n `99` status `ready` deltaP `-10.797` edge `-0.0234` maxDD `-4.7471`
- `market_context_high->equity_1h` score `-2.8129` n `111` status `ready` deltaP `0.8914` edge `-0.0226` maxDD `-11.0868`
- `market_context_high->fx_4h` score `-4.5586` n `99` status `ready` deltaP `-24.6736` edge `-0.0111` maxDD `-2.0104`
- `market_context_high->fx_24h` score `-6.6962` n `98` status `ready` deltaP `-18.4666` edge `-0.004` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.4877` n `99` status `ready` deltaP `-24.7105` edge `-0.1088` maxDD `-14.7015`
- `market_context_high->index_24h` score `-9.0949` n `98` status `ready` deltaP `-16.4222` edge `-0.1062` maxDD `-20.7114`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
