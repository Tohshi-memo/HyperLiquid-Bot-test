# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T01:52:30.201048+00:00`
- Price records: `672`
- Market context records: `5099`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10340`

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

- `market_context_high->unknown_24h` score `19.3624` n `79` status `ready` deltaP `27.3734` edge `1.4653` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `8.2682` n `106` status `ready` deltaP `21.9656` edge `0.6448` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `7.7227` n `118` status `ready` deltaP `4.6356` edge `0.6768` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `2.9396` n `106` status `ready` deltaP `13.9784` edge `0.4436` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `2.2743` n `106` status `ready` deltaP `12.244` edge `0.4392` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.145` n `106` status `ready` deltaP `10.9872` edge `0.1867` maxDD `-6.3852`
- `market_context_high->crypto_alt_1h` score `0.5672` n `118` status `ready` deltaP `7.3302` edge `0.12` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.5446` n `118` status `ready` deltaP `9.9208` edge `0.063` maxDD `-2.745`
- `market_context_high->crypto_major_1h` score `0.469` n `118` status `ready` deltaP `8.0813` edge `0.1308` maxDD `-6.9639`
- `market_context_high->metal_1h` score `0.3189` n `118` status `ready` deltaP `9.1266` edge `0.0297` maxDD `-1.3057`
- `market_context_high->index_4h` score `0.0732` n `106` status `ready` deltaP `7.2509` edge `0.0386` maxDD `-1.204`
- `market_context_high->index_1h` score `0.0037` n `118` status `ready` deltaP `5.7825` edge `0.0123` maxDD `-1.0296`
- `market_context_high->metal_4h` score `-0.4016` n `106` status `ready` deltaP `3.2386` edge `0.0645` maxDD `-4.3397`
- `market_context_high->commodity_1h` score `-0.9144` n `118` status `ready` deltaP `-0.0482` edge `-0.0001` maxDD `-2.062`
- `market_context_high->fx_1h` score `-1.4278` n `118` status `ready` deltaP `-7.8732` edge `-0.0024` maxDD `-0.7944`
- `market_context_high->fx_24h` score `-1.5606` n `79` status `ready` deltaP `-3.1426` edge `-0.0079` maxDD `-1.7626`
- `market_context_high->commodity_24h` score `-1.676` n `79` status `ready` deltaP `7.7004` edge `0.03` maxDD `-15.0303`
- `market_context_high->fx_4h` score `-1.9958` n `106` status `ready` deltaP `-7.7284` edge `-0.0075` maxDD `-1.9169`
- `market_context_high->commodity_4h` score `-2.1143` n `106` status `ready` deltaP `2.7237` edge `-0.0243` maxDD `-7.2707`
- `market_context_high->metal_24h` score `-4.5301` n `79` status `ready` deltaP `-6.5995` edge `0.0087` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
