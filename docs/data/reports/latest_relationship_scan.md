# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T06:37:29.753763+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8769`

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

- `market_context_high->unknown_24h` score `1204.2214` n `135` status `ready` deltaP `-3.7616` edge `100.4696` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `41.9112` n `148` status `ready` deltaP `5.2406` edge `3.4729` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.8907` n `135` status `ready` deltaP `27.1875` edge `0.0451` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3062` n `148` status `ready` deltaP `8.7797` edge `0.0028` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.069` n `148` status `ready` deltaP `8.7591` edge `0.0072` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0702` n `148` status `ready` deltaP `8.6219` edge `0.0082` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3758` n `148` status `ready` deltaP `6.9024` edge `0.0341` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.4198` n `135` status `ready` deltaP `12.257` edge `0.0217` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.5578` n `148` status `ready` deltaP `5.7144` edge `0.0373` maxDD `-1.0837`
- `market_context_high->metal_4h` score `-0.6723` n `148` status `ready` deltaP `10.0198` edge `0.0011` maxDD `-4.6603`
- `market_context_high->commodity_1h` score `-0.7341` n `148` status `ready` deltaP `-1.1207` edge `0.0047` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7346` n `148` status `ready` deltaP `-3.3743` edge `-0.0034` maxDD `-1.4631`
- `market_context_high->equity_24h` score `-1.3374` n `135` status `ready` deltaP `8.0671` edge `0.1312` maxDD `-15.7143`
- `market_context_high->equity_1h` score `-1.534` n `148` status `ready` deltaP `-0.0041` edge `-0.0054` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6376` n `148` status `ready` deltaP `2.4599` edge `0.01` maxDD `-12.2409`
- `market_context_high->metal_24h` score `-1.8501` n `135` status `ready` deltaP `9.1551` edge `0.0626` maxDD `-8.2244`
- `market_context_high->index_4h` score `-3.04` n `148` status `ready` deltaP `-8.9321` edge `-0.0316` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.2236` n `135` status `ready` deltaP `0.544` edge `0.0688` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.5839` n `148` status `ready` deltaP `2.8139` edge `-0.0463` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.6743` n `148` status `ready` deltaP `-4.3795` edge `-0.1749` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
