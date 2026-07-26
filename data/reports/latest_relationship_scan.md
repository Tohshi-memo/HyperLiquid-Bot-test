# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T07:07:28.493075+00:00`
- Price records: `672`
- Market context records: `7961`
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

- `market_context_high->equity_24h` score `16.4963` n `82` status `ready` deltaP `25.6013` edge `1.3382` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.1943` n `82` status `ready` deltaP `37.0884` edge `0.4356` maxDD `0.0`
- `market_context_high->equity_4h` score `6.7453` n `91` status `ready` deltaP `24.8681` edge `0.4856` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.7661` n `82` status `ready` deltaP `27.7058` edge `0.2824` maxDD `-6.5945`
- `market_context_high->metal_4h` score `2.7113` n `91` status `ready` deltaP `24.0268` edge `0.128` maxDD `-0.979`
- `market_context_high->index_4h` score `2.6681` n `91` status `ready` deltaP `27.3045` edge `0.0763` maxDD `-0.8791`
- `market_context_high->equity_1h` score `1.7425` n `95` status `ready` deltaP `13.9149` edge `0.1342` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.2486` n `82` status `ready` deltaP `26.5371` edge `0.0359` maxDD `-3.0343`
- `market_context_high->index_24h` score `1.2014` n `82` status `ready` deltaP `9.7434` edge `0.1561` maxDD `-1.3621`
- `market_context_high->crypto_alt_4h` score `1.1508` n `91` status `ready` deltaP `8.7628` edge `0.1492` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.0364` n `91` status `ready` deltaP `10.9606` edge `0.1851` maxDD `-6.7444`
- `market_context_high->index_1h` score `0.986` n `95` status `ready` deltaP `15.4164` edge `0.0224` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.6345` n `95` status `ready` deltaP `9.0923` edge `0.0301` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.4111` n `95` status `ready` deltaP `8.648` edge `0.0361` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `0.0691` n `95` status `ready` deltaP `2.3274` edge `0.0366` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.1467` n `95` status `ready` deltaP `2.4783` edge `0.0014` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.2822` n `95` status `ready` deltaP `2.9366` edge `0.0011` maxDD `-1.5486`
- `market_context_high->commodity_4h` score `-0.4188` n `91` status `ready` deltaP `3.6546` edge `0.0172` maxDD `-2.4502`
- `market_context_high->fx_4h` score `-0.4732` n `91` status `ready` deltaP `4.535` edge `0.0051` maxDD `-0.9813`
- `market_context_high->unknown_1h` score `-1.6219` n `95` status `ready` deltaP `9.2373` edge `-0.1544` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
