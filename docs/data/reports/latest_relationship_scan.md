# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T05:37:27.220865+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5111`

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

- `market_context_high->unknown_24h` score `6700.7767` n `38` status `ready` deltaP `1.3889` edge `558.3888` maxDD `0.0`
- `market_context_high->unknown_4h` score `525.6933` n `42` status `ready` deltaP `9.1463` edge `43.7468` maxDD `0.0`
- `market_context_high->unknown_1h` score `111.1779` n `43` status `ready` deltaP `6.2666` edge `9.2341` maxDD `-0.2178`
- `market_context_high->equity_24h` score `19.1173` n `38` status `ready` deltaP `41.9865` edge `1.3368` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.9042` n `94` status `ready` deltaP `34.2605` edge `1.0659` maxDD `-6.8493`
- `market_context_high->commodity_24h` score `7.1081` n `38` status `ready` deltaP `43.7591` edge `0.3317` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.663` n `42` status `ready` deltaP `29.007` edge `0.3913` maxDD `-1.6876`
- `market_context_high->index_24h` score `6.6414` n `38` status `ready` deltaP `49.1319` edge `0.2259` maxDD `0.0`
- `market_context_high->equity_4h` score `5.476` n `42` status `ready` deltaP `12.246` edge `0.4449` maxDD `-2.283`
- `market_context_high->crypto_major_4h` score `5.271` n `42` status `ready` deltaP `27.4463` edge `0.2899` maxDD `-1.6901`
- `market_context_high->commodity_4h` score `2.424` n `42` status `ready` deltaP `26.8003` edge `0.0569` maxDD `-1.3523`
- `market_context_high->equity_1h` score `2.3389` n `43` status `ready` deltaP `5.5146` edge `0.1982` maxDD `-1.2043`
- `news_risk_high->crypto_alt_4h` score `2.282` n `126` status `ready` deltaP `9.1657` edge `0.2677` maxDD `-7.4246`
- `market_context_high->metal_4h` score `1.9081` n `42` status `ready` deltaP `22.1545` edge `0.0538` maxDD `-0.7323`
- `market_context_high->crypto_alt_24h` score `1.8155` n `38` status `ready` deltaP `-7.1729` edge `0.3509` maxDD `-8.8096`
- `market_context_high->crypto_alt_1h` score `1.521` n `43` status `ready` deltaP `3.7878` edge `0.1475` maxDD `-1.6799`
- `market_context_high->crypto_major_1h` score `1.3608` n `43` status `ready` deltaP `5.5146` edge `0.1173` maxDD `-1.2532`
- `market_context_high->index_4h` score `0.8703` n `42` status `ready` deltaP `12.7033` edge `0.0331` maxDD `-1.2876`
- `market_context_high->metal_1h` score `0.7057` n `43` status `ready` deltaP `9.7062` edge `0.0198` maxDD `-0.3895`
- `market_context_high->fx_1h` score `0.5896` n `43` status `ready` deltaP `12.641` edge `0.0089` maxDD `-0.0736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
