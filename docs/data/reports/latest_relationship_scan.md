# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T00:37:25.606705+00:00`
- Price records: `672`
- Market context records: `7617`
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

- `market_context_high->equity_24h` score `0.8683` n `145` status `ready` deltaP `16.9771` edge `0.4887` maxDD `-34.5784`
- `market_context_high->unknown_24h` score `0.5508` n `146` status `ready` deltaP `11.3585` edge `0.0882` maxDD `-4.775`
- `market_context_high->commodity_24h` score `0.1625` n `145` status `ready` deltaP `14.4588` edge `0.0755` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.0937` n `146` status `ready` deltaP `7.2628` edge `0.0115` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1806` n `146` status `ready` deltaP `7.7065` edge `0.0215` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.217` n `146` status `ready` deltaP `2.2045` edge `0.0207` maxDD `-2.7243`
- `market_context_high->commodity_1h` score `-0.2734` n `146` status `ready` deltaP `3.4801` edge `-0.0012` maxDD `-1.5641`
- `market_context_high->commodity_4h` score `-0.304` n `146` status `ready` deltaP `5.2763` edge `0.014` maxDD `-2.2943`
- `market_context_high->fx_24h` score `-0.3479` n `145` status `ready` deltaP `9.2803` edge `0.0179` maxDD `-3.0343`
- `market_context_high->equity_1h` score `-0.4518` n `146` status `ready` deltaP `6.1274` edge `0.0526` maxDD `-7.7764`
- `market_context_high->index_4h` score `-0.5915` n `146` status `ready` deltaP `9.6749` edge `0.0298` maxDD `-3.2774`
- `market_context_high->metal_1h` score `-0.6139` n `146` status `ready` deltaP `1.6877` edge `0.0146` maxDD `-1.0307`
- `market_context_high->fx_1h` score `-0.6786` n `146` status `ready` deltaP `-0.722` edge `-0.0018` maxDD `-0.6615`
- `market_context_high->crypto_alt_4h` score `-0.9448` n `146` status `ready` deltaP `3.197` edge `0.0565` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.1563` n `146` status `ready` deltaP `8.5219` edge `0.0627` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.4127` n `146` status `ready` deltaP `-0.0861` edge `-0.0548` maxDD `-1.3217`
- `market_context_high->equity_4h` score `-1.4568` n `146` status `ready` deltaP `2.5198` edge `0.2108` maxDD `-20.4824`
- `market_context_high->metal_4h` score `-1.6086` n `146` status `ready` deltaP `-0.9084` edge `0.0455` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-1.9329` n `146` status `ready` deltaP `-2.93` edge `0.0974` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.5776` n `146` status `ready` deltaP `-6.3529` edge `-0.004` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
