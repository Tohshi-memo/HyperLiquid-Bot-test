# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T06:52:34.022372+00:00`
- Price records: `672`
- Market context records: `3765`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13073`

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

- `risk_on_high->crypto_major_24h` score `29.471` n `32` status `ready` deltaP `31.4236` edge `2.2507` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `29.471` n `32` status `ready` deltaP `31.4236` edge `2.2507` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `23.5707` n `32` status `ready` deltaP `36.9792` edge `1.7177` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `23.5707` n `32` status `ready` deltaP `36.9792` edge `1.7177` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `22.2087` n `32` status `ready` deltaP `31.9444` edge `1.6529` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `22.2087` n `32` status `ready` deltaP `31.9444` edge `1.6529` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.5036` n `32` status `ready` deltaP `31.25` edge `0.7503` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.5036` n `32` status `ready` deltaP `31.25` edge `0.7503` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.4489` n `32` status `ready` deltaP `19.3598` edge `0.8539` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.4489` n `32` status `ready` deltaP `19.3598` edge `0.8539` maxDD `-5.9781`
- `market_context_high->equity_24h` score `5.7032` n `158` status `ready` deltaP `17.3589` edge `0.6343` maxDD `-13.6477`
- `market_context_high->index_24h` score `5.3646` n `158` status `ready` deltaP `26.8196` edge `0.3822` maxDD `-7.1159`
- `market_context_high->metal_24h` score `4.4718` n `158` status `ready` deltaP `26.9581` edge `0.3361` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `4.3287` n `158` status `ready` deltaP `7.3334` edge `0.7582` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.9732` n `162` status `ready` deltaP `9.8691` edge `0.2887` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.4095` n `32` status `ready` deltaP `8.003` edge `0.2408` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.4095` n `32` status `ready` deltaP `8.003` edge `0.2408` maxDD `-5.7426`
- `risk_on_high->metal_24h` score `1.3442` n `32` status `ready` deltaP `14.0625` edge `0.0444` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.3442` n `32` status `ready` deltaP `14.0625` edge `0.0444` maxDD `-0.7574`
- `risk_on_high->crypto_alt_4h` score `1.3311` n `32` status `ready` deltaP `-1.4482` edge `0.305` maxDD `-11.7537`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
