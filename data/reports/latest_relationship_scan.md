# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T10:52:29.753019+00:00`
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

- `market_context_high->unknown_24h` score `1455.3778` n `135` status `ready` deltaP `-3.7616` edge `121.3993` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `33.6774` n `148` status `ready` deltaP `4.7833` edge `2.7898` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.7803` n `135` status `ready` deltaP `27.1875` edge `0.0359` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.281` n `148` status `ready` deltaP `8.4803` edge `0.0027` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.1103` n `148` status `ready` deltaP `9.2164` edge `0.0076` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1036` n `148` status `ready` deltaP `8.0231` edge `0.0079` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3953` n `148` status `ready` deltaP `6.7527` edge `0.0326` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.4182` n `148` status `ready` deltaP `6.9339` edge `0.0408` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.4421` n `135` status `ready` deltaP `12.0833` edge `0.02` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.6564` n `148` status `ready` deltaP `10.3247` edge `0.0011` maxDD `-4.6603`
- `market_context_high->commodity_1h` score `-0.6765` n `148` status `ready` deltaP `-0.6716` edge `0.0065` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7603` n `148` status `ready` deltaP `-3.8234` edge `-0.0037` maxDD `-1.4631`
- `market_context_high->equity_1h` score `-1.5675` n `148` status `ready` deltaP `-0.3035` edge `-0.0077` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6415` n `148` status `ready` deltaP `2.4599` edge `0.0095` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-2.1066` n `135` status `ready` deltaP `8.0671` edge `0.0671` maxDD `-15.7143`
- `market_context_high->metal_24h` score `-2.2854` n `135` status `ready` deltaP `6.2037` edge `0.046` maxDD `-8.2244`
- `market_context_high->index_4h` score `-3.0452` n `148` status `ready` deltaP `-9.237` edge `-0.03` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.2704` n `135` status `ready` deltaP `0.544` edge `0.0628` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.5068` n `148` status `ready` deltaP `3.5761` edge `-0.0415` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.5761` n `148` status `ready` deltaP `-4.532` edge `-0.1613` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
