# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T18:52:29.061358+00:00`
- Price records: `672`
- Market context records: `4341`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10810`

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

- `risk_on_high->unknown_4h` score `130.9781` n `44` status `ready` deltaP `-0.5266` edge `11.1002` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.9781` n `44` status `ready` deltaP `-0.5266` edge `11.1002` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `30.6406` n `227` status `ready` deltaP `3.6799` edge `2.6868` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `11.302` n `223` status `ready` deltaP `1.7869` edge `1.4729` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.0052` n `44` status `ready` deltaP `33.398` edge `0.0325` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.0052` n `44` status `ready` deltaP `33.398` edge `0.0325` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.5835` n `44` status `ready` deltaP `-18.6553` edge `0.517` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.5835` n `44` status `ready` deltaP `-18.6553` edge `0.517` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `2.1021` n `44` status `ready` deltaP `21.7014` edge `0.0305` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.1021` n `44` status `ready` deltaP `21.7014` edge `0.0305` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.7161` n `44` status `ready` deltaP `17.5444` edge `0.0926` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.7161` n `44` status `ready` deltaP `17.5444` edge `0.0926` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.4602` n `44` status `ready` deltaP `8.6418` edge `0.0037` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.4602` n `44` status `ready` deltaP `8.6418` edge `0.0037` maxDD `-0.1704`
- `risk_on_high->metal_4h` score `0.439` n `44` status `ready` deltaP `6.4856` edge `0.0466` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.439` n `44` status `ready` deltaP `6.4856` edge `0.0466` maxDD `-1.3516`
- `risk_on_high->index_24h` score `0.3789` n `44` status `ready` deltaP `19.2708` edge `-0.0969` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.3789` n `44` status `ready` deltaP `19.2708` edge `-0.0969` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.2688` n `44` status `ready` deltaP `8.4241` edge `0.0052` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.2688` n `44` status `ready` deltaP `8.4241` edge `0.0052` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
