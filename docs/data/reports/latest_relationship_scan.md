# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T19:22:23.393704+00:00`
- Price records: `672`
- Market context records: `7910`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14745`

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

- `market_context_high->equity_24h` score `15.8285` n `91` status `ready` deltaP `28.4284` edge `1.2637` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.656` n `91` status `ready` deltaP `37.8369` edge `0.39` maxDD `-0.0063`
- `market_context_high->equity_4h` score `6.1727` n `98` status `ready` deltaP `22.8109` edge `0.4516` maxDD `-5.1426`
- `market_context_high->index_4h` score `2.4568` n `98` status `ready` deltaP `25.4134` edge `0.0713` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.2507` n `98` status `ready` deltaP `19.9042` edge `0.1171` maxDD `-0.979`
- `market_context_high->commodity_24h` score `2.1214` n `91` status `ready` deltaP `20.675` edge `0.1973` maxDD `-7.0012`
- `market_context_high->index_24h` score `1.5906` n `91` status `ready` deltaP `7.8412` edge `0.1473` maxDD `-1.3621`
- `market_context_high->crypto_alt_4h` score `1.5173` n `98` status `ready` deltaP `11.5885` edge `0.1609` maxDD `-3.9374`
- `market_context_high->equity_1h` score `1.4623` n `100` status `ready` deltaP `11.5976` edge `0.1263` maxDD `-4.2072`
- `market_context_high->crypto_major_4h` score `1.1563` n `98` status `ready` deltaP `12.7146` edge `0.1834` maxDD `-6.7444`
- `market_context_high->fx_24h` score `1.1162` n `91` status `ready` deltaP `31.1641` edge `0.0441` maxDD `-3.0343`
- `market_context_high->crypto_major_1h` score `0.9938` n `100` status `ready` deltaP `12.2515` edge `0.042` maxDD `-1.6021`
- `market_context_high->index_1h` score `0.8595` n `100` status `ready` deltaP `14.0` edge `0.0213` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.5174` n `100` status `ready` deltaP `7.8982` edge `0.0283` maxDD `-0.6936`
- `market_context_high->crypto_alt_1h` score `0.2192` n `100` status `ready` deltaP `5.0479` edge `0.0377` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.1283` n `100` status `ready` deltaP `2.8018` edge `0.0016` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.15` n `98` status `ready` deltaP `7.3394` edge `0.0066` maxDD `-0.9813`
- `market_context_high->commodity_4h` score `-0.2754` n `98` status `ready` deltaP `3.7821` edge `0.0146` maxDD `-2.3427`
- `market_context_high->commodity_1h` score `-0.4569` n `100` status `ready` deltaP `0.1471` edge `-0.0027` maxDD `-1.5486`
- `market_context_high->unknown_1h` score `-2.1237` n `100` status `ready` deltaP `6.7006` edge `-0.1793` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
