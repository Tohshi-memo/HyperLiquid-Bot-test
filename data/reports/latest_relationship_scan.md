# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T02:07:33.615521+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6504`

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

- `risk_on_high->equity_1h` score `0.6161` n `37` status `ready` deltaP `15.2978` edge `0.0193` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.6161` n `37` status `ready` deltaP `15.2978` edge `0.0193` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.5153` n `37` status `ready` deltaP `13.202` edge `0.0051` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5153` n `37` status `ready` deltaP `13.202` edge `0.0051` maxDD `-0.1637`
- `market_context_high->commodity_24h` score `0.5044` n `82` status `ready` deltaP `16.3702` edge `0.0631` maxDD `-3.6055`
- `risk_on_high->commodity_24h` score `0.1799` n `37` status `ready` deltaP `11.1956` edge `0.0282` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1799` n `37` status `ready` deltaP `11.1956` edge `0.0282` maxDD `-1.7154`
- `risk_on_high->fx_1h` score `0.171` n `37` status `ready` deltaP `6.7487` edge `0.0028` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.171` n `37` status `ready` deltaP `6.7487` edge `0.0028` maxDD `-0.0698`
- `market_context_high->fx_1h` score `-0.0694` n `82` status `ready` deltaP `3.9141` edge `0.0036` maxDD `-0.1712`
- `risk_on_high->fx_4h` score `-0.074` n `37` status `ready` deltaP `1.6974` edge `0.0056` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.074` n `37` status `ready` deltaP `1.6974` edge `0.0056` maxDD `-0.1126`
- `market_context_high->fx_4h` score `-0.122` n `82` status `ready` deltaP `5.4878` edge `0.0084` maxDD `-0.5168`
- `market_context_high->index_1h` score `-0.2481` n `82` status `ready` deltaP `3.7425` edge `-0.0031` maxDD `-0.9588`
- `risk_on_high->index_4h` score `-0.2831` n `37` status `ready` deltaP `6.9916` edge `0.0016` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.2831` n `37` status `ready` deltaP `6.9916` edge `0.0016` maxDD `-0.7604`
- `risk_on_high->metal_1h` score `-0.4068` n `37` status `ready` deltaP `-2.2739` edge `0.0073` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.4068` n `37` status `ready` deltaP `-2.2739` edge `0.0073` maxDD `-0.0831`
- `market_context_high->commodity_1h` score `-0.5592` n `82` status `ready` deltaP `-0.3834` edge `-0.0024` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.8556` n `82` status `ready` deltaP `-1.3719` edge `-0.0018` maxDD `-2.8998`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
