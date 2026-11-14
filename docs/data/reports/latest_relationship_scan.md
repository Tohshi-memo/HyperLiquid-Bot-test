# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T23:52:25.813596+00:00`
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

- `market_context_high->unknown_24h` score `571.3483` n `66` status `ready` deltaP `2.6042` edge `47.595` maxDD `0.0`
- `news_risk_high->equity_24h` score `41.0154` n `53` status `ready` deltaP `44.9522` edge `3.1889` maxDD `-3.6503`
- `market_context_high->equity_24h` score `37.2618` n `66` status `ready` deltaP `39.9779` edge `2.9928` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `27.7682` n `66` status `ready` deltaP `57.7652` edge `2.0366` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `20.0942` n `53` status `ready` deltaP `43.0851` edge `2.4855` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.8425` n `53` status `ready` deltaP `38.9841` edge `0.84` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.3305` n `53` status `ready` deltaP `51.0417` edge `0.2706` maxDD `0.0`
- `market_context_high->index_24h` score `7.2368` n `66` status `ready` deltaP `42.077` edge `0.3317` maxDD `-0.0653`
- `news_risk_high->crypto_major_4h` score `5.9274` n `53` status `ready` deltaP `22.725` edge `0.4912` maxDD `-9.2335`
- `news_risk_high->index_24h` score `5.8788` n `53` status `ready` deltaP `38.332` edge `0.2647` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.4096` n `66` status `ready` deltaP `51.6888` edge `0.4381` maxDD `-3.7989`
- `news_risk_high->crypto_alt_24h` score `5.2082` n `53` status `ready` deltaP `14.4261` edge `1.0221` maxDD `-29.0448`
- `news_risk_high->metal_4h` score `5.0641` n `53` status `ready` deltaP `46.701` edge `0.1483` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.8501` n `53` status `ready` deltaP `20.8592` edge `0.2448` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.4694` n `53` status `ready` deltaP `32.1992` edge `0.0998` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `3.4192` n `53` status `ready` deltaP `28.0229` edge `0.4154` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.5474` n `53` status `ready` deltaP `26.3863` edge `0.08` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2614` n `53` status `ready` deltaP `26.0394` edge `0.0403` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.4143` n `53` status `ready` deltaP `18.8227` edge `0.0225` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `1.1935` n `53` status `ready` deltaP `20.2886` edge `0.1157` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
