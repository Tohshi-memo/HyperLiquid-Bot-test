# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T08:18:49.806765+00:00`
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

- `market_context_high->unknown_24h` score `188.9062` n `88` status `ready` deltaP `-22.3801` edge `24.6363` maxDD `-7.8016`
- `news_risk_high->equity_24h` score `12.204` n `36` status `ready` deltaP `21.0069` edge `0.9149` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.4566` n `36` status `ready` deltaP `37.3476` edge `0.3724` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.4461` n `88` status `ready` deltaP `41.3037` edge `0.3509` maxDD `-0.1266`
- `news_risk_high->index_24h` score `3.666` n `36` status `ready` deltaP `30.5556` edge `0.1018` maxDD `0.0`
- `market_context_high->commodity_4h` score `2.1577` n `103` status `ready` deltaP `19.5181` edge `0.0968` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.7097` n `36` status `ready` deltaP `19.6138` edge `0.0249` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6748` n `36` status `ready` deltaP `7.535` edge `0.1212` maxDD `-0.5496`
- `market_context_high->commodity_1h` score `0.0347` n `115` status `ready` deltaP `3.2283` edge `0.0225` maxDD `-0.624`
- `market_context_high->fx_4h` score `-0.0003` n `103` status `ready` deltaP `7.579` edge `0.0099` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.0269` n `115` status `ready` deltaP `3.4067` edge `0.002` maxDD `-0.2527`
- `news_risk_high->fx_4h` score `-0.0354` n `36` status `ready` deltaP `3.6416` edge `-0.0069` maxDD `-0.0863`
- `news_risk_high->index_1h` score `-0.1401` n `36` status `ready` deltaP `-0.4324` edge `0.0138` maxDD `-0.141`
- `news_risk_high->fx_1h` score `-0.2269` n `36` status `ready` deltaP `0.5323` edge `-0.0017` maxDD `-0.1414`
- `market_context_high->metal_1h` score `-0.6384` n `115` status `ready` deltaP `-0.4921` edge `-0.007` maxDD `-1.7257`
- `news_risk_high->metal_1h` score `-0.6761` n `36` status `ready` deltaP `-7.352` edge `-0.0108` maxDD `-0.8156`
- `market_context_high->index_1h` score `-0.7151` n `115` status `ready` deltaP `-5.5532` edge `-0.0025` maxDD `-0.5064`
- `news_risk_high->metal_4h` score `-1.0095` n `36` status `ready` deltaP `-1.8293` edge `-0.0279` maxDD `-2.4791`
- `news_risk_high->commodity_1h` score `-1.1093` n `36` status `ready` deltaP `-6.0712` edge `-0.0212` maxDD `-0.7946`
- `market_context_high->metal_4h` score `-1.2888` n `103` status `ready` deltaP `1.5688` edge `-0.0183` maxDD `-4.5909`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
