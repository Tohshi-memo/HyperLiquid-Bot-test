# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T13:22:30.946457+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10980`

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

- `risk_on_high->unknown_4h` score `20.1` n `133` status `ready` deltaP `7.4741` edge `1.687` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.1` n `133` status `ready` deltaP `7.4741` edge `1.687` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.9685` n `133` status `ready` deltaP `-1.353` edge `1.0641` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.9685` n `133` status `ready` deltaP `-1.353` edge `1.0641` maxDD `-1.95`
- `market_context_high->unknown_4h` score `10.7994` n `198` status `ready` deltaP `8.8184` edge `0.9107` maxDD `-2.563`
- `market_context_high->unknown_1h` score `7.9695` n `210` status `ready` deltaP `-1.0522` edge `0.7342` maxDD `-2.0446`
- `news_risk_high->commodity_4h` score `1.4308` n `61` status `ready` deltaP `12.1077` edge `0.0586` maxDD `-0.2737`
- `news_risk_high->commodity_24h` score `0.8655` n `61` status `ready` deltaP `10.5163` edge `0.0193` maxDD `-0.0495`
- `market_context_high->equity_24h` score `0.7291` n `167` status `ready` deltaP `14.3733` edge `0.3995` maxDD `-20.7654`
- `risk_on_high->metal_1h` score `0.1896` n `133` status `ready` deltaP `13.311` edge `0.0068` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1896` n `133` status `ready` deltaP `13.311` edge `0.0068` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0066` n `61` status `ready` deltaP `5.5806` edge `-0.0027` maxDD `-0.8275`
- `news_risk_high->commodity_1h` score `-0.098` n `61` status `ready` deltaP `5.2592` edge `0.0014` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1582` n `133` status `ready` deltaP `3.8427` edge `-0.0014` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1582` n `133` status `ready` deltaP `3.8427` edge `-0.0014` maxDD `-0.5605`
- `risk_on_high->crypto_alt_1h` score `-0.294` n `133` status `ready` deltaP `3.7031` edge `0.0525` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.294` n `133` status `ready` deltaP `3.7031` edge `0.0525` maxDD `-5.4685`
- `risk_on_high->commodity_1h` score `-0.4205` n `133` status `ready` deltaP `0.107` edge `-0.0001` maxDD `-1.0281`
- `risk_on_and_context->commodity_1h` score `-0.4205` n `133` status `ready` deltaP `0.107` edge `-0.0001` maxDD `-1.0281`
- `market_context_high->metal_1h` score `-0.434` n `210` status `ready` deltaP `6.5441` edge `-0.0035` maxDD `-2.9947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
