# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T19:52:30.679156+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8772`

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

- `market_context_high->unknown_4h` score `70.5075` n `139` status `ready` deltaP `4.8243` edge `5.8587` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9699` n `135` status `ready` deltaP `27.1875` edge `0.0517` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3804` n `148` status `ready` deltaP `9.6779` edge `0.003` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.3408` n `139` status `ready` deltaP `11.7367` edge `0.01` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1029` n `148` status `ready` deltaP `8.1728` edge `0.007` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3486` n `148` status `ready` deltaP `7.6509` edge `0.0326` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.3614` n `139` status `ready` deltaP `6.6394` edge `0.0475` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.4814` n `135` status `ready` deltaP `11.0417` edge `0.0219` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.5842` n `148` status `ready` deltaP `0.0769` edge `0.0092` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6677` n `148` status `ready` deltaP `-2.027` edge `-0.0038` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8788` n `139` status `ready` deltaP `7.2623` edge `-0.007` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-1.1255` n `135` status `ready` deltaP `14.537` edge `0.0871` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.4616` n `148` status `ready` deltaP `1.4929` edge `-0.0061` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.6434` n `135` status `ready` deltaP `8.0671` edge `0.1057` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.6797` n `148` status `ready` deltaP `2.4599` edge `0.0046` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.9565` n `139` status `ready` deltaP `-7.5726` edge `-0.0337` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.765` n `135` status `ready` deltaP `0.544` edge `-0.0006` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.7963` n `139` status `ready` deltaP `3.4995` edge `-0.0781` maxDD `-27.2215`
- `market_context_high->unknown_1h` score `-4.5727` n `148` status `ready` deltaP `0.5503` edge `-0.3358` maxDD `-1.5807`
- `market_context_high->equity_4h` score `-5.4624` n `139` status `ready` deltaP `0.0548` edge `-0.1773` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
