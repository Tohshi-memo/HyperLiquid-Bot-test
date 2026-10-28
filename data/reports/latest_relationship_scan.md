# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T16:22:41.693847+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8530`

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

- `market_context_high->unknown_24h` score `1366.8568` n `141` status `ready` deltaP `-2.9736` edge `114.0173` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `22.1328` n `149` status `ready` deltaP `4.385` edge `1.8304` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.5111` n `141` status `ready` deltaP `24.9926` edge `0.0281` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.1757` n `149` status `ready` deltaP `7.269` edge `0.002` maxDD `-0.1986`
- `market_context_high->fx_4h` score `-0.0373` n `149` status `ready` deltaP `7.6864` edge `0.0055` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0816` n `149` status `ready` deltaP `8.4767` edge `0.0077` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.2658` n `149` status `ready` deltaP `7.7282` edge `0.0427` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.3882` n `149` status `ready` deltaP `7.3539` edge `0.0405` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.5716` n `141` status `ready` deltaP `12.8694` edge `0.0238` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.7075` n `149` status `ready` deltaP `-0.9394` edge `0.0057` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7359` n `149` status `ready` deltaP `-3.4743` edge `-0.0029` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.745` n `149` status `ready` deltaP `9.0563` edge `-0.0018` maxDD `-4.6603`
- `market_context_high->equity_1h` score `-1.3875` n `149` status `ready` deltaP `1.2388` edge `0.0051` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5346` n `149` status `ready` deltaP `3.0452` edge `0.0193` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.7599` n `141` status `ready` deltaP `6.7709` edge `0.0213` maxDD `-15.7143`
- `market_context_high->metal_24h` score `-2.944` n `141` status `ready` deltaP `2.0871` edge `0.0277` maxDD `-8.9561`
- `market_context_high->index_4h` score `-3.0164` n `149` status `ready` deltaP `-9.0267` edge `-0.029` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.1563` n `141` status `ready` deltaP `1.5846` edge `0.0705` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.3608` n `149` status `ready` deltaP `4.119` edge `-0.0264` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.2991` n `149` status `ready` deltaP `-2.7152` edge `-0.1379` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
