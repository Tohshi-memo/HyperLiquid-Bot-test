# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T11:22:29.068049+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8465`

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

- `market_context_high->unknown_24h` score `1479.475` n `135` status `ready` deltaP `-3.7616` edge `123.4074` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `30.609` n `148` status `ready` deltaP `4.7833` edge `2.5341` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.7719` n `135` status `ready` deltaP `27.1875` edge `0.0352` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2919` n `149` status `ready` deltaP `8.6163` edge `0.0027` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0847` n `148` status `ready` deltaP `8.9115` edge `0.0075` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0785` n `149` status `ready` deltaP `8.4767` edge `0.0081` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.4014` n `149` status `ready` deltaP `6.6803` edge `0.0323` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.4182` n `148` status `ready` deltaP `6.9339` edge `0.0408` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.4542` n `135` status `ready` deltaP `11.9097` edge `0.0196` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.6485` n `148` status `ready` deltaP `10.4771` edge `0.0011` maxDD `-4.6603`
- `market_context_high->commodity_1h` score `-0.6728` n `149` status `ready` deltaP `-0.64` edge `0.0066` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7398` n `149` status `ready` deltaP `-3.4743` edge `-0.0034` maxDD `-1.4631`
- `market_context_high->equity_1h` score `-1.541` n `149` status `ready` deltaP `0.0412` edge `-0.0066` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6391` n `149` status `ready` deltaP `2.4464` edge `0.0099` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.1774` n `135` status `ready` deltaP `8.0671` edge `0.0612` maxDD `-15.7143`
- `market_context_high->metal_24h` score `-2.3287` n `135` status `ready` deltaP `5.8565` edge `0.0447` maxDD `-8.2244`
- `market_context_high->index_4h` score `-3.0392` n `148` status `ready` deltaP `-9.237` edge `-0.0295` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.2821` n `135` status `ready` deltaP `0.544` edge `0.0613` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.5115` n `148` status `ready` deltaP `3.5761` edge `-0.0421` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.5473` n `148` status `ready` deltaP `-4.532` edge `-0.1576` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
