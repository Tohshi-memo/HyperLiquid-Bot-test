# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T06:21:05.169109+00:00`
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

- `market_context_high->unknown_24h` score `184.4818` n `88` status `ready` deltaP `-22.4457` edge `24.0695` maxDD `-7.8016`
- `news_risk_high->equity_24h` score `12.4069` n `36` status `ready` deltaP `22.3281` edge `0.923` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.5744` n `36` status `ready` deltaP `38.4146` edge `0.3751` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.3902` n `88` status `ready` deltaP `41.0549` edge `0.3479` maxDD `-0.1266`
- `news_risk_high->index_24h` score `3.6642` n `36` status `ready` deltaP `30.5026` edge `0.102` maxDD `0.0`
- `market_context_high->commodity_4h` score `2.1205` n `102` status `ready` deltaP `19.022` edge `0.097` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.7999` n `36` status `ready` deltaP `20.6809` edge `0.0253` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7011` n `36` status `ready` deltaP `7.8344` edge `0.1214` maxDD `-0.5496`
- `market_context_high->commodity_1h` score `0.1734` n `107` status `ready` deltaP `4.5008` edge `0.0247` maxDD `-0.5536`
- `market_context_high->fx_4h` score `0.0231` n `102` status `ready` deltaP `7.9986` edge `0.0101` maxDD `-0.504`
- `news_risk_high->fx_4h` score `0.005` n `36` status `ready` deltaP `4.4038` edge `-0.0068` maxDD `-0.0863`
- `market_context_high->fx_1h` score `-0.0294` n `107` status `ready` deltaP `3.3438` edge `0.0021` maxDD `-0.2527`
- `news_risk_high->index_1h` score `-0.1162` n `36` status `ready` deltaP `-0.133` edge `0.0138` maxDD `-0.141`
- `news_risk_high->fx_1h` score `-0.2027` n `36` status `ready` deltaP `0.9814` edge `-0.0016` maxDD `-0.1414`
- `news_risk_high->metal_1h` score `-0.7002` n `36` status `ready` deltaP `-7.8011` edge `-0.0109` maxDD `-0.8156`
- `market_context_high->index_1h` score `-0.8468` n `107` status `ready` deltaP `-8.025` edge `-0.0029` maxDD `-0.5064`
- `market_context_high->metal_1h` score `-0.9416` n `107` status `ready` deltaP `0.0909` edge `-0.0075` maxDD `-1.7257`
- `news_risk_high->metal_4h` score `-1.0007` n `36` status `ready` deltaP `-1.6768` edge `-0.0278` maxDD `-2.4791`
- `news_risk_high->commodity_1h` score `-1.1213` n `36` status `ready` deltaP `-6.2209` edge `-0.0212` maxDD `-0.7946`
- `market_context_high->metal_4h` score `-1.3062` n `102` status `ready` deltaP `1.2644` edge `-0.0185` maxDD `-4.5909`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
