# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T15:07:29.996865+00:00`
- Price records: `672`
- Market context records: `3801`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13064`

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

- `risk_on_high->crypto_major_24h` score `30.9303` n `32` status `ready` deltaP `32.6389` edge `2.3642` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `30.9303` n `32` status `ready` deltaP `32.6389` edge `2.3642` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `25.419` n `32` status `ready` deltaP `40.9722` edge `1.8451` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `25.419` n `32` status `ready` deltaP `40.9722` edge `1.8451` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.1903` n `32` status `ready` deltaP `31.9444` edge `1.7347` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.1903` n `32` status `ready` deltaP `31.9444` edge `1.7347` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.4388` n `32` status `ready` deltaP `31.25` edge `0.7449` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.4388` n `32` status `ready` deltaP `31.25` edge `0.7449` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.4834` n `32` status `ready` deltaP `15.0915` edge `0.8019` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.4834` n `32` status `ready` deltaP `15.0915` edge `0.8019` maxDD `-5.9781`
- `market_context_high->equity_24h` score `7.3418` n `152` status `ready` deltaP `20.5775` edge `0.7494` maxDD `-13.6477`
- `market_context_high->crypto_major_24h` score `5.5868` n `152` status `ready` deltaP `7.4744` edge `0.8621` maxDD `-31.0425`
- `market_context_high->index_24h` score `5.359` n `152` status `ready` deltaP `26.6447` edge `0.3829` maxDD `-7.1159`
- `market_context_high->metal_24h` score `4.3377` n `152` status `ready` deltaP `26.4072` edge `0.3286` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.6159` n `181` status `ready` deltaP `13.1923` edge `0.3201` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.4505` n `32` status `ready` deltaP `7.5457` edge `0.2491` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.4505` n `32` status `ready` deltaP `7.5457` edge `0.2491` maxDD `-5.7426`
- `risk_on_high->commodity_4h` score `1.3467` n `32` status `ready` deltaP `16.3872` edge `0.0897` maxDD `-3.6044`
- `risk_on_and_context->commodity_4h` score `1.3467` n `32` status `ready` deltaP `16.3872` edge `0.0897` maxDD `-3.6044`
- `risk_on_high->metal_24h` score `1.3161` n `32` status `ready` deltaP `14.2361` edge `0.0409` maxDD `-0.7574`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
