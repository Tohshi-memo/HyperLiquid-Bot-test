# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T07:52:28.801342+00:00`
- Price records: `672`
- Market context records: `7965`
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

- `market_context_high->equity_24h` score `16.4174` n `82` status `ready` deltaP `25.0804` edge `1.3351` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.1467` n `82` status `ready` deltaP `36.5685` edge `0.4351` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7721` n `91` status `ready` deltaP `25.1739` edge `0.4858` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.8323` n `82` status `ready` deltaP `28.053` edge `0.2856` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.6815` n `91` status `ready` deltaP `27.4574` edge `0.0764` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.6699` n `91` status `ready` deltaP `23.5694` edge `0.1276` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.7601` n `96` status `ready` deltaP `14.2548` edge `0.1334` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.2022` n `82` status `ready` deltaP `26.0162` edge `0.0355` maxDD `-3.0343`
- `market_context_high->index_24h` score `1.1779` n `82` status `ready` deltaP `9.3962` edge `0.1554` maxDD `-1.3621`
- `market_context_high->crypto_alt_4h` score `1.1` n `91` status `ready` deltaP `8.4579` edge `0.147` maxDD `-3.9374`
- `market_context_high->index_1h` score `1.012` n `96` status `ready` deltaP `15.7563` edge `0.0223` maxDD `-0.7743`
- `market_context_high->crypto_major_4h` score `0.9914` n `91` status `ready` deltaP `10.5033` edge `0.1844` maxDD `-6.7444`
- `market_context_high->metal_1h` score `0.666` n `96` status `ready` deltaP `9.5309` edge `0.0298` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.4443` n `96` status `ready` deltaP `8.9259` edge `0.0385` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `0.118` n `96` status `ready` deltaP `2.8318` edge `0.0395` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.1506` n `96` status `ready` deltaP `2.4024` edge `0.0014` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.2968` n `96` status `ready` deltaP `2.8059` edge `0.0001` maxDD `-1.5486`
- `market_context_high->commodity_4h` score `-0.3749` n `91` status `ready` deltaP `4.1134` edge `0.0178` maxDD `-2.4502`
- `market_context_high->fx_4h` score `-0.5135` n `91` status `ready` deltaP `4.0763` edge `0.0048` maxDD `-0.9813`
- `market_context_high->unknown_1h` score `-1.6111` n `96` status `ready` deltaP `9.5372` edge `-0.1555` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
