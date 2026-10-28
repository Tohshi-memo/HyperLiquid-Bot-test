# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T06:22:27.601790+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8793`

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

- `market_context_high->unknown_24h` score `1190.9794` n `135` status `ready` deltaP `-3.7616` edge `99.3661` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `43.1616` n `148` status `ready` deltaP `5.2406` edge `3.5771` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9003` n `135` status `ready` deltaP `27.1875` edge `0.0459` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3062` n `148` status `ready` deltaP `8.7797` edge `0.0028` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.069` n `148` status `ready` deltaP `8.7591` edge `0.0072` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0694` n `148` status `ready` deltaP `8.6219` edge `0.0083` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3579` n `148` status `ready` deltaP `7.0521` edge `0.0354` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.41` n `135` status `ready` deltaP `12.4306` edge `0.0218` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.5614` n `148` status `ready` deltaP `5.7144` edge `0.037` maxDD `-1.0837`
- `market_context_high->metal_4h` score `-0.6723` n `148` status `ready` deltaP `10.0198` edge `0.0011` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.7261` n `148` status `ready` deltaP `-3.2246` edge `-0.0033` maxDD `-1.4631`
- `market_context_high->commodity_1h` score `-0.7341` n `148` status `ready` deltaP `-1.1207` edge `0.0047` maxDD `-1.0053`
- `market_context_high->equity_24h` score `-1.2726` n `135` status `ready` deltaP `8.0671` edge `0.1366` maxDD `-15.7143`
- `market_context_high->equity_1h` score `-1.5223` n `148` status `ready` deltaP `0.1456` edge `-0.0049` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6228` n `148` status `ready` deltaP `2.6096` edge `0.0109` maxDD `-12.2409`
- `market_context_high->metal_24h` score `-1.8242` n `135` status `ready` deltaP `9.3287` edge `0.0636` maxDD `-8.2244`
- `market_context_high->index_4h` score `-3.0254` n `148` status `ready` deltaP `-8.7797` edge `-0.0314` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.2143` n `135` status `ready` deltaP `0.544` edge `0.07` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.5666` n `148` status `ready` deltaP `2.9664` edge `-0.0451` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.6554` n `148` status `ready` deltaP `-4.2271` edge `-0.1735` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
