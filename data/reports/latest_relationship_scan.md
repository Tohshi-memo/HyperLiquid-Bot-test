# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T06:37:26.207565+00:00`
- Price records: `672`
- Market context records: `5119`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5560`

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

- `market_context_high->unknown_24h` score `24.8223` n `69` status `ready` deltaP `28.8572` edge `1.9104` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `8.1309` n `127` status `ready` deltaP `7.6689` edge `0.6906` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `7.3661` n `115` status `ready` deltaP `20.5593` edge `0.579` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.551` n `115` status `ready` deltaP `15.9001` edge `0.5165` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.9827` n `115` status `ready` deltaP `13.5963` edge `0.4705` maxDD `-14.0065`
- `market_context_high->crypto_alt_1h` score `0.9521` n `127` status `ready` deltaP `6.9145` edge `0.1294` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.7519` n `127` status `ready` deltaP `7.8457` edge `0.1349` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.6995` n `127` status `ready` deltaP `7.8905` edge `0.065` maxDD `-2.745`
- `market_context_high->equity_4h` score `0.1943` n `115` status `ready` deltaP `6.6119` edge `0.1447` maxDD `-7.4425`
- `market_context_high->metal_1h` score `0.1416` n `127` status `ready` deltaP `6.9475` edge `0.0233` maxDD `-1.4501`
- `market_context_high->index_1h` score `0.0078` n `127` status `ready` deltaP `5.4175` edge `0.0149` maxDD `-1.0296`
- `market_context_high->commodity_24h` score `-0.0017` n `69` status `ready` deltaP `14.855` edge `0.0879` maxDD `-9.639`
- `market_context_high->index_4h` score `-0.4838` n `115` status `ready` deltaP `3.4663` edge `0.0266` maxDD `-2.9391`
- `market_context_high->metal_4h` score `-0.5331` n `115` status `ready` deltaP `2.4271` edge `0.0565` maxDD `-4.6157`
- `market_context_high->fx_1h` score `-0.6613` n `127` status `ready` deltaP `-2.8337` edge `-0.0018` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.9004` n `127` status `ready` deltaP `0.4656` edge `-0.0012` maxDD `-2.155`
- `market_context_high->fx_4h` score `-1.0413` n `115` status `ready` deltaP `-4.0654` edge `0.0009` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.4974` n `69` status `ready` deltaP `-2.7551` edge `-0.009` maxDD `-1.4601`
- `market_context_high->commodity_4h` score `-2.5087` n `115` status `ready` deltaP `-0.8537` edge `-0.0301` maxDD `-7.5281`
- `market_context_high->metal_24h` score `-2.5143` n `69` status `ready` deltaP `-2.3702` edge `0.0779` maxDD `-23.4221`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
