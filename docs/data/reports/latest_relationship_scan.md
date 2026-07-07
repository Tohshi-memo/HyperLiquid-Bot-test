# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T14:37:34.364462+00:00`
- Price records: `672`
- Market context records: `5990`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11236`

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

- `news_risk_high->fx_24h` score `7.51` n `30` status `ready` deltaP `68.75` edge `0.1675` maxDD `0.0`
- `news_risk_high->commodity_24h` score `4.4552` n `30` status `ready` deltaP `33.5417` edge `0.1682` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `4.1543` n `30` status `ready` deltaP `43.0488` edge `0.0638` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2418` n `30` status `ready` deltaP `26.9261` edge `0.0212` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.0913` n `231` status `ready` deltaP `7.5573` edge `0.15` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.785` n `30` status `ready` deltaP `9.8902` edge `0.0814` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.1795` n `30` status `ready` deltaP `5.1697` edge `0.0347` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.082` n `30` status `ready` deltaP `9.2361` edge `0.0361` maxDD `-2.3058`
- `market_context_high->equity_1h` score `-0.3945` n `231` status `ready` deltaP `3.9992` edge `0.0356` maxDD `-4.3608`
- `news_risk_high->metal_1h` score `-0.4126` n `30` status `ready` deltaP `1.5369` edge `-0.0265` maxDD `-1.2643`
- `market_context_high->commodity_1h` score `-0.4222` n `231` status `ready` deltaP `-0.9164` edge `0.0019` maxDD `-0.9933`
- `market_context_high->metal_1h` score `-0.5368` n `231` status `ready` deltaP `1.8833` edge `-0.0015` maxDD `-2.0564`
- `market_context_high->equity_24h` score `-0.6835` n `204` status `ready` deltaP `22.0997` edge `0.3325` maxDD `-31.2762`
- `market_context_high->fx_1h` score `-0.7873` n `231` status `ready` deltaP `-1.8185` edge `-0.0018` maxDD `-0.8015`
- `news_risk_high->index_1h` score `-1.0454` n `30` status `ready` deltaP `-9.5509` edge `-0.0189` maxDD `-1.1161`
- `market_context_high->crypto_major_1h` score `-1.0784` n `231` status `ready` deltaP `2.834` edge `0.0196` maxDD `-9.807`
- `market_context_high->index_1h` score `-1.1407` n `231` status `ready` deltaP `-1.0661` edge `0.0034` maxDD `-1.3078`
- `market_context_high->commodity_4h` score `-1.153` n `231` status `ready` deltaP `-0.3564` edge `-0.001` maxDD `-4.2224`
- `market_context_high->crypto_alt_1h` score `-1.1777` n `231` status `ready` deltaP `1.7498` edge `0.0126` maxDD `-9.3536`
- `market_context_high->index_4h` score `-1.1893` n `231` status `ready` deltaP `0.1432` edge `0.0153` maxDD `-3.165`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
