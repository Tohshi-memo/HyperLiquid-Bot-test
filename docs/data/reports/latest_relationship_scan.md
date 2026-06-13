# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T06:22:27.860207+00:00`
- Price records: `672`
- Market context records: `3763`
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

- `risk_on_high->crypto_major_24h` score `29.4542` n `32` status `ready` deltaP `31.4236` edge `2.2493` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `29.4542` n `32` status `ready` deltaP `31.4236` edge `2.2493` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `23.4836` n `32` status `ready` deltaP `36.8056` edge `1.7116` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `23.4836` n `32` status `ready` deltaP `36.8056` edge `1.7116` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `22.1667` n `32` status `ready` deltaP `31.9444` edge `1.6494` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `22.1667` n `32` status `ready` deltaP `31.9444` edge `1.6494` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.5048` n `32` status `ready` deltaP `31.25` edge `0.7504` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.5048` n `32` status `ready` deltaP `31.25` edge `0.7504` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.5091` n `32` status `ready` deltaP `19.5122` edge `0.8579` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.5091` n `32` status `ready` deltaP `19.5122` edge `0.8579` maxDD `-5.9781`
- `market_context_high->equity_24h` score `5.7149` n `160` status `ready` deltaP `17.4306` edge `0.6348` maxDD `-13.6477`
- `market_context_high->index_24h` score `5.4182` n `160` status `ready` deltaP `26.875` edge `0.3863` maxDD `-7.1159`
- `market_context_high->metal_24h` score `4.5346` n `160` status `ready` deltaP `27.1875` edge `0.3398` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `4.3451` n `160` status `ready` deltaP `7.6736` edge `0.7573` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.708` n `164` status `ready` deltaP `9.2988` edge `0.2704` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.4165` n `32` status `ready` deltaP `8.003` edge `0.2417` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.4165` n `32` status `ready` deltaP `8.003` edge `0.2417` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.3877` n `32` status `ready` deltaP `-1.2957` edge `0.3087` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.3877` n `32` status `ready` deltaP `-1.2957` edge `0.3087` maxDD `-11.7537`
- `risk_on_high->metal_24h` score `1.3514` n `32` status `ready` deltaP `14.0625` edge `0.045` maxDD `-0.7574`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
