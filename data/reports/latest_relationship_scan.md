# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T07:22:19.838992+00:00`
- Price records: `672`
- Market context records: `2435`
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

- `news_risk_high->crypto_alt_24h` score `19.2345` n `43` status `ready` deltaP `43.2655` edge `1.3733` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.8383` n `43` status `ready` deltaP `52.1883` edge `1.2659` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.9083` n `43` status `ready` deltaP `29.7925` edge `1.0752` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `9.7308` n `43` status `ready` deltaP `16.9896` edge `0.7557` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.4009` n `43` status `ready` deltaP `24.5155` edge `0.4759` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.6438` n `101` status `ready` deltaP `23.2261` edge `0.3483` maxDD `-1.626`
- `news_risk_high->index_24h` score `4.9711` n `43` status `ready` deltaP `8.9309` edge `0.3966` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.6668` n `124` status `ready` deltaP `21.6906` edge `0.4253` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.5935` n `124` status `ready` deltaP `22.1233` edge `0.5032` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.3279` n `43` status `ready` deltaP `34.799` edge `0.0638` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.1746` n `43` status `ready` deltaP `28.8038` edge `0.2821` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.8058` n `124` status `ready` deltaP `14.1424` edge `0.2005` maxDD `-1.8773`
- `market_context_high->index_24h` score `2.4716` n `101` status `ready` deltaP `13.0294` edge `0.1448` maxDD `-0.3888`
- `market_context_high->crypto_major_24h` score `2.2037` n `101` status `ready` deltaP `9.5984` edge `0.6078` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.1098` n `43` status `ready` deltaP `26.8221` edge `0.0154` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.8761` n `43` status `ready` deltaP `16.4492` edge `0.119` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.2456` n `124` status `ready` deltaP `11.3724` edge `0.1474` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.0989` n `43` status `ready` deltaP `20.4463` edge `0.0022` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.0078` n `124` status `ready` deltaP `8.6875` edge `0.1448` maxDD `-6.1656`
- `news_risk_high->commodity_1h` score `0.5219` n `43` status `ready` deltaP `8.9681` edge `0.0751` maxDD `-2.1052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
