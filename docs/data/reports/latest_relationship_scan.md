# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T02:56:00.864127+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9342`

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

- `market_context_high->unknown_24h` score `559.752` n `66` status `ready` deltaP `2.4306` edge `46.6298` maxDD `0.0`
- `news_risk_high->equity_24h` score `41.282` n `53` status `ready` deltaP `45.2994` edge `3.2088` maxDD `-3.6503`
- `market_context_high->equity_24h` score `37.5283` n `66` status `ready` deltaP `40.3251` edge `3.0127` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `29.1134` n `66` status `ready` deltaP `57.7652` edge `2.1487` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `20.9779` n `53` status `ready` deltaP `43.0851` edge `2.5988` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.8487` n `53` status `ready` deltaP `39.1365` edge `0.8395` maxDD `-7.0416`
- `market_context_high->index_24h` score `7.2813` n `66` status `ready` deltaP `42.4242` edge `0.3331` maxDD `-0.0653`
- `news_risk_high->commodity_24h` score `7.2443` n `53` status `ready` deltaP `50.1736` edge `0.2692` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.0825` n `53` status `ready` deltaP `14.4261` edge `1.1342` maxDD `-29.0448`
- `news_risk_high->crypto_major_4h` score `5.9812` n `53` status `ready` deltaP `22.5725` edge `0.4967` maxDD `-9.2335`
- `news_risk_high->index_24h` score `5.9234` n `53` status `ready` deltaP `38.6792` edge `0.2661` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.6345` n `66` status `ready` deltaP `53.5985` edge `0.4542` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `5.0395` n `53` status `ready` deltaP `46.2437` edge `0.1493` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.7662` n `53` status `ready` deltaP `20.2604` edge `0.2418` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.388` n `53` status `ready` deltaP `31.437` edge `0.0981` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `3.2555` n `53` status `ready` deltaP `27.2607` edge `0.3995` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.4706` n `53` status `ready` deltaP `25.4717` edge `0.0797` maxDD `-0.8235`
- `market_context_high->crypto_major_24h` score `2.2741` n `66` status `ready` deltaP `12.6105` edge `1.138` maxDD `-76.2717`
- `news_risk_high->metal_1h` score `2.2398` n `53` status `ready` deltaP `25.74` edge `0.0405` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3771` n `53` status `ready` deltaP `18.3736` edge `0.0224` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
