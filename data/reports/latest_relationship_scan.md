# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T08:07:29.473471+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9268`

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

- `market_context_high->unknown_4h` score `34.6701` n `119` status `ready` deltaP `-2.9386` edge `2.9734` maxDD `-1.8373`
- `market_context_high->crypto_major_24h` score `10.8504` n `54` status `ready` deltaP `20.544` edge `1.5177` maxDD `-13.7531`
- `market_context_high->crypto_alt_24h` score `8.4376` n `54` status `ready` deltaP `8.9121` edge `1.3793` maxDD `-21.2243`
- `risk_on_high->crypto_alt_4h` score `4.423` n `51` status `ready` deltaP `22.9436` edge `0.2604` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.423` n `51` status `ready` deltaP `22.9436` edge `0.2604` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.6763` n `51` status `ready` deltaP `35.2492` edge `0.3216` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.6763` n `51` status `ready` deltaP `35.2492` edge `0.3216` maxDD `-4.1548`
- `market_context_high->equity_24h` score `3.0853` n `54` status `ready` deltaP `10.0116` edge `0.4691` maxDD `-7.5571`
- `market_context_high->index_24h` score `2.0464` n `54` status `ready` deltaP `28.9352` edge `0.1255` maxDD `-0.4833`
- `risk_on_high->crypto_alt_1h` score `1.4654` n `53` status `ready` deltaP `8.5217` edge `0.125` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.4654` n `53` status `ready` deltaP `8.5217` edge `0.125` maxDD `-2.4421`
- `risk_on_high->crypto_major_1h` score `1.139` n `53` status `ready` deltaP `7.8918` edge `0.1076` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.139` n `53` status `ready` deltaP `7.8918` edge `0.1076` maxDD `-3.2233`
- `market_context_high->crypto_alt_1h` score `1.0027` n `121` status `ready` deltaP `8.241` edge `0.1237` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `0.8227` n `119` status `ready` deltaP `11.7198` edge `0.2379` maxDD `-11.1784`
- `market_context_high->crypto_major_1h` score `0.492` n `121` status `ready` deltaP `3.9467` edge `0.091` maxDD `-3.4384`
- `market_context_high->unknown_1h` score `0.3528` n `121` status `ready` deltaP `-5.5599` edge `0.1001` maxDD `-1.024`
- `market_context_high->crypto_alt_4h` score `0.2724` n `119` status `ready` deltaP `5.8567` edge `0.2395` maxDD `-13.8008`
- `market_context_high->metal_1h` score `-0.166` n `121` status `ready` deltaP `5.3781` edge `0.0064` maxDD `-0.4868`
- `market_context_high->fx_1h` score `-0.2561` n `121` status `ready` deltaP `0.7312` edge `0.0003` maxDD `-0.3742`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
