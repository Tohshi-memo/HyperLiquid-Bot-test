# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T07:52:26.996273+00:00`
- Price records: `672`
- Market context records: `7649`
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

- `market_context_high->index_1h` score `0.0695` n `146` status `ready` deltaP `6.8123` edge `0.0114` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1129` n `146` status `ready` deltaP `8.455` edge `0.0252` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2186` n `146` status `ready` deltaP `2.0548` edge `0.0215` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3563` n `145` status `ready` deltaP `9.2803` edge `0.0172` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.4217` n `146` status `ready` deltaP `1.0777` edge `-0.0042` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.4729` n `146` status `ready` deltaP `5.677` edge `0.0529` maxDD `-7.7764`
- `market_context_high->metal_1h` score `-0.6691` n `146` status `ready` deltaP `0.6398` edge `0.0145` maxDD `-1.0307`
- `market_context_high->commodity_4h` score `-0.702` n `146` status `ready` deltaP `1.6066` edge `0.0053` maxDD `-2.2943`
- `market_context_high->index_4h` score `-0.7088` n `146` status `ready` deltaP `7.84` edge `0.027` maxDD `-3.2774`
- `market_context_high->commodity_24h` score `-0.7421` n `145` status `ready` deltaP `9.4065` edge `0.0338` maxDD `-7.0012`
- `market_context_high->fx_1h` score `-0.7422` n `146` status `ready` deltaP `-1.4727` edge `-0.0021` maxDD `-0.6615`
- `market_context_high->crypto_alt_4h` score `-1.0395` n `146` status `ready` deltaP `2.7397` edge `0.0474` maxDD `-9.5815`
- `market_context_high->equity_24h` score `-1.094` n `145` status `ready` deltaP `15.0607` edge `0.2499` maxDD `-34.5784`
- `market_context_high->crypto_major_4h` score `-1.1485` n `146` status `ready` deltaP `9.4366` edge `0.0576` maxDD `-14.4206`
- `market_context_high->unknown_24h` score `-1.4252` n `146` status `ready` deltaP `6.3237` edge `-0.0429` maxDD `-4.775`
- `market_context_high->unknown_1h` score `-1.4571` n `146` status `ready` deltaP `-0.5352` edge `-0.0555` maxDD `-1.3217`
- `market_context_high->equity_4h` score `-1.6145` n `146` status `ready` deltaP `1.6023` edge `0.1967` maxDD `-20.4824`
- `market_context_high->metal_4h` score `-1.7366` n `146` status `ready` deltaP `-2.8901` edge `0.0423` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-2.2083` n `146` status `ready` deltaP `-3.2772` edge `0.0644` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.6997` n `146` status `ready` deltaP `-7.7291` edge `-0.005` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
