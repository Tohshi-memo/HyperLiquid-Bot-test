# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T17:37:27.320501+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7576`

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

- `market_context_high->unknown_4h` score `13.251` n `108` status `ready` deltaP `-1.7728` edge `1.1496` maxDD `-1.016`
- `risk_on_high->index_1h` score `0.467` n `37` status `ready` deltaP `12.7529` edge `0.0019` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.467` n `37` status `ready` deltaP `12.7529` edge `0.0019` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.4235` n `37` status `ready` deltaP `14.3996` edge `0.0006` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.4235` n `37` status `ready` deltaP `14.3996` edge `0.0006` maxDD `-0.7172`
- `market_context_high->commodity_24h` score `0.3077` n `82` status `ready` deltaP `13.5924` edge `0.0564` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.234` n `37` status `ready` deltaP `7.9463` edge `0.0029` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.234` n `37` status `ready` deltaP `7.9463` edge `0.0029` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `0.0424` n `37` status `ready` deltaP `3.8315` edge `0.0063` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.0424` n `37` status `ready` deltaP `3.8315` edge `0.0063` maxDD `-0.1126`
- `risk_on_high->commodity_24h` score `-0.0168` n `37` status `ready` deltaP `8.4178` edge `0.0215` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.0168` n `37` status `ready` deltaP `8.4178` edge `0.0215` maxDD `-1.7154`
- `market_context_high->commodity_4h` score `-0.2001` n `108` status `ready` deltaP `6.8992` edge `0.0271` maxDD `-2.8998`
- `market_context_high->fx_1h` score `-0.2405` n `112` status `ready` deltaP `0.3208` edge `0.0025` maxDD `-0.1712`
- `market_context_high->commodity_1h` score `-0.3257` n `112` status `ready` deltaP `3.101` edge `0.0043` maxDD `-1.0053`
- `risk_on_high->index_4h` score `-0.4029` n `37` status `ready` deltaP `6.3819` edge `-0.0097` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4029` n `37` status `ready` deltaP `6.3819` edge `-0.0097` maxDD `-0.7604`
- `risk_on_high->metal_1h` score `-0.4391` n `37` status `ready` deltaP `-2.5733` edge `0.0066` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4391` n `37` status `ready` deltaP `-2.5733` edge `0.0066` maxDD `-0.0831`
- `market_context_high->fx_4h` score `-0.4501` n `108` status `ready` deltaP `-0.3727` edge `0.0054` maxDD `-0.5168`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
