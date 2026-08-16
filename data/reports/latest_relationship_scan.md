# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T05:37:31.781041+00:00`
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

- `market_context_high->unknown_24h` score `184.5115` n `88` status `ready` deltaP `-22.0991` edge `24.071` maxDD `-7.8016`
- `news_risk_high->equity_24h` score `12.4893` n `36` status `ready` deltaP `22.848` edge `0.9264` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6096` n `36` status `ready` deltaP `38.7195` edge `0.376` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.3258` n `88` status `ready` deltaP `40.5349` edge `0.346` maxDD `-0.1266`
- `news_risk_high->index_24h` score `3.6654` n `36` status `ready` deltaP `30.5026` edge `0.1021` maxDD `0.0`
- `market_context_high->commodity_4h` score `2.0937` n `102` status `ready` deltaP `18.7171` edge `0.0968` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.8389` n `36` status `ready` deltaP `21.1382` edge `0.0255` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7011` n `36` status `ready` deltaP `7.8344` edge `0.1214` maxDD `-0.5496`
- `market_context_high->commodity_1h` score `0.1885` n `104` status `ready` deltaP `4.5486` edge `0.0256` maxDD `-0.5506`
- `market_context_high->fx_1h` score `0.0549` n `104` status `ready` deltaP `4.9344` edge `0.0023` maxDD `-0.2527`
- `market_context_high->fx_4h` score `0.0238` n `102` status `ready` deltaP `7.9986` edge `0.0102` maxDD `-0.504`
- `news_risk_high->fx_4h` score `0.0058` n `36` status `ready` deltaP `4.4038` edge `-0.0067` maxDD `-0.0863`
- `news_risk_high->index_1h` score `-0.0791` n `36` status `ready` deltaP `0.3161` edge `0.0139` maxDD `-0.141`
- `news_risk_high->fx_1h` score `-0.2027` n `36` status `ready` deltaP `0.9814` edge `-0.0016` maxDD `-0.1414`
- `market_context_high->metal_1h` score `-0.6882` n `104` status `ready` deltaP `-1.284` edge `-0.0081` maxDD `-1.7257`
- `news_risk_high->metal_1h` score `-0.6994` n `36` status `ready` deltaP `-7.8011` edge `-0.0108` maxDD `-0.8156`
- `market_context_high->index_1h` score `-0.902` n `104` status `ready` deltaP `-9.0857` edge `-0.0029` maxDD `-0.5064`
- `news_risk_high->metal_4h` score `-1.0007` n `36` status `ready` deltaP `-1.6768` edge `-0.0278` maxDD `-2.4791`
- `news_risk_high->commodity_1h` score `-1.0961` n `36` status `ready` deltaP `-5.9215` edge `-0.0211` maxDD `-0.7946`
- `market_context_high->index_4h` score `-1.2839` n `102` status `ready` deltaP `-11.2147` edge `-0.0086` maxDD `-0.8328`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
