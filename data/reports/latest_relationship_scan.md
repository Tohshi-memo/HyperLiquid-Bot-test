# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T09:52:26.802442+00:00`
- Price records: `672`
- Market context records: `3371`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13080`

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

- `risk_on_high->crypto_major_24h` score `56.4589` n `32` status `ready` deltaP `59.2014` edge `4.3145` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `56.4589` n `32` status `ready` deltaP `59.2014` edge `4.3145` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `53.5469` n `32` status `ready` deltaP `54.6875` edge `4.1128` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `53.5469` n `32` status `ready` deltaP `54.6875` edge `4.1128` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `45.8361` n `32` status `ready` deltaP `56.7708` edge `3.4412` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `45.8361` n `32` status `ready` deltaP `56.7708` edge `3.4412` maxDD `0.0`
- `risk_on_high->index_24h` score `23.1398` n `32` status `ready` deltaP `50.8681` edge `1.5892` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.1398` n `32` status `ready` deltaP `50.8681` edge `1.5892` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `21.7328` n `155` status `ready` deltaP `19.1028` edge `2.5115` maxDD `-59.2225`
- `risk_on_high->crypto_major_4h` score `15.4764` n `32` status `ready` deltaP `28.3537` edge `1.2129` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.4764` n `32` status `ready` deltaP `28.3537` edge `1.2129` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `14.7538` n `32` status `ready` deltaP `32.1181` edge `1.0415` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `14.7538` n `32` status `ready` deltaP `32.1181` edge `1.0415` maxDD `-0.7574`
- `market_context_high->index_24h` score `11.8193` n `155` status `ready` deltaP `35.3842` edge `1.0045` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.6814` n `155` status `ready` deltaP `30.3192` edge `2.0089` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.4416` n `32` status `ready` deltaP `8.9177` edge `0.7451` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.4416` n `32` status `ready` deltaP `8.9177` edge `0.7451` maxDD `-11.7537`
- `market_context_high->crypto_major_24h` score `5.8559` n `155` status `ready` deltaP `22.3264` edge `2.1727` maxDD `-115.9964`
- `risk_on_high->equity_4h` score `3.5298` n `32` status `ready` deltaP `13.9482` edge `0.473` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.5298` n `32` status `ready` deltaP `13.9482` edge `0.473` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
