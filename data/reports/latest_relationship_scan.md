# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T02:56:13.589790+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11744`

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

- `market_context_high->unknown_24h` score `25.1657` n `143` status `ready` deltaP `-14.9919` edge `2.4425` maxDD `-9.6329`
- `market_context_high->fx_24h` score `1.0651` n `143` status `ready` deltaP `20.0592` edge `0.0358` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.9257` n `168` status `ready` deltaP `12.4201` edge `0.0658` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6441` n `180` status `ready` deltaP `8.9055` edge `0.0286` maxDD `-0.7439`
- `market_context_high->fx_1h` score `-0.1629` n `180` status `ready` deltaP `3.7159` edge `-0.0005` maxDD `-0.613`
- `market_context_high->fx_4h` score `-0.1975` n `168` status `ready` deltaP `4.4788` edge `0.0048` maxDD `-0.4647`
- `market_context_high->index_1h` score `-0.8397` n `180` status `ready` deltaP `-6.67` edge `-0.0044` maxDD `-1.0359`
- `market_context_high->metal_1h` score `-1.2984` n `180` status `ready` deltaP `-5.2195` edge `-0.0098` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-1.477` n `180` status `ready` deltaP `-6.4604` edge `-0.0186` maxDD `-6.8818`
- `market_context_high->metal_24h` score `-1.7668` n `143` status `ready` deltaP `2.2203` edge `-0.0296` maxDD `-2.9283`
- `market_context_high->index_4h` score `-1.8686` n `168` status `ready` deltaP `-7.259` edge `-0.0179` maxDD `-1.4875`
- `market_context_high->commodity_24h` score `-1.9627` n `143` status `ready` deltaP `8.4231` edge `0.092` maxDD `-23.3158`
- `market_context_high->index_24h` score `-2.2211` n `143` status `ready` deltaP `-9.7829` edge `-0.01` maxDD `-6.7627`
- `market_context_high->crypto_alt_1h` score `-2.7195` n `180` status `ready` deltaP `-9.9201` edge `-0.0419` maxDD `-6.4874`
- `market_context_high->metal_4h` score `-3.2123` n `168` status `ready` deltaP `-8.101` edge `-0.0373` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.6161` n `180` status `ready` deltaP `-9.0186` edge `-0.0508` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-4.5115` n `168` status `ready` deltaP `-16.7973` edge `-0.1555` maxDD `-15.8728`
- `market_context_high->crypto_alt_4h` score `-6.675` n `168` status `ready` deltaP `-12.2314` edge `-0.1399` maxDD `-20.1177`
- `market_context_high->crypto_major_24h` score `-6.6881` n `143` status `ready` deltaP `-13.1122` edge `-0.1929` maxDD `-33.5037`
- `market_context_high->crypto_alt_24h` score `-9.5405` n `143` status `ready` deltaP `-12.9485` edge `-0.2289` maxDD `-27.3857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
