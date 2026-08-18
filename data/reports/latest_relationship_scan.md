# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T11:07:28.898816+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11633`

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

- `market_context_high->crypto_major_24h` score `2.2083` n `84` status `ready` deltaP `7.8918` edge `0.2522` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.5219` n `84` status `ready` deltaP `16.6254` edge `0.2676` maxDD `-4.666`
- `market_context_high->equity_1h` score `1.0437` n `96` status `ready` deltaP `9.3127` edge `0.0553` maxDD `-0.4329`
- `market_context_high->metal_4h` score `0.8051` n `96` status `ready` deltaP `15.0406` edge `0.0244` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.7812` n `96` status `ready` deltaP `9.629` edge `0.103` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.6611` n `96` status `ready` deltaP `12.9179` edge `0.0077` maxDD `-0.0982`
- `market_context_high->crypto_alt_4h` score `0.6335` n `96` status `ready` deltaP `11.128` edge `0.1056` maxDD `-5.4926`
- `market_context_high->unknown_1h` score `0.5903` n `96` status `ready` deltaP `9.8054` edge `0.0065` maxDD `-0.4807`
- `market_context_high->unknown_24h` score `-0.0019` n `84` status `ready` deltaP `14.3105` edge `-0.0778` maxDD `-0.0875`
- `market_context_high->metal_1h` score `-0.0405` n `96` status `ready` deltaP `4.0232` edge `0.0085` maxDD `-0.4291`
- `market_context_high->equity_4h` score `-0.0887` n `96` status `ready` deltaP `1.8546` edge `0.0707` maxDD `-2.5696`
- `market_context_high->fx_4h` score `-0.2416` n `96` status `ready` deltaP `2.9217` edge `-0.0002` maxDD `-0.3539`
- `market_context_high->crypto_alt_1h` score `-0.341` n `96` status `ready` deltaP `2.5262` edge `0.0196` maxDD `-2.413`
- `market_context_high->commodity_4h` score `-0.3662` n `96` status `ready` deltaP `4.2429` edge `0.0098` maxDD `-2.4692`
- `market_context_high->fx_1h` score `-0.4545` n `96` status `ready` deltaP `-3.5679` edge `0.0014` maxDD `-0.2043`
- `market_context_high->crypto_major_1h` score `-0.4647` n `96` status `ready` deltaP `1.4845` edge `0.015` maxDD `-2.7581`
- `market_context_high->index_4h` score `-0.5835` n `96` status `ready` deltaP `0.94` edge `0.0106` maxDD `-0.5728`
- `market_context_high->commodity_1h` score `-0.8464` n `96` status `ready` deltaP `-6.9923` edge `-0.0053` maxDD `-1.1941`
- `market_context_high->metal_24h` score `-1.9756` n `84` status `ready` deltaP `-6.9819` edge `0.0179` maxDD `-6.9709`
- `market_context_high->index_24h` score `-4.4197` n `84` status `ready` deltaP `-14.8263` edge `-0.1795` maxDD `-12.0629`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
