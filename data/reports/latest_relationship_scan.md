# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T05:07:24.964696+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11734`

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

- `market_context_high->unknown_24h` score `184.5397` n `88` status `ready` deltaP `-21.7524` edge `24.0723` maxDD `-7.8016`
- `news_risk_high->equity_24h` score `12.5398` n `36` status `ready` deltaP `23.1947` edge `0.9283` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6132` n `36` status `ready` deltaP `38.7195` edge `0.3763` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.2813` n `88` status `ready` deltaP `40.1883` edge `0.3446` maxDD `-0.1266`
- `news_risk_high->index_24h` score `3.6817` n `36` status `ready` deltaP `30.6759` edge `0.1023` maxDD `0.0`
- `market_context_high->commodity_4h` score `2.0803` n `102` status `ready` deltaP `18.5647` edge `0.0967` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.8645` n `36` status `ready` deltaP `21.4431` edge `0.0256` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6879` n `36` status `ready` deltaP `7.6847` edge `0.1213` maxDD `-0.5496`
- `market_context_high->commodity_1h` score `0.2912` n `102` status `ready` deltaP `5.5301` edge `0.027` maxDD `-0.5016`
- `market_context_high->fx_1h` score `0.0703` n `102` status `ready` deltaP `5.216` edge `0.0024` maxDD `-0.2527`
- `market_context_high->fx_4h` score `0.0405` n `102` status `ready` deltaP `8.3035` edge `0.0103` maxDD `-0.504`
- `news_risk_high->fx_4h` score `0.0225` n `36` status `ready` deltaP `4.7087` edge `-0.0066` maxDD `-0.0863`
- `news_risk_high->index_1h` score `-0.0671` n `36` status `ready` deltaP `0.4658` edge `0.0139` maxDD `-0.141`
- `news_risk_high->fx_1h` score `-0.1949` n `36` status `ready` deltaP `1.1311` edge `-0.0016` maxDD `-0.1414`
- `market_context_high->metal_1h` score `-0.6973` n `102` status `ready` deltaP `-1.4148` edge `-0.0084` maxDD `-1.7257`
- `news_risk_high->metal_1h` score `-0.7072` n `36` status `ready` deltaP `-7.9508` edge `-0.0108` maxDD `-0.8156`
- `market_context_high->index_1h` score `-0.9506` n `102` status `ready` deltaP `-9.9918` edge `-0.0031` maxDD `-0.5064`
- `news_risk_high->metal_4h` score `-1.0007` n `36` status `ready` deltaP `-1.6768` edge `-0.0278` maxDD `-2.4791`
- `news_risk_high->commodity_1h` score `-1.1105` n `36` status `ready` deltaP `-6.0712` edge `-0.0213` maxDD `-0.7946`
- `market_context_high->index_4h` score `-1.2673` n `102` status `ready` deltaP `-10.9098` edge `-0.0085` maxDD `-0.8328`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
