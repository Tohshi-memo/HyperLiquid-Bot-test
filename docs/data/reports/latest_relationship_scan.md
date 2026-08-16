# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T07:50:08.573044+00:00`
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

- `market_context_high->unknown_24h` score `187.343` n `88` status `ready` deltaP `-22.7273` edge `24.4382` maxDD `-7.8016`
- `news_risk_high->equity_24h` score `12.2498` n `36` status `ready` deltaP `21.3541` edge `0.9164` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.487` n `36` status `ready` deltaP `37.6524` edge `0.3729` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.4365` n `88` status `ready` deltaP `41.3037` edge `0.3501` maxDD `-0.1266`
- `news_risk_high->index_24h` score `3.666` n `36` status `ready` deltaP `30.5556` edge `0.1018` maxDD `0.0`
- `market_context_high->commodity_4h` score `2.2056` n `102` status `ready` deltaP `19.9366` edge `0.098` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.7353` n `36` status `ready` deltaP `19.9187` edge `0.025` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6736` n `36` status `ready` deltaP `7.535` edge `0.1211` maxDD `-0.5496`
- `market_context_high->fx_4h` score `-0.0094` n `102` status `ready` deltaP `7.3888` edge `0.01` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.0217` n `113` status `ready` deltaP `3.5067` edge `0.002` maxDD `-0.2527`
- `news_risk_high->fx_4h` score `-0.0274` n `36` status `ready` deltaP `3.794` edge `-0.0069` maxDD `-0.0863`
- `market_context_high->commodity_1h` score `-0.0281` n `113` status `ready` deltaP `2.4588` edge `0.0224` maxDD `-0.624`
- `news_risk_high->index_1h` score `-0.1401` n `36` status `ready` deltaP `-0.4324` edge `0.0138` maxDD `-0.141`
- `news_risk_high->fx_1h` score `-0.2269` n `36` status `ready` deltaP `0.5323` edge `-0.0017` maxDD `-0.1414`
- `market_context_high->metal_1h` score `-0.6076` n `113` status `ready` deltaP `0.1166` edge `-0.0071` maxDD `-1.7257`
- `news_risk_high->metal_1h` score `-0.6916` n `36` status `ready` deltaP `-7.6514` edge `-0.0108` maxDD `-0.8156`
- `market_context_high->index_1h` score `-0.7147` n `113` status `ready` deltaP `-5.5455` edge `-0.0025` maxDD `-0.5064`
- `news_risk_high->metal_4h` score `-1.0015` n `36` status `ready` deltaP `-1.6768` edge `-0.0279` maxDD `-2.4791`
- `news_risk_high->commodity_1h` score `-1.1105` n `36` status `ready` deltaP `-6.0712` edge `-0.0213` maxDD `-0.7946`
- `market_context_high->metal_4h` score `-1.3069` n `102` status `ready` deltaP `1.2644` edge `-0.0186` maxDD `-4.5909`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
