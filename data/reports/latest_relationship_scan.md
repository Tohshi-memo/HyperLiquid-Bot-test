# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T06:07:31.991508+00:00`
- Price records: `672`
- Market context records: `3762`
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

- `risk_on_high->crypto_major_24h` score `29.4254` n `32` status `ready` deltaP `31.4236` edge `2.2469` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `29.4254` n `32` status `ready` deltaP `31.4236` edge `2.2469` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `23.4266` n `32` status `ready` deltaP `36.6319` edge `1.708` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `23.4266` n `32` status `ready` deltaP `36.6319` edge `1.708` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `22.1259` n `32` status `ready` deltaP `31.9444` edge `1.646` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `22.1259` n `32` status `ready` deltaP `31.9444` edge `1.646` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.5036` n `32` status `ready` deltaP `31.25` edge `0.7503` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.5036` n `32` status `ready` deltaP `31.25` edge `0.7503` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.5079` n `32` status `ready` deltaP `19.5122` edge `0.8578` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.5079` n `32` status `ready` deltaP `19.5122` edge `0.8578` maxDD `-5.9781`
- `market_context_high->equity_24h` score `5.6578` n `160` status `ready` deltaP `17.2569` edge `0.6312` maxDD `-13.6477`
- `market_context_high->index_24h` score `5.417` n `160` status `ready` deltaP `26.875` edge `0.3862` maxDD `-7.1159`
- `market_context_high->metal_24h` score `4.5346` n `160` status `ready` deltaP `27.1875` edge `0.3398` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `4.3163` n `160` status `ready` deltaP `7.6736` edge `0.7549` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.7068` n `164` status `ready` deltaP `9.2988` edge `0.2703` maxDD `-10.5381`
- `risk_on_high->equity_4h` score `1.415` n `32` status `ready` deltaP `8.003` edge `0.2415` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.415` n `32` status `ready` deltaP `8.003` edge `0.2415` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.3853` n `32` status `ready` deltaP `-1.2957` edge `0.3085` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `1.3853` n `32` status `ready` deltaP `-1.2957` edge `0.3085` maxDD `-11.7537`
- `risk_on_high->metal_24h` score `1.3514` n `32` status `ready` deltaP `14.0625` edge `0.045` maxDD `-0.7574`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
