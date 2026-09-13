# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T11:37:25.769936+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12986`

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

- `market_context_high->unknown_24h` score `16682.1762` n `59` status `ready` deltaP `14.5412` edge `1390.0896` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `403.7247` n `82` status `ready` deltaP `-5.1008` edge `33.7199` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `17.9714` n `82` status `ready` deltaP `33.6165` edge `1.3223` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.9494` n `82` status `ready` deltaP `37.8512` edge `1.3905` maxDD `-9.098`
- `market_context_high->crypto_alt_24h` score `10.2516` n `59` status `ready` deltaP `23.5711` edge `0.7799` maxDD `-3.9523`
- `market_context_high->equity_24h` score `9.0996` n `59` status `ready` deltaP `44.4564` edge `0.5379` maxDD `-4.4114`
- `news_risk_high->equity_24h` score `7.7773` n `82` status `ready` deltaP `22.4432` edge `0.6765` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.6712` n `82` status `ready` deltaP `47.5946` edge `0.2563` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.5756` n `82` status `ready` deltaP `24.2431` edge `0.2651` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.031` n `59` status `ready` deltaP `39.8276` edge `0.0704` maxDD `0.0`
- `market_context_high->index_24h` score `3.8219` n `59` status `ready` deltaP `41.4144` edge `0.0845` maxDD `-0.7014`
- `market_context_high->metal_24h` score `0.9099` n `59` status `ready` deltaP `13.5155` edge `0.114` maxDD `-1.9958`
- `risk_on_high->crypto_alt_4h` score `0.5476` n `65` status `ready` deltaP `11.5152` edge `0.1609` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.5476` n `65` status `ready` deltaP `11.5152` edge `0.1609` maxDD `-6.7304`
- `news_risk_high->index_4h` score `0.4297` n `82` status `ready` deltaP `12.6496` edge `0.0336` maxDD `-0.6935`
- `risk_on_high->fx_1h` score `0.0981` n `65` status `ready` deltaP `4.5532` edge `0.0034` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.0981` n `65` status `ready` deltaP `4.5532` edge `0.0034` maxDD `-0.0464`
- `market_context_high->fx_1h` score `-0.0091` n `143` status `ready` deltaP `4.6931` edge `-0.0008` maxDD `-0.5323`
- `risk_on_high->metal_1h` score `-0.0604` n `65` status `ready` deltaP `3.9129` edge `0.0019` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0604` n `65` status `ready` deltaP `3.9129` edge `0.0019` maxDD `-0.3081`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
