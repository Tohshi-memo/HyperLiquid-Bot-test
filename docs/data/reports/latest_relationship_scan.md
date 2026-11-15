# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T20:37:26.133366+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8260`

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

- `market_context_high->unknown_24h` score `655.9533` n `56` status `ready` deltaP `3.9861` edge `54.6362` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.0641` n `50` status `ready` deltaP `50.565` edge `3.5722` maxDD `-3.6503`
- `market_context_high->equity_24h` score `41.0458` n `56` status `ready` deltaP `44.7079` edge `3.2766` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `34.448` n `56` status `ready` deltaP `62.3174` edge `2.5629` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `22.9186` n `50` status `ready` deltaP `45.3484` edge `2.7503` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.9592` n `50` status `ready` deltaP `37.8476` edge `0.8573` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `10.2428` n `56` status `ready` deltaP `15.9198` edge `1.4046` maxDD `-47.9068`
- `news_risk_high->crypto_alt_24h` score `9.5019` n `50` status `ready` deltaP `20.6031` edge `1.5314` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.149` n `56` status `ready` deltaP `48.889` edge `0.3618` maxDD `-0.0251`
- `news_risk_high->index_24h` score `6.6443` n `50` status `ready` deltaP `42.2461` edge `0.3024` maxDD `-0.4279`
- `market_context_high->metal_24h` score `6.5631` n `56` status `ready` deltaP `62.9055` edge `0.5112` maxDD `-3.7989`
- `news_risk_high->commodity_24h` score `6.4556` n `50` status `ready` deltaP `42.1144` edge `0.2572` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `4.9318` n `50` status `ready` deltaP `21.9085` edge `0.4025` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `4.8688` n `50` status `ready` deltaP `44.0793` edge `0.1495` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.3518` n `50` status `ready` deltaP `26.5366` edge `0.3293` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9588` n `50` status `ready` deltaP `21.1976` edge `0.2516` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6734` n `50` status `ready` deltaP `34.1341` edge `0.1039` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4759` n `50` status `ready` deltaP `23.8841` edge `0.0821` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1586` n `50` status `ready` deltaP `24.6946` edge `0.0407` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2795` n `50` status `ready` deltaP `17.0479` edge `0.0231` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
