# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T20:07:31.181009+00:00`
- Price records: `672`
- Market context records: `7914`
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

- `market_context_high->equity_24h` score `16.0733` n `88` status `ready` deltaP `27.6042` edge `1.2896` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.0314` n `88` status `ready` deltaP `39.688` edge `0.4047` maxDD `0.0`
- `market_context_high->equity_4h` score `6.3858` n `97` status `ready` deltaP `24.3355` edge `0.4592` maxDD `-5.1426`
- `market_context_high->index_4h` score `2.6029` n `97` status `ready` deltaP `26.9696` edge `0.0731` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.4584` n `97` status `ready` deltaP `22.2451` edge `0.1188` maxDD `-0.979`
- `market_context_high->commodity_24h` score `2.4228` n `88` status `ready` deltaP `22.2222` edge `0.2115` maxDD `-6.9533`
- `market_context_high->index_24h` score `1.7492` n `88` status `ready` deltaP `9.0435` edge `0.1525` maxDD `-1.3621`
- `market_context_high->fx_24h` score `1.5868` n `88` status `ready` deltaP `29.9242` edge `0.0415` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `1.5206` n `97` status `ready` deltaP `11.2098` edge `0.1637` maxDD `-3.9374`
- `market_context_high->equity_1h` score `1.4869` n `97` status `ready` deltaP `11.3649` edge `0.1299` maxDD `-4.2072`
- `market_context_high->crypto_major_4h` score `1.1817` n `97` status `ready` deltaP `12.357` edge `0.1879` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `0.9334` n `97` status `ready` deltaP `11.5563` edge `0.0416` maxDD `-1.6021`
- `market_context_high->index_1h` score `0.9329` n `97` status `ready` deltaP `14.7983` edge `0.0221` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.5151` n `97` status `ready` deltaP `7.7489` edge `0.0291` maxDD `-0.6936`
- `market_context_high->crypto_alt_1h` score `0.3279` n `97` status `ready` deltaP `6.718` edge `0.0405` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.1155` n `97` status `ready` deltaP `3.0479` edge `0.0016` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.2177` n `97` status `ready` deltaP `6.0989` edge `0.0062` maxDD `-0.9813`
- `market_context_high->commodity_4h` score `-0.4054` n `97` status `ready` deltaP `1.7687` edge `0.0127` maxDD `-2.4502`
- `market_context_high->commodity_1h` score `-0.8084` n `97` status `ready` deltaP `-0.856` edge `-0.0048` maxDD `-1.5486`
- `market_context_high->unknown_1h` score `-1.9405` n `97` status `ready` deltaP `8.0144` edge `-0.1728` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
