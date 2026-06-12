# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T06:37:32.028686+00:00`
- Price records: `672`
- Market context records: `3661`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13157`

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

- `risk_on_high->crypto_major_24h` score `34.8688` n `32` status `ready` deltaP `39.9306` edge `2.6438` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.8688` n `32` status `ready` deltaP `39.9306` edge `2.6438` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `30.3599` n `32` status `ready` deltaP `42.0139` edge `2.2499` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `30.3599` n `32` status `ready` deltaP `42.0139` edge `2.2499` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `26.7729` n `32` status `ready` deltaP `39.0625` edge `1.9858` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `26.7729` n `32` status `ready` deltaP `39.0625` edge `1.9858` maxDD `-0.8779`
- `risk_on_high->index_24h` score `17.1515` n `32` status `ready` deltaP `42.0139` edge `1.1492` maxDD `0.0`
- `risk_on_and_context->index_24h` score `17.1515` n `32` status `ready` deltaP `42.0139` edge `1.1492` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.2838` n `32` status `ready` deltaP `20.122` edge `0.9184` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.2838` n `32` status `ready` deltaP `20.122` edge `0.9184` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `8.7815` n `32` status `ready` deltaP `27.6042` edge `0.5739` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `8.7815` n `32` status `ready` deltaP `27.6042` edge `0.5739` maxDD `-0.7574`
- `market_context_high->index_24h` score `6.7555` n `157` status `ready` deltaP `27.3642` edge `0.5521` maxDD `-11.3924`
- `market_context_high->equity_24h` score `6.072` n `157` status `ready` deltaP `19.084` edge `0.9452` maxDD `-35.3144`
- `risk_on_high->equity_4h` score `2.5193` n `32` status `ready` deltaP `9.6799` edge `0.3719` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5193` n `32` status `ready` deltaP `9.6799` edge `0.3719` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `2.4938` n `32` status `ready` deltaP `0.3811` edge `0.3897` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.4938` n `32` status `ready` deltaP `0.3811` edge `0.3897` maxDD `-11.7537`
- `market_context_high->metal_24h` score `1.9271` n `157` status `ready` deltaP `21.9115` edge `0.4962` maxDD `-21.6171`
- `risk_on_high->crypto_major_1h` score `1.2362` n `32` status `ready` deltaP `3.2747` edge `0.2436` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
