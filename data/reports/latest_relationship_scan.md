# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-20T03:52:36.757787+00:00`
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

- `risk_on_high->equity_1h` score `0.7302` n `37` status `ready` deltaP `16.0463` edge `0.029` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.7302` n `37` status `ready` deltaP `16.0463` edge `0.029` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.5045` n `37` status `ready` deltaP `12.7529` edge `0.0067` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5045` n `37` status `ready` deltaP `12.7529` edge `0.0067` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.1528` n `60` status `ready` deltaP `15.3125` edge `-0.0042` maxDD `-1.8119`
- `market_context_high->index_1h` score `-0.0212` n `78` status `ready` deltaP `4.5755` edge `0.0023` maxDD `-0.5082`
- `risk_on_high->fx_1h` score `-0.0478` n `37` status `ready` deltaP `2.8565` edge `0.0007` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `-0.0478` n `37` status `ready` deltaP `2.8565` edge `0.0007` maxDD `-0.0698`
- `risk_on_high->index_4h` score `-0.1635` n `37` status `ready` deltaP `7.2965` edge `0.0149` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.1635` n `37` status `ready` deltaP `7.2965` edge `0.0149` maxDD `-0.7604`
- `risk_on_high->fx_4h` score `-0.2048` n `37` status `ready` deltaP `0.173` edge `-0.001` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2048` n `37` status `ready` deltaP `0.173` edge `-0.001` maxDD `-0.1126`
- `risk_on_high->equity_4h` score `-0.2292` n `37` status `ready` deltaP `4.1776` edge `0.0682` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.2292` n `37` status `ready` deltaP `4.1776` edge `0.0682` maxDD `-4.0351`
- `market_context_high->commodity_1h` score `-0.3163` n `78` status `ready` deltaP `3.4623` edge `0.0029` maxDD `-0.9891`
- `risk_on_high->commodity_24h` score `-0.3596` n `37` status `ready` deltaP `13.1053` edge `-0.0537` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `-0.3596` n `37` status `ready` deltaP `13.1053` edge `-0.0537` maxDD `-1.7154`
- `market_context_high->commodity_4h` score `-0.5308` n `78` status `ready` deltaP `7.0825` edge `-0.0121` maxDD `-2.9203`
- `market_context_high->metal_1h` score `-0.5755` n `78` status `ready` deltaP `-5.0822` edge `-0.0024` maxDD `-0.6669`
- `risk_on_high->metal_1h` score `-0.7242` n `37` status `ready` deltaP `-5.5673` edge `0.0028` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
