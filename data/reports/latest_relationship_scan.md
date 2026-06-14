# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T23:52:34.132658+00:00`
- Price records: `672`
- Market context records: `3940`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11355`

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

- `risk_on_high->unknown_4h` score `140.2922` n `42` status `ready` deltaP `2.5697` edge `11.8586` maxDD `-11.1108`
- `risk_on_and_context->unknown_4h` score `140.2922` n `42` status `ready` deltaP `2.5697` edge `11.8586` maxDD `-11.1108`
- `market_context_high->unknown_4h` score `15.9049` n `178` status `ready` deltaP `-3.4496` edge `1.8893` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.1475` n `40` status `ready` deltaP `42.0139` edge `0.4822` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.1475` n `40` status `ready` deltaP `42.0139` edge `0.4822` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.4037` n `165` status `ready` deltaP `-11.2311` edge `2.1604` maxDD `-109.4842`
- `risk_on_high->equity_4h` score `3.9666` n `42` status `ready` deltaP `37.7686` edge `0.0835` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.9666` n `42` status `ready` deltaP `37.7686` edge `0.0835` maxDD `-0.0458`
- `market_context_high->equity_24h` score `3.588` n `165` status `ready` deltaP `20.8018` edge `0.4633` maxDD `-14.5715`
- `market_context_high->index_24h` score `3.4308` n `165` status `ready` deltaP `25.7923` edge `0.2279` maxDD `-7.1159`
- `market_context_high->metal_24h` score `2.9635` n `165` status `ready` deltaP `15.8649` edge `0.2927` maxDD `-9.1203`
- `risk_on_high->index_24h` score `2.878` n `40` status `ready` deltaP `30.0347` edge `0.0396` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.878` n `40` status `ready` deltaP `30.0347` edge `0.0396` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `2.6255` n `42` status `ready` deltaP `23.9619` edge `0.1256` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.6255` n `42` status `ready` deltaP `23.9619` edge `0.1256` maxDD `-2.6576`
- `market_context_high->crypto_major_4h` score `1.4296` n `178` status `ready` deltaP `17.0063` edge `0.1822` maxDD `-9.4488`
- `risk_on_high->commodity_24h` score `1.195` n `40` status `ready` deltaP `4.1667` edge `0.2885` maxDD `-12.6689`
- `risk_on_and_context->commodity_24h` score `1.195` n `40` status `ready` deltaP `4.1667` edge `0.2885` maxDD `-12.6689`
- `market_context_high->equity_4h` score `1.0179` n `178` status `ready` deltaP `15.0024` edge `0.1552` maxDD `-8.2982`
- `risk_on_high->equity_1h` score `0.688` n `42` status `ready` deltaP `10.6787` edge `0.0255` maxDD `-0.8151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
