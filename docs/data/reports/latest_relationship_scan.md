# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T13:22:27.452080+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11609`

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

- `news_risk_high->unknown_24h` score `53.6077` n `50` status `ready` deltaP `11.6118` edge `4.3899` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.2526` n `50` status `ready` deltaP `41.5806` edge `2.3713` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.2925` n `55` status `ready` deltaP `23.3786` edge `0.7994` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.4439` n `50` status `ready` deltaP `30.1005` edge `0.3458` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.6303` n `50` status `ready` deltaP `45.3137` edge `0.088` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9133` n `55` status `ready` deltaP `45.4712` edge `0.032` maxDD `-0.0559`
- `news_risk_high->crypto_major_24h` score `3.4432` n `50` status `ready` deltaP `20.0485` edge `0.2026` maxDD `-2.6128`
- `market_context_high->metal_24h` score `2.6081` n `131` status `ready` deltaP `23.6496` edge `0.1616` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.4987` n `50` status `ready` deltaP `28.3813` edge `0.0341` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.4356` n `131` status `ready` deltaP `17.9657` edge `0.1239` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.1604` n `56` status `ready` deltaP `12.7246` edge `0.1309` maxDD `-0.8558`
- `market_context_high->unknown_24h` score `1.9388` n `131` status `ready` deltaP `5.5049` edge `0.1981` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.4935` n `56` status `ready` deltaP `20.092` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.1123` n `56` status `ready` deltaP `15.601` edge `0.0192` maxDD `-0.4409`
- `market_context_high->unknown_1h` score `0.9974` n `131` status `ready` deltaP `7.1902` edge `0.0802` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.8837` n `55` status `ready` deltaP `20.7456` edge `0.0513` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.5194` n `56` status `ready` deltaP `14.1467` edge `0.0043` maxDD `-0.5618`
- `news_risk_high->metal_4h` score `0.4769` n `55` status `ready` deltaP `12.3836` edge `0.0103` maxDD `-0.249`
- `news_risk_high->metal_1h` score `0.3351` n `56` status `ready` deltaP `6.8435` edge `0.0049` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.0732` n `55` status `ready` deltaP `6.8098` edge `0.0006` maxDD `-0.1919`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
