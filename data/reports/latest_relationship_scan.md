# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T23:52:27.064602+00:00`
- Price records: `672`
- Market context records: `7614`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14551`

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

- `market_context_high->equity_24h` score `0.9993` n `145` status `ready` deltaP `16.9771` edge `0.5055` maxDD `-34.5784`
- `market_context_high->unknown_24h` score `0.7305` n `146` status `ready` deltaP `11.8793` edge `0.0997` maxDD `-4.775`
- `market_context_high->commodity_24h` score `0.2619` n `145` status `ready` deltaP `14.9814` edge `0.0803` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.1156` n `146` status `ready` deltaP `7.5631` edge `0.0123` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1354` n `146` status `ready` deltaP `8.1556` edge `0.0243` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.1796` n `146` status `ready` deltaP `2.6536` edge `0.0225` maxDD `-2.7243`
- `market_context_high->commodity_4h` score `-0.2457` n `146` status `ready` deltaP `5.735` edge `0.0158` maxDD `-2.2943`
- `market_context_high->commodity_1h` score `-0.2476` n `146` status `ready` deltaP `3.9306` edge `-0.0009` maxDD `-1.5641`
- `market_context_high->fx_24h` score `-0.3419` n `145` status `ready` deltaP `9.2803` edge `0.0184` maxDD `-3.0343`
- `market_context_high->equity_1h` score `-0.4026` n `146` status `ready` deltaP `6.5779` edge `0.0559` maxDD `-7.7764`
- `market_context_high->index_4h` score `-0.5622` n `146` status `ready` deltaP `10.1336` edge `0.0305` maxDD `-3.2774`
- `market_context_high->metal_1h` score `-0.5944` n `146` status `ready` deltaP `1.9871` edge `0.0151` maxDD `-1.0307`
- `market_context_high->fx_1h` score `-0.6786` n `146` status `ready` deltaP `-0.722` edge `-0.0018` maxDD `-0.6615`
- `market_context_high->crypto_alt_4h` score `-0.9242` n `146` status `ready` deltaP `3.5019` edge `0.0571` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.1076` n `146` status `ready` deltaP `8.9792` edge `0.0659` maxDD `-14.4206`
- `market_context_high->equity_4h` score `-1.4119` n `146` status `ready` deltaP `2.9785` edge `0.2135` maxDD `-20.4824`
- `market_context_high->unknown_1h` score `-1.4331` n `146` status `ready` deltaP `-0.2358` edge `-0.0555` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.6039` n `146` status `ready` deltaP `-0.9084` edge `0.0461` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-1.8652` n `146` status `ready` deltaP `-2.4092` edge `0.1026` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.5654` n `146` status `ready` deltaP `-6.2` edge `-0.004` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
