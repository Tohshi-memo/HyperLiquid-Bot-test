# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T23:07:26.245688+00:00`
- Price records: `672`
- Market context records: `7926`
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

- `market_context_high->equity_24h` score `16.5702` n `82` status `ready` deltaP `25.7749` edge `1.3432` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.3762` n `82` status `ready` deltaP `39.1681` edge `0.4369` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7357` n `91` status `ready` deltaP `24.8681` edge `0.4848` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.4119` n `82` status `ready` deltaP `27.3586` edge `0.2552` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.8147` n `91` status `ready` deltaP `28.9865` edge `0.0773` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.7541` n `91` status `ready` deltaP `24.6365` edge `0.1275` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.7709` n `91` status `ready` deltaP `13.5795` edge `0.1388` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `1.3512` n `91` status `ready` deltaP `9.6774` edge `0.1598` maxDD `-3.9374`
- `market_context_high->index_24h` score `1.3052` n `82` status `ready` deltaP `10.9587` edge `0.1613` maxDD `-1.3621`
- `market_context_high->fx_24h` score `1.2414` n `82` status `ready` deltaP `26.5371` edge `0.0353` maxDD `-3.0343`
- `market_context_high->crypto_major_4h` score `1.1002` n `91` status `ready` deltaP `11.113` edge `0.1894` maxDD `-6.7444`
- `market_context_high->index_1h` score `1.0468` n `91` status `ready` deltaP `15.9819` edge `0.0237` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6288` n `91` status `ready` deltaP `8.8406` edge `0.0313` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5681` n `91` status `ready` deltaP `10.5893` edge `0.0431` maxDD `-1.6021`
- `market_context_high->crypto_alt_1h` score `0.2304` n `91` status `ready` deltaP `4.8431` edge `0.0405` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.3648` n `91` status `ready` deltaP `0.754` edge `0.0013` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.3957` n `91` status `ready` deltaP `1.1435` edge `-0.0015` maxDD `-1.5486`
- `market_context_high->commodity_4h` score `-0.503` n `91` status `ready` deltaP `2.7372` edge `0.0163` maxDD `-2.4502`
- `market_context_high->fx_4h` score `-0.5809` n `91` status `ready` deltaP `3.1589` edge `0.0053` maxDD `-0.9813`
- `market_context_high->unknown_1h` score `-1.8468` n `91` status `ready` deltaP `8.2418` edge `-0.1665` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
