# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T18:22:24.038316+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11666`

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

- `news_risk_high->unknown_24h` score `54.2727` n `50` status `ready` deltaP `13.5182` edge `4.4326` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.7158` n `50` status `ready` deltaP `44.1802` edge `2.4759` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `10.704` n `57` status `ready` deltaP `23.1627` edge `0.7518` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.8099` n `50` status `ready` deltaP `30.1005` edge `0.3763` maxDD `-4.7584`
- `news_risk_high->crypto_major_24h` score `5.7298` n `50` status `ready` deltaP `23.3414` edge `0.3712` maxDD `-2.6128`
- `news_risk_high->metal_24h` score `4.3326` n `50` status `ready` deltaP `43.4073` edge `0.0759` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `4.0959` n `57` status `ready` deltaP `47.7081` edge `0.0323` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `3.5814` n `120` status `ready` deltaP `6.8515` edge `0.326` maxDD `-3.1917`
- `market_context_high->metal_24h` score `3.1498` n `120` status `ready` deltaP `28.7406` edge `0.1728` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `2.8779` n `68` status `ready` deltaP `9.7834` edge `0.2103` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `2.4688` n `120` status `ready` deltaP `17.8557` edge `0.1274` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.3734` n `50` status `ready` deltaP `26.9948` edge `0.0329` maxDD `-0.2064`
- `market_context_high->unknown_1h` score `0.9911` n `120` status `ready` deltaP `9.3913` edge `0.065` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6688` n `68` status `ready` deltaP `13.2617` edge `0.006` maxDD `-0.094`
- `news_risk_high->equity_4h` score `0.6559` n `57` status `ready` deltaP `19.1083` edge `0.0461` maxDD `-3.1515`
- `news_risk_high->commodity_1h` score `0.5662` n `68` status `ready` deltaP `14.7323` edge `0.0064` maxDD `-0.5618`
- `news_risk_high->metal_4h` score `0.5318` n `57` status `ready` deltaP `13.2382` edge `0.0134` maxDD `-0.5872`
- `market_context_high->metal_4h` score `0.0136` n `120` status `ready` deltaP `13.1504` edge `0.0058` maxDD `-3.3377`
- `news_risk_high->index_4h` score `0.0092` n `57` status `ready` deltaP `6.5227` edge `-0.0014` maxDD `-0.2729`
- `news_risk_high->index_1h` score `-0.3651` n `68` status `ready` deltaP `0.819` edge `-0.0091` maxDD `-0.787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
