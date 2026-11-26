# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T06:07:26.193632+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3983`

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

- `news_risk_high->unknown_1h` score `3218.8801` n `31` status `ready` deltaP `1.6322` edge `268.2467` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3213.2911` n `31` status `ready` deltaP `3.4815` edge `267.7567` maxDD `-0.1191`
- `market_context_high->unknown_1h` score `88.5882` n `31` status `ready` deltaP `1.6322` edge `7.3809` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `41.3296` n `31` status `ready` deltaP `47.5694` edge `3.127` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `39.2558` n `31` status `ready` deltaP `48.4375` edge `2.9484` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.7114` n `31` status `ready` deltaP `47.7431` edge `2.491` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.8077` n `31` status `ready` deltaP `26.4555` edge `0.8113` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.3529` n `31` status `ready` deltaP `37.5295` edge `0.6606` maxDD `-2.178`
- `news_risk_high->metal_24h` score `10.0064` n `31` status `ready` deltaP `34.1174` edge `0.6339` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.7961` n `31` status `ready` deltaP `17.3879` edge `0.8971` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.7775` n `31` status `ready` deltaP `48.9583` edge `0.2384` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.3655` n `31` status `ready` deltaP `45.8782` edge `0.1541` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6727` n `31` status `ready` deltaP `20.1371` edge `0.1905` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3776` n `31` status `ready` deltaP `36.4625` edge `0.0644` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6758` n `31` status `ready` deltaP `31.6931` edge `0.0202` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.468` n `31` status `ready` deltaP `10.0106` edge `0.2958` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2464` n `31` status `ready` deltaP `12.7052` edge `0.239` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.091` n `31` status `ready` deltaP `26.6572` edge `0.025` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.5001` n `31` status `ready` deltaP `29.433` edge `0.024` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.0874` n `31` status `ready` deltaP `16.6257` edge `0.0843` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
