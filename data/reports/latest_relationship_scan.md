# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T19:53:59.434592+00:00`
- Price records: `672`
- Market context records: `7913`
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

- `market_context_high->equity_24h` score `15.989` n `89` status `ready` deltaP `27.8851` edge `1.2807` maxDD `-6.0681`
- `market_context_high->metal_24h` score `7.8451` n `89` status `ready` deltaP `38.7378` edge `0.3997` maxDD `-0.0021`
- `market_context_high->equity_4h` score `6.2805` n `98` status `ready` deltaP `23.6784` edge `0.4548` maxDD `-5.1426`
- `market_context_high->index_4h` score `2.61` n `98` status `ready` deltaP `27.1485` edge `0.0725` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.392` n `98` status `ready` deltaP `21.6401` edge `0.1173` maxDD `-0.979`
- `market_context_high->commodity_24h` score `2.2904` n `89` status `ready` deltaP `21.3795` edge `0.2063` maxDD `-6.9701`
- `market_context_high->index_24h` score `1.6969` n `89` status `ready` deltaP `8.6298` edge `0.1509` maxDD `-1.3621`
- `market_context_high->crypto_alt_4h` score `1.5485` n `98` status `ready` deltaP `11.5885` edge `0.1635` maxDD `-3.9374`
- `market_context_high->equity_1h` score `1.4324` n `98` status `ready` deltaP `10.8629` edge `0.1287` maxDD `-4.2072`
- `market_context_high->crypto_major_4h` score `1.2199` n `98` status `ready` deltaP `12.7146` edge `0.1887` maxDD `-6.7444`
- `market_context_high->fx_24h` score `1.0614` n `89` status `ready` deltaP `30.3507` edge `0.0425` maxDD `-3.0343`
- `market_context_high->index_1h` score `0.9603` n `98` status `ready` deltaP `15.1559` edge `0.022` maxDD `-0.7743`
- `market_context_high->crypto_major_1h` score `0.9537` n `98` status `ready` deltaP `11.7958` edge `0.0417` maxDD `-1.6021`
- `market_context_high->metal_1h` score `0.5348` n `98` status `ready` deltaP `8.0411` edge `0.0288` maxDD `-0.6936`
- `market_context_high->crypto_alt_1h` score `0.2921` n `98` status `ready` deltaP `6.1499` edge `0.0397` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.0882` n `98` status `ready` deltaP `3.5423` edge `0.0018` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.1959` n `98` status `ready` deltaP `6.472` edge `0.0065` maxDD `-0.9813`
- `market_context_high->commodity_4h` score `-0.3917` n `98` status `ready` deltaP `2.0471` edge `0.0126` maxDD `-2.4502`
- `market_context_high->commodity_1h` score `-0.7748` n `98` status `ready` deltaP `-0.5118` edge `-0.0043` maxDD `-1.5486`
- `market_context_high->unknown_1h` score `-2.0053` n `98` status `ready` deltaP `7.5645` edge `-0.1752` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
