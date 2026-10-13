# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T07:07:29.580031+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9714`

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

- `market_context_high->crypto_alt_4h` score `7.4992` n `116` status `ready` deltaP `19.1127` edge `0.6424` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `6.7237` n `116` status `ready` deltaP `22.9814` edge `0.563` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.8824` n `53` status `ready` deltaP `21.1459` edge `0.394` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.8824` n `53` status `ready` deltaP `21.1459` edge `0.394` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `5.3398` n `48` status `ready` deltaP `30.087` edge `0.2444` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.3398` n `48` status `ready` deltaP `30.087` edge `0.2444` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.8415` n `53` status `ready` deltaP `36.0101` edge `0.4659` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.8415` n `53` status `ready` deltaP `36.0101` edge `0.4659` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `2.8195` n `116` status `ready` deltaP `-3.3168` edge `0.3217` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `1.824` n `117` status `ready` deltaP `13.2671` edge `0.1703` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.418` n `117` status `ready` deltaP `7.1588` edge `0.151` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0205` n `116` status `ready` deltaP `11.9166` edge `0.0268` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.2347` n `54` status `ready` deltaP `2.6004` edge `0.0248` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2347` n `54` status `ready` deltaP `2.6004` edge `0.0248` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3443` n `117` status `ready` deltaP `1.0973` edge `0.002` maxDD `-0.3742`
- `market_context_high->index_1h` score `-0.525` n `117` status `ready` deltaP `1.3744` edge `-0.0017` maxDD `-1.3154`
- `market_context_high->metal_1h` score `-0.5267` n `117` status `ready` deltaP `5.768` edge `0.0046` maxDD `-0.9556`
- `risk_on_high->crypto_alt_1h` score `-0.5477` n `54` status `ready` deltaP `3.0107` edge `0.0123` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.5477` n `54` status `ready` deltaP `3.0107` edge `0.0123` maxDD `-5.8734`
- `risk_on_high->metal_1h` score `-0.5567` n `54` status `ready` deltaP `0.3549` edge `-0.0006` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
