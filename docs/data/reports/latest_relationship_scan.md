# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T00:22:25.152300+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9354`

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

- `market_context_high->unknown_24h` score `569.4187` n `66` status `ready` deltaP `2.6042` edge `47.4342` maxDD `0.0`
- `news_risk_high->equity_24h` score `41.061` n `53` status `ready` deltaP `44.9522` edge `3.1927` maxDD `-3.6503`
- `market_context_high->equity_24h` score `37.3074` n `66` status `ready` deltaP `39.9779` edge `2.9966` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `28.001` n `66` status `ready` deltaP `57.7652` edge `2.056` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `20.2642` n `53` status `ready` deltaP `43.0851` edge `2.5073` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.8789` n `53` status `ready` deltaP `39.289` edge `0.841` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.298` n `53` status `ready` deltaP `50.6944` edge `0.2702` maxDD `0.0`
- `market_context_high->index_24h` score `7.2416` n `66` status `ready` deltaP `42.077` edge `0.3321` maxDD `-0.0653`
- `news_risk_high->crypto_major_4h` score `6.02` n `53` status `ready` deltaP `22.8774` edge `0.4979` maxDD `-9.2335`
- `news_risk_high->index_24h` score `5.8836` n `53` status `ready` deltaP `38.332` edge `0.2651` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.4409` n `66` status `ready` deltaP `52.036` edge `0.4398` maxDD `-3.7989`
- `news_risk_high->crypto_alt_24h` score `5.3595` n `53` status `ready` deltaP `14.4261` edge `1.0415` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `5.0701` n `53` status `ready` deltaP `46.701` edge `0.1488` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.8405` n `53` status `ready` deltaP `20.8592` edge `0.244` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.4402` n `53` status `ready` deltaP `31.8943` edge `0.0994` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `3.4356` n `53` status `ready` deltaP `28.0229` edge `0.4175` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.5474` n `53` status `ready` deltaP `26.3863` edge `0.08` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2614` n `53` status `ready` deltaP `26.0394` edge `0.0403` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4143` n `53` status `ready` deltaP `18.8227` edge `0.0225` maxDD `-0.4103`
- `market_context_high->crypto_major_24h` score `1.1761` n `66` status `ready` deltaP `12.6105` edge `1.0465` maxDD `-76.2717`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
