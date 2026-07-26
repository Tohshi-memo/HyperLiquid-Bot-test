# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T07:37:27.749931+00:00`
- Price records: `672`
- Market context records: `7964`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11781`

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

- `market_context_high->equity_24h` score `16.4445` n `82` status `ready` deltaP `25.254` edge `1.3362` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.1617` n `82` status `ready` deltaP `36.7418` edge `0.4352` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7599` n `91` status `ready` deltaP `25.021` edge `0.4858` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.8052` n `82` status `ready` deltaP `27.8794` edge `0.2845` maxDD `-6.5945`
- `market_context_high->metal_4h` score `2.6833` n `91` status `ready` deltaP `23.7219` edge `0.1277` maxDD `-0.979`
- `market_context_high->index_4h` score `2.6693` n `91` status `ready` deltaP `27.3045` edge `0.0764` maxDD `-0.8791`
- `market_context_high->equity_1h` score `1.7481` n `96` status `ready` deltaP `14.1047` edge `0.1334` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.2184` n `82` status `ready` deltaP `26.1898` edge `0.0357` maxDD `-3.0343`
- `market_context_high->index_24h` score `1.1795` n `82` status `ready` deltaP `9.3962` edge `0.1556` maxDD `-1.3621`
- `market_context_high->crypto_alt_4h` score `1.1206` n `91` status `ready` deltaP `8.6103` edge `0.1477` maxDD `-3.9374`
- `market_context_high->index_1h` score `1.012` n `96` status `ready` deltaP `15.7563` edge `0.0223` maxDD `-0.7743`
- `market_context_high->crypto_major_4h` score `1.0048` n `91` status `ready` deltaP `10.6557` edge `0.1845` maxDD `-6.7444`
- `market_context_high->metal_1h` score `0.666` n `96` status `ready` deltaP `9.5309` edge `0.0298` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.4435` n `96` status `ready` deltaP `8.9259` edge `0.0384` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `0.1188` n `96` status `ready` deltaP `2.8318` edge `0.0396` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.1584` n `96` status `ready` deltaP `2.2523` edge `0.0014` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.3062` n `96` status `ready` deltaP `2.6557` edge `-0.0001` maxDD `-1.5486`
- `market_context_high->commodity_4h` score `-0.3895` n `91` status `ready` deltaP `3.9605` edge `0.0176` maxDD `-2.4502`
- `market_context_high->fx_4h` score `-0.5001` n `91` status `ready` deltaP `4.2292` edge `0.0049` maxDD `-0.9813`
- `market_context_high->unknown_1h` score `-1.6111` n `96` status `ready` deltaP `9.5372` edge `-0.1555` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
