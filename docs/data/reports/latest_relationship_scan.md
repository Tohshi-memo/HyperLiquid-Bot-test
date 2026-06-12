# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T07:52:28.413176+00:00`
- Price records: `672`
- Market context records: `3666`
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

- `risk_on_high->crypto_major_24h` score `34.4634` n `32` status `ready` deltaP `39.0625` edge `2.6158` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.4634` n `32` status `ready` deltaP `39.0625` edge `2.6158` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `29.4193` n `32` status `ready` deltaP `41.1458` edge `2.1773` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `29.4193` n `32` status `ready` deltaP `41.1458` edge `2.1773` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `26.2931` n `32` status `ready` deltaP `38.1944` edge `1.9516` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `26.2931` n `32` status `ready` deltaP `38.1944` edge `1.9516` maxDD `-0.8779`
- `risk_on_high->index_24h` score `16.5313` n `32` status `ready` deltaP `41.1458` edge `1.1033` maxDD `0.0`
- `risk_on_and_context->index_24h` score `16.5313` n `32` status `ready` deltaP `41.1458` edge `1.1033` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.5594` n `32` status `ready` deltaP `20.7317` edge `0.9373` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.5594` n `32` status `ready` deltaP `20.7317` edge `0.9373` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `8.0629` n `32` status `ready` deltaP `26.7361` edge `0.5198` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `8.0629` n `32` status `ready` deltaP `26.7361` edge `0.5198` maxDD `-0.7574`
- `market_context_high->index_24h` score `6.1352` n `157` status `ready` deltaP `26.4961` edge `0.5062` maxDD `-11.3924`
- `market_context_high->equity_24h` score `5.1313` n `157` status `ready` deltaP `18.2159` edge `0.8726` maxDD `-35.3144`
- `risk_on_high->crypto_alt_4h` score `2.7346` n `32` status `ready` deltaP `0.9909` edge `0.4057` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.7346` n `32` status `ready` deltaP `0.9909` edge `0.4057` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.6681` n `32` status `ready` deltaP `10.4421` edge `0.3859` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6681` n `32` status `ready` deltaP `10.4421` edge `0.3859` maxDD `-5.7426`
- `market_context_high->metal_24h` score `1.46` n `157` status `ready` deltaP `21.0434` edge `0.4421` maxDD `-21.6171`
- `risk_on_high->crypto_major_1h` score `1.3407` n `32` status `ready` deltaP `3.5741` edge `0.255` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
