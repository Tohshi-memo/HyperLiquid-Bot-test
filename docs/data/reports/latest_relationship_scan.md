# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T10:07:25.951544+00:00`
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

- `market_context_high->unknown_24h` score `194.3583` n `88` status `ready` deltaP `-21.512` edge `25.3295` maxDD `-7.8016`
- `news_risk_high->equity_24h` score `12.1047` n `36` status `ready` deltaP `20.4861` edge `0.9101` maxDD `-1.0358`
- `market_context_high->commodity_24h` score `7.4881` n `88` status `ready` deltaP `41.3037` edge `0.3544` maxDD `-0.1266`
- `news_risk_high->equity_4h` score `7.3946` n `36` status `ready` deltaP `36.7378` edge `0.3713` maxDD `0.0`
- `news_risk_high->index_24h` score `3.6696` n `36` status `ready` deltaP `30.5556` edge `0.1021` maxDD `0.0`
- `market_context_high->commodity_4h` score `1.9998` n `110` status `ready` deltaP `18.7584` edge `0.0887` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.6585` n `36` status `ready` deltaP `19.004` edge `0.0247` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6328` n `36` status `ready` deltaP `7.0859` edge `0.1207` maxDD `-0.5496`
- `market_context_high->commodity_1h` score `0.0602` n `122` status `ready` deltaP `3.7131` edge `0.0214` maxDD `-0.624`
- `market_context_high->fx_4h` score `-0.035` n `110` status `ready` deltaP `7.076` edge `0.0088` maxDD `-0.504`
- `news_risk_high->fx_4h` score `-0.0354` n `36` status `ready` deltaP `3.6416` edge `-0.0069` maxDD `-0.0863`
- `market_context_high->fx_1h` score `-0.1108` n `122` status `ready` deltaP `1.8529` edge `0.0016` maxDD `-0.2527`
- `news_risk_high->index_1h` score `-0.1892` n `36` status `ready` deltaP `-1.0312` edge `0.0137` maxDD `-0.141`
- `news_risk_high->fx_1h` score `-0.2269` n `36` status `ready` deltaP `0.5323` edge `-0.0017` maxDD `-0.1414`
- `market_context_high->metal_1h` score `-0.5815` n `122` status `ready` deltaP `0.5129` edge `-0.0064` maxDD `-1.7257`
- `news_risk_high->metal_1h` score `-0.6838` n `36` status `ready` deltaP `-7.5017` edge `-0.0108` maxDD `-0.8156`
- `market_context_high->index_1h` score `-0.7278` n `122` status `ready` deltaP `-5.7671` edge `-0.0027` maxDD `-0.5064`
- `news_risk_high->metal_4h` score `-1.034` n `36` status `ready` deltaP `-2.2866` edge `-0.028` maxDD `-2.4791`
- `news_risk_high->commodity_1h` score `-1.0686` n `36` status `ready` deltaP `-5.6221` edge `-0.0208` maxDD `-0.7946`
- `market_context_high->metal_4h` score `-1.1916` n `110` status `ready` deltaP `3.1679` edge `-0.0165` maxDD `-4.5909`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
