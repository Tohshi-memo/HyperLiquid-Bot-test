# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T09:22:31.548327+00:00`
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

- `market_context_high->unknown_24h` score `192.0221` n `88` status `ready` deltaP `-21.8592` edge `25.0323` maxDD `-7.8016`
- `news_risk_high->equity_24h` score `12.1577` n `36` status `ready` deltaP `20.8333` edge `0.9122` maxDD `-1.0358`
- `market_context_high->commodity_24h` score `7.4641` n `88` status `ready` deltaP `41.3037` edge `0.3524` maxDD `-0.1266`
- `news_risk_high->equity_4h` score `7.3946` n `36` status `ready` deltaP `36.7378` edge `0.3713` maxDD `0.0`
- `news_risk_high->index_24h` score `3.6684` n `36` status `ready` deltaP `30.5556` edge `0.102` maxDD `0.0`
- `market_context_high->commodity_4h` score `2.0818` n `107` status `ready` deltaP `19.2586` edge `0.0922` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.6585` n `36` status `ready` deltaP `19.004` edge `0.0247` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6328` n `36` status `ready` deltaP `7.0859` edge `0.1207` maxDD `-0.5496`
- `market_context_high->commodity_1h` score `0.148` n `119` status `ready` deltaP `4.6898` edge `0.0222` maxDD `-0.624`
- `news_risk_high->fx_4h` score `-0.0195` n `36` status `ready` deltaP `3.9465` edge `-0.0069` maxDD `-0.0863`
- `market_context_high->fx_4h` score `-0.0678` n `107` status `ready` deltaP `6.3868` edge `0.0092` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.0828` n `119` status `ready` deltaP `2.3763` edge `0.0017` maxDD `-0.2527`
- `news_risk_high->index_1h` score `-0.1653` n `36` status `ready` deltaP `-0.7318` edge `0.0137` maxDD `-0.141`
- `news_risk_high->fx_1h` score `-0.2269` n `36` status `ready` deltaP `0.5323` edge `-0.0017` maxDD `-0.1414`
- `market_context_high->metal_1h` score `-0.5658` n `119` status `ready` deltaP `0.8454` edge `-0.0066` maxDD `-1.7257`
- `news_risk_high->metal_1h` score `-0.6916` n `36` status `ready` deltaP `-7.6514` edge `-0.0108` maxDD `-0.8156`
- `market_context_high->index_1h` score `-0.733` n `119` status `ready` deltaP `-5.8672` edge `-0.0027` maxDD `-0.5064`
- `news_risk_high->metal_4h` score `-1.0419` n `36` status `ready` deltaP `-2.439` edge `-0.028` maxDD `-2.4791`
- `news_risk_high->commodity_1h` score `-1.1081` n `36` status `ready` deltaP `-6.0712` edge `-0.0211` maxDD `-0.7946`
- `market_context_high->metal_4h` score `-1.2205` n `107` status `ready` deltaP `2.7012` edge `-0.0171` maxDD `-4.5909`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
