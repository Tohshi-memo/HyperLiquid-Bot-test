# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T19:22:25.033260+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `54.5729` n `50` status `ready` deltaP `14.2114` edge `4.453` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.1492` n `50` status `ready` deltaP `44.8735` edge `2.5074` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.4956` n `61` status `ready` deltaP `23.548` edge `0.8152` maxDD `-0.1374`
- `news_risk_high->crypto_major_24h` score `6.3949` n `50` status `ready` deltaP `24.0347` edge `0.422` maxDD `-2.6128`
- `news_risk_high->equity_24h` score `5.9563` n `50` status `ready` deltaP `30.1005` edge `0.3885` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.353` n `50` status `ready` deltaP `43.4073` edge `0.0776` maxDD `-0.0053`
- `market_context_high->unknown_24h` score `3.8816` n `120` status `ready` deltaP `7.5447` edge `0.3464` maxDD `-3.1917`
- `news_risk_high->fx_4h` score `3.4966` n `61` status `ready` deltaP `41.9157` edge `0.0295` maxDD `-0.0711`
- `news_risk_high->unknown_1h` score `3.4933` n `71` status `ready` deltaP `9.5556` edge `0.2631` maxDD `-0.8558`
- `market_context_high->metal_24h` score `3.1702` n `120` status `ready` deltaP `28.7406` edge `0.1745` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.3794` n `50` status `ready` deltaP `26.9948` edge `0.0334` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2969` n `120` status `ready` deltaP `17.5508` edge `0.1151` maxDD `-0.5894`
- `market_context_high->unknown_1h` score `0.9059` n `120` status `ready` deltaP `9.3913` edge `0.0579` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.5818` n `71` status `ready` deltaP `12.2101` edge `0.0058` maxDD `-0.0975`
- `news_risk_high->commodity_1h` score `0.4016` n `71` status `ready` deltaP `11.9107` edge `0.0041` maxDD `-0.5618`
- `market_context_high->metal_4h` score `0.0495` n `120` status `ready` deltaP `13.1504` edge `0.0104` maxDD `-3.3377`
- `news_risk_high->index_4h` score `-0.3936` n `61` status `ready` deltaP `3.0313` edge `-0.0169` maxDD `-1.3012`
- `market_context_high->fx_1h` score `-0.4044` n `120` status `ready` deltaP `3.3134` edge `-0.0007` maxDD `-0.8587`
- `news_risk_high->index_1h` score `-0.4756` n `71` status `ready` deltaP `-1.1807` edge `-0.0097` maxDD `-0.8054`
- `news_risk_high->metal_4h` score `-0.5771` n `61` status `ready` deltaP `8.7515` edge `-0.0351` maxDD `-3.7783`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
