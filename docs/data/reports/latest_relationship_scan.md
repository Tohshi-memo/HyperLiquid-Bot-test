# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T15:22:34.160945+00:00`
- Price records: `672`
- Market context records: `3495`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13142`

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

- `risk_on_high->crypto_major_24h` score `54.7857` n `32` status `ready` deltaP `58.5069` edge `4.1797` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `54.7857` n `32` status `ready` deltaP `58.5069` edge `4.1797` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `51.8696` n `32` status `ready` deltaP `58.6806` edge `3.9464` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `51.8696` n `32` status `ready` deltaP `58.6806` edge `3.9464` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.7977` n `32` status `ready` deltaP `56.0764` edge `3.3593` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.7977` n `32` status `ready` deltaP `56.0764` edge `3.3593` maxDD `0.0`
- `risk_on_high->index_24h` score `24.5135` n `32` status `ready` deltaP `51.3889` edge `1.7002` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.5135` n `32` status `ready` deltaP `51.3889` edge `1.7002` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `19.5901` n `155` status `ready` deltaP `24.2125` edge `2.2442` maxDD `-54.8486`
- `market_context_high->equity_24h` score `19.2102` n `155` status `ready` deltaP `32.8506` edge `2.0231` maxDD `-40.9667`
- `market_context_high->crypto_alt_24h` score `17.9627` n `155` status `ready` deltaP `19.225` edge `2.1688` maxDD `-56.6728`
- `risk_on_high->metal_24h` score `15.9332` n `32` status `ready` deltaP `30.5556` edge `1.1502` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `15.9332` n `32` status `ready` deltaP `30.5556` edge `1.1502` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `15.0796` n `32` status `ready` deltaP `28.6585` edge `1.1778` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.0796` n `32` status `ready` deltaP `28.6585` edge `1.1778` maxDD `-5.9781`
- `market_context_high->index_24h` score `13.1401` n `155` status `ready` deltaP `35.905` edge `1.0773` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.3883` n `32` status `ready` deltaP `9.5274` edge `0.7366` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.3883` n `32` status `ready` deltaP `9.5274` edge `0.7366` maxDD `-11.7537`
- `market_context_high->metal_24h` score `5.93` n `155` status `ready` deltaP `25.0314` edge `1.0474` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `4.0538` n `32` status `ready` deltaP `17.4543` edge `0.5168` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
