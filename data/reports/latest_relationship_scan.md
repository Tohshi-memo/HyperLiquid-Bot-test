# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T18:37:28.778849+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7582`

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

- `market_context_high->unknown_4h` score `12.9678` n `108` status `ready` deltaP `-1.7728` edge `1.126` maxDD `-1.016`
- `market_context_high->commodity_24h` score `0.6579` n `80` status `ready` deltaP `14.5139` edge `0.0573` maxDD `-3.6055`
- `risk_on_high->equity_1h` score `0.5281` n `36` status `ready` deltaP `16.3506` edge `0.001` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.5281` n `36` status `ready` deltaP `16.3506` edge `0.001` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.424` n `36` status `ready` deltaP `11.9261` edge `0.0019` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.424` n `36` status `ready` deltaP `11.9261` edge `0.0019` maxDD `-0.1637`
- `risk_on_high->fx_1h` score `0.3298` n `36` status `ready` deltaP `9.1484` edge `0.003` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.3298` n `36` status `ready` deltaP `9.1484` edge `0.003` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `0.1135` n `36` status `ready` deltaP `5.1829` edge `0.0064` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.1135` n `36` status `ready` deltaP `5.1829` edge `0.0064` maxDD `-0.1126`
- `risk_on_high->commodity_24h` score `0.0792` n `36` status `ready` deltaP `9.375` edge `0.0219` maxDD `-1.6066`
- `risk_on_and_context->commodity_24h` score `0.0792` n `36` status `ready` deltaP `9.375` edge `0.0219` maxDD `-1.6066`
- `market_context_high->commodity_4h` score `0.0269` n `108` status `ready` deltaP `8.2938` edge `0.0313` maxDD `-2.415`
- `market_context_high->fx_1h` score `-0.2056` n `114` status `ready` deltaP `0.9612` edge `0.0027` maxDD `-0.1712`
- `market_context_high->commodity_1h` score `-0.326` n `114` status `ready` deltaP `2.9756` edge `0.0051` maxDD `-1.0053`
- `market_context_high->fx_4h` score `-0.4517` n `108` status `ready` deltaP `-0.3727` edge `0.0052` maxDD `-0.5168`
- `risk_on_high->index_4h` score `-0.4541` n `36` status `ready` deltaP `5.4878` edge `-0.0103` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4541` n `36` status `ready` deltaP `5.4878` edge `-0.0103` maxDD `-0.7604`
- `risk_on_high->metal_1h` score `-0.5737` n `36` status `ready` deltaP `-4.2249` edge `0.0064` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.5737` n `36` status `ready` deltaP `-4.2249` edge `0.0064` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
