# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T22:52:25.673586+00:00`
- Price records: `672`
- Market context records: `7609`
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

- `market_context_high->equity_24h` score `1.1397` n `145` status `ready` deltaP `16.9771` edge `0.5235` maxDD `-34.5784`
- `market_context_high->unknown_24h` score `0.9648` n `146` status `ready` deltaP `12.5737` edge `0.1146` maxDD `-4.775`
- `market_context_high->commodity_24h` score `0.3909` n `145` status `ready` deltaP `15.6783` edge `0.0864` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.1156` n `146` status `ready` deltaP `7.5631` edge `0.0123` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1284` n `146` status `ready` deltaP `8.3053` edge `0.0242` maxDD `-4.0162`
- `market_context_high->commodity_4h` score `-0.1776` n `146` status `ready` deltaP `6.3467` edge `0.0174` maxDD `-2.2943`
- `market_context_high->crypto_alt_1h` score `-0.2046` n `146` status `ready` deltaP `2.3542` edge `0.0213` maxDD `-2.7243`
- `market_context_high->commodity_1h` score `-0.2468` n `146` status `ready` deltaP `3.9306` edge `-0.0008` maxDD `-1.5641`
- `market_context_high->fx_24h` score `-0.3311` n `145` status `ready` deltaP `9.2803` edge `0.0193` maxDD `-3.0343`
- `market_context_high->equity_1h` score `-0.4034` n `146` status `ready` deltaP `6.5779` edge `0.0558` maxDD `-7.7764`
- `market_context_high->index_4h` score `-0.5496` n `146` status `ready` deltaP `10.2865` edge `0.0311` maxDD `-3.2774`
- `market_context_high->metal_1h` score `-0.5858` n `146` status `ready` deltaP `2.1368` edge `0.0152` maxDD `-1.0307`
- `market_context_high->fx_1h` score `-0.6534` n `146` status `ready` deltaP `-0.4217` edge `-0.0017` maxDD `-0.6615`
- `market_context_high->crypto_alt_4h` score `-0.9281` n `146` status `ready` deltaP `3.5019` edge `0.0566` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.069` n `146` status `ready` deltaP `9.4366` edge `0.0678` maxDD `-14.4206`
- `market_context_high->equity_4h` score `-1.3788` n `146` status `ready` deltaP `3.2843` edge `0.2157` maxDD `-20.4824`
- `market_context_high->unknown_1h` score `-1.4799` n `146` status `ready` deltaP `-0.3855` edge `-0.0584` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.5976` n `146` status `ready` deltaP `-0.9084` edge `0.0469` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-1.7745` n `146` status `ready` deltaP `-1.7147` edge `0.1096` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.5654` n `146` status `ready` deltaP `-6.2` edge `-0.004` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
