# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T01:52:28.284437+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8775`

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

- `market_context_high->unknown_24h` score `889.1134` n `135` status `ready` deltaP `-3.7616` edge `74.2106` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `47.4718` n `148` status `ready` deltaP `5.0882` edge `3.9373` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9315` n `135` status `ready` deltaP `27.1875` edge `0.0485` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3026` n `148` status `ready` deltaP `8.7797` edge `0.0025` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.087` n `148` status `ready` deltaP `8.7591` edge `0.0087` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.148` n `148` status `ready` deltaP `7.4243` edge `0.0062` maxDD `-1.3073`
- `market_context_high->commodity_4h` score `-0.2105` n `148` status `ready` deltaP `8.001` edge `0.051` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.3712` n `135` status `ready` deltaP `12.9514` edge `0.0233` maxDD `-1.2451`
- `market_context_high->crypto_major_1h` score `-0.4515` n `148` status `ready` deltaP `6.603` edge `0.0264` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.5603` n `148` status `ready` deltaP `0.3763` edge `0.0092` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7315` n `148` status `ready` deltaP `-3.0749` edge `-0.005` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8489` n `148` status `ready` deltaP `7.7332` edge `-0.0063` maxDD `-4.6603`
- `market_context_high->equity_24h` score `-1.1682` n `135` status `ready` deltaP `8.0671` edge `0.1453` maxDD `-15.7143`
- `market_context_high->equity_1h` score `-1.5629` n `148` status `ready` deltaP `0.5947` edge `-0.0131` maxDD `-9.2993`
- `market_context_high->metal_24h` score `-1.6616` n `135` status `ready` deltaP `10.3704` edge `0.0702` maxDD `-8.2244`
- `market_context_high->crypto_alt_1h` score `-1.7756` n `148` status `ready` deltaP `1.7114` edge `-0.0027` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.0564` n `148` status `ready` deltaP `-8.6273` edge `-0.035` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.5427` n `135` status `ready` deltaP `0.544` edge `0.0279` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.7458` n `148` status `ready` deltaP `3.2713` edge `-0.0701` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.7932` n `148` status `ready` deltaP `-3.9222` edge `-0.1932` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
