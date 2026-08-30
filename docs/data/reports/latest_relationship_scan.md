# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T22:37:29.321451+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11748`

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

- `risk_on_high->crypto_alt_24h` score `23.8674` n `50` status `ready` deltaP `49.1319` edge `1.6614` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `23.8674` n `50` status `ready` deltaP `49.1319` edge `1.6614` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `12.1296` n `50` status `ready` deltaP `33.9236` edge `0.8137` maxDD `-1.658`
- `risk_on_and_context->crypto_major_24h` score `12.1296` n `50` status `ready` deltaP `33.9236` edge `0.8137` maxDD `-1.658`
- `risk_on_high->unknown_4h` score `8.7871` n `80` status `ready` deltaP `30.0305` edge `0.5749` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `8.7871` n `80` status `ready` deltaP `30.0305` edge `0.5749` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.2042` n `50` status `ready` deltaP `69.6181` edge `0.0529` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.2042` n `50` status `ready` deltaP `69.6181` edge `0.0529` maxDD `0.0`
- `risk_on_high->metal_24h` score `5.1198` n `50` status `ready` deltaP `45.9931` edge `0.1412` maxDD `-0.3601`
- `risk_on_and_context->metal_24h` score `5.1198` n `50` status `ready` deltaP `45.9931` edge `0.1412` maxDD `-0.3601`
- `market_context_high->unknown_4h` score `5.0729` n `149` status `ready` deltaP `21.054` edge `0.3294` maxDD `-1.0945`
- `risk_on_high->unknown_1h` score `4.3052` n `90` status `ready` deltaP `11.191` edge `0.3086` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `4.3052` n `90` status `ready` deltaP `11.191` edge `0.3086` maxDD `-0.2885`
- `market_context_high->metal_24h` score `4.2742` n `117` status `ready` deltaP `34.335` edge `0.2292` maxDD `-3.1535`
- `market_context_high->crypto_major_24h` score `4.2571` n `117` status `ready` deltaP `17.4279` edge `0.496` maxDD `-17.2607`
- `risk_on_high->equity_24h` score `3.7052` n `50` status `ready` deltaP `26.7153` edge `0.1495` maxDD `-0.5071`
- `risk_on_and_context->equity_24h` score `3.7052` n `50` status `ready` deltaP `26.7153` edge `0.1495` maxDD `-0.5071`
- `market_context_high->crypto_alt_24h` score `3.4418` n `117` status `ready` deltaP `16.6533` edge `0.7492` maxDD `-27.517`
- `market_context_high->unknown_1h` score `2.8384` n `161` status `ready` deltaP `9.8728` edge `0.2116` maxDD `-0.9372`
- `risk_on_high->index_24h` score `2.0137` n `50` status `ready` deltaP `25.5972` edge `0.0116` maxDD `-0.1549`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
