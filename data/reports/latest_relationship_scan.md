# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-28T00:22:27.087417+00:00`
- Price records: `672`
- Market context records: `4988`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `20.9704` n `89` status `ready` deltaP `3.8586` edge `1.7719` maxDD `-1.674`
- `market_context_high->crypto_major_4h` score `6.1642` n `87` status `ready` deltaP `17.944` edge `0.5426` maxDD `-7.8836`
- `market_context_high->unknown_24h` score `5.8577` n `74` status `ready` deltaP `28.4253` edge `0.3329` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `5.1492` n `87` status `ready` deltaP `12.5841` edge `0.4846` maxDD `-7.8181`
- `market_context_high->unknown_4h` score `1.4761` n `87` status `ready` deltaP `20.5845` edge `0.088` maxDD `-5.5109`
- `market_context_high->metal_4h` score `1.1097` n `87` status `ready` deltaP `11.0352` edge `0.1268` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.8835` n `89` status `ready` deltaP `6.3261` edge `0.1232` maxDD `-4.6734`
- `market_context_high->equity_1h` score `0.8813` n `89` status `ready` deltaP `7.7525` edge `0.0791` maxDD `-2.5875`
- `market_context_high->equity_4h` score `0.5905` n `87` status `ready` deltaP `4.7029` edge `0.1825` maxDD `-6.3852`
- `market_context_high->metal_1h` score `0.3531` n `89` status `ready` deltaP `6.0267` edge `0.0389` maxDD `-1.3057`
- `market_context_high->index_4h` score `0.3454` n `87` status `ready` deltaP `5.1479` edge `0.0427` maxDD `-0.8587`
- `market_context_high->crypto_alt_1h` score `0.1043` n `89` status `ready` deltaP `4.0066` edge `0.0889` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.2479` n `74` status `ready` deltaP `5.9122` edge `0.005` maxDD `-1.7626`
- `market_context_high->commodity_1h` score `-0.4441` n `89` status `ready` deltaP `0.0353` edge `0.0088` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5204` n `89` status `ready` deltaP `2.5096` edge `0.014` maxDD `-0.5946`
- `market_context_high->fx_4h` score `-0.8271` n `87` status `ready` deltaP `-1.1845` edge `-0.0011` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.2654` n `87` status `ready` deltaP `3.5867` edge `-0.0041` maxDD `-5.021`
- `market_context_high->fx_1h` score `-1.6469` n `89` status `ready` deltaP `-10.7515` edge `-0.0053` maxDD `-0.4876`
- `market_context_high->commodity_24h` score `-3.9379` n `74` status `ready` deltaP `7.8782` edge `-0.0465` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-4.3154` n `74` status `ready` deltaP `-1.7361` edge `0.0038` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
