# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T09:07:28.792629+00:00`
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

- `market_context_high->unknown_24h` score `191.2507` n `88` status `ready` deltaP `-21.8592` edge `24.9334` maxDD `-7.8016`
- `news_risk_high->equity_24h` score `12.18` n `36` status `ready` deltaP `21.0069` edge `0.9129` maxDD `-1.0358`
- `market_context_high->commodity_24h` score `7.4581` n `88` status `ready` deltaP `41.3037` edge `0.3519` maxDD `-0.1266`
- `news_risk_high->equity_4h` score `7.4104` n `36` status `ready` deltaP `36.8902` edge `0.3716` maxDD `0.0`
- `news_risk_high->index_24h` score `3.6684` n `36` status `ready` deltaP `30.5556` edge `0.102` maxDD `0.0`
- `market_context_high->commodity_4h` score `2.0874` n `106` status `ready` deltaP `19.1642` edge `0.0933` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.6719` n `36` status `ready` deltaP `19.1565` edge `0.0248` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6352` n `36` status `ready` deltaP `7.0859` edge `0.1209` maxDD `-0.5496`
- `market_context_high->commodity_1h` score `0.1207` n `118` status `ready` deltaP `4.3337` edge `0.0223` maxDD `-0.624`
- `news_risk_high->fx_4h` score `-0.0274` n `36` status `ready` deltaP `3.794` edge `-0.0069` maxDD `-0.0863`
- `market_context_high->fx_4h` score `-0.0437` n `106` status `ready` deltaP `6.8338` edge `0.0093` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.1028` n `118` status `ready` deltaP `1.9918` edge `0.0017` maxDD `-0.2527`
- `news_risk_high->index_1h` score `-0.1533` n `36` status `ready` deltaP `-0.5821` edge `0.0137` maxDD `-0.141`
- `news_risk_high->fx_1h` score `-0.2269` n `36` status `ready` deltaP `0.5323` edge `-0.0017` maxDD `-0.1414`
- `market_context_high->metal_1h` score `-0.5795` n `118` status `ready` deltaP `0.5963` edge `-0.0067` maxDD `-1.7257`
- `news_risk_high->metal_1h` score `-0.6838` n `36` status `ready` deltaP `-7.5017` edge `-0.0108` maxDD `-0.8156`
- `market_context_high->index_1h` score `-0.7471` n `118` status `ready` deltaP `-6.1377` edge `-0.0027` maxDD `-0.5064`
- `news_risk_high->metal_4h` score `-1.034` n `36` status `ready` deltaP `-2.2866` edge `-0.028` maxDD `-2.4791`
- `news_risk_high->commodity_1h` score `-1.1093` n `36` status `ready` deltaP `-6.0712` edge `-0.0212` maxDD `-0.7946`
- `market_context_high->metal_4h` score `-1.237` n `106` status `ready` deltaP `2.4304` edge `-0.0174` maxDD `-4.5909`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
