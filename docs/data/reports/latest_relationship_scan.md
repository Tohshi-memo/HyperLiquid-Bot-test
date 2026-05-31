# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T13:37:18.933364+00:00`
- Price records: `672`
- Market context records: `2462`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9224`

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

- `news_risk_high->crypto_alt_24h` score `21.5747` n `34` status `ready` deltaP `45.3227` edge `1.5546` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `21.3052` n `34` status `ready` deltaP `55.7394` edge `1.4478` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `18.5215` n `34` status `ready` deltaP `29.1769` edge `1.3804` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `12.373` n `34` status `ready` deltaP `22.4775` edge `0.9393` maxDD `-3.3119`
- `news_risk_high->index_24h` score `8.7537` n `34` status `ready` deltaP `27.0935` edge `0.5699` maxDD `-1.3507`
- `news_risk_high->unknown_24h` score `7.3513` n `34` status `ready` deltaP `24.3157` edge `0.4731` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.8185` n `112` status `ready` deltaP `21.8998` edge `0.3717` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `3.9835` n `136` status `ready` deltaP `20.5882` edge `0.4626` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.9405` n `136` status `ready` deltaP `18.1761` edge `0.3882` maxDD `-10.1468`
- `news_risk_high->commodity_4h` score `3.6882` n `34` status `ready` deltaP `23.7267` edge `0.2163` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.6419` n `34` status `ready` deltaP `36.5196` edge `0.0785` maxDD `-0.1442`
- `market_context_high->crypto_major_24h` score `2.4863` n `112` status `ready` deltaP `12.0783` edge `0.6275` maxDD `-25.1408`
- `news_risk_high->metal_4h` score `2.4026` n `34` status `ready` deltaP `11.3702` edge `0.3335` maxDD `-4.4354`
- `news_risk_high->fx_4h` score `1.8486` n `34` status `ready` deltaP `23.4218` edge `0.0163` maxDD `-0.1382`
- `news_risk_high->equity_4h` score `1.5581` n `34` status `ready` deltaP `-10.8411` edge `0.3612` maxDD `-3.4672`
- `news_risk_high->unknown_1h` score `1.5348` n `34` status `ready` deltaP `19.5403` edge `0.0408` maxDD `-1.4536`
- `market_context_high->unknown_4h` score `1.4357` n `136` status `ready` deltaP `9.3885` edge `0.1591` maxDD `-3.4972`
- `news_risk_high->fx_1h` score `0.9607` n `34` status `ready` deltaP `13.8077` edge `0.0136` maxDD `-0.0473`
- `market_context_high->index_24h` score `0.8886` n `112` status `ready` deltaP `5.0347` edge `0.1` maxDD `-1.0948`
- `market_context_high->crypto_major_1h` score `0.8261` n `136` status `ready` deltaP `8.9336` edge `0.1287` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
