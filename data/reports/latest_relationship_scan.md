# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T22:37:27.141029+00:00`
- Price records: `672`
- Market context records: `7924`
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

- `market_context_high->equity_24h` score `16.5678` n `82` status `ready` deltaP `25.7749` edge `1.343` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.3901` n `82` status `ready` deltaP `39.3414` edge `0.4369` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7333` n `91` status `ready` deltaP `24.8681` edge `0.4846` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.3692` n `82` status `ready` deltaP `27.185` edge `0.2528` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.8281` n `91` status `ready` deltaP `29.1394` edge `0.0774` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.7285` n `91` status `ready` deltaP `24.3316` edge `0.1274` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.7841` n `91` status `ready` deltaP `13.7297` edge `0.1389` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `1.3366` n `91` status `ready` deltaP `9.525` edge `0.1596` maxDD `-3.9374`
- `market_context_high->index_24h` score `1.3189` n `82` status `ready` deltaP `11.1323` edge `0.1619` maxDD `-1.3621`
- `market_context_high->fx_24h` score `1.2203` n `82` status `ready` deltaP `26.3635` edge `0.0347` maxDD `-3.0343`
- `market_context_high->crypto_major_4h` score `1.0626` n `91` status `ready` deltaP `10.8081` edge `0.1883` maxDD `-6.7444`
- `market_context_high->index_1h` score `1.0468` n `91` status `ready` deltaP `15.9819` edge `0.0237` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6408` n `91` status `ready` deltaP `8.9903` edge `0.0313` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5767` n `91` status `ready` deltaP `10.739` edge `0.0432` maxDD `-1.6021`
- `market_context_high->crypto_alt_1h` score `0.2218` n `91` status `ready` deltaP `4.6934` edge `0.0404` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.378` n `91` status `ready` deltaP `0.6039` edge `0.0012` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.4145` n `91` status `ready` deltaP `0.8432` edge `-0.0019` maxDD `-1.5486`
- `market_context_high->commodity_4h` score `-0.5334` n `91` status `ready` deltaP `2.4314` edge `0.0158` maxDD `-2.4502`
- `market_context_high->fx_4h` score `-0.5955` n `91` status `ready` deltaP `3.006` edge `0.0051` maxDD `-0.9813`
- `market_context_high->unknown_1h` score `-1.8911` n `91` status `ready` deltaP `7.9424` edge `-0.1682` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
