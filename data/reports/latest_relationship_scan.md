# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T06:52:25.925778+00:00`
- Price records: `672`
- Market context records: `7960`
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

- `market_context_high->equity_24h` score `16.5071` n `82` status `ready` deltaP `25.6013` edge `1.3391` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.2105` n `82` status `ready` deltaP `37.2617` edge `0.4358` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7453` n `91` status `ready` deltaP `24.8681` edge `0.4856` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.7553` n `82` status `ready` deltaP `27.7058` edge `0.2815` maxDD `-6.5945`
- `market_context_high->metal_4h` score `2.7235` n `91` status `ready` deltaP `24.1792` edge `0.128` maxDD `-0.979`
- `market_context_high->index_4h` score `2.6669` n `91` status `ready` deltaP `27.3045` edge `0.0762` maxDD `-0.8791`
- `market_context_high->equity_1h` score `1.7231` n `94` status `ready` deltaP `13.5678` edge `0.1349` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.2649` n `82` status `ready` deltaP `26.7107` edge `0.0361` maxDD `-3.0343`
- `market_context_high->index_24h` score `1.203` n `82` status `ready` deltaP `9.7434` edge `0.1563` maxDD `-1.3621`
- `market_context_high->crypto_alt_4h` score `1.1616` n `91` status `ready` deltaP `8.7628` edge `0.1501` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.04` n `91` status `ready` deltaP `10.9606` edge `0.1854` maxDD `-6.7444`
- `market_context_high->index_1h` score `0.9606` n `94` status `ready` deltaP `15.0693` edge `0.0226` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6023` n `94` status `ready` deltaP `8.6444` edge `0.0304` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.379` n `94` status `ready` deltaP `8.2112` edge `0.0349` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `0.0267` n `94` status `ready` deltaP `1.8123` edge `0.0346` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.174` n `94` status `ready` deltaP `1.952` edge `0.0014` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.2989` n `94` status `ready` deltaP `2.6164` edge `0.0011` maxDD `-1.5486`
- `market_context_high->commodity_4h` score `-0.4334` n `91` status `ready` deltaP `3.5017` edge `0.017` maxDD `-2.4502`
- `market_context_high->fx_4h` score `-0.4598` n `91` status `ready` deltaP `4.6879` edge `0.0052` maxDD `-0.9813`
- `market_context_high->unknown_1h` score `-1.6466` n `94` status `ready` deltaP `8.7782` edge `-0.1534` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
