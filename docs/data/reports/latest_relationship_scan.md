# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T08:07:28.635376+00:00`
- Price records: `672`
- Market context records: `3770`
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

- `risk_on_high->crypto_major_24h` score `29.6138` n `32` status `ready` deltaP `31.4236` edge `2.2626` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `29.6138` n `32` status `ready` deltaP `31.4236` edge `2.2626` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `23.8066` n `32` status `ready` deltaP `37.1528` edge `1.7362` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `23.8066` n `32` status `ready` deltaP `37.1528` edge `1.7362` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `22.3623` n `32` status `ready` deltaP `31.9444` edge `1.6657` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `22.3623` n `32` status `ready` deltaP `31.9444` edge `1.6657` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.5012` n `32` status `ready` deltaP `31.25` edge `0.7501` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.5012` n `32` status `ready` deltaP `31.25` edge `0.7501` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.3233` n `32` status `ready` deltaP `18.75` edge `0.8475` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.3233` n `32` status `ready` deltaP `18.75` edge `0.8475` maxDD `-5.9781`
- `market_context_high->equity_24h` score `5.8571` n `157` status `ready` deltaP `17.4076` edge `0.6468` maxDD `-13.6477`
- `market_context_high->index_24h` score `5.3311` n `157` status `ready` deltaP `26.7914` edge `0.3796` maxDD `-7.1159`
- `market_context_high->metal_24h` score `4.4001` n `157` status `ready` deltaP `26.8412` edge `0.3309` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `4.3652` n `157` status `ready` deltaP `7.1601` edge `0.7624` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.9647` n `161` status `ready` deltaP `9.6273` edge `0.2896` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.4268` n `32` status `ready` deltaP `8.1555` edge `0.242` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.4268` n `32` status `ready` deltaP `8.1555` edge `0.242` maxDD `-5.7426`
- `risk_on_high->metal_24h` score `1.3046` n `32` status `ready` deltaP `14.0625` edge `0.0411` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.3046` n `32` status `ready` deltaP `14.0625` edge `0.0411` maxDD `-0.7574`
- `risk_on_high->crypto_alt_4h` score `1.2189` n `32` status `ready` deltaP `-1.9055` edge `0.2987` maxDD `-11.7537`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
