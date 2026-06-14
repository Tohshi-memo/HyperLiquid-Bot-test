# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T11:21:07.679092+00:00`
- Price records: `672`
- Market context records: `3887`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13657`

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

- `risk_on_high->unknown_4h` score `47.4` n `72` status `ready` deltaP `5.8943` edge `6.2518` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `47.4` n `72` status `ready` deltaP `5.8943` edge `6.2518` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.4398` n `32` status `ready` deltaP `34.0278` edge `2.6474` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.4398` n `32` status `ready` deltaP `34.0278` edge `2.6474` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.9075` n `32` status `ready` deltaP `42.0139` edge `1.9622` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.9075` n `32` status `ready` deltaP `42.0139` edge `1.9622` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.2792` n `32` status `ready` deltaP `31.0764` edge `1.7479` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.2792` n `32` status `ready` deltaP `31.0764` edge `1.7479` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.1724` n `32` status `ready` deltaP `30.0347` edge `0.7308` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.1724` n `32` status `ready` deltaP `30.0347` edge `0.7308` maxDD `0.0`
- `market_context_high->unknown_4h` score `7.0147` n `206` status `ready` deltaP `-1.4681` edge `1.45` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.3686` n `149` status `ready` deltaP `18.524` edge `0.7102` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.4086` n `72` status `ready` deltaP `19.4613` edge `0.4332` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.4086` n `72` status `ready` deltaP `19.4613` edge `0.4332` maxDD `-5.9781`
- `market_context_high->index_24h` score `5.0564` n `149` status `ready` deltaP `25.3367` edge `0.3664` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.5672` n `149` status `ready` deltaP `22.9551` edge `0.2874` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.4422` n `72` status `ready` deltaP `24.3394` edge `0.1547` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4422` n `72` status `ready` deltaP `24.3394` edge `0.1547` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.2624` n `149` status `ready` deltaP `5.6092` edge `0.5975` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `2.2165` n `206` status `ready` deltaP `14.6474` edge `0.2635` maxDD `-9.4488`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
