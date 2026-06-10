# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T14:37:36.701486+00:00`
- Price records: `672`
- Market context records: `3492`
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

- `risk_on_high->crypto_major_24h` score `55.0161` n `32` status `ready` deltaP `58.5069` edge `4.1989` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `55.0161` n `32` status `ready` deltaP `58.5069` edge `4.1989` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `52.324` n `32` status `ready` deltaP `59.2014` edge `3.9808` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `52.324` n `32` status `ready` deltaP `59.2014` edge `3.9808` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.8721` n `32` status `ready` deltaP `56.0764` edge `3.3655` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.8721` n `32` status `ready` deltaP `56.0764` edge `3.3655` maxDD `0.0`
- `risk_on_high->index_24h` score `24.5147` n `32` status `ready` deltaP `51.3889` edge `1.7003` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.5147` n `32` status `ready` deltaP `51.3889` edge `1.7003` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `19.8205` n `155` status `ready` deltaP `24.2125` edge `2.2634` maxDD `-54.8486`
- `market_context_high->equity_24h` score `19.2846` n `155` status `ready` deltaP `32.8506` edge `2.0293` maxDD `-40.9667`
- `market_context_high->crypto_alt_24h` score `18.4171` n `155` status `ready` deltaP `19.7458` edge `2.2032` maxDD `-56.6728`
- `risk_on_high->metal_24h` score `15.8113` n `32` status `ready` deltaP `30.3819` edge `1.1412` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `15.8113` n `32` status `ready` deltaP `30.3819` edge `1.1412` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `15.2338` n `32` status `ready` deltaP `29.1159` edge `1.1876` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.2338` n `32` status `ready` deltaP `29.1159` edge `1.1876` maxDD `-5.9781`
- `market_context_high->index_24h` score `13.1413` n `155` status `ready` deltaP `35.905` edge `1.0774` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.5533` n `32` status `ready` deltaP `9.9848` edge `0.7473` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.5533` n `32` status `ready` deltaP `9.9848` edge `0.7473` maxDD `-11.7537`
- `market_context_high->metal_24h` score `5.8508` n `155` status `ready` deltaP `24.8577` edge `1.0384` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `4.1501` n `32` status `ready` deltaP `17.9116` edge `0.5261` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
