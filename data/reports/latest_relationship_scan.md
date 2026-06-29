# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T04:07:27.587036+00:00`
- Price records: `672`
- Market context records: `5108`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10340`

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

- `market_context_high->unknown_24h` score `20.504` n `76` status `ready` deltaP `28.189` edge `1.555` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `8.2193` n `112` status `ready` deltaP `22.9747` edge `0.634` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `7.1303` n `124` status `ready` deltaP `5.3458` edge `0.6227` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `5.064` n `112` status `ready` deltaP `14.8519` edge `0.4829` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `2.4732` n `112` status `ready` deltaP `13.2186` edge `0.4582` maxDD `-14.0065`
- `market_context_high->crypto_alt_1h` score `1.1644` n `124` status `ready` deltaP `7.9486` edge `0.1402` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.605` n `124` status `ready` deltaP `8.8227` edge `0.1433` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.5501` n `124` status `ready` deltaP `9.4698` edge `0.0667` maxDD `-2.745`
- `market_context_high->metal_1h` score `0.3831` n `124` status `ready` deltaP `9.8947` edge `0.0328` maxDD `-1.3057`
- `market_context_high->equity_4h` score `0.1706` n `112` status `ready` deltaP `6.1411` edge `0.1448` maxDD `-7.4425`
- `market_context_high->index_1h` score `0.0331` n `124` status `ready` deltaP `6.3019` edge `0.0126` maxDD `-1.0296`
- `market_context_high->metal_4h` score `-0.3973` n `112` status `ready` deltaP `3.8981` edge `0.0641` maxDD `-4.6157`
- `market_context_high->index_4h` score `-0.4619` n `112` status `ready` deltaP `3.5497` edge `0.0246` maxDD `-2.9316`
- `market_context_high->fx_1h` score `-0.7327` n `124` status `ready` deltaP `-4.3558` edge `-0.0008` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.7775` n `124` status `ready` deltaP `1.497` edge `0.001` maxDD `-2.062`
- `market_context_high->fx_4h` score `-1.0424` n `112` status `ready` deltaP `-3.8763` edge `-0.0005` maxDD `-1.9169`
- `market_context_high->commodity_24h` score `-1.1798` n `76` status `ready` deltaP `9.6491` edge `0.0465` maxDD `-13.2998`
- `market_context_high->fx_24h` score `-1.5315` n `76` status `ready` deltaP `-3.0063` edge `-0.0082` maxDD `-1.6175`
- `market_context_high->commodity_4h` score `-2.169` n `112` status `ready` deltaP `1.9817` edge `-0.023` maxDD `-7.3435`
- `market_context_high->metal_24h` score `-4.1171` n `76` status `ready` deltaP `-5.5739` edge `0.0156` maxDD `-30.8351`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
