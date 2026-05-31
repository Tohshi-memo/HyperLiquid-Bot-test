# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T07:37:16.080787+00:00`
- Price records: `672`
- Market context records: `2436`
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

- `news_risk_high->crypto_alt_24h` score `19.2369` n `43` status `ready` deltaP `43.2655` edge `1.3735` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.8654` n `43` status `ready` deltaP `52.3619` edge `1.267` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.8939` n `43` status `ready` deltaP `29.7925` edge `1.074` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `9.7104` n `43` status `ready` deltaP `16.9896` edge `0.754` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.3702` n `43` status `ready` deltaP `24.3419` edge `0.4745` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.6131` n `101` status `ready` deltaP `23.0525` edge `0.3469` maxDD `-1.626`
- `news_risk_high->index_24h` score `4.9699` n `43` status `ready` deltaP `8.9309` edge `0.3965` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.703` n `124` status `ready` deltaP `21.8431` edge `0.4273` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.6237` n `124` status `ready` deltaP `22.2757` edge `0.5047` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.3104` n `43` status `ready` deltaP `34.6254` edge `0.0635` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.1746` n `43` status `ready` deltaP `28.8038` edge `0.2821` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.8444` n `124` status `ready` deltaP `14.2949` edge `0.2027` maxDD `-1.8773`
- `market_context_high->index_24h` score `2.4704` n `101` status `ready` deltaP `13.0294` edge `0.1447` maxDD `-0.3888`
- `market_context_high->crypto_major_24h` score `2.1905` n `101` status `ready` deltaP `9.5984` edge `0.6061` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.0976` n `43` status `ready` deltaP `26.6697` edge `0.0154` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.9147` n `43` status `ready` deltaP `16.6017` edge `0.1212` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.1635` n `125` status `ready` deltaP `11.006` edge `0.143` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.1301` n `43` status `ready` deltaP `20.596` edge `0.0038` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `0.9066` n `125` status `ready` deltaP `8.2036` edge `0.1396` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.5343` n `124` status `ready` deltaP `12.4508` edge `0.0441` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
