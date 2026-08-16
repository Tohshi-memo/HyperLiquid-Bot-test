# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T08:37:29.931877+00:00`
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

- `market_context_high->unknown_24h` score `189.6867` n `88` status `ready` deltaP `-22.2065` edge `24.7352` maxDD `-7.8016`
- `news_risk_high->equity_24h` score `12.1968` n `36` status `ready` deltaP `21.0069` edge `0.9143` maxDD `-1.0358`
- `market_context_high->commodity_24h` score `7.4497` n `88` status `ready` deltaP `41.3037` edge `0.3512` maxDD `-0.1266`
- `news_risk_high->equity_4h` score `7.442` n `36` status `ready` deltaP `37.1951` edge `0.3722` maxDD `0.0`
- `news_risk_high->index_24h` score `3.6672` n `36` status `ready` deltaP `30.5556` edge `0.1019` maxDD `0.0`
- `market_context_high->commodity_4h` score `2.083` n `104` status `ready` deltaP `18.8086` edge `0.0953` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.6975` n `36` status `ready` deltaP `19.4613` edge `0.0249` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6616` n `36` status `ready` deltaP `7.3853` edge `0.1211` maxDD `-0.5496`
- `market_context_high->commodity_1h` score `0.0647` n `116` status `ready` deltaP `3.6032` edge `0.0225` maxDD `-0.624`
- `news_risk_high->fx_4h` score `-0.0274` n `36` status `ready` deltaP `3.794` edge `-0.0069` maxDD `-0.0863`
- `market_context_high->fx_1h` score `-0.0526` n `116` status `ready` deltaP `2.9269` edge `0.0019` maxDD `-0.2527`
- `market_context_high->fx_4h` score `-0.0773` n `104` status `ready` deltaP `6.1444` edge `0.0096` maxDD `-0.504`
- `news_risk_high->index_1h` score `-0.1401` n `36` status `ready` deltaP `-0.4324` edge `0.0138` maxDD `-0.141`
- `news_risk_high->fx_1h` score `-0.2269` n `36` status `ready` deltaP `0.5323` edge `-0.0017` maxDD `-0.1414`
- `market_context_high->metal_1h` score `-0.6236` n `116` status `ready` deltaP `-0.222` edge `-0.0069` maxDD `-1.7257`
- `news_risk_high->metal_1h` score `-0.6838` n `36` status `ready` deltaP `-7.5017` edge `-0.0108` maxDD `-0.8156`
- `market_context_high->index_1h` score `-0.7385` n `116` status `ready` deltaP `-5.988` edge `-0.0026` maxDD `-0.5064`
- `news_risk_high->metal_4h` score `-1.0174` n `36` status `ready` deltaP `-1.9817` edge `-0.0279` maxDD `-2.4791`
- `news_risk_high->commodity_1h` score `-1.1093` n `36` status `ready` deltaP `-6.0712` edge `-0.0212` maxDD `-0.7946`
- `market_context_high->metal_4h` score `-1.2703` n `104` status `ready` deltaP `1.8645` edge `-0.0179` maxDD `-4.5909`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
