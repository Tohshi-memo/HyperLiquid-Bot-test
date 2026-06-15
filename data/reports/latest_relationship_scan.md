# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T22:37:37.541081+00:00`
- Price records: `672`
- Market context records: `4033`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10624`

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

- `risk_on_high->unknown_4h` score `145.8077` n `40` status `ready` deltaP `-6.8293` edge `12.3778` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `145.8077` n `40` status `ready` deltaP `-6.8293` edge `12.3778` maxDD `-10.864`
- `market_context_high->unknown_24h` score `47.0292` n `134` status `ready` deltaP `-6.5457` edge `4.3656` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `24.8262` n `150` status `ready` deltaP `1.6707` edge `2.6` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `5.2091` n `40` status `ready` deltaP `36.5685` edge `0.1903` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.2091` n `40` status `ready` deltaP `36.5685` edge `0.1903` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.2063` n `40` status `ready` deltaP `35.7622` edge `0.0335` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.2063` n `40` status `ready` deltaP `35.7622` edge `0.0335` maxDD `-0.0446`
- `market_context_high->index_24h` score `2.9001` n `134` status `ready` deltaP `23.5171` edge `0.1061` maxDD `-1.3629`
- `market_context_high->equity_4h` score `1.8998` n `150` status `ready` deltaP `17.5955` edge `0.1691` maxDD `-6.9137`
- `market_context_high->metal_24h` score `1.7017` n `134` status `ready` deltaP `11.7011` edge `0.1625` maxDD `-4.8962`
- `market_context_high->equity_1h` score `1.1615` n `156` status `ready` deltaP `8.3487` edge `0.0971` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `0.9221` n `40` status `ready` deltaP `18.689` edge `0.0188` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.9221` n `40` status `ready` deltaP `18.689` edge `0.0188` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `0.6616` n `40` status `ready` deltaP `3.1629` edge `0.2622` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.6616` n `40` status `ready` deltaP `3.1629` edge `0.2622` maxDD `-12.9187`
- `market_context_high->crypto_major_1h` score `0.5286` n `156` status `ready` deltaP `7.6693` edge `0.0539` maxDD `-2.8785`
- `risk_on_high->index_24h` score `0.4579` n `40` status `ready` deltaP `24.2634` edge `-0.1236` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.4579` n `40` status `ready` deltaP `24.2634` edge `-0.1236` maxDD `0.0`
- `market_context_high->metal_1h` score `0.4077` n `156` status `ready` deltaP `9.8303` edge `0.0493` maxDD `-3.0049`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
