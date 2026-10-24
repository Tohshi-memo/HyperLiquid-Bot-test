# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T04:37:30.739870+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7070`

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

- `market_context_high->commodity_24h` score `0.5368` n `82` status `ready` deltaP `16.5438` edge `0.0661` maxDD `-3.6055`
- `risk_on_high->equity_1h` score `0.4969` n `37` status `ready` deltaP `14.2499` edge `0.011` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.4969` n `37` status `ready` deltaP `14.2499` edge `0.011` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.4686` n `37` status `ready` deltaP `12.4535` edge `0.0041` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4686` n `37` status `ready` deltaP `12.4535` edge `0.0041` maxDD `-0.1637`
- `risk_on_high->commodity_24h` score `0.2123` n `37` status `ready` deltaP `11.3692` edge `0.0312` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.2123` n `37` status `ready` deltaP `11.3692` edge `0.0312` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.1865` n `37` status `ready` deltaP `7.0481` edge `0.0028` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1865` n `37` status `ready` deltaP `7.0481` edge `0.0028` maxDD `-0.0698`
- `risk_on_high->fx_4h` score `-0.0162` n `37` status `ready` deltaP `2.7645` edge `0.0059` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0162` n `37` status `ready` deltaP `2.7645` edge `0.0059` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.0454` n `82` status `ready` deltaP `4.2135` edge `0.0036` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.0642` n `82` status `ready` deltaP `6.5549` edge `0.0087` maxDD `-0.5168`
- `market_context_high->index_1h` score `-0.2948` n `82` status `ready` deltaP `2.994` edge `-0.0041` maxDD `-0.9588`
- `risk_on_high->index_4h` score `-0.3886` n `37` status `ready` deltaP `5.7721` edge `-0.0038` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.3886` n `37` status `ready` deltaP `5.7721` edge `-0.0038` maxDD `-0.7604`
- `risk_on_high->metal_1h` score `-0.4451` n `37` status `ready` deltaP `-2.723` edge `0.0071` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4451` n `37` status `ready` deltaP `-2.723` edge `0.0071` maxDD `-0.0831`
- `market_context_high->commodity_1h` score `-0.5755` n `82` status `ready` deltaP `-0.5331` edge `-0.0035` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.7856` n `82` status `ready` deltaP `-0.6098` edge `0.0021` maxDD `-2.8998`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
