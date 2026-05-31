# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T08:52:21.529752+00:00`
- Price records: `672`
- Market context records: `2441`
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

- `news_risk_high->crypto_alt_24h` score `19.2465` n `43` status `ready` deltaP `43.2655` edge `1.3743` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.9546` n `43` status `ready` deltaP `53.0563` edge `1.2698` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.8243` n `43` status `ready` deltaP `29.7925` edge `1.0682` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `9.5856` n `43` status `ready` deltaP `16.9896` edge `0.7436` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.1502` n `43` status `ready` deltaP `23.6474` edge `0.4608` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.6364` n `103` status `ready` deltaP `22.4734` edge `0.3527` maxDD `-1.626`
- `news_risk_high->index_24h` score `4.9627` n `43` status `ready` deltaP `8.9309` edge `0.3959` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.8948` n `124` status `ready` deltaP `22.6053` edge `0.4382` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.7758` n `124` status `ready` deltaP `23.0379` edge `0.5123` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.2278` n `43` status `ready` deltaP `33.7573` edge `0.0624` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.1808` n `43` status `ready` deltaP `28.8038` edge `0.2829` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.7368` n `124` status `ready` deltaP `13.6851` edge `0.1978` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `2.287` n `103` status `ready` deltaP `10.329` edge `0.6136` maxDD `-25.1408`
- `market_context_high->index_24h` score `2.2356` n `103` status `ready` deltaP `11.4145` edge `0.1359` maxDD `-0.3888`
- `news_risk_high->fx_4h` score `2.122` n `43` status `ready` deltaP `26.9746` edge `0.0154` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.8071` n `43` status `ready` deltaP `15.9919` edge `0.1163` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.1007` n `130` status `ready` deltaP `11.1516` edge `0.1368` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.0929` n `43` status `ready` deltaP `20.2966` edge `0.0027` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `0.8622` n `130` status `ready` deltaP `8.503` edge `0.1339` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.5623` n `124` status `ready` deltaP `12.7557` edge `0.0444` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
