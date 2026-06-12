# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T11:37:25.184604+00:00`
- Price records: `672`
- Market context records: `3682`
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

- `risk_on_high->crypto_major_24h` score `32.6098` n `32` status `ready` deltaP `36.4583` edge `2.4787` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `32.6098` n `32` status `ready` deltaP `36.4583` edge `2.4787` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.4492` n `32` status `ready` deltaP `38.7153` edge `1.946` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.4492` n `32` status `ready` deltaP `38.7153` edge `1.946` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `24.3543` n `32` status `ready` deltaP `35.5903` edge `1.8074` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `24.3543` n `32` status `ready` deltaP `35.5903` edge `1.8074` maxDD `-0.8779`
- `risk_on_high->index_24h` score `14.5721` n `32` status `ready` deltaP `38.5417` edge `0.9574` maxDD `0.0`
- `risk_on_and_context->index_24h` score `14.5721` n `32` status `ready` deltaP `38.5417` edge `0.9574` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.0527` n `32` status `ready` deltaP `19.5122` edge `0.9032` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.0527` n `32` status `ready` deltaP `19.5122` edge `0.9032` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `5.5457` n `32` status `ready` deltaP `24.1319` edge `0.3274` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `5.5457` n `32` status `ready` deltaP `24.1319` edge `0.3274` maxDD `-0.7574`
- `market_context_high->index_24h` score `4.1761` n `157` status `ready` deltaP `23.892` edge `0.3603` maxDD `-11.3924`
- `risk_on_high->equity_4h` score `2.3061` n `32` status `ready` deltaP `9.375` edge `0.3466` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.3061` n `32` status `ready` deltaP `9.375` edge `0.3466` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `2.1821` n `32` status `ready` deltaP `-0.3811` edge `0.3688` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.1821` n `32` status `ready` deltaP `-0.3811` edge `0.3688` maxDD `-11.7537`
- `market_context_high->equity_24h` score `2.1613` n `157` status `ready` deltaP `15.7854` edge `0.6413` maxDD `-35.3144`
- `risk_on_high->crypto_major_1h` score `1.2262` n `32` status `ready` deltaP `2.6759` edge `0.2463` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.2262` n `32` status `ready` deltaP `2.6759` edge `0.2463` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
