# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T10:04:35.938984+00:00`
- Price records: `672`
- Market context records: `7553`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14475`

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

- `risk_on_high->crypto_major_4h` score `7.8472` n `34` status `ready` deltaP `41.9387` edge `0.3936` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.8472` n `34` status `ready` deltaP `41.9387` edge `0.3936` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `5.426` n `34` status `ready` deltaP `14.8488` edge `0.435` maxDD `-4.8796`
- `risk_on_and_context->crypto_major_24h` score `5.426` n `34` status `ready` deltaP `14.8488` edge `0.435` maxDD `-4.8796`
- `risk_on_high->crypto_alt_4h` score `4.9725` n `34` status `ready` deltaP `30.9362` edge `0.2325` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.9725` n `34` status `ready` deltaP `30.9362` edge `0.2325` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `4.8987` n `34` status `ready` deltaP `16.1406` edge `0.3436` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.8987` n `34` status `ready` deltaP `16.1406` edge `0.3436` maxDD `-0.4384`
- `risk_on_high->crypto_alt_24h` score `2.6397` n `34` status `ready` deltaP `14.7263` edge `0.1923` maxDD `-3.9732`
- `risk_on_and_context->crypto_alt_24h` score `2.6397` n `34` status `ready` deltaP `14.7263` edge `0.1923` maxDD `-3.9732`
- `risk_on_high->crypto_major_1h` score `1.606` n `34` status `ready` deltaP `23.3797` edge `0.0745` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.606` n `34` status `ready` deltaP `23.3797` edge `0.0745` maxDD `-0.957`
- `risk_on_high->fx_24h` score `0.8898` n `33` status `ready` deltaP `21.0591` edge `0.0193` maxDD `-1.3162`
- `risk_on_and_context->fx_24h` score `0.8898` n `33` status `ready` deltaP `21.0591` edge `0.0193` maxDD `-1.3162`
- `risk_on_high->equity_1h` score `0.4534` n `34` status `ready` deltaP `6.9953` edge `0.0492` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.4534` n `34` status `ready` deltaP `6.9953` edge `0.0492` maxDD `-1.3497`
- `risk_on_high->unknown_24h` score `0.3762` n `34` status `ready` deltaP `3.2476` edge `0.0368` maxDD `-0.5015`
- `risk_on_and_context->unknown_24h` score `0.3762` n `34` status `ready` deltaP `3.2476` edge `0.0368` maxDD `-0.5015`
- `risk_on_high->commodity_1h` score `0.1764` n `34` status `ready` deltaP `3.1797` edge `0.0216` maxDD `-0.2479`
- `risk_on_and_context->commodity_1h` score `0.1764` n `34` status `ready` deltaP `3.1797` edge `0.0216` maxDD `-0.2479`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
