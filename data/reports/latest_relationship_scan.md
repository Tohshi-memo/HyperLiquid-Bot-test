# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T08:52:29.924912+00:00`
- Price records: `672`
- Market context records: `7969`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11769`

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

- `market_context_high->equity_24h` score `16.3055` n `82` status `ready` deltaP `24.386` edge `1.3304` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.0804` n `82` status `ready` deltaP `35.8752` edge `0.4342` maxDD `0.0`
- `market_context_high->equity_4h` score `6.8227` n `91` status `ready` deltaP `25.716` edge `0.4864` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.908` n `82` status `ready` deltaP `28.4002` edge `0.2896` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.7265` n `91` status `ready` deltaP `28.0044` edge `0.0765` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.6151` n `91` status `ready` deltaP `22.9597` edge `0.1271` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.7439` n `97` status `ready` deltaP `14.1574` edge `0.1327` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.1569` n `82` status `ready` deltaP `25.4954` edge `0.0352` maxDD `-3.0343`
- `market_context_high->index_24h` score `1.1332` n `82` status `ready` deltaP `8.7018` edge `0.1543` maxDD `-1.3621`
- `market_context_high->crypto_alt_4h` score `1.0614` n `91` status `ready` deltaP `8.3055` edge `0.1448` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.012` n `91` status `ready` deltaP `10.6557` edge `0.1851` maxDD `-6.7444`
- `market_context_high->index_1h` score `0.9657` n `97` status `ready` deltaP `15.2085` edge `0.0221` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6465` n `97` status `ready` deltaP `9.3617` edge `0.0293` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.498` n `97` status `ready` deltaP `9.7938` edge `0.0396` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `0.0854` n `97` status `ready` deltaP `2.2949` edge `0.0389` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.1478` n `97` status `ready` deltaP `2.4875` edge `0.0012` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.3123` n `97` status `ready` deltaP `2.5371` edge `-0.0001` maxDD `-1.5486`
- `market_context_high->commodity_4h` score `-0.3524` n `91` status `ready` deltaP `4.3487` edge `0.0181` maxDD `-2.4502`
- `market_context_high->fx_4h` score `-0.4694` n `91` status `ready` deltaP `4.5969` edge `0.005` maxDD `-0.9813`
- `market_context_high->unknown_1h` score `-1.6884` n `97` status `ready` deltaP `8.7968` edge `-0.157` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
