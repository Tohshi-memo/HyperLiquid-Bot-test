# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T08:07:27.896160+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9843`

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

- `market_context_high->crypto_alt_4h` score `6.4903` n `117` status `ready` deltaP `16.612` edge `0.575` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.2404` n `54` status `ready` deltaP `32.0` edge `0.3067` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2404` n `54` status `ready` deltaP `32.0` edge `0.3067` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.9866` n `117` status `ready` deltaP `20.9676` edge `0.515` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.0792` n `54` status `ready` deltaP `18.8912` edge `0.3421` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.0792` n `54` status `ready` deltaP `18.8912` edge `0.3421` maxDD `-1.9151`
- `market_context_high->unknown_4h` score `4.7044` n `117` status `ready` deltaP `-2.7048` edge `0.4747` maxDD `-1.8373`
- `risk_on_high->crypto_major_4h` score `4.4311` n `54` status `ready` deltaP `34.073` edge `0.4262` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.4311` n `54` status `ready` deltaP `34.073` edge `0.4262` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7866` n `117` status `ready` deltaP `14.315` edge `0.1602` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.3244` n `117` status `ready` deltaP `7.1588` edge `0.1432` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0814` n `117` status `ready` deltaP `12.3932` edge `0.0287` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.2955` n `54` status `ready` deltaP `2.6004` edge `0.017` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2955` n `54` status `ready` deltaP `2.6004` edge `0.017` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3564` n `117` status `ready` deltaP `0.9471` edge `0.002` maxDD `-0.3742`
- `market_context_high->metal_1h` score `-0.4009` n `117` status `ready` deltaP `7.1153` edge `0.0061` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.475` n `54` status `ready` deltaP `1.7022` edge `0.0009` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.475` n `54` status `ready` deltaP `1.7022` edge `0.0009` maxDD `-0.8513`
- `risk_on_high->crypto_alt_1h` score `-0.5719` n `54` status `ready` deltaP `4.0586` edge `0.0022` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.5719` n `54` status `ready` deltaP `4.0586` edge `0.0022` maxDD `-5.8734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
