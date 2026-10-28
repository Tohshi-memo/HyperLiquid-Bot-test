# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T13:22:29.322149+00:00`
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

- `market_context_high->unknown_24h` score `1502.1094` n `135` status `ready` deltaP `-3.7616` edge `125.2936` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `24.5727` n `148` status `ready` deltaP `4.4784` edge `2.0331` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.6317` n `135` status `ready` deltaP `26.3194` edge `0.0293` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2656` n `149` status `ready` deltaP `8.3169` edge `0.0025` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.013` n `148` status `ready` deltaP `8.1493` edge `0.0066` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0832` n `149` status `ready` deltaP `8.4767` edge `0.0075` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.2697` n `149` status `ready` deltaP `7.8779` edge `0.0412` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.4073` n `148` status `ready` deltaP `7.0863` edge `0.0407` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.5118` n `135` status `ready` deltaP `11.0417` edge `0.018` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.6808` n `148` status `ready` deltaP `10.0198` edge `0.0` maxDD `-4.6603`
- `market_context_high->commodity_1h` score `-0.6991` n `149` status `ready` deltaP `-0.9394` edge `0.0064` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7102` n `149` status `ready` deltaP `-3.0252` edge `-0.0026` maxDD `-1.4631`
- `market_context_high->equity_1h` score `-1.4` n `149` status `ready` deltaP `1.2388` edge `0.0035` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5307` n `149` status `ready` deltaP `3.1949` edge `0.0188` maxDD `-12.2409`
- `market_context_high->metal_24h` score `-2.5203` n `135` status `ready` deltaP `4.4676` edge `0.038` maxDD `-8.2244`
- `market_context_high->equity_24h` score `-2.6685` n `135` status `ready` deltaP `7.3727` edge `0.0249` maxDD `-15.7143`
- `market_context_high->index_4h` score `-3.0308` n `148` status `ready` deltaP `-9.237` edge `-0.0288` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.3157` n `135` status `ready` deltaP `0.544` edge `0.057` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.4324` n `148` status `ready` deltaP `4.0334` edge `-0.035` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.4006` n `148` status `ready` deltaP `-3.6173` edge `-0.1449` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
