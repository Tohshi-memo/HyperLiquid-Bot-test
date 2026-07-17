# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T22:22:25.312348+00:00`
- Price records: `672`
- Market context records: `7074`
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

- `market_context_high->fx_4h` score `0.727` n `177` status `ready` deltaP `17.6975` edge `0.0126` maxDD `-0.9333`
- `market_context_high->unknown_1h` score `-0.0703` n `177` status `ready` deltaP `1.0648` edge `0.0429` maxDD `-1.4688`
- `market_context_high->fx_1h` score `-0.1221` n `177` status `ready` deltaP `4.8361` edge `0.0027` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.3757` n `177` status `ready` deltaP `1.1951` edge `0.0303` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.5997` n `177` status `ready` deltaP `-0.3595` edge `-0.0042` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.623` n `177` status `ready` deltaP `3.3391` edge `0.0331` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.855` n `177` status `ready` deltaP `-4.2567` edge `-0.0196` maxDD `-1.9306`
- `market_context_high->unknown_4h` score `-0.9859` n `177` status `ready` deltaP `-5.673` edge `0.1191` maxDD `-4.742`
- `market_context_high->metal_1h` score `-1.3735` n `177` status `ready` deltaP `-5.111` edge `-0.0036` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.6962` n `177` status `ready` deltaP `-8.2541` edge `-0.0464` maxDD `-2.9494`
- `market_context_high->equity_1h` score `-1.8993` n `177` status `ready` deltaP `4.2423` edge `-0.0295` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.226` n `177` status `ready` deltaP `2.8378` edge `-0.0344` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.4707` n `177` status `ready` deltaP `-2.8219` edge `-0.0562` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-3.0183` n `177` status `ready` deltaP `-0.3186` edge `-0.0063` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-3.1299` n `177` status `ready` deltaP `2.0222` edge `0.0137` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.6986` n `177` status `ready` deltaP `-1.8008` edge `-0.0135` maxDD `-3.9503`
- `market_context_high->metal_4h` score `-3.7102` n `177` status `ready` deltaP `-0.9388` edge `-0.0046` maxDD `-5.5324`
- `market_context_high->unknown_24h` score `-4.5959` n `177` status `ready` deltaP `-17.42` edge `0.0416` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-7.9671` n `177` status `ready` deltaP `3.7076` edge `-0.1591` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.6008` n `177` status `ready` deltaP `-22.2134` edge `-0.1064` maxDD `-44.3131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
