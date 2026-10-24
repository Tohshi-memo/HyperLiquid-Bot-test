# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T06:52:25.871725+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7596`

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

- `market_context_high->commodity_24h` score `0.6` n `82` status `ready` deltaP `16.5438` edge `0.0742` maxDD `-3.6055`
- `risk_on_high->equity_1h` score `0.4477` n `37` status `ready` deltaP `14.1002` edge `0.0057` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.4477` n `37` status `ready` deltaP `14.1002` edge `0.0057` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.4452` n `37` status `ready` deltaP `12.1541` edge `0.0031` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4452` n `37` status `ready` deltaP `12.1541` edge `0.0031` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.2755` n `37` status `ready` deltaP `11.3692` edge `0.0393` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.2755` n `37` status `ready` deltaP `11.3692` edge `0.0393` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1546` n `37` status `ready` deltaP `6.4493` edge `0.0027` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1546` n `37` status `ready` deltaP `6.4493` edge `0.0027` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.0748` n `37` status `ready` deltaP `1.6974` edge `0.0055` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0748` n `37` status `ready` deltaP `1.6974` edge `0.0055` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.0945` n `82` status `ready` deltaP `3.6147` edge `0.0035` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.1228` n `82` status `ready` deltaP `5.4878` edge `0.0083` maxDD `-0.5168`
- `market_context_high->index_1h` score `-0.3181` n `82` status `ready` deltaP `2.6946` edge `-0.0051` maxDD `-0.9588`
- `risk_on_high->metal_1h` score `-0.4811` n `37` status `ready` deltaP `-3.0224` edge `0.0061` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4811` n `37` status `ready` deltaP `-3.0224` edge `0.0061` maxDD `-0.0831`
- `risk_on_high->index_4h` score `-0.4934` n `37` status `ready` deltaP `4.5526` edge `-0.0091` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.4934` n `37` status `ready` deltaP `4.5526` edge `-0.0091` maxDD `-0.7604`
- `market_context_high->commodity_1h` score `-0.5475` n `82` status `ready` deltaP `-0.2337` edge `-0.0019` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.6206` n `82` status `ready` deltaP `0.7622` edge `0.0141` maxDD `-2.8998`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
