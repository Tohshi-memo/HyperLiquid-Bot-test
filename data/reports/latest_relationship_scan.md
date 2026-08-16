# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T08:52:25.731688+00:00`
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

- `market_context_high->unknown_24h` score `190.4679` n `88` status `ready` deltaP `-22.0329` edge `24.8342` maxDD `-7.8016`
- `news_risk_high->equity_24h` score `12.1896` n `36` status `ready` deltaP `21.0069` edge `0.9137` maxDD `-1.0358`
- `market_context_high->commodity_24h` score `7.4533` n `88` status `ready` deltaP `41.3037` edge `0.3515` maxDD `-0.1266`
- `news_risk_high->equity_4h` score `7.4262` n `36` status `ready` deltaP `37.0427` edge `0.3719` maxDD `0.0`
- `news_risk_high->index_24h` score `3.6672` n `36` status `ready` deltaP `30.5556` edge `0.1019` maxDD `0.0`
- `market_context_high->commodity_4h` score `2.0781` n `105` status `ready` deltaP `18.9126` edge `0.0942` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.6841` n `36` status `ready` deltaP `19.3089` edge `0.0248` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6484` n `36` status `ready` deltaP `7.2356` edge `0.121` maxDD `-0.5496`
- `market_context_high->commodity_1h` score `0.0941` n `117` status `ready` deltaP `3.9716` edge `0.0225` maxDD `-0.624`
- `news_risk_high->fx_4h` score `-0.0274` n `36` status `ready` deltaP `3.794` edge `-0.0069` maxDD `-0.0863`
- `market_context_high->fx_4h` score `-0.0599` n `105` status `ready` deltaP `6.4924` edge `0.0095` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.0779` n `117` status `ready` deltaP `2.4554` edge `0.0018` maxDD `-0.2527`
- `news_risk_high->index_1h` score `-0.1413` n `36` status `ready` deltaP `-0.4324` edge `0.0137` maxDD `-0.141`
- `news_risk_high->fx_1h` score `-0.2269` n `36` status `ready` deltaP `0.5323` edge `-0.0017` maxDD `-0.1414`
- `market_context_high->metal_1h` score `-0.6014` n `117` status `ready` deltaP `0.1907` edge `-0.0068` maxDD `-1.7257`
- `news_risk_high->metal_1h` score `-0.6838` n `36` status `ready` deltaP `-7.5017` edge `-0.0108` maxDD `-0.8156`
- `market_context_high->index_1h` score `-0.7615` n `117` status `ready` deltaP `-6.4154` edge `-0.0027` maxDD `-0.5064`
- `news_risk_high->metal_4h` score `-1.0253` n `36` status `ready` deltaP `-2.1341` edge `-0.0279` maxDD `-2.4791`
- `news_risk_high->commodity_1h` score `-1.1093` n `36` status `ready` deltaP `-6.0712` edge `-0.0212` maxDD `-0.7946`
- `market_context_high->metal_4h` score `-1.253` n `105` status `ready` deltaP `2.1516` edge `-0.0176` maxDD `-4.5909`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
