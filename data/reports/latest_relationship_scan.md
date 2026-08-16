# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T08:07:32.055125+00:00`
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

- `market_context_high->unknown_24h` score `188.125` n `88` status `ready` deltaP `-22.5537` edge `24.5373` maxDD `-7.8016`
- `news_risk_high->equity_24h` score `12.2263` n `36` status `ready` deltaP `21.1805` edge `0.9156` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.4724` n `36` status `ready` deltaP `37.5` edge `0.3727` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.4413` n `88` status `ready` deltaP `41.3037` edge `0.3505` maxDD `-0.1266`
- `news_risk_high->index_24h` score `3.666` n `36` status `ready` deltaP `30.5556` edge `0.1018` maxDD `0.0`
- `market_context_high->commodity_4h` score `2.2202` n `102` status `ready` deltaP `20.0891` edge `0.0982` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.7231` n `36` status `ready` deltaP `19.7662` edge `0.025` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6748` n `36` status `ready` deltaP `7.535` edge `0.1212` maxDD `-0.5496`
- `market_context_high->commodity_1h` score `0.0042` n `114` status `ready` deltaP `2.847` edge `0.0225` maxDD `-0.624`
- `market_context_high->fx_1h` score `-0.0007` n `114` status `ready` deltaP `3.8949` edge `0.0021` maxDD `-0.2527`
- `market_context_high->fx_4h` score `-0.0094` n `102` status `ready` deltaP `7.3888` edge `0.01` maxDD `-0.504`
- `news_risk_high->fx_4h` score `-0.0274` n `36` status `ready` deltaP `3.794` edge `-0.0069` maxDD `-0.0863`
- `news_risk_high->index_1h` score `-0.1282` n `36` status `ready` deltaP `-0.2827` edge `0.0138` maxDD `-0.141`
- `news_risk_high->fx_1h` score `-0.2269` n `36` status `ready` deltaP `0.5323` edge `-0.0017` maxDD `-0.1414`
- `market_context_high->metal_1h` score `-0.6236` n `114` status `ready` deltaP `-0.1917` edge `-0.0071` maxDD `-1.7257`
- `news_risk_high->metal_1h` score `-0.6838` n `36` status `ready` deltaP `-7.5017` edge `-0.0108` maxDD `-0.8156`
- `market_context_high->index_1h` score `-0.73` n `114` status `ready` deltaP `-5.8383` edge `-0.0025` maxDD `-0.5064`
- `news_risk_high->metal_4h` score `-1.0007` n `36` status `ready` deltaP `-1.6768` edge `-0.0278` maxDD `-2.4791`
- `news_risk_high->commodity_1h` score `-1.1093` n `36` status `ready` deltaP `-6.0712` edge `-0.0212` maxDD `-0.7946`
- `market_context_high->metal_4h` score `-1.3062` n `102` status `ready` deltaP `1.2644` edge `-0.0185` maxDD `-4.5909`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
