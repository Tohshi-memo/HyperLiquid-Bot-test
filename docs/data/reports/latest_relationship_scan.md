# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T05:52:34.273506+00:00`
- Price records: `672`
- Market context records: `3760`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13105`

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

- `risk_on_high->crypto_major_24h` score `29.3648` n `32` status `ready` deltaP `31.25` edge `2.243` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `29.3648` n `32` status `ready` deltaP `31.25` edge `2.243` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `23.3659` n `32` status `ready` deltaP `36.4583` edge `1.7041` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `23.3659` n `32` status `ready` deltaP `36.4583` edge `1.7041` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `22.0647` n `32` status `ready` deltaP `31.9444` edge `1.6409` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `22.0647` n `32` status `ready` deltaP `31.9444` edge `1.6409` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.4988` n `32` status `ready` deltaP `31.25` edge `0.7499` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.4988` n `32` status `ready` deltaP `31.25` edge `0.7499` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.4789` n `32` status `ready` deltaP `19.3598` edge `0.8564` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.4789` n `32` status `ready` deltaP `19.3598` edge `0.8564` maxDD `-5.9781`
- `market_context_high->equity_24h` score `5.5971` n `160` status `ready` deltaP `17.0833` edge `0.6273` maxDD `-13.6477`
- `market_context_high->index_24h` score `5.4122` n `160` status `ready` deltaP `26.875` edge `0.3858` maxDD `-7.1159`
- `market_context_high->metal_24h` score `4.5334` n `160` status `ready` deltaP `27.1875` edge `0.3397` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `4.2556` n `160` status `ready` deltaP `7.5` edge `0.751` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.6778` n `164` status `ready` deltaP `9.1464` edge `0.2689` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.4118` n `32` status `ready` deltaP `8.003` edge `0.2411` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.4118` n `32` status `ready` deltaP `8.003` edge `0.2411` maxDD `-5.7426`
- `risk_on_high->metal_24h` score `1.3502` n `32` status `ready` deltaP `14.0625` edge `0.0449` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.3502` n `32` status `ready` deltaP `14.0625` edge `0.0449` maxDD `-0.7574`
- `risk_on_high->crypto_alt_4h` score `1.3443` n `32` status `ready` deltaP `-1.4482` edge `0.3061` maxDD `-11.7537`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
