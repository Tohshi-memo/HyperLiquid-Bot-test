# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T06:22:28.105721+00:00`
- Price records: `672`
- Market context records: `7642`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14697`

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

- `market_context_high->index_1h` score `0.0515` n `146` status `ready` deltaP `6.512` edge `0.0111` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.0864` n `146` status `ready` deltaP `8.7544` edge `0.0266` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.1905` n `146` status `ready` deltaP `2.3542` edge `0.0231` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3515` n `145` status `ready` deltaP `9.2803` edge `0.0176` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.3788` n `146` status `ready` deltaP `1.6783` edge `-0.0027` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.4729` n `146` status `ready` deltaP `5.677` edge `0.0529` maxDD `-7.7764`
- `market_context_high->equity_24h` score `-0.5327` n `145` status `ready` deltaP `16.106` edge `0.3149` maxDD `-34.5784`
- `market_context_high->commodity_24h` score `-0.548` n `145` status `ready` deltaP `10.4518` edge `0.043` maxDD `-7.0012`
- `market_context_high->index_4h` score `-0.6707` n `146` status `ready` deltaP `8.4516` edge `0.0278` maxDD `-3.2774`
- `market_context_high->metal_1h` score `-0.6761` n `146` status `ready` deltaP `0.6398` edge `0.0136` maxDD `-1.0307`
- `market_context_high->commodity_4h` score `-0.6766` n `146` status `ready` deltaP `1.7595` edge `0.0064` maxDD `-2.2943`
- `market_context_high->fx_1h` score `-0.6894` n `146` status `ready` deltaP `-0.8721` edge `-0.0017` maxDD `-0.6615`
- `market_context_high->unknown_24h` score `-0.8642` n `146` status `ready` deltaP `7.3654` edge `-0.0031` maxDD `-4.775`
- `market_context_high->crypto_alt_4h` score `-0.9233` n `146` status `ready` deltaP `3.6543` edge `0.0562` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.079` n `146` status `ready` deltaP `9.589` edge `0.0655` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.4139` n `146` status `ready` deltaP `-0.0861` edge `-0.0549` maxDD `-1.3217`
- `market_context_high->equity_4h` score `-1.5376` n `146` status `ready` deltaP `2.061` edge `0.2035` maxDD `-20.4824`
- `market_context_high->metal_4h` score `-1.7585` n `146` status `ready` deltaP `-3.0425` edge `0.0405` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-2.1584` n `146` status `ready` deltaP `-3.2772` edge `0.0708` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.6155` n `146` status `ready` deltaP `-6.8116` edge `-0.0041` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
