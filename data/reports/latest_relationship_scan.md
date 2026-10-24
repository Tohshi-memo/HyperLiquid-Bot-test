# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T11:07:25.208985+00:00`
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

- `market_context_high->commodity_24h` score `0.5656` n `82` status `ready` deltaP `16.1966` edge `0.0721` maxDD `-3.6055`
- `risk_on_high->index_1h` score `0.4257` n `37` status `ready` deltaP `12.0044` edge `0.0016` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4257` n `37` status `ready` deltaP `12.0044` edge `0.0016` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.3924` n `37` status `ready` deltaP `13.9505` edge `-0.0004` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.3924` n `37` status `ready` deltaP `13.9505` edge `-0.0004` maxDD `-0.7172`
- `risk_on_high->commodity_24h` score `0.2411` n `37` status `ready` deltaP `11.022` edge `0.0372` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.2411` n `37` status `ready` deltaP `11.022` edge `0.0372` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1702` n `37` status `ready` deltaP `6.7487` edge `0.0027` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1702` n `37` status `ready` deltaP `6.7487` edge `0.0027` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.0495` n `37` status `ready` deltaP `2.1547` edge `0.0057` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0495` n `37` status `ready` deltaP `2.1547` edge `0.0057` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.0555` n `94` status `ready` deltaP `3.7584` edge `0.0033` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.0669` n `83` status `ready` deltaP `6.5181` edge `0.0086` maxDD `-0.5168`
- `risk_on_high->metal_1h` score `-0.4583` n `37` status `ready` deltaP `-2.723` edge `0.006` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4583` n `37` status `ready` deltaP `-2.723` edge `0.006` maxDD `-0.0831`
- `market_context_high->commodity_1h` score `-0.4751` n `94` status `ready` deltaP `0.8281` edge `0.0003` maxDD `-1.0053`
- `risk_on_high->index_4h` score `-0.5137` n `37` status `ready` deltaP `4.5526` edge `-0.0117` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.5137` n `37` status `ready` deltaP `4.5526` edge `-0.0117` maxDD `-0.7604`
- `market_context_high->commodity_4h` score `-0.5884` n `83` status `ready` deltaP `1.2471` edge `0.015` maxDD `-2.8998`
- `market_context_high->index_1h` score `-0.6339` n `94` status `ready` deltaP `-1.7104` edge `-0.0067` maxDD `-1.0529`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
