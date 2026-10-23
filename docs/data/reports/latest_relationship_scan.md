# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-23T08:37:30.033808+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6756`

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

- `risk_on_high->index_1h` score `0.4779` n `37` status `ready` deltaP `12.6032` edge `0.0043` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4779` n `37` status `ready` deltaP `12.6032` edge `0.0043` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.4641` n `37` status `ready` deltaP `13.9505` edge `0.0088` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.4641` n `37` status `ready` deltaP `13.9505` edge `0.0088` maxDD `-0.7172`
- `risk_on_high->fx_1h` score `0.1531` n `37` status `ready` deltaP `6.4493` edge `0.0025` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1531` n `37` status `ready` deltaP `6.4493` edge `0.0025` maxDD `-0.0698`
- `market_context_high->commodity_24h` score `0.0985` n `72` status `ready` deltaP `12.6736` edge `0.0357` maxDD `-3.6055`
- `risk_on_high->commodity_24h` score `0.0952` n `37` status `ready` deltaP `11.022` edge `0.0185` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.0952` n `37` status `ready` deltaP `11.022` edge `0.0185` maxDD `-1.7154`
- `market_context_high->fx_1h` score `-0.1004` n `87` status `ready` deltaP `2.9699` edge `0.0028` maxDD `-0.1712`
- `risk_on_high->fx_4h` score `-0.1428` n `37` status `ready` deltaP `0.6303` edge `0.0039` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1428` n `37` status `ready` deltaP `0.6303` edge `0.0039` maxDD `-0.1126`
- `market_context_high->fx_4h` score `-0.1523` n `87` status `ready` deltaP `6.0047` edge `0.0079` maxDD `-0.5168`
- `risk_on_high->index_4h` score `-0.2966` n `37` status `ready` deltaP `6.6868` edge `0.0019` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.2966` n `37` status `ready` deltaP `6.6868` edge `0.0019` maxDD `-0.7604`
- `market_context_high->commodity_1h` score `-0.4148` n `87` status `ready` deltaP `1.4781` edge `0.0037` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.4562` n `87` status `ready` deltaP `4.5872` edge `0.0141` maxDD `-2.9203`
- `market_context_high->index_1h` score `-0.4899` n `87` status `ready` deltaP `2.569` edge `-0.0043` maxDD `-0.9588`
- `risk_on_high->metal_1h` score `-0.517` n `37` status `ready` deltaP `-3.3218` edge `0.0051` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.517` n `37` status `ready` deltaP `-3.3218` edge `0.0051` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
