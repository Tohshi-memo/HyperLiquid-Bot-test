# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T13:37:16.748472+00:00`
- Price records: `672`
- Market context records: `1016`
- Flow alert records: `4835`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8634`

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

- `market_context_high->crypto_major_24h` score `13.514` n `196` status `ready` deltaP `32.3877` edge `0.9691` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.3344` n `196` status `ready` deltaP `11.0997` edge `0.4106` maxDD `-9.5387`
- `market_context_high->equity_24h` score `0.5553` n `196` status `ready` deltaP `7.0765` edge `0.1956` maxDD `-8.3865`
- `market_context_high->index_24h` score `0.4239` n `196` status `ready` deltaP `6.4115` edge `0.164` maxDD `-4.7137`
- `market_context_high->fx_1h` score `-0.1943` n `196` status `ready` deltaP `3.0399` edge `0.0004` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.4273` n `196` status `ready` deltaP `2.9665` edge `0.0254` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.7814` n `196` status `ready` deltaP `-0.773` edge `0.0169` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.7994` n `196` status `ready` deltaP `1.9552` edge `0.0057` maxDD `-2.8282`
- `market_context_high->fx_4h` score `-0.893` n `196` status `ready` deltaP `3.3194` edge `0.0031` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.232` n `196` status `ready` deltaP `4.598` edge `-0.0163` maxDD `-11.4508`
- `market_context_high->equity_4h` score `-1.3302` n `196` status `ready` deltaP `2.4981` edge `0.0877` maxDD `-10.5498`
- `market_context_high->crypto_alt_1h` score `-1.3327` n `196` status `ready` deltaP `-1.1243` edge `-0.0194` maxDD `-8.1842`
- `market_context_high->index_4h` score `-1.5161` n `196` status `ready` deltaP `-0.616` edge `0.0254` maxDD `-6.1444`
- `market_context_high->metal_1h` score `-1.8427` n `196` status `ready` deltaP `0.0733` edge `-0.0408` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-2.8321` n `196` status `ready` deltaP `7.1086` edge `0.0872` maxDD `-22.648`
- `market_context_high->crypto_alt_4h` score `-2.8617` n `196` status `ready` deltaP `-0.1898` edge `0.0406` maxDD `-15.2248`
- `market_context_high->commodity_4h` score `-3.2204` n `196` status `ready` deltaP `-2.3706` edge `0.0642` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.3092` n `196` status `ready` deltaP `0.567` edge `-0.0204` maxDD `-19.2774`
- `market_context_high->metal_4h` score `-4.3934` n `196` status `ready` deltaP `-2.7719` edge `-0.1644` maxDD `-23.7635`
- `market_context_high->metal_24h` score `-6.933` n `196` status `ready` deltaP `-9.1695` edge `0.2209` maxDD `-48.0013`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
