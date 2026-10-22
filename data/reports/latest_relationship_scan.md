# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-22T22:37:24.539469+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7032`

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

- `risk_on_high->equity_1h` score `0.5867` n `37` status `ready` deltaP `15.5972` edge `0.0136` maxDD `-0.7219`
- `risk_on_and_context->equity_1h` score `0.5867` n `37` status `ready` deltaP `15.5972` edge `0.0136` maxDD `-0.7219`
- `risk_on_high->index_1h` score `0.4881` n `37` status `ready` deltaP `12.9026` edge `0.0036` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4881` n `37` status `ready` deltaP `12.9026` edge `0.0036` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.4465` n `72` status `ready` deltaP `15.812` edge `0.0594` maxDD `-3.6055`
- `risk_on_high->commodity_24h` score `0.4432` n `37` status `ready` deltaP `14.1604` edge `0.0422` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.4432` n `37` status `ready` deltaP `14.1604` edge `0.0422` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.111` n `37` status `ready` deltaP `5.7008` edge `0.0021` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.111` n `37` status `ready` deltaP `5.7008` edge `0.0021` maxDD `-0.0698`
- `market_context_high->fx_1h` score `-0.1425` n `87` status `ready` deltaP `2.2214` edge `0.0024` maxDD `-0.1712`
- `risk_on_high->fx_4h` score `-0.2219` n `37` status `ready` deltaP `-0.7416` edge `0.0029` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2219` n `37` status `ready` deltaP `-0.7416` edge `0.0029` maxDD `-0.1126`
- `market_context_high->fx_4h` score `-0.2741` n `87` status `ready` deltaP `4.6328` edge `0.0069` maxDD `-0.5168`
- `risk_on_high->index_4h` score `-0.3522` n `37` status `ready` deltaP `6.3819` edge `-0.0032` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.3522` n `37` status `ready` deltaP `6.3819` edge `-0.0032` maxDD `-0.7604`
- `market_context_high->commodity_4h` score `-0.4046` n `87` status `ready` deltaP `5.6542` edge `0.0136` maxDD `-2.9203`
- `market_context_high->commodity_1h` score `-0.4537` n `87` status `ready` deltaP `0.8793` edge `0.0027` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.4743` n `87` status `ready` deltaP `2.8684` edge `-0.005` maxDD `-0.9588`
- `risk_on_high->metal_1h` score `-0.6284` n `37` status `ready` deltaP `-4.5194` edge `0.0038` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.6284` n `37` status `ready` deltaP `-4.5194` edge `0.0038` maxDD `-0.0831`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
