# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T22:26:09.831349+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8697`

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

- `market_context_high->unknown_4h` score `49.3618` n `148` status `ready` deltaP `5.0882` edge `4.0948` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9519` n `135` status `ready` deltaP `27.1875` edge `0.0502` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3685` n `148` status `ready` deltaP `9.5282` edge `0.003` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0638` n `148` status `ready` deltaP `8.4542` edge `0.0088` maxDD `-0.4545`
- `market_context_high->commodity_4h` score `-0.0709` n `148` status `ready` deltaP `9.2205` edge `0.0545` maxDD `-1.0837`
- `market_context_high->metal_1h` score `-0.1379` n `148` status `ready` deltaP `7.574` edge `0.0065` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.4102` n `148` status `ready` deltaP `7.0521` edge `0.0287` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.4579` n `135` status `ready` deltaP `11.3889` edge `0.0226` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.5723` n `148` status `ready` deltaP `0.2266` edge `0.0092` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6584` n `148` status `ready` deltaP `-1.8773` edge `-0.0036` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7794` n `148` status `ready` deltaP `8.8003` edge `-0.0045` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-1.3424` n `135` status `ready` deltaP `12.8009` edge `0.0806` maxDD `-8.2244`
- `market_context_high->equity_24h` score `-1.4394` n `135` status `ready` deltaP `8.0671` edge `0.1227` maxDD `-15.7143`
- `market_context_high->equity_1h` score `-1.4492` n `148` status `ready` deltaP `1.6426` edge `-0.0055` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.714` n `148` status `ready` deltaP `2.3102` edge `0.0012` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.9653` n `148` status `ready` deltaP `-7.7126` edge `-0.0335` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.7579` n `135` status `ready` deltaP `0.544` edge `0.0003` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.7641` n `148` status `ready` deltaP `3.7286` edge `-0.0755` maxDD `-27.2215`
- `market_context_high->unknown_1h` score `-4.5786` n `148` status `ready` deltaP `0.2509` edge `-0.3343` maxDD `-1.5807`
- `market_context_high->equity_4h` score `-5.6779` n `148` status `ready` deltaP `-3.16` edge `-0.1835` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
