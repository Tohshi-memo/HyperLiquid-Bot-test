# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T04:22:41.313481+00:00`
- Price records: `672`
- Market context records: `3652`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13163`

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

- `risk_on_high->crypto_major_24h` score `36.3378` n `32` status `ready` deltaP `41.4931` edge `2.7558` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `36.3378` n `32` status `ready` deltaP `41.4931` edge `2.7558` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `32.4013` n `32` status `ready` deltaP `43.5764` edge `2.4096` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `32.4013` n `32` status `ready` deltaP `43.5764` edge `2.4096` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `28.4795` n `32` status `ready` deltaP `40.625` edge `2.1176` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `28.4795` n `32` status `ready` deltaP `40.625` edge `2.1176` maxDD `-0.8779`
- `risk_on_high->index_24h` score `18.4057` n `32` status `ready` deltaP `43.5764` edge `1.2433` maxDD `0.0`
- `risk_on_and_context->index_24h` score `18.4057` n `32` status `ready` deltaP `43.5764` edge `1.2433` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.426` n `32` status `ready` deltaP `20.5793` edge `0.9272` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.426` n `32` status `ready` deltaP `20.5793` edge `0.9272` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `10.2169` n `32` status `ready` deltaP `29.1667` edge `0.6831` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `10.2169` n `32` status `ready` deltaP `29.1667` edge `0.6831` maxDD `-0.7574`
- `market_context_high->equity_24h` score `8.1134` n `157` status `ready` deltaP `20.6465` edge `1.1049` maxDD `-35.3144`
- `market_context_high->index_24h` score `8.0097` n `157` status `ready` deltaP `28.9267` edge `0.6462` maxDD `-11.3924`
- `market_context_high->metal_24h` score `2.8601` n `157` status `ready` deltaP `23.474` edge `0.6054` maxDD `-21.6171`
- `risk_on_high->crypto_alt_4h` score `2.7872` n `32` status `ready` deltaP `0.8384` edge `0.4111` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.7872` n `32` status `ready` deltaP `0.8384` edge `0.4111` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.4526` n `32` status `ready` deltaP `9.2226` edge `0.3664` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4526` n `32` status `ready` deltaP `9.2226` edge `0.3664` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.3328` n `157` status `ready` deltaP `7.6754` edge `0.8499` maxDD `-49.5335`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
