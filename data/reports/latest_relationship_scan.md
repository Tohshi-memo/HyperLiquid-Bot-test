# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T04:22:23.879873+00:00`
- Price records: `672`
- Market context records: `7633`
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

- `market_context_high->equity_24h` score `0.1234` n `145` status `ready` deltaP `16.9771` edge `0.3932` maxDD `-34.5784`
- `market_context_high->index_1h` score `0.0781` n `146` status `ready` deltaP `6.9625` edge `0.0115` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1386` n `146` status `ready` deltaP `8.1556` edge `0.0239` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.1687` n `146` status `ready` deltaP `2.6536` edge `0.0239` maxDD `-2.7243`
- `market_context_high->commodity_24h` score `-0.3021` n `145` status `ready` deltaP `11.8455` edge `0.0542` maxDD `-7.0012`
- `market_context_high->fx_24h` score `-0.3515` n `145` status `ready` deltaP `9.2803` edge `0.0176` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.3546` n `146` status `ready` deltaP `2.1288` edge `-0.0026` maxDD `-1.5641`
- `market_context_high->unknown_24h` score `-0.4147` n `146` status `ready` deltaP `8.7543` edge `0.0251` maxDD `-4.775`
- `market_context_high->equity_1h` score `-0.4471` n `146` status `ready` deltaP `5.9773` edge `0.0542` maxDD `-7.7764`
- `market_context_high->commodity_4h` score `-0.5619` n `146` status `ready` deltaP `2.9827` edge `0.0078` maxDD `-2.2943`
- `market_context_high->index_4h` score `-0.6573` n `146` status `ready` deltaP `8.6045` edge `0.0285` maxDD `-3.2774`
- `market_context_high->metal_1h` score `-0.6707` n `146` status `ready` deltaP `0.7895` edge `0.0133` maxDD `-1.0307`
- `market_context_high->fx_1h` score `-0.6882` n `146` status `ready` deltaP `-0.8721` edge `-0.0016` maxDD `-0.6615`
- `market_context_high->crypto_alt_4h` score `-0.8584` n `146` status `ready` deltaP `3.8068` edge `0.0635` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.0423` n `146` status `ready` deltaP `9.589` edge `0.0702` maxDD `-14.4206`
- `market_context_high->equity_4h` score `-1.4828` n `146` status `ready` deltaP `2.214` edge `0.2095` maxDD `-20.4824`
- `market_context_high->unknown_1h` score `-1.565` n `146` status `ready` deltaP `-1.134` edge `-0.0605` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.6977` n `146` status `ready` deltaP `-2.1279` edge `0.0422` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-2.0773` n `146` status `ready` deltaP `-3.2772` edge `0.0812` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.5704` n `146` status `ready` deltaP `-6.3529` edge `-0.0034` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
