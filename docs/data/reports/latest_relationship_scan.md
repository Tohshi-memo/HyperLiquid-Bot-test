# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-21T13:52:25.920678+00:00`
- Price records: `672`
- Market context records: `7462`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14679`

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

- `risk_on_high->crypto_major_4h` score `6.9787` n `36` status `ready` deltaP `37.3984` edge `0.3515` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.9787` n `36` status `ready` deltaP `37.3984` edge `0.3515` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `6.1439` n `32` status `ready` deltaP `16.7732` edge `0.5023` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `6.1439` n `32` status `ready` deltaP `16.7732` edge `0.5023` maxDD `-5.8371`
- `risk_on_high->crypto_alt_4h` score `4.9787` n `36` status `ready` deltaP `30.0983` edge `0.2386` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.9787` n `36` status `ready` deltaP `30.0983` edge `0.2386` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `4.8072` n `36` status `ready` deltaP `17.0223` edge `0.3301` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.8072` n `36` status `ready` deltaP `17.0223` edge `0.3301` maxDD `-0.4384`
- `risk_on_high->crypto_alt_24h` score `2.39` n `32` status `ready` deltaP `17.0927` edge `0.2853` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `2.39` n `32` status `ready` deltaP `17.0927` edge `0.2853` maxDD `-5.0938`
- `risk_on_high->crypto_major_1h` score `1.4488` n `36` status `ready` deltaP `21.8563` edge `0.0645` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.4488` n `36` status `ready` deltaP `21.8563` edge `0.0645` maxDD `-0.957`
- `risk_on_high->equity_24h` score `0.9501` n `31` status `ready` deltaP `13.0996` edge `0.2632` maxDD `-19.375`
- `risk_on_and_context->equity_24h` score `0.9501` n `31` status `ready` deltaP `13.0996` edge `0.2632` maxDD `-19.375`
- `risk_on_high->metal_4h` score `0.5816` n `36` status `ready` deltaP `6.7073` edge `0.0861` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `0.5816` n `36` status `ready` deltaP `6.7073` edge `0.0861` maxDD `-0.5882`
- `risk_on_high->commodity_1h` score `0.5477` n `36` status `ready` deltaP `6.6816` edge `0.0292` maxDD `-0.2479`
- `risk_on_and_context->commodity_1h` score `0.5477` n `36` status `ready` deltaP `6.6816` edge `0.0292` maxDD `-0.2479`
- `risk_on_high->equity_1h` score `0.5191` n `36` status `ready` deltaP `8.5586` edge `0.0472` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.5191` n `36` status `ready` deltaP `8.5586` edge `0.0472` maxDD `-1.3497`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
