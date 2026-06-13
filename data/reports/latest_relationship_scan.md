# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T23:37:47.323082+00:00`
- Price records: `672`
- Market context records: `3838`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13787`

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

- `risk_on_high->crypto_major_24h` score `33.1102` n `32` status `ready` deltaP `34.0278` edge `2.5366` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `33.1102` n `32` status `ready` deltaP `34.0278` edge `2.5366` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.4251` n `32` status `ready` deltaP `42.0139` edge `1.922` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.4251` n `32` status `ready` deltaP `42.0139` edge `1.922` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.5911` n `32` status `ready` deltaP `31.9444` edge `1.7681` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.5911` n `32` status `ready` deltaP `31.9444` edge `1.7681` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.2588` n `32` status `ready` deltaP `31.25` edge `0.7299` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.2588` n `32` status `ready` deltaP `31.25` edge `0.7299` maxDD `0.0`
- `market_context_high->equity_24h` score `6.519` n `132` status `ready` deltaP `15.4987` edge `0.7429` maxDD `-14.5715`
- `market_context_high->index_24h` score `5.9248` n `132` status `ready` deltaP `25.947` edge `0.4347` maxDD `-7.1159`
- `risk_on_high->crypto_major_4h` score `5.5722` n `53` status `ready` deltaP `12.8365` edge `0.491` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.5722` n `53` status `ready` deltaP `12.8365` edge `0.491` maxDD `-5.9781`
- `market_context_high->unknown_24h` score `4.9094` n `132` status `ready` deltaP `-18.4817` edge `3.847` maxDD `-218.5504`
- `market_context_high->metal_24h` score `4.0928` n `132` status `ready` deltaP `23.69` edge `0.3263` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.6401` n `53` status `ready` deltaP `21.6233` edge `0.1893` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6401` n `53` status `ready` deltaP `21.6233` edge `0.1893` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.0646` n `132` status `ready` deltaP `1.5467` edge `0.6081` maxDD `-31.0425`
- `risk_on_high->metal_24h` score `1.396` n `32` status `ready` deltaP `14.4097` edge `0.0464` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.396` n `32` status `ready` deltaP `14.4097` edge `0.0464` maxDD `-0.7574`
- `market_context_high->crypto_major_4h` score `1.3813` n `191` status `ready` deltaP `10.1496` edge `0.2375` maxDD `-10.5381`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
