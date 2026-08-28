# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T16:52:29.204118+00:00`
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

- `news_risk_high->unknown_24h` score `53.9999` n `50` status `ready` deltaP `12.4783` edge `4.4168` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.1082` n `50` status `ready` deltaP `43.1404` edge `2.4322` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.2611` n `56` status `ready` deltaP `23.7369` edge `0.7944` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.6095` n `50` status `ready` deltaP `30.1005` edge `0.3596` maxDD `-4.7584`
- `news_risk_high->crypto_major_24h` score `4.8726` n `50` status `ready` deltaP `22.3016` edge `0.3067` maxDD `-2.6128`
- `news_risk_high->metal_24h` score `4.3218` n `50` status `ready` deltaP `43.4073` edge `0.075` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `4.0407` n `56` status `ready` deltaP `46.973` edge `0.0326` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `3.4759` n `62` status `ready` deltaP `11.9181` edge `0.2459` maxDD `-0.8558`
- `market_context_high->unknown_24h` score `3.3086` n `120` status `ready` deltaP `5.8116` edge `0.3102` maxDD `-3.1917`
- `market_context_high->metal_24h` score `3.139` n `120` status `ready` deltaP `28.7406` edge `0.1719` maxDD `-3.1535`
- `market_context_high->unknown_4h` score `2.8274` n `120` status `ready` deltaP `18.6179` edge `0.1522` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.3638` n `50` status `ready` deltaP `26.9948` edge `0.0321` maxDD `-0.2064`
- `news_risk_high->fx_1h` score `1.3534` n `62` status `ready` deltaP `18.3407` edge `0.0075` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.0055` n `120` status `ready` deltaP `9.3913` edge `0.0662` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.8962` n `56` status `ready` deltaP `20.0566` edge `0.0575` maxDD `-2.105`
- `news_risk_high->metal_4h` score `0.7281` n `56` status `ready` deltaP `14.3075` edge `0.0184` maxDD `-0.249`
- `news_risk_high->commodity_1h` score `0.4425` n `62` status `ready` deltaP `12.6376` edge `0.0045` maxDD `-0.5618`
- `news_risk_high->index_4h` score `0.1329` n `56` status `ready` deltaP `7.5566` edge `0.0006` maxDD `-0.1919`
- `market_context_high->metal_4h` score `-0.0388` n `120` status `ready` deltaP `12.9979` edge `0.0001` maxDD `-3.3377`
- `news_risk_high->metal_1h` score `-0.2816` n `62` status `ready` deltaP `3.5252` edge `-0.0173` maxDD `-1.718`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
