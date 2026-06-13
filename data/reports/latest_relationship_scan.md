# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T07:22:32.725063+00:00`
- Price records: `672`
- Market context records: `3767`
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

- `risk_on_high->crypto_major_24h` score `29.5454` n `32` status `ready` deltaP `31.4236` edge `2.2569` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `29.5454` n `32` status `ready` deltaP `31.4236` edge `2.2569` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `23.6511` n `32` status `ready` deltaP `36.9792` edge `1.7244` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `23.6511` n `32` status `ready` deltaP `36.9792` edge `1.7244` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `22.2999` n `32` status `ready` deltaP `31.9444` edge `1.6605` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `22.2999` n `32` status `ready` deltaP `31.9444` edge `1.6605` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.4976` n `32` status `ready` deltaP `31.25` edge `0.7498` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.4976` n `32` status `ready` deltaP `31.25` edge `0.7498` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.4175` n `32` status `ready` deltaP `19.2073` edge `0.8523` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.4175` n `32` status `ready` deltaP `19.2073` edge `0.8523` maxDD `-5.9781`
- `market_context_high->equity_24h` score `5.7016` n `157` status `ready` deltaP `17.234` edge `0.635` maxDD `-13.6477`
- `market_context_high->index_24h` score `5.3275` n `157` status `ready` deltaP `26.7914` edge `0.3793` maxDD `-7.1159`
- `market_context_high->metal_24h` score `4.4253` n `157` status `ready` deltaP `26.8412` edge `0.333` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `4.2968` n `157` status `ready` deltaP `7.1601` edge `0.7567` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `2.0589` n `161` status `ready` deltaP `10.0846` edge `0.2944` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.4111` n `32` status `ready` deltaP `8.003` edge `0.241` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.4111` n `32` status `ready` deltaP `8.003` edge `0.241` maxDD `-5.7426`
- `risk_on_high->metal_24h` score `1.3298` n `32` status `ready` deltaP `14.0625` edge `0.0432` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.3298` n `32` status `ready` deltaP `14.0625` edge `0.0432` maxDD `-0.7574`
- `risk_on_high->crypto_alt_4h` score `1.3203` n `32` status `ready` deltaP `-1.4482` edge `0.3041` maxDD `-11.7537`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
