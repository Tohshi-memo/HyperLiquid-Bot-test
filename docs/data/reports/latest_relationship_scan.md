# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T07:07:16.745347+00:00`
- Price records: `672`
- Market context records: `2222`
- Flow alert records: `8288`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `news_risk_high->crypto_alt_24h` score `26.6682` n `32` status `ready` deltaP `57.8125` edge `1.8958` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `14.8836` n `32` status `ready` deltaP `48.2639` edge `0.9625` maxDD `-3.1836`
- `market_context_high->crypto_alt_4h` score `12.9729` n `132` status `ready` deltaP `37.6063` edge `0.924` maxDD `-5.1574`
- `news_risk_high->equity_24h` score `12.8222` n `32` status `ready` deltaP `39.2361` edge `0.8384` maxDD `-2.1831`
- `market_context_high->crypto_major_4h` score `11.733` n `132` status `ready` deltaP `41.9762` edge `0.7509` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `10.1497` n `32` status `ready` deltaP `38.7153` edge `0.6103` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `7.7167` n `32` status `ready` deltaP `19.6181` edge `0.9166` maxDD `-3.3119`
- `market_context_high->unknown_4h` score `5.4875` n `132` status `ready` deltaP `21.3738` edge `0.3827` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.9292` n `43` status `ready` deltaP `32.9197` edge `0.3514` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.3544` n `132` status `ready` deltaP `23.2631` edge `0.2339` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.232` n `135` status `ready` deltaP `17.7068` edge `0.199` maxDD `-1.817`
- `market_context_high->index_4h` score `3.2186` n `132` status `ready` deltaP `26.6214` edge `0.1591` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `3.0605` n `135` status `ready` deltaP `16.8164` edge `0.2293` maxDD `-4.9097`
- `news_risk_high->fx_24h` score `2.873` n `32` status `ready` deltaP `30.2083` edge `0.0565` maxDD `-0.1442`
- `news_risk_high->commodity_24h` score `2.2487` n `32` status `ready` deltaP `-2.7778` edge `0.2876` maxDD `-3.202`
- `news_risk_high->fx_4h` score `2.2048` n `43` status `ready` deltaP `27.8892` edge `0.0162` maxDD `-0.1382`
- `market_context_high->unknown_24h` score `1.9994` n `132` status `ready` deltaP `24.5108` edge `0.4847` maxDD `-32.8525`
- `market_context_high->index_24h` score `1.8313` n `132` status `ready` deltaP `9.517` edge `0.212` maxDD `-4.1604`
- `news_risk_high->unknown_1h` score `1.43` n `43` status `ready` deltaP `21.1948` edge `0.0248` maxDD `-1.7548`
- `news_risk_high->index_24h` score `1.3708` n `32` status `ready` deltaP `10.9375` edge `0.0832` maxDD `-1.3507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
