# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T02:22:32.111169+00:00`
- Price records: `672`
- Market context records: `3746`
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

- `risk_on_high->crypto_major_24h` score `28.5398` n `32` status `ready` deltaP `28.9931` edge `2.1893` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `28.5398` n `32` status `ready` deltaP `28.9931` edge `2.1893` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.4286` n `32` status `ready` deltaP `34.0278` edge `1.6422` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.4286` n `32` status `ready` deltaP `34.0278` edge `1.6422` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.1292` n `32` status `ready` deltaP `30.5556` edge `1.5722` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.1292` n `32` status `ready` deltaP `30.5556` edge `1.5722` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.4088` n `32` status `ready` deltaP `31.25` edge `0.7424` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.4088` n `32` status `ready` deltaP `31.25` edge `0.7424` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.9899` n `32` status `ready` deltaP `17.9878` edge `0.8248` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.9899` n `32` status `ready` deltaP `17.9878` edge `0.8248` maxDD `-5.9781`
- `market_context_high->equity_24h` score `5.6642` n `161` status `ready` deltaP `16.6365` edge `0.613` maxDD `-12.8184`
- `market_context_high->index_24h` score `5.4156` n `161` status `ready` deltaP `26.9022` edge `0.3859` maxDD `-7.1159`
- `market_context_high->metal_24h` score `4.5748` n `161` status `ready` deltaP `27.3001` edge `0.3424` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `4.2651` n `161` status `ready` deltaP `7.2734` edge `0.7533` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.7286` n `168` status `ready` deltaP `8.7616` edge `0.2757` maxDD `-10.5381`
- `risk_on_high->metal_24h` score `1.3154` n `32` status `ready` deltaP `14.0625` edge `0.042` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.3154` n `32` status `ready` deltaP `14.0625` edge `0.042` maxDD `-0.7574`
- `risk_on_high->equity_4h` score `1.1565` n `32` status `ready` deltaP `6.7835` edge `0.2165` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.1565` n `32` status `ready` deltaP `6.7835` edge `0.2165` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `1.1225` n `32` status `ready` deltaP `-1.2957` edge `0.2866` maxDD `-11.7537`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
