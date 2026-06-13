# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T12:52:31.709886+00:00`
- Price records: `672`
- Market context records: `3791`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13040`

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

- `risk_on_high->crypto_major_24h` score `30.6781` n `32` status `ready` deltaP `32.2917` edge `2.3455` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `30.6781` n `32` status `ready` deltaP `32.2917` edge `2.3455` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `25.1241` n `32` status `ready` deltaP `40.4514` edge `1.824` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `25.1241` n `32` status `ready` deltaP `40.4514` edge `1.824` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.1423` n `32` status `ready` deltaP `31.9444` edge `1.7307` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.1423` n `32` status `ready` deltaP `31.9444` edge `1.7307` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.5372` n `32` status `ready` deltaP `31.25` edge `0.7531` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.5372` n `32` status `ready` deltaP `31.25` edge `0.7531` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.9028` n `32` status `ready` deltaP `16.4634` edge `0.8277` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.9028` n `32` status `ready` deltaP `16.4634` edge `0.8277` maxDD `-5.9781`
- `market_context_high->equity_24h` score `7.1745` n `157` status `ready` deltaP `20.7062` edge `0.7346` maxDD `-13.6477`
- `market_context_high->crypto_major_24h` score `5.4295` n `157` status `ready` deltaP `8.0282` edge `0.8453` maxDD `-31.0425`
- `market_context_high->index_24h` score `5.3671` n `157` status `ready` deltaP `26.7914` edge `0.3826` maxDD `-7.1159`
- `market_context_high->metal_24h` score `4.5135` n `157` status `ready` deltaP `27.0148` edge `0.3392` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `2.0089` n `177` status `ready` deltaP `10.9902` edge `0.2842` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.5451` n `32` status `ready` deltaP `8.7652` edge `0.2531` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.5451` n `32` status `ready` deltaP `8.7652` edge `0.2531` maxDD `-5.7426`
- `risk_on_high->metal_24h` score `1.4181` n `32` status `ready` deltaP `14.2361` edge `0.0494` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.4181` n `32` status `ready` deltaP `14.2361` edge `0.0494` maxDD `-0.7574`
- `risk_on_high->commodity_4h` score `1.1518` n `32` status `ready` deltaP `15.0152` edge `0.0826` maxDD `-3.6044`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
