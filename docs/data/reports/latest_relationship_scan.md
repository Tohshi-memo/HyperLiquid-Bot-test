# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T13:07:18.675013+00:00`
- Price records: `672`
- Market context records: `2247`
- Flow alert records: `8361`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9227`

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

- `news_risk_high->crypto_alt_24h` score `24.726` n `42` status `ready` deltaP `55.1339` edge `1.7518` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.345` n `42` status `ready` deltaP `44.8412` edge `1.1071` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.918` n `42` status `ready` deltaP `35.8134` edge `1.1192` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `13.7583` n `42` status `ready` deltaP `25.124` edge `1.0371` maxDD `-3.3119`
- `market_context_high->crypto_alt_4h` score `11.4679` n `131` status `ready` deltaP `31.0603` edge `0.8663` maxDD `-6.0832`
- `market_context_high->crypto_major_4h` score `10.3595` n `131` status `ready` deltaP `37.3255` edge `0.6901` maxDD `-3.7185`
- `market_context_high->unknown_24h` score `10.0518` n `116` status `ready` deltaP `31.3158` edge `0.6816` maxDD `-2.5508`
- `news_risk_high->unknown_24h` score `9.8394` n `42` status `ready` deltaP `36.0367` edge `0.6023` maxDD `-1.4744`
- `market_context_high->crypto_major_24h` score `7.0392` n `116` status `ready` deltaP `19.0074` edge `1.165` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.4747` n `131` status `ready` deltaP `20.8388` edge `0.3684` maxDD `-1.7549`
- `market_context_high->index_4h` score `4.1173` n `131` status `ready` deltaP `31.5409` edge `0.1702` maxDD `-0.3228`
- `news_risk_high->commodity_4h` score `3.8967` n `43` status `ready` deltaP `33.2246` edge `0.3452` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.8448` n `42` status `ready` deltaP `13.4672` edge `0.2725` maxDD `-1.3507`
- `news_risk_high->fx_24h` score `3.6181` n `42` status `ready` deltaP `36.7311` edge `0.0751` maxDD `-0.1442`
- `market_context_high->equity_24h` score `3.5542` n `116` status `ready` deltaP `22.6772` edge `0.2977` maxDD `-6.8828`
- `market_context_high->index_24h` score `3.5484` n `116` status `ready` deltaP `15.0682` edge `0.247` maxDD `-1.4737`
- `market_context_high->equity_4h` score `3.3611` n `131` status `ready` deltaP `21.3159` edge `0.2322` maxDD `-3.204`
- `news_risk_high->commodity_24h` score `2.8458` n `42` status `ready` deltaP `1.0417` edge `0.3119` maxDD `-3.202`
- `market_context_high->crypto_alt_1h` score `2.3455` n `143` status `ready` deltaP `14.0855` edge `0.1949` maxDD `-5.1346`
- `news_risk_high->fx_4h` score `2.1232` n `43` status `ready` deltaP `26.9746` edge `0.0155` maxDD `-0.1382`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
