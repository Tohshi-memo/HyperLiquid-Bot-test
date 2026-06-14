# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T09:37:31.293316+00:00`
- Price records: `672`
- Market context records: `3880`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13633`

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

- `risk_on_high->unknown_4h` score `47.5812` n `72` status `ready` deltaP `6.1992` edge `6.273` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `47.5812` n `72` status `ready` deltaP `6.1992` edge `6.273` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.3546` n `32` status `ready` deltaP `34.0278` edge `2.6403` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.3546` n `32` status `ready` deltaP `34.0278` edge `2.6403` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.8799` n `32` status `ready` deltaP `42.0139` edge `1.9599` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.8799` n `32` status `ready` deltaP `42.0139` edge `1.9599` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.2077` n `32` status `ready` deltaP `30.9028` edge `1.7431` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.2077` n `32` status `ready` deltaP `30.9028` edge `1.7431` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.1376` n `32` status `ready` deltaP `30.0347` edge `0.7279` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.1376` n `32` status `ready` deltaP `30.0347` edge `0.7279` maxDD `0.0`
- `market_context_high->unknown_4h` score `6.9085` n `206` status `ready` deltaP `-1.6487` edge `1.4376` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.4258` n `147` status `ready` deltaP `18.2044` edge `0.7171` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.5522` n `72` status `ready` deltaP `20.0711` edge `0.4411` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.5522` n `72` status `ready` deltaP `20.0711` edge `0.4411` maxDD `-5.9781`
- `market_context_high->index_24h` score `5.194` n `147` status `ready` deltaP `25.2728` edge `0.3783` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.1419` n `147` status `ready` deltaP `20.5499` edge `0.268` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.4726` n `72` status `ready` deltaP `24.6443` edge `0.1552` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4726` n `72` status `ready` deltaP `24.6443` edge `0.1552` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.3852` n `147` status `ready` deltaP `5.18` edge `0.6106` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.8906` n `206` status `ready` deltaP `13.8009` edge `0.2556` maxDD `-10.5381`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
