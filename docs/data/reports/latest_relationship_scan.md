# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T08:22:20.685876+00:00`
- Price records: `672`
- Market context records: `2439`
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

- `news_risk_high->crypto_alt_24h` score `19.2441` n `43` status `ready` deltaP `43.2655` edge `1.3741` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.9323` n `43` status `ready` deltaP `52.8827` edge `1.2691` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.8519` n `43` status `ready` deltaP `29.7925` edge `1.0705` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `9.636` n `43` status `ready` deltaP `16.9896` edge `0.7478` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.2584` n `43` status `ready` deltaP `23.9946` edge `0.4675` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.5013` n `101` status `ready` deltaP `22.7052` edge `0.3399` maxDD `-1.626`
- `news_risk_high->index_24h` score `4.9639` n `43` status `ready` deltaP `8.9309` edge `0.396` maxDD `-1.3507`
- `market_context_high->crypto_major_4h` score `4.8212` n `124` status `ready` deltaP `22.3004` edge `0.4341` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `4.7203` n `124` status `ready` deltaP `22.733` edge `0.5097` maxDD `-15.4319`
- `news_risk_high->fx_24h` score `3.2627` n `43` status `ready` deltaP `34.1045` edge `0.063` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.1754` n `43` status `ready` deltaP `28.8038` edge `0.2822` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.8188` n `124` status `ready` deltaP `13.99` edge `0.2026` maxDD `-1.8773`
- `market_context_high->index_24h` score `2.4644` n `101` status `ready` deltaP `13.0294` edge `0.1442` maxDD `-0.3888`
- `market_context_high->crypto_major_24h` score `2.1421` n `101` status `ready` deltaP `9.5984` edge `0.5999` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.122` n `43` status `ready` deltaP `26.9746` edge `0.0154` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.8891` n `43` status `ready` deltaP `16.2968` edge `0.1211` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.1433` n `43` status `ready` deltaP `20.596` edge `0.0049` maxDD `-1.7548`
- `market_context_high->crypto_major_1h` score `1.0555` n `128` status `ready` deltaP `10.5866` edge `0.1368` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.799` n `128` status `ready` deltaP `7.878` edge `0.1328` maxDD `-6.1656`
- `market_context_high->index_4h` score `0.5465` n `124` status `ready` deltaP `12.6033` edge `0.0441` maxDD `-2.2732`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
