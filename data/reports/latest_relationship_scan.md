# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T02:37:30.898307+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8301`

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

- `market_context_high->commodity_24h` score `1.0297` n `64` status `ready` deltaP `17.7083` edge `0.0529` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.9928` n `39` status `ready` deltaP `17.8259` edge `0.0508` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.9928` n `39` status `ready` deltaP `17.8259` edge `0.0508` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.6204` n `39` status `ready` deltaP `14.6822` edge `0.0087` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.6204` n `39` status `ready` deltaP `14.6822` edge `0.0087` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.1866` n `39` status `ready` deltaP `15.1843` edge `-0.0059` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1866` n `39` status `ready` deltaP `15.1843` edge `-0.0059` maxDD `-1.7154`
- `market_context_high->index_1h` score `0.1118` n `82` status `ready` deltaP `6.8022` edge `0.0045` maxDD `-0.5082`
- `risk_on_high->equity_4h` score `-0.0163` n `39` status `ready` deltaP `6.1874` edge `0.0821` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.0163` n `39` status `ready` deltaP `6.1874` edge `0.0821` maxDD `-4.0351`
- `risk_on_high->index_4h` score `-0.0445` n `39` status `ready` deltaP `9.0291` edge `0.0186` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.0445` n `39` status `ready` deltaP `9.0291` edge `0.0186` maxDD `-0.7604`
- `risk_on_high->fx_1h` score `-0.2504` n `39` status `ready` deltaP `0.3839` edge `-0.0001` maxDD `-0.0985`
- `risk_on_and_context->fx_1h` score `-0.2504` n `39` status `ready` deltaP `0.3839` edge `-0.0001` maxDD `-0.0985`
- `risk_on_high->metal_1h` score `-0.2685` n `39` status `ready` deltaP `-2.5181` edge `0.0084` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.2685` n `39` status `ready` deltaP `-2.5181` edge `0.0084` maxDD `-0.0831`
- `market_context_high->commodity_1h` score `-0.3189` n `82` status `ready` deltaP `3.6366` edge `0.0014` maxDD `-0.9891`
- `risk_on_high->fx_4h` score `-0.3369` n `39` status `ready` deltaP `-2.3218` edge `-0.0013` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.3369` n `39` status `ready` deltaP `-2.3218` edge `-0.0013` maxDD `-0.1126`
- `market_context_high->equity_1h` score `-0.3551` n `82` status `ready` deltaP `7.5069` edge `-0.0004` maxDD `-4.6137`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
