# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T11:52:30.198267+00:00`
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

- `market_context_high->unknown_24h` score `16686.9456` n `59` status `ready` deltaP `14.7136` edge `1390.4859` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `406.6311` n `82` status `ready` deltaP `-5.1008` edge `33.9621` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.002` n `82` status `ready` deltaP `33.7889` edge `1.3237` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.9746` n `82` status `ready` deltaP `37.8512` edge `1.3926` maxDD `-9.098`
- `market_context_high->crypto_alt_24h` score `10.2822` n `59` status `ready` deltaP `23.7435` edge `0.7813` maxDD `-3.9523`
- `market_context_high->equity_24h` score `9.1566` n `59` status `ready` deltaP `44.6288` edge `0.5415` maxDD `-4.4114`
- `news_risk_high->equity_24h` score `7.8343` n `82` status `ready` deltaP `22.6156` edge `0.6801` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.691` n `82` status `ready` deltaP `47.767` edge `0.2568` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.5756` n `82` status `ready` deltaP `24.2431` edge `0.2651` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.0262` n `59` status `ready` deltaP `39.8276` edge `0.07` maxDD `0.0`
- `market_context_high->index_24h` score `3.8417` n `59` status `ready` deltaP `41.5868` edge `0.085` maxDD `-0.7014`
- `market_context_high->metal_24h` score `0.9099` n `59` status `ready` deltaP `13.5155` edge `0.114` maxDD `-1.9958`
- `risk_on_high->crypto_alt_4h` score `0.5468` n `65` status `ready` deltaP `11.5152` edge `0.1608` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.5468` n `65` status `ready` deltaP `11.5152` edge `0.1608` maxDD `-6.7304`
- `news_risk_high->index_4h` score `0.4305` n `82` status `ready` deltaP `12.6496` edge `0.0337` maxDD `-0.6935`
- `risk_on_high->fx_1h` score `0.0861` n `65` status `ready` deltaP `4.4035` edge `0.0034` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.0861` n `65` status `ready` deltaP `4.4035` edge `0.0034` maxDD `-0.0464`
- `market_context_high->fx_1h` score `0.0003` n `144` status `ready` deltaP `4.8736` edge `-0.0008` maxDD `-0.5323`
- `risk_on_high->metal_1h` score `-0.0484` n `65` status `ready` deltaP `4.0626` edge `0.0019` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0484` n `65` status `ready` deltaP `4.0626` edge `0.0019` maxDD `-0.3081`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
