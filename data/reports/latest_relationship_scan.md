# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T00:22:32.098518+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4818`

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

- `market_context_high->unknown_1h` score `364.0619` n `50` status `ready` deltaP `10.4251` edge `30.2739` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.0549` n `50` status `ready` deltaP `10.3659` edge `24.2688` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.7885` n `70` status `ready` deltaP `36.7014` edge `1.116` maxDD `-1.931`
- `market_context_high->crypto_alt_24h` score `10.7504` n `50` status `ready` deltaP `20.7014` edge `0.9282` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `9.4778` n `70` status `ready` deltaP `33.7351` edge `0.6134` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.0138` n `50` status `ready` deltaP `31.8264` edge `0.6806` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.7153` n `50` status `ready` deltaP `18.7622` edge `0.5882` maxDD `-3.294`
- `news_risk_high->crypto_alt_4h` score `7.1789` n `108` status `ready` deltaP `28.4327` edge `0.5431` maxDD `-6.4195`
- `market_context_high->crypto_alt_4h` score `6.1451` n `50` status `ready` deltaP `16.9512` edge `0.528` maxDD `-7.6465`
- `market_context_high->crypto_alt_1h` score `3.2362` n `50` status `ready` deltaP `14.8024` edge `0.2373` maxDD `-3.6376`
- `news_risk_high->crypto_major_24h` score `3.2129` n `70` status `ready` deltaP `8.3978` edge `0.5567` maxDD `-9.3956`
- `news_risk_high->equity_4h` score `3.1103` n `108` status `ready` deltaP `26.1687` edge `0.146` maxDD `-2.9013`
- `market_context_high->crypto_major_1h` score `3.0025` n `50` status `ready` deltaP `13.4012` edge `0.2059` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8153` n `50` status `ready` deltaP `31.4695` edge `0.0383` maxDD `-0.0791`
- `news_risk_high->crypto_major_4h` score `2.7788` n `108` status `ready` deltaP `20.2066` edge `0.3802` maxDD `-7.3592`
- `news_risk_high->index_24h` score `1.5816` n `70` status `ready` deltaP `19.2361` edge `0.0486` maxDD `-0.2696`
- `market_context_high->fx_1h` score `1.4603` n `50` status `ready` deltaP `20.491` edge `0.0115` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.3863` n `70` status `ready` deltaP `14.6528` edge `0.206` maxDD `-2.0759`
- `news_risk_high->crypto_alt_1h` score `1.3588` n `108` status `ready` deltaP `6.2098` edge `0.1279` maxDD `-2.4854`
- `market_context_high->equity_24h` score `1.2788` n `50` status `ready` deltaP `6.0208` edge `0.31` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
