# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T03:22:25.534677+00:00`
- Price records: `672`
- Market context records: `2827`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `2.3459` n `142` status `ready` deltaP `2.9489` edge `0.2223` maxDD `-1.7175`
- `market_context_high->unknown_4h` score `0.9496` n `142` status `ready` deltaP `6.4904` edge `0.1412` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.8624` n `142` status `ready` deltaP `12.4266` edge `0.2984` maxDD `-12.4171`
- `market_context_high->crypto_alt_24h` score `0.3294` n `142` status `ready` deltaP `-0.5966` edge `0.4231` maxDD `-22.6673`
- `market_context_high->index_4h` score `0.2776` n `142` status `ready` deltaP `12.996` edge `0.0331` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.2074` n `142` status `ready` deltaP `4.6302` edge `0.0595` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.114` n `142` status `ready` deltaP `3.8986` edge `0.0088` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.5322` n `142` status `ready` deltaP `0.7654` edge `0.002` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.5766` n `142` status `ready` deltaP `-0.9867` edge `0.0029` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.728` n `142` status `ready` deltaP `4.9465` edge `0.0497` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7612` n `142` status `ready` deltaP `-0.3163` edge `-0.0109` maxDD `-3.0996`
- `market_context_high->index_24h` score `-0.96` n `142` status `ready` deltaP `2.4257` edge `0.0019` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `-0.9732` n `142` status `ready` deltaP `3.6266` edge `0.038` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.0454` n `142` status `ready` deltaP `-3.1985` edge `0.0175` maxDD `-2.6634`
- `market_context_high->equity_4h` score `-1.1482` n `142` status `ready` deltaP `1.9624` edge `0.0292` maxDD `-5.7037`
- `market_context_high->fx_4h` score `-1.1957` n `142` status `ready` deltaP `-4.2103` edge `0.0063` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.291` n `142` status `ready` deltaP `2.2951` edge `0.0112` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.6572` n `142` status `ready` deltaP `-4.1422` edge `-0.0233` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.8531` n `142` status `ready` deltaP `13.1183` edge `0.1922` maxDD `-28.7261`
- `market_context_high->metal_4h` score `-2.4538` n `142` status `ready` deltaP `-1.6854` edge `-0.0483` maxDD `-11.4038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
