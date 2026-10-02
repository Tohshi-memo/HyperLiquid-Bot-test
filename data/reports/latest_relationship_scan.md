# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T13:22:32.540918+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4842`

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

- `market_context_high->unknown_1h` score `362.2341` n `50` status `ready` deltaP `11.1737` edge `30.1166` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.5802` n `50` status `ready` deltaP `11.128` edge `24.3075` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.354` n `73` status `ready` deltaP `39.795` edge `1.0351` maxDD `-1.005`
- `news_risk_high->equity_24h` score `9.8068` n `73` status `ready` deltaP `34.1419` edge `0.6381` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.5768` n `50` status `ready` deltaP `33.3889` edge `0.7171` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `9.0287` n `50` status `ready` deltaP `16.5347` edge `0.8125` maxDD `-11.6271`
- `market_context_high->crypto_major_4h` score `6.5668` n `50` status `ready` deltaP `15.8659` edge `0.5118` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.6052` n `50` status `ready` deltaP `13.9024` edge `0.42` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `4.3102` n `113` status `ready` deltaP `19.1236` edge `0.3661` maxDD `-6.4195`
- `market_context_high->fx_4h` score `2.9564` n `50` status `ready` deltaP `32.9939` edge `0.0399` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.8307` n `50` status `ready` deltaP `13.6048` edge `0.2115` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.8117` n `50` status `ready` deltaP `13.5509` edge `0.189` maxDD `-2.2692`
- `news_risk_high->equity_4h` score `2.3187` n `113` status `ready` deltaP `22.1132` edge `0.1154` maxDD `-2.9013`
- `market_context_high->equity_24h` score `2.201` n `50` status `ready` deltaP `10.3611` edge `0.3993` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `1.8897` n `73` status `ready` deltaP `7.5533` edge `0.5073` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.5023` n `50` status `ready` deltaP `20.9401` edge `0.012` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.2393` n `73` status `ready` deltaP `11.9673` edge `0.2065` maxDD `-2.192`
- `news_risk_high->crypto_major_4h` score `0.8865` n `113` status `ready` deltaP `12.4677` edge `0.2615` maxDD `-10.477`
- `market_context_high->index_24h` score `0.8503` n `50` status `ready` deltaP `14.4444` edge `0.0698` maxDD `-1.2338`
- `news_risk_high->index_24h` score `0.7509` n `73` status `ready` deltaP `14.3074` edge `0.0487` maxDD `-0.4916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
