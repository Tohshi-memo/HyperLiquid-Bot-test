# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T22:52:30.114847+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10332`

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

- `market_context_high->unknown_24h` score `377.9549` n `75` status `ready` deltaP `2.1944` edge `31.4957` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `34.8894` n `53` status `ready` deltaP `34.3619` edge `2.749` maxDD `-3.6503`
- `market_context_high->equity_24h` score `26.6557` n `75` status `ready` deltaP `28.9027` edge `2.1828` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.8702` n `75` status `ready` deltaP `47.5834` edge `1.3401` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.6728` n `53` status `ready` deltaP `42.0434` edge `1.7974` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.8998` n `53` status `ready` deltaP `34.7158` edge `0.7899` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.9798` n `53` status `ready` deltaP `39.0625` edge `0.2379` maxDD `0.0`
- `market_context_high->index_24h` score `5.1907` n `75` status `ready` deltaP `28.8611` edge `0.2493` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.9979` n `53` status `ready` deltaP `47.4632` edge `0.1377` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.5097` n `53` status `ready` deltaP `26.8736` edge `0.227` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.1067` n `75` status `ready` deltaP `41.3334` edge `0.3401` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.5181` n `53` status `ready` deltaP `18.3143` edge `0.2341` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.2829` n `53` status `ready` deltaP `20.1335` edge `0.2881` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.2513` n `53` status `ready` deltaP `29.6077` edge `0.0989` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2901` n `53` status `ready` deltaP `26.7879` edge `0.0377` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.8874` n `53` status `ready` deltaP `18.9168` edge `0.0748` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.7619` n `53` status `ready` deltaP `25.4314` edge `0.2202` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.7598` n `53` status `ready` deltaP `14.4261` edge `0.58` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.1616` n `53` status `ready` deltaP `15.8287` edge `0.0214` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6447` n `53` status `ready` deltaP `16.9952` edge `0.0673` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
