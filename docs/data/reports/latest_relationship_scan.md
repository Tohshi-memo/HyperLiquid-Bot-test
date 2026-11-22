# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T22:37:23.002345+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5108`

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

- `market_context_high->unknown_1h` score `12499.2869` n `103` status `ready` deltaP `1.292` edge `1041.6148` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `8362.2064` n `98` status `ready` deltaP `-2.7346` edge `696.8993` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1377.0526` n `31` status `ready` deltaP `3.5783` edge `114.7481` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1211.5072` n `31` status `ready` deltaP `4.2437` edge `100.9363` maxDD `-0.119`
- `news_risk_high->equity_4h` score `12.2098` n `31` status `ready` deltaP `40.4259` edge `0.7962` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0745` n `31` status `ready` deltaP `25.8457` edge `0.8376` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.8195` n `31` status `ready` deltaP `15.5586` edge `0.9123` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `4.0385` n `31` status `ready` deltaP `19.9874` edge `0.222` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.6336` n `31` status `ready` deltaP `37.682` edge `0.0776` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7358` n `31` status `ready` deltaP `31.9925` edge `0.0232` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5117` n `31` status `ready` deltaP `10.0106` edge `0.3014` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.097` n `31` status `ready` deltaP `8.5136` edge `0.2478` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.7096` n `31` status `ready` deltaP `22.8757` edge `0.1224` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.575` n `31` status `ready` deltaP `29.5827` edge `0.0326` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7559` n `31` status `ready` deltaP `17.6682` edge `0.0189` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0801` n `31` status `ready` deltaP `1.2314` edge `0.0113` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3084` n `103` status `ready` deltaP `2.962` edge `0.0072` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4225` n `103` status `ready` deltaP `1.8327` edge `0.0014` maxDD `-1.2394`
- `market_context_high->fx_4h` score `-1.2627` n `98` status `ready` deltaP `0.42` edge `0.0051` maxDD `-1.2495`
- `market_context_high->fx_1h` score `-1.3531` n `103` status `ready` deltaP `-10.4122` edge `-0.0011` maxDD `-0.3797`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
