# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T07:52:21.514098+00:00`
- Price records: `672`
- Market context records: `1199`
- Flow alert records: `5359`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `18.5513` n `134` status `ready` deltaP `44.2553` edge `1.3641` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `7.4626` n `134` status `ready` deltaP `22.0668` edge `0.6764` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `5.6623` n `134` status `ready` deltaP `4.0362` edge `0.5666` maxDD `-6.7322`
- `market_context_high->metal_24h` score `4.2272` n `134` status `ready` deltaP `-4.2625` edge `0.5474` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `3.3007` n `134` status `ready` deltaP `-3.3556` edge `0.5854` maxDD `-18.0378`
- `market_context_high->equity_4h` score `2.8019` n `134` status `ready` deltaP `14.5682` edge `0.2027` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.0523` n `134` status `ready` deltaP `16.8091` edge `0.1676` maxDD `-5.3574`
- `market_context_high->equity_24h` score `1.6006` n `134` status `ready` deltaP `17.0528` edge `0.3242` maxDD `-14.2815`
- `market_context_high->index_4h` score `0.9374` n `134` status `ready` deltaP `10.4273` edge `0.0769` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4652` n `134` status `ready` deltaP `8.1687` edge `0.016` maxDD `-0.5353`
- `market_context_high->fx_24h` score `0.4472` n `134` status `ready` deltaP `8.8438` edge `0.0542` maxDD `-2.7379`
- `market_context_high->equity_1h` score `0.3563` n `134` status `ready` deltaP `3.8341` edge `0.0419` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `-0.0971` n `134` status `ready` deltaP `6.4593` edge `0.1366` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.125` n `134` status `ready` deltaP `5.2127` edge `0.0004` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.2094` n `134` status `ready` deltaP `8.3386` edge `-0.012` maxDD `-2.2164`
- `market_context_high->crypto_major_1h` score `-0.3403` n `134` status `ready` deltaP `3.5772` edge `0.0091` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.373` n `134` status `ready` deltaP `0.7284` edge `0.0316` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.8484` n `134` status `ready` deltaP `-2.9873` edge `0.0107` maxDD `-2.252`
- `market_context_high->metal_4h` score `-0.9579` n `134` status `ready` deltaP `8.4592` edge `-0.0361` maxDD `-6.4478`
- `market_context_high->crypto_alt_4h` score `-1.0516` n `134` status `ready` deltaP `5.3217` edge `0.1262` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
