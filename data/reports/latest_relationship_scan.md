# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T18:52:27.750804+00:00`
- Price records: `672`
- Market context records: `7058`
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

- `market_context_high->fx_4h` score `0.5462` n `191` status `ready` deltaP `15.6772` edge `0.011` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.2308` n `191` status `ready` deltaP `3.5528` edge `0.0022` maxDD `-0.276`
- `market_context_high->crypto_alt_1h` score `-0.3263` n `191` status `ready` deltaP `1.8309` edge `0.0324` maxDD `-4.5815`
- `market_context_high->crypto_major_1h` score `-0.5762` n `191` status `ready` deltaP `4.1501` edge `0.0337` maxDD `-7.1523`
- `market_context_high->unknown_1h` score `-0.7186` n `191` status `ready` deltaP `-1.6067` edge `0.0209` maxDD `-1.939`
- `market_context_high->metal_1h` score `-0.7601` n `191` status `ready` deltaP `-2.8749` edge `-0.0015` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.8129` n `191` status `ready` deltaP `-1.3795` edge `-0.0039` maxDD `-2.2895`
- `market_context_high->commodity_1h` score `-0.8705` n `191` status `ready` deltaP `-4.7512` edge `-0.0183` maxDD `-1.9306`
- `market_context_high->unknown_4h` score `-1.0458` n `191` status `ready` deltaP `-5.5365` edge `0.1132` maxDD `-4.742`
- `market_context_high->equity_1h` score `-1.9622` n `191` status `ready` deltaP `3.1076` edge `-0.03` maxDD `-14.716`
- `market_context_high->metal_4h` score `-2.2348` n `191` status `ready` deltaP `1.8468` edge `-0.0005` maxDD `-5.5324`
- `market_context_high->index_4h` score `-2.2858` n `191` status `ready` deltaP `1.3424` edge `-0.0321` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-2.3707` n `191` status `ready` deltaP `-1.7371` edge `-0.0551` maxDD `-4.4704`
- `market_context_high->commodity_4h` score `-2.4687` n `191` status `ready` deltaP `-6.9891` edge `-0.0431` maxDD `-2.9494`
- `market_context_high->crypto_alt_4h` score `-2.7159` n `191` status `ready` deltaP `2.0911` edge `0.0164` maxDD `-22.2831`
- `market_context_high->crypto_major_4h` score `-2.8855` n `191` status `ready` deltaP `4.2316` edge `0.0303` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.4831` n `191` status `ready` deltaP `0.4436` edge `-0.0105` maxDD `-3.9503`
- `market_context_high->unknown_24h` score `-3.5177` n `191` status `ready` deltaP `-13.9207` edge `0.1565` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-7.8558` n `191` status `ready` deltaP `3.8077` edge `-0.1455` maxDD `-63.963`
- `market_context_high->metal_24h` score `-15.2491` n `191` status `ready` deltaP `-18.69` edge `-0.0868` maxDD `-44.4154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
