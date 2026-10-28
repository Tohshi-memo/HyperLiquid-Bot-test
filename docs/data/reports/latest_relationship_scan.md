# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T09:52:28.109047+00:00`
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

- `market_context_high->unknown_24h` score `1395.3718` n `135` status `ready` deltaP `-3.7616` edge `116.3988` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `39.5458` n `148` status `ready` deltaP `5.0882` edge `3.2768` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.8019` n `135` status `ready` deltaP `27.1875` edge `0.0377` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.293` n `148` status `ready` deltaP `8.63` edge `0.0027` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.1627` n `148` status `ready` deltaP `9.8261` edge `0.0079` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1145` n `148` status `ready` deltaP `7.8734` edge `0.0075` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3984` n `148` status `ready` deltaP `6.7527` edge `0.0322` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-0.4389` n `135` status `ready` deltaP `12.0833` edge `0.0204` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.4474` n `148` status `ready` deltaP `6.629` edge `0.0404` maxDD `-1.0837`
- `market_context_high->commodity_1h` score `-0.6621` n `148` status `ready` deltaP `-0.5219` edge `0.0067` maxDD `-1.0053`
- `market_context_high->metal_4h` score `-0.6738` n `148` status `ready` deltaP `10.0198` edge `0.0009` maxDD `-4.6603`
- `market_context_high->index_1h` score `-0.7518` n `148` status `ready` deltaP `-3.6737` edge `-0.0036` maxDD `-1.4631`
- `market_context_high->equity_1h` score `-1.5574` n `148` status `ready` deltaP `-0.3035` edge `-0.0064` maxDD `-9.2993`
- `market_context_high->crypto_alt_1h` score `-1.6516` n `148` status `ready` deltaP `2.3102` edge `0.0092` maxDD `-12.2409`
- `market_context_high->equity_24h` score `-1.9518` n `135` status `ready` deltaP `8.0671` edge `0.08` maxDD `-15.7143`
- `market_context_high->metal_24h` score `-2.1914` n `135` status `ready` deltaP `6.8981` edge `0.0492` maxDD `-8.2244`
- `market_context_high->index_4h` score `-3.0682` n `148` status `ready` deltaP `-9.3895` edge `-0.0309` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.2361` n `135` status `ready` deltaP `0.544` edge `0.0672` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.5084` n `148` status `ready` deltaP `3.5761` edge `-0.0417` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.6418` n `148` status `ready` deltaP `-4.6844` edge `-0.1687` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
