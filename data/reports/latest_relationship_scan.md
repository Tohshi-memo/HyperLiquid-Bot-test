# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T16:37:26.307991+00:00`
- Price records: `672`
- Market context records: `6936`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11706`

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

- `market_context_high->fx_1h` score `-0.2501` n `233` status `ready` deltaP `2.1806` edge `0.0019` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4486` n `233` status `ready` deltaP `2.7801` edge `0.0205` maxDD `-3.7803`
- `market_context_high->metal_1h` score `-0.7061` n `233` status `ready` deltaP `-1.9718` edge `-0.0006` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.7237` n `233` status `ready` deltaP `-0.205` edge `-0.0003` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.7593` n `233` status `ready` deltaP `3.2292` edge `0.0158` maxDD `-5.0483`
- `market_context_high->fx_4h` score `-0.821` n `224` status `ready` deltaP `13.6978` edge `0.0098` maxDD `-2.1765`
- `market_context_high->unknown_24h` score `-1.0357` n `216` status `ready` deltaP `-7.4892` edge `0.3383` maxDD `-16.026`
- `market_context_high->commodity_1h` score `-1.1602` n `233` status `ready` deltaP `-2.1209` edge `-0.0137` maxDD `-2.1742`
- `market_context_high->commodity_4h` score `-1.594` n `224` status `ready` deltaP `-3.8655` edge `-0.0296` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6161` n `233` status `ready` deltaP `-2.3509` edge `-0.0289` maxDD `-3.2083`
- `market_context_high->index_4h` score `-1.6363` n `224` status `ready` deltaP `8.8197` edge `-0.0106` maxDD `-11.3047`
- `market_context_high->equity_1h` score `-1.856` n `233` status `ready` deltaP `2.6297` edge `-0.0175` maxDD `-14.7052`
- `market_context_high->metal_4h` score `-1.9245` n `224` status `ready` deltaP `5.368` edge `0.0158` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.7766` n `224` status `ready` deltaP `1.6006` edge `-0.0083` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.7777` n `224` status `ready` deltaP `-0.2396` edge `-0.0218` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-2.9815` n `224` status `ready` deltaP `-7.6655` edge `0.0392` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.3747` n `216` status `ready` deltaP `-4.1699` edge `-0.0666` maxDD `-5.2791`
- `market_context_high->fx_24h` score `-4.222` n `216` status `ready` deltaP `-5.761` edge `-0.0098` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-6.4533` n `224` status `ready` deltaP `6.2173` edge `-0.0743` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.8674` n `216` status `ready` deltaP `-13.235` edge `-0.1183` maxDD `-34.0917`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
