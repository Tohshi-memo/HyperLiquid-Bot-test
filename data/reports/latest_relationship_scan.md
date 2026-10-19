# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T23:52:29.116294+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8202`

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

- `market_context_high->commodity_24h` score `2.7574` n `74` status `ready` deltaP `22.5647` edge `0.1645` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.6922` n `41` status `ready` deltaP `15.4228` edge `0.0296` maxDD `-0.8277`
- `risk_on_and_context->equity_1h` score `0.6922` n `41` status `ready` deltaP `15.4228` edge `0.0296` maxDD `-0.8277`
- `risk_on_high->commodity_24h` score `0.6235` n `41` status `ready` deltaP `17.0604` edge `0.018` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.6235` n `41` status `ready` deltaP `17.0604` edge `0.018` maxDD `-1.7154`
- `risk_on_high->index_1h` score `0.4598` n `41` status `ready` deltaP `12.2791` edge `0.0044` maxDD `-0.1852`
- `risk_on_and_context->index_1h` score `0.4598` n `41` status `ready` deltaP `12.2791` edge `0.0044` maxDD `-0.1852`
- `risk_on_high->fx_1h` score `-0.1595` n `41` status `ready` deltaP `2.1615` edge `-0.0003` maxDD `-0.0985`
- `risk_on_and_context->fx_1h` score `-0.1595` n `41` status `ready` deltaP `2.1615` edge `-0.0003` maxDD `-0.0985`
- `risk_on_high->equity_4h` score `-0.2176` n `41` status `ready` deltaP `5.0305` edge `0.064` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.2176` n `41` status `ready` deltaP `5.0305` edge `0.064` maxDD `-4.0351`
- `risk_on_high->index_4h` score `-0.2917` n `41` status `ready` deltaP `5.6402` edge `0.0095` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.2917` n `41` status `ready` deltaP `5.6402` edge `0.0095` maxDD `-0.7604`
- `market_context_high->crypto_major_1h` score `-0.2939` n `93` status `ready` deltaP `0.9739` edge `0.0575` maxDD `-4.8007`
- `market_context_high->metal_1h` score `-0.3222` n `93` status `ready` deltaP `-1.0962` edge `0.0035` maxDD `-0.6669`
- `risk_on_high->fx_4h` score `-0.4098` n `41` status `ready` deltaP `-1.3719` edge `0.0014` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.4098` n `41` status `ready` deltaP `-1.3719` edge `0.0014` maxDD `-0.1126`
- `risk_on_high->metal_1h` score `-0.4233` n `41` status `ready` deltaP `-4.7941` edge `0.0045` maxDD `-0.1445`
- `risk_on_and_context->metal_1h` score `-0.4233` n `41` status `ready` deltaP `-4.7941` edge `0.0045` maxDD `-0.1445`
- `market_context_high->fx_4h` score `-0.5862` n `93` status `ready` deltaP `-1.7653` edge `0.0007` maxDD `-0.7936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
