# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T09:07:25.708129+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8795`

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

- `market_context_high->unknown_24h` score `1350.5182` n `135` status `ready` deltaP `-3.7616` edge `112.661` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `41.8032` n `148` status `ready` deltaP `5.2406` edge `3.4639` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.8199` n `135` status `ready` deltaP `27.1875` edge `0.0392` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.293` n `148` status `ready` deltaP `8.63` edge `0.0027` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.1505` n `148` status `ready` deltaP `9.6737` edge `0.0079` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0974` n `148` status `ready` deltaP `8.1728` edge `0.0077` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3704` n `148` status `ready` deltaP `7.0521` edge `0.0338` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.435` n `135` status `ready` deltaP `12.0833` edge `0.0209` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.4948` n `148` status `ready` deltaP `6.1717` edge `0.0395` maxDD `-1.0837`
- `market_context_high->metal_4h` score `-0.6723` n `148` status `ready` deltaP `10.0198` edge `0.0011` maxDD `-4.6603`
- `market_context_high->commodity_1h` score `-0.6933` n `148` status `ready` deltaP `-0.8213` edge `0.0061` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7432` n `148` status `ready` deltaP `-3.524` edge `-0.0035` maxDD `-1.4631`
- `market_context_high->equity_1h` score `-1.555` n `148` status `ready` deltaP `-0.3035` edge `-0.0061` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.615` n `148` status `ready` deltaP `2.6096` edge `0.0119` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-1.8342` n `135` status `ready` deltaP `8.0671` edge `0.0898` maxDD `-15.7143`
- `market_context_high->metal_24h` score `-2.1125` n `135` status `ready` deltaP `7.419` edge `0.0523` maxDD `-8.2244`
- `market_context_high->index_4h` score `-3.0876` n `148` status `ready` deltaP `-9.5419` edge `-0.0315` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.208` n `135` status `ready` deltaP `0.544` edge `0.0708` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.5092` n `148` status `ready` deltaP `3.5761` edge `-0.0418` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.691` n `148` status `ready` deltaP `-4.8368` edge `-0.174` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
