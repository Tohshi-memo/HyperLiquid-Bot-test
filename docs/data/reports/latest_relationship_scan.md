# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T07:07:30.019366+00:00`
- Price records: `672`
- Market context records: `7645`
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

- `market_context_high->index_1h` score `0.0687` n `146` status `ready` deltaP `6.8123` edge `0.0113` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1097` n `146` status `ready` deltaP `8.455` edge `0.0256` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2131` n `146` status `ready` deltaP `2.0548` edge `0.0222` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3551` n `145` status `ready` deltaP `9.2803` edge `0.0173` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.4077` n `146` status `ready` deltaP `1.2279` edge `-0.0034` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.4737` n `146` status `ready` deltaP `5.677` edge `0.0528` maxDD `-7.7764`
- `market_context_high->commodity_24h` score `-0.6451` n `145` status `ready` deltaP `9.9291` edge `0.0384` maxDD `-7.0012`
- `market_context_high->metal_1h` score `-0.6761` n `146` status `ready` deltaP `0.6398` edge `0.0136` maxDD `-1.0307`
- `market_context_high->commodity_4h` score `-0.6948` n `146` status `ready` deltaP `1.6066` edge `0.0059` maxDD `-2.2943`
- `market_context_high->index_4h` score `-0.6985` n `146` status `ready` deltaP `7.9929` edge `0.0273` maxDD `-3.2774`
- `market_context_high->fx_1h` score `-0.7158` n `146` status `ready` deltaP `-1.1724` edge `-0.0019` maxDD `-0.6615`
- `market_context_high->equity_24h` score `-0.8258` n `145` status `ready` deltaP `15.5834` edge `0.2808` maxDD `-34.5784`
- `market_context_high->crypto_alt_4h` score `-0.9869` n `146` status `ready` deltaP `3.197` edge `0.0511` maxDD `-9.5815`
- `market_context_high->unknown_24h` score `-1.0451` n `146` status `ready` deltaP `6.8446` edge `-0.0147` maxDD `-4.775`
- `market_context_high->crypto_major_4h` score `-1.1275` n `146` status `ready` deltaP `9.4366` edge `0.0603` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.4259` n `146` status `ready` deltaP `-0.2358` edge `-0.0549` maxDD `-1.3217`
- `market_context_high->equity_4h` score `-1.5942` n `146` status `ready` deltaP `1.6023` edge `0.1993` maxDD `-20.4824`
- `market_context_high->metal_4h` score `-1.757` n `146` status `ready` deltaP `-3.0425` edge `0.0407` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-2.1911` n `146` status `ready` deltaP `-3.2772` edge `0.0666` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.657` n `146` status `ready` deltaP `-7.2703` edge `-0.0045` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
