# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T12:52:25.769983+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7738`

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

- `market_context_high->unknown_4h` score `25.5575` n `90` status `ready` deltaP `-5.8468` edge `2.2023` maxDD `-1.016`
- `market_context_high->commodity_24h` score `0.5187` n `82` status `ready` deltaP `15.8494` edge `0.0684` maxDD `-3.6055`
- `risk_on_high->index_1h` score `0.4164` n `37` status `ready` deltaP `11.8547` edge `0.0014` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4164` n `37` status `ready` deltaP `11.8547` edge `0.0014` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.3519` n `37` status `ready` deltaP `13.5014` edge `-0.0026` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.3519` n `37` status `ready` deltaP `13.5014` edge `-0.0026` maxDD `-0.7172`
- `risk_on_high->commodity_24h` score `0.1941` n `37` status `ready` deltaP `10.6748` edge `0.0335` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1941` n `37` status `ready` deltaP `10.6748` edge `0.0335` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1624` n `37` status `ready` deltaP `6.599` edge `0.0027` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1624` n `37` status `ready` deltaP `6.599` edge `0.0027` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.0495` n `37` status `ready` deltaP `2.1547` edge `0.0057` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0495` n `37` status `ready` deltaP `2.1547` edge `0.0057` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.096` n `101` status `ready` deltaP `3.0399` edge `0.0029` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.1103` n `90` status `ready` deltaP `5.7283` edge `0.0083` maxDD `-0.5168`
- `market_context_high->commodity_1h` score `-0.307` n `101` status `ready` deltaP `3.4757` edge `0.0042` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.3769` n `90` status `ready` deltaP `4.3394` edge `0.0215` maxDD `-2.8998`
- `risk_on_high->metal_1h` score `-0.4344` n `37` status `ready` deltaP `-2.4236` edge `0.006` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4344` n `37` status `ready` deltaP `-2.4236` edge `0.006` maxDD `-0.0831`
- `risk_on_high->index_4h` score `-0.5216` n `37` status `ready` deltaP `4.4002` edge `-0.0117` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.5216` n `37` status `ready` deltaP `4.4002` edge `-0.0117` maxDD `-0.7604`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
