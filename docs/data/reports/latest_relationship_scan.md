# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T10:37:18.652894+00:00`
- Price records: `672`
- Market context records: `2236`
- Flow alert records: `8331`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9203`

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

- `news_risk_high->crypto_alt_24h` score `25.3296` n `34` status `ready` deltaP `55.7495` edge `1.798` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `14.645` n `34` status `ready` deltaP `46.0171` edge `0.9576` maxDD `-3.1836`
- `market_context_high->crypto_alt_4h` score `12.9979` n `131` status `ready` deltaP `37.1695` edge `0.929` maxDD `-5.1574`
- `news_risk_high->equity_24h` score `12.7529` n `34` status `ready` deltaP `36.9894` edge `0.8476` maxDD `-2.1831`
- `market_context_high->crypto_major_4h` score `11.7519` n `131` status `ready` deltaP `42.2129` edge `0.7509` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `9.189` n `34` status `ready` deltaP `36.6523` edge `0.544` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `7.5289` n `34` status `ready` deltaP `19.5772` edge `0.8928` maxDD `-3.3119`
- `market_context_high->unknown_4h` score `6.0721` n `131` status `ready` deltaP `23.8934` edge `0.3921` maxDD `-1.6306`
- `market_context_high->unknown_24h` score `4.6531` n `126` status `ready` deltaP `25.868` edge `0.5216` maxDD `-20.8368`
- `market_context_high->equity_4h` score `4.3749` n `131` status `ready` deltaP `24.3705` edge `0.248` maxDD `-1.6716`
- `news_risk_high->commodity_4h` score `3.9615` n `43` status `ready` deltaP `33.377` edge `0.3525` maxDD `-3.0367`
- `market_context_high->index_4h` score `3.7705` n `131` status `ready` deltaP `28.4863` edge `0.1656` maxDD `-0.6372`
- `news_risk_high->fx_24h` score `3.0582` n `34` status `ready` deltaP `31.8627` edge `0.0609` maxDD `-0.1442`
- `market_context_high->crypto_major_1h` score `2.9814` n `143` status `ready` deltaP `16.2839` edge `0.1876` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `2.7915` n `143` status `ready` deltaP `15.7343` edge `0.2141` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `2.7409` n `126` status `ready` deltaP `15.749` edge `0.8717` maxDD `-44.0238`
- `news_risk_high->commodity_24h` score `2.4592` n `34` status `ready` deltaP `-1.0315` edge `0.2935` maxDD `-3.202`
- `market_context_high->index_24h` score `2.3714` n `126` status `ready` deltaP `10.4414` edge `0.21` maxDD `-2.8927`
- `news_risk_high->fx_4h` score `2.15` n `43` status `ready` deltaP `27.2794` edge `0.0157` maxDD `-0.1382`
- `news_risk_high->index_24h` score `1.5763` n `34` status `ready` deltaP `10.1613` edge `0.1055` maxDD `-1.3507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
