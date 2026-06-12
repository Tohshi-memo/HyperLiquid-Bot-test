# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T11:07:34.963060+00:00`
- Price records: `672`
- Market context records: `3680`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12897`

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

- `risk_on_high->crypto_major_24h` score `32.8836` n `32` status `ready` deltaP `36.8056` edge `2.4992` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `32.8836` n `32` status `ready` deltaP `36.8056` edge `2.4992` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.8826` n `32` status `ready` deltaP `39.0625` edge `1.9798` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.8826` n `32` status `ready` deltaP `39.0625` edge `1.9798` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `24.6281` n `32` status `ready` deltaP `35.9375` edge `1.8279` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `24.6281` n `32` status `ready` deltaP `35.9375` edge `1.8279` maxDD `-0.8779`
- `risk_on_high->index_24h` score `14.8399` n `32` status `ready` deltaP `38.8889` edge `0.9774` maxDD `0.0`
- `risk_on_and_context->index_24h` score `14.8399` n `32` status `ready` deltaP `38.8889` edge `0.9774` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.2163` n `32` status `ready` deltaP `19.8171` edge `0.9148` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.2163` n `32` status `ready` deltaP `19.8171` edge `0.9148` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `5.8879` n `32` status `ready` deltaP `24.4792` edge `0.3536` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `5.8879` n `32` status `ready` deltaP `24.4792` edge `0.3536` maxDD `-0.7574`
- `market_context_high->index_24h` score `4.4439` n `157` status `ready` deltaP `24.2392` edge `0.3803` maxDD `-11.3924`
- `market_context_high->equity_24h` score `2.5946` n `157` status `ready` deltaP `16.1326` edge `0.6751` maxDD `-35.3144`
- `risk_on_high->equity_4h` score `2.4179` n `32` status `ready` deltaP `9.6799` edge `0.3589` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4179` n `32` status `ready` deltaP `9.6799` edge `0.3589` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `2.3276` n `32` status `ready` deltaP `-0.0762` edge `0.3789` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.3276` n `32` status `ready` deltaP `-0.0762` edge `0.3789` maxDD `-11.7537`
- `risk_on_high->crypto_major_1h` score `1.2573` n `32` status `ready` deltaP `2.9753` edge `0.2483` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.2573` n `32` status `ready` deltaP `2.9753` edge `0.2483` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
