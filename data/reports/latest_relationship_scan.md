# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T10:07:30.297105+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8411`

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

- `market_context_high->unknown_24h` score `1410.3718` n `135` status `ready` deltaP `-3.7616` edge `117.6488` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `38.5642` n `148` status `ready` deltaP `5.0882` edge `3.195` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.7971` n `135` status `ready` deltaP `27.1875` edge `0.0373` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.281` n `148` status `ready` deltaP `8.4803` edge `0.0027` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.1493` n `148` status `ready` deltaP `9.6737` edge `0.0078` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1145` n `148` status `ready` deltaP `7.8734` edge `0.0075` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.4` n `148` status `ready` deltaP `6.7527` edge `0.032` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.434` n `148` status `ready` deltaP `6.7814` edge `0.0405` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.4397` n `135` status `ready` deltaP `12.0833` edge `0.0203` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.6609` n `148` status `ready` deltaP `-0.5219` edge `0.0068` maxDD `-1.0053`
- `market_context_high->metal_4h` score `-0.673` n `148` status `ready` deltaP `10.0198` edge `0.001` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.7518` n `148` status `ready` deltaP `-3.6737` edge `-0.0036` maxDD `-1.4631`
- `market_context_high->equity_1h` score `-1.548` n `148` status `ready` deltaP `-0.1538` edge `-0.0062` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6547` n `148` status `ready` deltaP `2.3102` edge `0.0088` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-1.9842` n `135` status `ready` deltaP `8.0671` edge `0.0773` maxDD `-15.7143`
- `market_context_high->metal_24h` score `-2.2149` n `135` status `ready` deltaP `6.7245` edge `0.0484` maxDD `-8.2244`
- `market_context_high->index_4h` score `-3.0524` n `148` status `ready` deltaP `-9.237` edge `-0.0306` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.2463` n `135` status `ready` deltaP `0.544` edge `0.0659` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.5061` n `148` status `ready` deltaP `3.5761` edge `-0.0414` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.6136` n `148` status `ready` deltaP `-4.532` edge `-0.1661` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
