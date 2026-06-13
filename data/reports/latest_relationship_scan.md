# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T03:07:28.664292+00:00`
- Price records: `672`
- Market context records: `3749`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13153`

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

- `risk_on_high->crypto_major_24h` score `28.582` n `32` status `ready` deltaP `29.3403` edge `2.1905` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `28.582` n `32` status `ready` deltaP `29.3403` edge `2.1905` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.5927` n `32` status `ready` deltaP `34.5486` edge `1.6524` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.5927` n `32` status `ready` deltaP `34.5486` edge `1.6524` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.1712` n `32` status `ready` deltaP `30.5556` edge `1.5757` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.1712` n `32` status `ready` deltaP `30.5556` edge `1.5757` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.404` n `32` status `ready` deltaP `31.25` edge `0.742` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.404` n `32` status `ready` deltaP `31.25` edge `0.742` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.9731` n `32` status `ready` deltaP `17.9878` edge `0.8234` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.9731` n `32` status `ready` deltaP `17.9878` edge `0.8234` maxDD `-5.9781`
- `market_context_high->index_24h` score `5.428` n `164` status `ready` deltaP `26.9817` edge `0.3864` maxDD `-7.1159`
- `market_context_high->equity_24h` score `5.0297` n `164` status `ready` deltaP `15.6462` edge `0.5896` maxDD `-13.6477`
- `market_context_high->metal_24h` score `4.6047` n `164` status `ready` deltaP `27.6296` edge `0.3427` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `3.8145` n `164` status `ready` deltaP `6.2458` edge `0.7226` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.7118` n `168` status `ready` deltaP `8.7616` edge `0.2743` maxDD `-10.5381`
- `risk_on_high->metal_24h` score `1.3022` n `32` status `ready` deltaP `14.0625` edge `0.0409` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.3022` n `32` status `ready` deltaP `14.0625` edge `0.0409` maxDD `-0.7574`
- `risk_on_high->equity_4h` score `1.1612` n `32` status `ready` deltaP `6.7835` edge `0.2171` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.1612` n `32` status `ready` deltaP `6.7835` edge `0.2171` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `1.0383` n `32` status `ready` deltaP `1.9274` edge `0.2272` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
