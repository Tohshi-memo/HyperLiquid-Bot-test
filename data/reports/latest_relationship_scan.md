# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T19:22:30.976403+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7592`

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

- `market_context_high->unknown_4h` score `14.894` n `105` status `ready` deltaP `-2.3548` edge `1.2904` maxDD `-1.016`
- `market_context_high->commodity_24h` score `0.9707` n `77` status `ready` deltaP `16.5743` edge `0.0613` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.6195` n `33` status `ready` deltaP `14.0492` edge `0.0033` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.6195` n `33` status `ready` deltaP `14.0492` edge `0.0033` maxDD `-0.0698`
- `risk_on_high->commodity_24h` score `0.5327` n `33` status `ready` deltaP `14.4098` edge `0.0299` maxDD `-1.2802`
- `risk_on_and_context->commodity_24h` score `0.5327` n `33` status `ready` deltaP `14.4098` edge `0.0299` maxDD `-1.2802`
- `risk_on_high->index_1h` score `0.5266` n `33` status `ready` deltaP `13.8995` edge `0.0019` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.5266` n `33` status `ready` deltaP `13.8995` edge `0.0019` maxDD `-0.1637`
- `market_context_high->commodity_4h` score `0.5097` n `105` status `ready` deltaP `10.0726` edge `0.0381` maxDD `-1.6884`
- `risk_on_high->equity_1h` score `0.4831` n `33` status `ready` deltaP `15.6959` edge `-0.0004` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.4831` n `33` status `ready` deltaP `15.6959` edge `-0.0004` maxDD `-0.7172`
- `risk_on_high->fx_4h` score `0.201` n `33` status `ready` deltaP `6.8506` edge `0.0065` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.201` n `33` status `ready` deltaP `6.8506` edge `0.0065` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.1461` n `111` status `ready` deltaP `2.0917` edge `0.0028` maxDD `-0.1712`
- `market_context_high->commodity_1h` score `-0.2868` n `111` status `ready` deltaP `3.0143` edge `0.0057` maxDD `-1.0053`
- `market_context_high->fx_4h` score `-0.4265` n `105` status `ready` deltaP `0.0973` edge `0.0053` maxDD `-0.5168`
- `risk_on_high->metal_1h` score `-0.5535` n `33` status `ready` deltaP `-4.0193` edge `0.0065` maxDD `-0.0661`
- `risk_on_and_context->metal_1h` score `-0.5535` n `33` status `ready` deltaP `-4.0193` edge `0.0065` maxDD `-0.0661`
- `market_context_high->index_1h` score `-0.6925` n `111` status `ready` deltaP `-2.5625` edge `-0.0065` maxDD `-1.2155`
- `risk_on_high->index_4h` score `-0.7193` n `33` status `ready` deltaP `0.9423` edge `-0.014` maxDD `-0.7604`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
