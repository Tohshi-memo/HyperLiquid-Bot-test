# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T21:52:24.554350+00:00`
- Price records: `672`
- Market context records: `5707`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8874`

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

- `market_context_high->crypto_major_4h` score `1.92` n `265` status `ready` deltaP `11.6895` edge `0.2192` maxDD `-6.6368`
- `market_context_high->equity_24h` score `1.0553` n `215` status `ready` deltaP `16.7693` edge `0.5314` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `0.7726` n `265` status `ready` deltaP `8.9531` edge `0.1656` maxDD `-7.5392`
- `market_context_high->equity_4h` score `0.1767` n `265` status `ready` deltaP `6.6889` edge `0.134` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2461` n `277` status `ready` deltaP `2.3466` edge `0.0009` maxDD `-0.5144`
- `market_context_high->crypto_major_1h` score `-0.3467` n `277` status `ready` deltaP `3.9754` edge `0.0402` maxDD `-3.9811`
- `market_context_high->metal_1h` score `-0.4331` n `277` status `ready` deltaP `1.8445` edge `-0.0003` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.4956` n `277` status `ready` deltaP `2.3023` edge `0.0377` maxDD `-3.8812`
- `market_context_high->equity_1h` score `-0.5643` n `277` status `ready` deltaP `3.7901` edge `0.0284` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6401` n `277` status `ready` deltaP `0.1011` edge `0.0041` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-1.0861` n `215` status `ready` deltaP `11.2645` edge `0.0426` maxDD `-3.5553`
- `market_context_high->commodity_1h` score `-1.0991` n `277` status `ready` deltaP `-1.0609` edge `-0.0038` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2588` n `265` status `ready` deltaP `2.4528` edge `0.0057` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2609` n `265` status `ready` deltaP `-0.3785` edge `0.0096` maxDD `-3.165`
- `market_context_high->metal_4h` score `-2.6598` n `265` status `ready` deltaP `-7.9257` edge `-0.0506` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.894` n `215` status `ready` deltaP `2.0438` edge `0.0297` maxDD `-18.1481`
- `market_context_high->commodity_4h` score `-3.9206` n `265` status `ready` deltaP `-4.3149` edge `-0.0304` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.3648` n `215` status `ready` deltaP `6.0546` edge `0.0416` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.9445` n `215` status `ready` deltaP `-7.4128` edge `-0.2415` maxDD `-32.5421`
- `market_context_high->commodity_24h` score `-12.0787` n `215` status `ready` deltaP `-10.9003` edge `-0.073` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
