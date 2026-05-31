# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T07:07:21.116704+00:00`
- Price records: `672`
- Market context records: `2434`
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

- `news_risk_high->crypto_alt_24h` score `19.2616` n `43` status `ready` deltaP `43.4391` edge `1.3744` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.8112` n `43` status `ready` deltaP `52.0147` edge `1.2648` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.9203` n `43` status `ready` deltaP `29.7925` edge `1.0762` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `9.7548` n `43` status `ready` deltaP `16.9896` edge `0.7577` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.4328` n `43` status `ready` deltaP `24.6891` edge `0.4774` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.6757` n `101` status `ready` deltaP `23.3997` edge `0.3498` maxDD `-1.626`
- `news_risk_high->index_24h` score `4.9699` n `43` status `ready` deltaP `8.9309` edge `0.3965` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.6354` n `124` status `ready` deltaP `21.5382` edge `0.4237` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.5887` n `124` status `ready` deltaP `22.1233` edge `0.5028` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.3454` n `43` status `ready` deltaP `34.9726` edge `0.0641` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.1738` n `43` status `ready` deltaP `28.8038` edge `0.282` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.7708` n `124` status `ready` deltaP `13.99` edge `0.1986` maxDD `-1.8773`
- `market_context_high->index_24h` score `2.4704` n `101` status `ready` deltaP `13.0294` edge `0.1447` maxDD `-0.3888`
- `market_context_high->crypto_major_24h` score `2.2193` n `101` status `ready` deltaP `9.5984` edge `0.6098` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.1232` n `43` status `ready` deltaP `26.9746` edge `0.0155` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.8411` n `43` status `ready` deltaP `16.2968` edge `0.1171` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.2216` n `124` status `ready` deltaP `11.2227` edge `0.1464` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.0941` n `43` status `ready` deltaP `20.4463` edge `0.0018` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.0078` n `124` status `ready` deltaP `8.6875` edge `0.1448` maxDD `-6.1656`
- `news_risk_high->commodity_1h` score `0.5226` n `43` status `ready` deltaP `8.9681` edge `0.0752` maxDD `-2.1052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
