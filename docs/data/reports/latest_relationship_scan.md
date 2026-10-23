# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-23T16:07:31.304769+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6658`

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

- `market_context_high->commodity_24h` score `1.229` n `87` status `ready` deltaP `18.4028` edge `0.0873` maxDD `-3.6055`
- `risk_on_high->equity_1h` score `0.5624` n `37` status `ready` deltaP `14.5493` edge `0.0174` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.5624` n `37` status `ready` deltaP `14.5493` edge `0.0174` maxDD `-0.7172`
- `risk_on_high->index_1h` score `0.4889` n `37` status `ready` deltaP `12.7529` edge `0.0047` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4889` n `37` status `ready` deltaP `12.7529` edge `0.0047` maxDD `-0.1637`
- `risk_on_high->fx_1h` score `0.1484` n `37` status `ready` deltaP `6.2996` edge `0.0029` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.1484` n `37` status `ready` deltaP `6.2996` edge `0.0029` maxDD `-0.0698`
- `risk_on_high->commodity_24h` score `0.1362` n `37` status `ready` deltaP `11.1956` edge `0.0226` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1362` n `37` status `ready` deltaP `11.1956` edge `0.0226` maxDD `-1.7154`
- `market_context_high->fx_4h` score `-0.0236` n `87` status `ready` deltaP `7.2242` edge `0.0105` maxDD `-0.5168`
- `risk_on_high->fx_4h` score `-0.0591` n `37` status `ready` deltaP `1.8498` edge `0.0065` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0591` n `37` status `ready` deltaP `1.8498` edge `0.0065` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.1051` n `87` status `ready` deltaP `2.8202` edge `0.0032` maxDD `-0.1712`
- `risk_on_high->index_4h` score `-0.216` n `37` status `ready` deltaP `7.9063` edge `0.0041` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.216` n `37` status `ready` deltaP `7.9063` edge `0.0041` maxDD `-0.7604`
- `market_context_high->commodity_1h` score `-0.46` n `87` status `ready` deltaP `0.8793` edge `0.0019` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.4731` n `87` status `ready` deltaP `2.7187` edge `-0.0039` maxDD `-0.9588`
- `risk_on_high->metal_1h` score `-0.5446` n `37` status `ready` deltaP `-3.6212` edge `0.0048` maxDD `-0.0831`
- `risk_on_and_context->metal_1h` score `-0.5446` n `37` status `ready` deltaP `-3.6212` edge `0.0048` maxDD `-0.0831`
- `market_context_high->commodity_4h` score `-0.6592` n `87` status `ready` deltaP `1.5384` edge `0.0084` maxDD `-2.9203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
