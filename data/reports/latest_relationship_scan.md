# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T17:37:28.303576+00:00`
- Price records: `672`
- Market context records: `7052`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11502`

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

- `market_context_high->fx_4h` score `0.4785` n `196` status `ready` deltaP `14.8768` edge `0.0107` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.323` n `196` status `ready` deltaP `2.4899` edge `0.0016` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.6313` n `196` status `ready` deltaP `0.7546` edge `0.0288` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.8144` n `196` status `ready` deltaP `-1.3932` edge `-0.004` maxDD `-2.2895`
- `market_context_high->commodity_1h` score `-0.8167` n `196` status `ready` deltaP `-3.9258` edge `-0.0169` maxDD `-1.9306`
- `market_context_high->metal_1h` score `-0.8182` n `196` status `ready` deltaP `-3.9167` edge `-0.002` maxDD `-2.1427`
- `market_context_high->unknown_1h` score `-0.8869` n `196` status `ready` deltaP `-2.496` edge `0.0156` maxDD `-2.1627`
- `market_context_high->crypto_major_1h` score `-0.9853` n `196` status `ready` deltaP `3.3942` edge `0.0305` maxDD `-7.1523`
- `market_context_high->unknown_4h` score `-1.292` n `196` status `ready` deltaP `-5.6558` edge `0.1031` maxDD `-5.5117`
- `market_context_high->equity_1h` score `-2.0003` n `196` status `ready` deltaP `2.7496` edge `-0.0325` maxDD `-14.716`
- `market_context_high->metal_4h` score `-2.1237` n `196` status `ready` deltaP `3.503` edge `0.0027` maxDD `-5.5324`
- `market_context_high->index_4h` score `-2.2096` n `196` status `ready` deltaP `2.3737` edge `-0.0292` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.2591` n `196` status `ready` deltaP `-0.8823` edge `-0.0515` maxDD `-4.4704`
- `market_context_high->commodity_4h` score `-2.3275` n `196` status `ready` deltaP `-5.7336` edge `-0.0397` maxDD `-2.9494`
- `market_context_high->crypto_alt_4h` score `-2.6404` n `196` status `ready` deltaP `2.6443` edge `0.0224` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-2.8428` n `196` status `ready` deltaP `4.3336` edge `0.0351` maxDD `-24.6094`
- `market_context_high->unknown_24h` score `-3.176` n `196` status `ready` deltaP `-12.5851` edge `0.1914` maxDD `-23.5076`
- `market_context_high->fx_24h` score `-3.511` n `196` status `ready` deltaP `-0.0106` edge `-0.0098` maxDD `-3.9503`
- `market_context_high->equity_4h` score `-7.7794` n `196` status `ready` deltaP `3.3412` edge `-0.1326` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.0485` n `196` status `ready` deltaP `-17.1273` edge `-0.0805` maxDD `-44.4154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
