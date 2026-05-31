# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T11:37:21.993987+00:00`
- Price records: `672`
- Market context records: `2453`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `news_risk_high->crypto_alt_24h` score `19.5277` n `42` status `ready` deltaP `43.6756` edge `1.395` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `19.4317` n `42` status `ready` deltaP `54.9107` edge `1.2972` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.0431` n `42` status `ready` deltaP `29.7371` edge `1.0868` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `9.4414` n `42` status `ready` deltaP `15.9226` edge `0.7387` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.3229` n `42` status `ready` deltaP `24.8759` edge `0.467` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.8047` n `110` status `ready` deltaP `21.8024` edge `0.3712` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.3517` n `42` status `ready` deltaP `10.8135` edge `0.4116` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.5755` n `129` status `ready` deltaP `21.3438` edge `0.42` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.3818` n `129` status `ready` deltaP `21.4572` edge `0.49` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.3233` n `42` status `ready` deltaP `34.7718` edge `0.0636` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.1865` n `42` status `ready` deltaP `28.2085` edge `0.2876` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `2.54` n `110` status `ready` deltaP `12.3295` edge `0.6327` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.1024` n `42` status `ready` deltaP `26.6841` edge `0.0157` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.9499` n `42` status `ready` deltaP `16.8772` edge `0.1223` maxDD `-2.7857`
- `market_context_high->unknown_4h` score `1.9042` n `129` status `ready` deltaP `10.731` edge `0.1677` maxDD `-2.4448`
- `news_risk_high->unknown_1h` score `1.6726` n `42` status `ready` deltaP `22.3125` edge `0.0338` maxDD `-1.4536`
- `market_context_high->index_24h` score `1.2269` n `110` status `ready` deltaP `6.2247` edge `0.1072` maxDD `-0.7163`
- `market_context_high->crypto_major_1h` score `0.8848` n `136` status `ready` deltaP `9.3827` edge `0.1306` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.7236` n `136` status `ready` deltaP `7.7756` edge `0.1272` maxDD `-6.1656`
- `news_risk_high->fx_1h` score `0.5214` n `42` status `ready` deltaP `8.7753` edge `0.0106` maxDD `-0.0524`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
