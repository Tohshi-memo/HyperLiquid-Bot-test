# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T10:22:37.621220+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4058`

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

- `market_context_high->unknown_24h` score `104.777` n `30` status `ready` deltaP `3.9931` edge `8.7048` maxDD `0.0`
- `news_risk_high->equity_24h` score `50.8053` n `50` status `ready` deltaP `54.8403` edge `3.9388` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `21.3141` n `50` status `ready` deltaP `41.5069` edge `2.5702` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `17.9776` n `30` status `ready` deltaP `13.1944` edge `1.5646` maxDD `-8.6878`
- `market_context_high->crypto_major_24h` score `12.4496` n `30` status `ready` deltaP `43.5069` edge `1.6331` maxDD `-22.8301`
- `news_risk_high->equity_4h` score `12.3955` n `50` status `ready` deltaP `39.372` edge `0.8835` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.91` n `50` status `ready` deltaP `23.8611` edge `1.562` maxDD `-29.0448`
- `news_risk_high->index_24h` score `7.4288` n `50` status `ready` deltaP `45.8125` edge `0.344` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.0654` n `50` status `ready` deltaP `40.9722` edge `0.2323` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.0985` n `50` status `ready` deltaP `45.4512` edge `0.1595` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.6496` n `50` status `ready` deltaP `27.6037` edge `0.347` maxDD `-9.4848`
- `news_risk_high->crypto_major_4h` score `4.413` n `50` status `ready` deltaP `21.6037` edge `0.3613` maxDD `-9.0062`
- `news_risk_high->equity_1h` score `3.9445` n `50` status `ready` deltaP `20.2994` edge `0.2564` maxDD `-3.7082`
- `market_context_high->metal_24h` score `3.932` n `30` status `ready` deltaP `48.2639` edge `0.2715` maxDD `-3.7989`
- `news_risk_high->commodity_4h` score `3.6602` n `50` status `ready` deltaP `34.1341` edge `0.1028` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.5765` n `50` status `ready` deltaP `24.6463` edge `0.0854` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2389` n `50` status `ready` deltaP `25.2934` edge `0.0434` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2603` n `50` status `ready` deltaP `16.7485` edge `0.0235` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `1.0535` n `50` status `ready` deltaP `19.5972` edge `0.2217` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.8637` n `50` status `ready` deltaP `18.3413` edge `0.0864` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
