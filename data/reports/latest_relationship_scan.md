# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T06:52:29.073635+00:00`
- Price records: `672`
- Market context records: `7644`
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

- `market_context_high->index_1h` score `0.0601` n `146` status `ready` deltaP `6.6622` edge `0.0112` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1004` n `146` status `ready` deltaP `8.6047` edge `0.0258` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.203` n `146` status `ready` deltaP `2.2045` edge `0.0225` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3539` n `145` status `ready` deltaP `9.2803` edge `0.0174` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.3975` n `146` status `ready` deltaP `1.378` edge `-0.0031` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.483` n `146` status `ready` deltaP `5.5268` edge `0.0526` maxDD `-7.7764`
- `market_context_high->commodity_24h` score `-0.6107` n `145` status `ready` deltaP `10.1034` edge `0.0401` maxDD `-7.0012`
- `market_context_high->metal_1h` score `-0.6761` n `146` status `ready` deltaP `0.6398` edge `0.0136` maxDD `-1.0307`
- `market_context_high->index_4h` score `-0.6897` n `146` status `ready` deltaP `8.1458` edge `0.0274` maxDD `-3.2774`
- `market_context_high->commodity_4h` score `-0.6924` n `146` status `ready` deltaP `1.6066` edge `0.0061` maxDD `-2.2943`
- `market_context_high->fx_1h` score `-0.7146` n `146` status `ready` deltaP `-1.1724` edge `-0.0018` maxDD `-0.6615`
- `market_context_high->equity_24h` score `-0.7317` n `145` status `ready` deltaP `15.7576` edge `0.2917` maxDD `-34.5784`
- `market_context_high->crypto_alt_4h` score `-0.9665` n `146` status `ready` deltaP `3.3495` edge `0.0527` maxDD `-9.5815`
- `market_context_high->unknown_24h` score `-0.9856` n `146` status `ready` deltaP `7.0182` edge `-0.0109` maxDD `-4.775`
- `market_context_high->crypto_major_4h` score `-1.115` n `146` status `ready` deltaP `9.4366` edge `0.0619` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.4259` n `146` status `ready` deltaP `-0.2358` edge `-0.0549` maxDD `-1.3217`
- `market_context_high->equity_4h` score `-1.5776` n `146` status `ready` deltaP `1.7552` edge `0.2004` maxDD `-20.4824`
- `market_context_high->metal_4h` score `-1.7577` n `146` status `ready` deltaP `-3.0425` edge `0.0406` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-2.181` n `146` status `ready` deltaP `-3.2772` edge `0.0679` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.6436` n `146` status `ready` deltaP `-7.1174` edge `-0.0044` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
