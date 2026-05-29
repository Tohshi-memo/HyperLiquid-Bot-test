# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T06:22:21.241757+00:00`
- Price records: `672`
- Market context records: `2219`
- Flow alert records: `8279`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9177`

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

- `news_risk_high->crypto_alt_24h` score `26.3538` n `30` status `ready` deltaP `57.9166` edge `1.8689` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `14.3038` n `30` status `ready` deltaP `48.5764` edge `0.9121` maxDD `-3.1836`
- `market_context_high->crypto_alt_4h` score `13.0103` n `132` status `ready` deltaP `37.7587` edge `0.9261` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.8115` n `132` status `ready` deltaP `42.4335` edge `0.7544` maxDD `-1.9063`
- `news_risk_high->equity_24h` score `10.9908` n `30` status `ready` deltaP `39.5486` edge `0.6837` maxDD `-2.1831`
- `news_risk_high->unknown_24h` score `10.2564` n `30` status `ready` deltaP `38.8194` edge `0.6185` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `6.9173` n `30` status `ready` deltaP `17.4306` edge `0.8287` maxDD `-3.3119`
- `market_context_high->unknown_4h` score `5.5009` n `132` status `ready` deltaP `21.5263` edge `0.3828` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.8923` n `43` status `ready` deltaP `32.6148` edge `0.3487` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.4038` n `132` status `ready` deltaP `23.4156` edge `0.237` maxDD `-5.0894`
- `market_context_high->index_4h` score `3.227` n `132` status `ready` deltaP `26.6214` edge `0.1598` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `3.1931` n `132` status `ready` deltaP `17.2655` edge `0.1987` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `2.9962` n `132` status `ready` deltaP `16.2085` edge `0.228` maxDD `-4.9097`
- `news_risk_high->fx_24h` score `2.6162` n `30` status `ready` deltaP `28.3333` edge `0.0476` maxDD `-0.1442`
- `news_risk_high->fx_4h` score `2.234` n `43` status `ready` deltaP `28.1941` edge `0.0166` maxDD `-0.1382`
- `market_context_high->unknown_24h` score `2.2163` n `132` status `ready` deltaP `25.0316` edge `0.4993` maxDD `-32.8525`
- `market_context_high->index_24h` score `1.9292` n `132` status `ready` deltaP `9.6906` edge `0.219` maxDD `-4.1604`
- `news_risk_high->commodity_24h` score `1.7735` n `30` status `ready` deltaP `-6.5278` edge `0.273` maxDD `-3.202`
- `news_risk_high->unknown_1h` score `1.5007` n `43` status `ready` deltaP `21.6439` edge `0.0277` maxDD `-1.7548`
- `market_context_high->metal_4h` score `1.3437` n `132` status `ready` deltaP `17.1332` edge `0.1365` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
