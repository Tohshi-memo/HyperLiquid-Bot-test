# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T08:37:23.129826+00:00`
- Price records: `672`
- Market context records: `2440`
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

- `news_risk_high->crypto_alt_24h` score `19.2477` n `43` status `ready` deltaP `43.2655` edge `1.3744` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.9347` n `43` status `ready` deltaP `52.8827` edge `1.2693` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.8363` n `43` status `ready` deltaP `29.7925` edge `1.0692` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `9.612` n `43` status `ready` deltaP `16.9896` edge `0.7458` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.2025` n `43` status `ready` deltaP `23.821` edge `0.464` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.5677` n `102` status `ready` deltaP `22.5898` edge `0.3462` maxDD `-1.626`
- `news_risk_high->index_24h` score `4.9615` n `43` status `ready` deltaP `8.9309` edge `0.3958` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.8574` n `124` status `ready` deltaP `22.4528` edge `0.4361` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.7481` n `124` status `ready` deltaP `22.8855` edge `0.511` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.244` n `43` status `ready` deltaP `33.9309` edge `0.0626` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.1785` n `43` status `ready` deltaP `28.8038` edge `0.2826` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.7766` n `124` status `ready` deltaP `13.8376` edge `0.2001` maxDD `-1.8773`
- `market_context_high->index_24h` score `2.3524` n `102` status `ready` deltaP `12.214` edge `0.1403` maxDD `-0.3888`
- `market_context_high->crypto_major_24h` score `2.2182` n `102` status `ready` deltaP `9.9673` edge `0.6072` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.122` n `43` status `ready` deltaP `26.9746` edge `0.0154` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.8469` n `43` status `ready` deltaP `16.1444` edge `0.1186` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.1109` n `43` status `ready` deltaP `20.4463` edge `0.0032` maxDD `-1.7548`
- `market_context_high->crypto_major_1h` score `1.0795` n `129` status `ready` deltaP `10.8713` edge `0.1369` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.8386` n `129` status `ready` deltaP `8.1929` edge `0.134` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.5477` n `124` status `ready` deltaP `12.6033` edge `0.0442` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
