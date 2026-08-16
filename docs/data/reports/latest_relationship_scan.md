# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T07:37:28.290066+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11798`

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

- `market_context_high->unknown_24h` score `186.5731` n `88` status `ready` deltaP `-22.7273` edge `24.3395` maxDD `-7.8016`
- `news_risk_high->equity_24h` score `12.2744` n `36` status `ready` deltaP `21.5277` edge `0.9173` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.5028` n `36` status `ready` deltaP `37.8049` edge `0.3732` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.4305` n `88` status `ready` deltaP `41.3037` edge `0.3496` maxDD `-0.1266`
- `news_risk_high->index_24h` score `3.666` n `36` status `ready` deltaP `30.5556` edge `0.1018` maxDD `0.0`
- `market_context_high->commodity_4h` score `2.1922` n `102` status `ready` deltaP `19.7842` edge `0.0979` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.7487` n `36` status `ready` deltaP `20.0711` edge `0.0251` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6748` n `36` status `ready` deltaP `7.535` edge `0.1212` maxDD `-0.5496`
- `market_context_high->fx_4h` score `-0.0007` n `102` status `ready` deltaP `7.5413` edge `0.0101` maxDD `-0.504`
- `news_risk_high->fx_4h` score `-0.0187` n `36` status `ready` deltaP `3.9465` edge `-0.0068` maxDD `-0.0863`
- `market_context_high->fx_1h` score `-0.0352` n `112` status `ready` deltaP `3.2613` edge `0.0019` maxDD `-0.2527`
- `market_context_high->commodity_1h` score `-0.0573` n `112` status `ready` deltaP `2.0637` edge `0.0226` maxDD `-0.624`
- `news_risk_high->index_1h` score `-0.1401` n `36` status `ready` deltaP `-0.4324` edge `0.0138` maxDD `-0.141`
- `news_risk_high->fx_1h` score `-0.2191` n `36` status `ready` deltaP `0.682` edge `-0.0017` maxDD `-0.1414`
- `market_context_high->metal_1h` score `-0.5911` n `112` status `ready` deltaP `0.4331` edge `-0.0071` maxDD `-1.7257`
- `news_risk_high->metal_1h` score `-0.6994` n `36` status `ready` deltaP `-7.8011` edge `-0.0108` maxDD `-0.8156`
- `market_context_high->index_1h` score `-0.7378` n `112` status `ready` deltaP `-5.988` edge `-0.0025` maxDD `-0.5064`
- `news_risk_high->metal_4h` score `-1.0015` n `36` status `ready` deltaP `-1.6768` edge `-0.0279` maxDD `-2.4791`
- `news_risk_high->commodity_1h` score `-1.1093` n `36` status `ready` deltaP `-6.0712` edge `-0.0212` maxDD `-0.7946`
- `market_context_high->metal_4h` score `-1.3069` n `102` status `ready` deltaP `1.2644` edge `-0.0186` maxDD `-4.5909`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
