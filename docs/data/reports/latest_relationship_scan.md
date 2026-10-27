# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T21:37:32.155286+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8673`

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

- `market_context_high->unknown_4h` score `53.6604` n `146` status `ready` deltaP `5.1203` edge `4.4528` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9579` n `135` status `ready` deltaP `27.1875` edge `0.0507` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4056` n `148` status `ready` deltaP `9.9773` edge `0.0031` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.1415` n `146` status `ready` deltaP `9.3656` edge `0.0092` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1286` n `148` status `ready` deltaP `7.7237` edge `0.0067` maxDD `-1.3073`
- `market_context_high->commodity_4h` score `-0.1386` n `146` status `ready` deltaP `8.6744` edge `0.0525` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.3728` n `148` status `ready` deltaP `7.5012` edge `0.0305` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.4595` n `135` status `ready` deltaP `11.3889` edge `0.0224` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.6154` n `148` status `ready` deltaP `-0.2225` edge `0.0086` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6498` n `148` status `ready` deltaP `-1.7276` edge `-0.0035` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7932` n `146` status `ready` deltaP `8.6097` edge `-0.005` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-1.2731` n `135` status `ready` deltaP `13.3218` edge `0.0829` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.4258` n `148` status `ready` deltaP `1.942` edge `-0.0045` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.503` n `135` status `ready` deltaP `8.0671` edge `0.1174` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.6844` n `148` status `ready` deltaP `2.6096` edge `0.003` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.9879` n `146` status `ready` deltaP `-7.9957` edge `-0.0335` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.7657` n `135` status `ready` deltaP `0.544` edge `-0.0007` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.7815` n `146` status `ready` deltaP `3.575` edge `-0.0767` maxDD `-27.2215`
- `market_context_high->unknown_1h` score `-4.533` n `148` status `ready` deltaP `0.2509` edge `-0.3305` maxDD `-1.5807`
- `market_context_high->equity_4h` score `-5.627` n `146` status `ready` deltaP `-2.3597` edge `-0.1823` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
