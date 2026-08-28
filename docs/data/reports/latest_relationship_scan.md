# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T16:22:27.109940+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11634`

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

- `news_risk_high->unknown_24h` score `53.8869` n `50` status `ready` deltaP `12.1317` edge `4.4097` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.957` n `50` status `ready` deltaP `43.1404` edge `2.4196` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.1744` n `56` status `ready` deltaP `23.432` edge `0.7892` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.5579` n `50` status `ready` deltaP `30.1005` edge `0.3553` maxDD `-4.7584`
- `news_risk_high->crypto_major_24h` score `4.6289` n `50` status `ready` deltaP `21.9549` edge `0.2887` maxDD `-2.6128`
- `news_risk_high->metal_24h` score `4.3194` n `50` status `ready` deltaP `43.4073` edge `0.0748` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `4.0273` n `56` status `ready` deltaP `46.8205` edge `0.0325` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `3.668` n `61` status `ready` deltaP `12.9847` edge `0.2548` maxDD `-0.8558`
- `market_context_high->unknown_24h` score `3.1956` n `120` status `ready` deltaP `5.465` edge `0.3031` maxDD `-3.1917`
- `market_context_high->metal_24h` score `3.1366` n `120` status `ready` deltaP `28.7406` edge `0.1717` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `2.7406` n `120` status `ready` deltaP `18.313` edge `0.147` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.3626` n `50` status `ready` deltaP `26.9948` edge `0.032` maxDD `-0.2064`
- `news_risk_high->fx_1h` score `1.4195` n `61` status `ready` deltaP `19.1519` edge `0.0076` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `0.9971` n `120` status `ready` deltaP `9.2416` edge `0.0665` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.8673` n `56` status `ready` deltaP `20.0566` edge `0.0538` maxDD `-2.105`
- `news_risk_high->metal_4h` score `0.6785` n `56` status `ready` deltaP `14.0027` edge `0.0163` maxDD `-0.249`
- `news_risk_high->commodity_1h` score `0.4079` n `61` status `ready` deltaP `12.1527` edge `0.0033` maxDD `-0.5618`
- `news_risk_high->index_4h` score `0.1305` n `56` status `ready` deltaP `7.5566` edge `0.0004` maxDD `-0.1919`
- `market_context_high->metal_4h` score `-0.071` n `120` status `ready` deltaP `12.6931` edge `-0.002` maxDD `-3.3377`
- `news_risk_high->metal_1h` score `-0.1778` n `61` status `ready` deltaP `4.0984` edge `-0.0128` maxDD `-1.3186`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
