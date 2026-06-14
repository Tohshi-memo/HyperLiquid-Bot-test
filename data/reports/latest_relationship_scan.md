# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T08:22:30.490721+00:00`
- Price records: `672`
- Market context records: `3874`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13658`

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

- `risk_on_high->unknown_4h` score `48.0319` n `72` status `ready` deltaP `6.9613` edge `6.3257` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `48.0319` n `72` status `ready` deltaP `6.9613` edge `6.3257` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.357` n `32` status `ready` deltaP `34.0278` edge `2.6405` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.357` n `32` status `ready` deltaP `34.0278` edge `2.6405` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.8703` n `32` status `ready` deltaP `42.0139` edge `1.9591` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.8703` n `32` status `ready` deltaP `42.0139` edge `1.9591` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.3099` n `32` status `ready` deltaP `31.25` edge `1.7493` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.3099` n `32` status `ready` deltaP `31.25` edge `1.7493` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.1448` n `32` status `ready` deltaP `30.0347` edge `0.7285` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.1448` n `32` status `ready` deltaP `30.0347` edge `0.7285` maxDD `0.0`
- `market_context_high->unknown_4h` score `7.3592` n `206` status `ready` deltaP `-0.8866` edge `1.4903` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.5052` n `142` status `ready` deltaP `17.366` edge `0.7293` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.7096` n `72` status `ready` deltaP `20.2235` edge `0.4532` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.7096` n `72` status `ready` deltaP `20.2235` edge `0.4532` maxDD `-5.9781`
- `market_context_high->index_24h` score `5.3738` n `142` status `ready` deltaP `25.1051` edge `0.3944` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.3118` n `142` status `ready` deltaP `20.7233` edge `0.281` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.5827` n `72` status `ready` deltaP `25.4065` edge `0.1593` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5827` n `72` status `ready` deltaP `25.4065` edge `0.1593` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.4188` n `142` status `ready` deltaP `4.0542` edge `0.6209` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `2.0479` n `206` status `ready` deltaP `13.9533` edge `0.2677` maxDD `-10.5381`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
