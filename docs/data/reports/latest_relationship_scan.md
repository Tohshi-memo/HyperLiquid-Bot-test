# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T02:52:28.111551+00:00`
- Price records: `672`
- Market context records: `3748`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13153`

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

- `risk_on_high->crypto_major_24h` score `28.5808` n `32` status `ready` deltaP `29.3403` edge `2.1904` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `28.5808` n `32` status `ready` deltaP `29.3403` edge `2.1904` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.5356` n `32` status `ready` deltaP `34.375` edge `1.6488` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.5356` n `32` status `ready` deltaP `34.375` edge `1.6488` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.1604` n `32` status `ready` deltaP `30.5556` edge `1.5748` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.1604` n `32` status `ready` deltaP `30.5556` edge `1.5748` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.4052` n `32` status `ready` deltaP `31.25` edge `0.7421` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.4052` n `32` status `ready` deltaP `31.25` edge `0.7421` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `10.0069` n `32` status `ready` deltaP `18.1402` edge `0.8252` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `10.0069` n `32` status `ready` deltaP `18.1402` edge `0.8252` maxDD `-5.9781`
- `market_context_high->index_24h` score `5.4211` n `163` status `ready` deltaP `26.9555` edge `0.386` maxDD `-7.1159`
- `market_context_high->equity_24h` score `5.284` n `163` status `ready` deltaP `15.9701` edge `0.5972` maxDD `-13.067`
- `market_context_high->metal_24h` score `4.6008` n `163` status `ready` deltaP `27.5211` edge `0.3431` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `3.9743` n `163` status `ready` deltaP `6.6984` edge `0.7329` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.7456` n `168` status `ready` deltaP `8.914` edge `0.2761` maxDD `-10.5381`
- `risk_on_high->metal_24h` score `1.3046` n `32` status `ready` deltaP `14.0625` edge `0.0411` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.3046` n `32` status `ready` deltaP `14.0625` edge `0.0411` maxDD `-0.7574`
- `risk_on_high->equity_4h` score `1.1612` n `32` status `ready` deltaP `6.7835` edge `0.2171` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.1612` n `32` status `ready` deltaP `6.7835` edge `0.2171` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `1.0484` n `32` status `ready` deltaP `1.9274` edge `0.2285` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
