# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T03:52:28.868752+00:00`
- Price records: `672`
- Market context records: `5107`
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

- `market_context_high->unknown_24h` score `19.9575` n `77` status `ready` deltaP `28.1521` edge `1.5097` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `8.2217` n `112` status `ready` deltaP `22.9747` edge `0.6342` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `6.3889` n `124` status `ready` deltaP `4.689` edge `0.5653` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `4.9776` n `112` status `ready` deltaP `14.8519` edge `0.4757` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `2.456` n `112` status `ready` deltaP `13.2186` edge `0.456` maxDD `-14.0065`
- `market_context_high->crypto_alt_1h` score `1.235` n `124` status `ready` deltaP `8.6054` edge `0.1417` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.6688` n `124` status `ready` deltaP `9.4794` edge `0.1471` maxDD `-6.9639`
- `market_context_high->metal_1h` score `0.6467` n `124` status `ready` deltaP `10.5515` edge `0.0332` maxDD `-1.3057`
- `market_context_high->equity_1h` score `0.5858` n `124` status `ready` deltaP `10.1265` edge `0.0669` maxDD `-2.745`
- `market_context_high->equity_4h` score `0.267` n `112` status `ready` deltaP `6.8815` edge `0.1471` maxDD `-7.366`
- `market_context_high->index_1h` score `-0.0026` n `124` status `ready` deltaP `5.6452` edge `0.0124` maxDD `-1.0296`
- `market_context_high->metal_4h` score `-0.3927` n `112` status `ready` deltaP `3.8981` edge `0.0647` maxDD `-4.6157`
- `market_context_high->index_4h` score `-0.4248` n `112` status `ready` deltaP `3.5497` edge `0.0248` maxDD `-2.9012`
- `market_context_high->fx_1h` score `-0.7335` n `124` status `ready` deltaP `-4.3558` edge `-0.0009` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.8349` n `124` status `ready` deltaP `0.8402` edge `0.0006` maxDD `-2.062`
- `market_context_high->fx_4h` score `-1.0871` n `112` status `ready` deltaP `-4.6167` edge `-0.0013` maxDD `-1.9169`
- `market_context_high->commodity_24h` score `-1.344` n `77` status `ready` deltaP `8.9827` edge `0.0409` maxDD `-13.8469`
- `market_context_high->fx_24h` score `-1.5718` n `77` status `ready` deltaP `-3.4136` edge `-0.0083` maxDD `-1.6605`
- `market_context_high->commodity_4h` score `-2.157` n `112` status `ready` deltaP `1.9817` edge `-0.022` maxDD `-7.3435`
- `market_context_high->metal_24h` score `-4.2741` n `77` status `ready` deltaP `-5.984` edge `0.0113` maxDD `-31.5494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
