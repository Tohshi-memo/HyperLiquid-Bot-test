# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T13:52:29.314474+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11602`

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

- `news_risk_high->unknown_24h` score `53.6509` n `50` status `ready` deltaP `11.6118` edge `4.3935` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.3751` n `50` status `ready` deltaP `41.9272` edge `2.3792` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `10.9662` n `56` status `ready` deltaP `22.0601` edge `0.781` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.4379` n `50` status `ready` deltaP `30.1005` edge `0.3453` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.5582` n `50` status `ready` deltaP `44.9671` edge `0.0843` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9091` n `56` status `ready` deltaP `45.4486` edge `0.0318` maxDD `-0.0559`
- `news_risk_high->crypto_major_24h` score `3.6226` n `50` status `ready` deltaP `20.2218` edge `0.2164` maxDD `-2.6128`
- `market_context_high->metal_24h` score `2.6763` n `129` status `ready` deltaP `24.4865` edge `0.1617` maxDD `-3.1535`
- `news_risk_high->index_24h` score `2.4626` n `50` status `ready` deltaP `28.0347` edge `0.0334` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.328` n `129` status `ready` deltaP `18.0457` edge `0.1144` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.2336` n `56` status `ready` deltaP `13.024` edge `0.135` maxDD `-0.8558`
- `market_context_high->unknown_24h` score `2.0825` n `129` status `ready` deltaP `5.4102` edge `0.2107` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.4803` n `56` status `ready` deltaP `19.9423` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.1075` n `56` status `ready` deltaP `15.601` edge `0.0188` maxDD `-0.4409`
- `market_context_high->unknown_1h` score `0.8755` n `129` status `ready` deltaP `7.0162` edge `0.0712` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.7787` n `56` status `ready` deltaP `19.4469` edge `0.0465` maxDD `-2.105`
- `news_risk_high->metal_4h` score `0.5523` n `56` status `ready` deltaP `12.9356` edge `0.0129` maxDD `-0.249`
- `news_risk_high->commodity_1h` score `0.5093` n `56` status `ready` deltaP `13.997` edge `0.004` maxDD `-0.5618`
- `news_risk_high->metal_1h` score `0.3195` n `56` status `ready` deltaP `6.6938` edge `0.0046` maxDD `-0.1413`
- `news_risk_high->index_4h` score `0.1074` n `56` status `ready` deltaP `7.2518` edge `0.0005` maxDD `-0.1919`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
