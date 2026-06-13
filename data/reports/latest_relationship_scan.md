# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T09:37:28.466367+00:00`
- Price records: `672`
- Market context records: `3777`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13055`

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

- `risk_on_high->crypto_major_24h` score `29.8977` n `32` status `ready` deltaP `31.5972` edge `2.2851` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `29.8977` n `32` status `ready` deltaP `31.5972` edge `2.2851` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `24.2212` n `32` status `ready` deltaP `38.1944` edge `1.7638` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `24.2212` n `32` status `ready` deltaP `38.1944` edge `1.7638` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `22.5759` n `32` status `ready` deltaP `31.9444` edge `1.6835` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `22.5759` n `32` status `ready` deltaP `31.9444` edge `1.6835` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.5324` n `32` status `ready` deltaP `31.25` edge `0.7527` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.5324` n `32` status `ready` deltaP `31.25` edge `0.7527` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.0977` n `32` status `ready` deltaP `17.8354` edge `0.8348` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.0977` n `32` status `ready` deltaP `17.8354` edge `0.8348` maxDD `-5.9781`
- `market_context_high->equity_24h` score `6.2716` n `157` status `ready` deltaP `18.4492` edge `0.6744` maxDD `-13.6477`
- `market_context_high->index_24h` score `5.3623` n `157` status `ready` deltaP `26.7914` edge `0.3822` maxDD `-7.1159`
- `market_context_high->crypto_major_24h` score `4.6491` n `157` status `ready` deltaP `7.3337` edge `0.7849` maxDD `-31.0425`
- `market_context_high->metal_24h` score `4.4667` n `157` status `ready` deltaP `27.0148` edge `0.3353` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `1.9098` n `164` status `ready` deltaP `9.4513` edge `0.2862` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.4337` n `32` status `ready` deltaP `8.003` edge `0.2439` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.4337` n `32` status `ready` deltaP `8.003` edge `0.2439` maxDD `-5.7426`
- `risk_on_high->metal_24h` score `1.3713` n `32` status `ready` deltaP `14.2361` edge `0.0455` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.3713` n `32` status `ready` deltaP `14.2361` edge `0.0455` maxDD `-0.7574`
- `market_context_high->equity_4h` score `1.1058` n `164` status `ready` deltaP `8.8414` edge `0.2036` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
