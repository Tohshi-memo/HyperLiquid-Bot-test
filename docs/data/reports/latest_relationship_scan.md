# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T15:52:27.707923+00:00`
- Price records: `672`
- Market context records: `2258`
- Flow alert records: `8394`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9257`

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

- `news_risk_high->crypto_alt_24h` score `22.8012` n `43` status `ready` deltaP `53.3349` edge `1.6034` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.881` n `43` status `ready` deltaP `42.9869` edge `1.0808` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.1781` n `43` status `ready` deltaP `33.9591` edge `1.0699` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `12.4739` n `43` status `ready` deltaP `23.9341` edge `0.938` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `9.6472` n `115` status `ready` deltaP `30.1932` edge `0.6438` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `9.2107` n `43` status `ready` deltaP `34.2377` edge `0.5619` maxDD `-1.4744`
- `market_context_high->crypto_alt_4h` score `8.2425` n `141` status `ready` deltaP `27.3709` edge `0.7723` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.9242` n `141` status `ready` deltaP `32.9323` edge `0.6218` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `6.3864` n `115` status `ready` deltaP `17.645` edge `1.0904` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.4033` n `141` status `ready` deltaP `21.5318` edge `0.3677` maxDD `-1.8773`
- `news_risk_high->index_24h` score `3.7626` n `43` status `ready` deltaP `12.2295` edge `0.2739` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.7585` n `43` status `ready` deltaP `32.1575` edge `0.3346` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.6507` n `43` status `ready` deltaP `37.2295` edge `0.0745` maxDD `-0.1442`
- `market_context_high->index_4h` score `3.4022` n `141` status `ready` deltaP `27.7363` edge `0.152` maxDD `-1.605`
- `market_context_high->index_24h` score `3.3729` n `115` status `ready` deltaP `14.0293` edge `0.2393` maxDD `-1.4737`
- `news_risk_high->commodity_24h` score `3.0493` n `43` status `ready` deltaP `2.2045` edge `0.3211` maxDD `-3.202`
- `market_context_high->equity_24h` score `2.8169` n `115` status `ready` deltaP `21.5021` edge `0.2441` maxDD `-6.8828`
- `market_context_high->crypto_alt_1h` score `2.3517` n `153` status `ready` deltaP `14.2969` edge `0.2194` maxDD `-6.1656`
- `market_context_high->equity_4h` score `2.2737` n `141` status `ready` deltaP `19.1133` edge `0.2025` maxDD `-5.9024`
- `news_risk_high->fx_4h` score `2.0637` n `43` status `ready` deltaP `26.3648` edge `0.0146` maxDD `-0.1382`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
