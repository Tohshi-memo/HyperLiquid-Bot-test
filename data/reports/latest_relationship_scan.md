# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T22:52:22.108585+00:00`
- Price records: `672`
- Market context records: `2398`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9201`

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

- `news_risk_high->crypto_alt_24h` score `21.2022` n `43` status `ready` deltaP `48.6474` edge `1.5014` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.2402` n `43` status `ready` deltaP `49.9313` edge `1.2311` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.3595` n `43` status `ready` deltaP `29.7925` edge `1.1128` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.6018` n `43` status `ready` deltaP `19.7674` edge `0.8931` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `8.3417` n `43` status `ready` deltaP `28.1613` edge `0.53` maxDD `-1.4744`
- `news_risk_high->index_24h` score `5.4769` n `43` status `ready` deltaP `13.6184` edge `0.4075` maxDD `-1.3507`
- `market_context_high->unknown_24h` score `5.3091` n `116` status `ready` deltaP `22.4677` edge `0.3338` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.7771` n `139` status `ready` deltaP `23.4295` edge `0.4229` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.5935` n `43` status `ready` deltaP `37.924` edge `0.0651` maxDD `-0.1442`
- `market_context_high->crypto_alt_4h` score `3.4895` n `139` status `ready` deltaP `17.8639` edge `0.4396` maxDD `-15.4319`
- `news_risk_high->commodity_4h` score `3.2765` n `43` status `ready` deltaP `30.3282` edge `0.285` maxDD `-3.0367`
- `market_context_high->crypto_major_24h` score `3.0568` n `116` status `ready` deltaP `13.7931` edge `0.6892` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.3803` n `139` status `ready` deltaP `13.0232` edge `0.1725` maxDD `-1.8773`
- `news_risk_high->fx_4h` score `2.0745` n `43` status `ready` deltaP `26.3648` edge `0.0155` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.6743` n `43` status `ready` deltaP `15.3822` edge `0.1093` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.2652` n `139` status `ready` deltaP `12.6524` edge `0.1405` maxDD `-4.2199`
- `market_context_high->index_24h` score `1.2175` n `116` status `ready` deltaP `8.6865` edge `0.0953` maxDD `-1.4737`
- `news_risk_high->unknown_1h` score `1.057` n `43` status `ready` deltaP `19.6978` edge `0.0037` maxDD `-1.7548`
- `market_context_high->index_4h` score `0.7933` n `139` status `ready` deltaP `13.5583` edge `0.0583` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `0.6987` n `139` status `ready` deltaP `7.6746` edge `0.1258` maxDD `-6.1656`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
