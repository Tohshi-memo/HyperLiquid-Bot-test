# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T00:07:25.242817+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9422`

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

- `market_context_high->crypto_alt_4h` score `7.3587` n `117` status `ready` deltaP `19.3559` edge `0.6286` maxDD `-9.2196`
- `risk_on_high->commodity_24h` score `7.1448` n `54` status `ready` deltaP `36.5854` edge `0.3515` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.1448` n `54` status `ready` deltaP `36.5854` edge `0.3515` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.3656` n `117` status `ready` deltaP `21.7298` edge `0.5415` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.954` n `54` status `ready` deltaP `21.6351` edge `0.3966` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.954` n `54` status `ready` deltaP `21.6351` edge `0.3966` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.6774` n `54` status `ready` deltaP `34.8352` edge `0.4527` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.6774` n `54` status `ready` deltaP `34.8352` edge `0.4527` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.8552` n `117` status `ready` deltaP `14.0156` edge `0.1676` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.2502` n `117` status `ready` deltaP `5.6618` edge `0.147` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.5252` n `117` status `ready` deltaP `14.9847` edge `0.0484` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.2775` n `117` status `ready` deltaP `8.3129` edge `0.0084` maxDD `-0.9556`
- `market_context_high->fx_1h` score `-0.3119` n `117` status `ready` deltaP `1.5477` edge `0.0017` maxDD `-0.3742`
- `risk_on_high->crypto_major_1h` score `-0.3437` n `54` status `ready` deltaP `1.1034` edge `0.0208` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3437` n `54` status `ready` deltaP `1.1034` edge `0.0208` maxDD `-3.7781`
- `risk_on_high->metal_1h` score `-0.3948` n `54` status `ready` deltaP `2.8998` edge `0.0032` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3948` n `54` status `ready` deltaP `2.8998` edge `0.0032` maxDD `-0.8513`
- `risk_on_high->metal_4h` score `-0.4396` n `54` status `ready` deltaP `2.5915` edge `0.0309` maxDD `-1.6961`
- `risk_on_and_context->metal_4h` score `-0.4396` n `54` status `ready` deltaP `2.5915` edge `0.0309` maxDD `-1.6961`
- `market_context_high->index_1h` score `-0.4712` n `117` status `ready` deltaP `1.975` edge `0.0012` maxDD `-1.3154`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
