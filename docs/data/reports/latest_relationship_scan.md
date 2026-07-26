# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T00:07:26.675047+00:00`
- Price records: `672`
- Market context records: `7931`
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

- `market_context_high->equity_24h` score `16.5618` n `82` status `ready` deltaP `25.7749` edge `1.3425` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.3552` n `82` status `ready` deltaP `38.9948` edge `0.4363` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7417` n `91` status `ready` deltaP `24.8681` edge `0.4853` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.4925` n `82` status `ready` deltaP `27.7058` edge `0.2596` maxDD `-6.5945`
- `market_context_high->metal_4h` score `2.8077` n `91` status `ready` deltaP `25.2463` edge `0.1279` maxDD `-0.979`
- `market_context_high->index_4h` score `2.7621` n `91` status `ready` deltaP `28.3749` edge `0.077` maxDD `-0.8791`
- `market_context_high->equity_1h` score `1.7433` n `91` status `ready` deltaP `13.2792` edge `0.1385` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `1.4252` n `91` status `ready` deltaP `10.2872` edge `0.1619` maxDD `-3.9374`
- `market_context_high->fx_24h` score `1.3078` n `82` status `ready` deltaP `27.2315` edge `0.0362` maxDD `-3.0343`
- `market_context_high->index_24h` score `1.2786` n `82` status `ready` deltaP `10.6115` edge `0.1602` maxDD `-1.3621`
- `market_context_high->crypto_major_4h` score `1.1922` n `91` status `ready` deltaP `11.7228` edge `0.193` maxDD `-6.7444`
- `market_context_high->index_1h` score `1.0468` n `91` status `ready` deltaP `15.9819` edge `0.0237` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6408` n `91` status `ready` deltaP `8.9903` edge `0.0313` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5969` n `91` status `ready` deltaP `11.0384` edge `0.0438` maxDD `-1.6021`
- `market_context_high->crypto_alt_1h` score `0.2662` n `91` status `ready` deltaP `5.2922` edge `0.0421` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.3942` n `91` status `ready` deltaP `1.1435` edge `-0.0013` maxDD `-1.5486`
- `market_context_high->fx_1h` score `-0.4141` n `91` status `ready` deltaP `0.1534` edge `0.0012` maxDD `-0.2715`
- `market_context_high->commodity_4h` score `-0.5176` n `91` status `ready` deltaP `2.5843` edge `0.0161` maxDD `-2.4502`
- `market_context_high->fx_4h` score `-0.554` n `91` status `ready` deltaP `3.4647` edge `0.0055` maxDD `-0.9813`
- `market_context_high->unknown_1h` score `-1.8024` n `91` status `ready` deltaP `8.6909` edge `-0.1658` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
