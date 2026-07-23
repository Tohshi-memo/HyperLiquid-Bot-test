# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T07:22:38.528390+00:00`
- Price records: `672`
- Market context records: `7646`
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
- `market_context_high->crypto_major_1h` score `-0.1082` n `146` status `ready` deltaP `8.455` edge `0.0258` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2123` n `146` status `ready` deltaP `2.0548` edge `0.0223` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3563` n `145` status `ready` deltaP `9.2803` edge `0.0172` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.4186` n `146` status `ready` deltaP `1.0777` edge `-0.0038` maxDD `-1.5641`
- `market_context_high->equity_1h` score `-0.4737` n `146` status `ready` deltaP `5.677` edge `0.0528` maxDD `-7.7764`
- `market_context_high->metal_1h` score `-0.6746` n `146` status `ready` deltaP `0.6398` edge `0.0138` maxDD `-1.0307`
- `market_context_high->commodity_24h` score `-0.6806` n `145` status `ready` deltaP `9.7549` edge `0.0366` maxDD `-7.0012`
- `market_context_high->commodity_4h` score `-0.6972` n `146` status `ready` deltaP `1.6066` edge `0.0057` maxDD `-2.2943`
- `market_context_high->index_4h` score `-0.708` n `146` status `ready` deltaP `7.84` edge `0.0271` maxDD `-3.2774`
- `market_context_high->fx_1h` score `-0.729` n `146` status `ready` deltaP `-1.3226` edge `-0.002` maxDD `-0.6615`
- `market_context_high->equity_24h` score `-0.9152` n `145` status `ready` deltaP `15.4091` edge `0.2705` maxDD `-34.5784`
- `market_context_high->crypto_alt_4h` score `-1.0049` n `146` status `ready` deltaP `3.0446` edge `0.0498` maxDD `-9.5815`
- `market_context_high->unknown_24h` score `-1.1046` n `146` status `ready` deltaP `6.671` edge `-0.0185` maxDD `-4.775`
- `market_context_high->crypto_major_4h` score `-1.136` n `146` status `ready` deltaP `9.4366` edge `0.0592` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.4283` n `146` status `ready` deltaP `-0.2358` edge `-0.0551` maxDD `-1.3217`
- `market_context_high->equity_4h` score `-1.6051` n `146` status `ready` deltaP `1.6023` edge `0.1979` maxDD `-20.4824`
- `market_context_high->metal_4h` score `-1.7538` n `146` status `ready` deltaP `-3.0425` edge `0.0411` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-2.1974` n `146` status `ready` deltaP `-3.2772` edge `0.0658` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.6716` n `146` status `ready` deltaP `-7.4232` edge `-0.0047` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
