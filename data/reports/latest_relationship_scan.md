# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T13:07:34.321563+00:00`
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

- `market_context_high->unknown_24h` score `1499.8918` n `135` status `ready` deltaP `-3.7616` edge `125.1088` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `24.6076` n `148` status `ready` deltaP `4.6308` edge `2.035` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.6563` n `135` status `ready` deltaP `26.493` edge `0.0302` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2656` n `149` status `ready` deltaP `8.3169` edge `0.0025` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0142` n `148` status `ready` deltaP `8.1493` edge `0.0067` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0832` n `149` status `ready` deltaP `8.4767` edge `0.0075` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.283` n `149` status `ready` deltaP `7.7282` edge `0.0405` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.4061` n `148` status `ready` deltaP `7.0863` edge `0.0408` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.5012` n `135` status `ready` deltaP `11.2153` edge `0.0182` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.6801` n `148` status `ready` deltaP `10.0198` edge `0.0001` maxDD `-4.6603`
- `market_context_high->commodity_1h` score `-0.686` n `149` status `ready` deltaP `-0.7897` edge `0.0065` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.718` n `149` status `ready` deltaP `-3.1749` edge `-0.0026` maxDD `-1.4631`
- `market_context_high->equity_1h` score `-1.414` n `149` status `ready` deltaP `1.0891` edge `0.0027` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.5323` n `149` status `ready` deltaP `3.1949` edge `0.0186` maxDD `-12.2409`
- `market_context_high->metal_24h` score `-2.4968` n `135` status `ready` deltaP `4.6412` edge `0.0388` maxDD `-8.2244`
- `market_context_high->equity_24h` score `-2.5958` n `135` status `ready` deltaP `7.5463` edge `0.0298` maxDD `-15.7143`
- `market_context_high->index_4h` score `-3.032` n `148` status `ready` deltaP `-9.237` edge `-0.0289` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.318` n `135` status `ready` deltaP `0.544` edge `0.0567` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.4559` n `148` status `ready` deltaP `3.881` edge `-0.037` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.421` n `148` status `ready` deltaP `-3.7698` edge `-0.1465` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
