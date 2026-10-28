# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T13:52:29.124723+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8297`

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

- `market_context_high->unknown_24h` score `1506.6178` n `135` status `ready` deltaP `-3.7616` edge `125.6693` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `24.5331` n `148` status `ready` deltaP `4.4784` edge `2.0298` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.5823` n `135` status `ready` deltaP `25.9722` edge `0.0275` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2392` n `149` status `ready` deltaP `8.0175` edge `0.0023` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0106` n `148` status `ready` deltaP `8.1493` edge `0.0064` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0832` n `149` status `ready` deltaP `8.4767` edge `0.0075` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.2791` n `149` status `ready` deltaP `7.7282` edge `0.041` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.4109` n `148` status `ready` deltaP `7.0863` edge `0.0404` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.5346` n `135` status `ready` deltaP `10.6945` edge `0.0174` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.6927` n `148` status `ready` deltaP `9.8673` edge `-0.0005` maxDD `-4.6603`
- `market_context_high->commodity_1h` score `-0.7003` n `149` status `ready` deltaP `-0.9394` edge `0.0063` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7196` n `149` status `ready` deltaP `-3.1749` edge `-0.0028` maxDD `-1.4631`
- `market_context_high->equity_1h` score `-1.3922` n `149` status `ready` deltaP `1.2388` edge `0.0045` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5447` n `149` status `ready` deltaP `3.0452` edge `0.018` maxDD `-12.2409`
- `market_context_high->metal_24h` score `-2.5648` n `135` status `ready` deltaP `4.1204` edge `0.0366` maxDD `-8.2244`
- `market_context_high->equity_24h` score `-2.8055` n `135` status `ready` deltaP `7.0255` edge `0.0158` maxDD `-15.7143`
- `market_context_high->index_4h` score `-3.0186` n `148` status `ready` deltaP `-9.0846` edge `-0.0288` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.3141` n `135` status `ready` deltaP `0.544` edge `0.0572` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.409` n `148` status `ready` deltaP `4.0334` edge `-0.032` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.3676` n `148` status `ready` deltaP `-3.3125` edge `-0.1427` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
