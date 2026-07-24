# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T09:07:26.473250+00:00`
- Price records: `672`
- Market context records: `7760`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `5.803` n `132` status `ready` deltaP `24.0999` edge `0.4571` maxDD `-6.0681`
- `market_context_high->metal_24h` score `0.9488` n `133` status `ready` deltaP `10.1465` edge `0.2205` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `0.796` n `133` status `ready` deltaP `11.6609` edge `0.0327` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.5073` n `132` status `ready` deltaP `20.6552` edge `0.0361` maxDD `-3.0343`
- `market_context_high->crypto_major_4h` score `0.4721` n `133` status `ready` deltaP `12.5172` edge `0.1277` maxDD `-6.7444`
- `market_context_high->equity_4h` score `0.3989` n `133` status `ready` deltaP `1.9694` edge `0.2293` maxDD `-6.9701`
- `market_context_high->equity_1h` score `0.3518` n `133` status `ready` deltaP `7.4454` edge `0.0656` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.3038` n `133` status `ready` deltaP `8.194` edge `0.0137` maxDD `-0.7743`
- `market_context_high->crypto_alt_4h` score `0.216` n `133` status `ready` deltaP `6.8276` edge `0.0842` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `-0.0278` n `133` status `ready` deltaP `3.2304` edge `0.0194` maxDD `-1.4603`
- `market_context_high->commodity_4h` score `-0.0715` n `133` status `ready` deltaP `4.6343` edge `0.0225` maxDD `-1.0817`
- `market_context_high->commodity_1h` score `-0.0944` n `133` status `ready` deltaP `4.4458` edge `0.0084` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2608` n `133` status `ready` deltaP `10.5585` edge `0.042` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.4363` n `133` status `ready` deltaP `0.3737` edge `-0.0001` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.883` n `133` status `ready` deltaP `1.2674` edge `0.0183` maxDD `-0.6936`
- `market_context_high->commodity_24h` score `-1.3912` n `132` status `ready` deltaP `6.5569` edge `-0.0013` maxDD `-7.0012`
- `market_context_high->fx_4h` score `-1.4769` n `133` status `ready` deltaP `-3.8559` edge `-0.0008` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.5267` n `133` status `ready` deltaP `0.6808` edge `0.0737` maxDD `-1.4368`
- `market_context_high->index_24h` score `-2.1419` n `132` status `ready` deltaP `-14.7952` edge `0.0343` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.3219` n `133` status `ready` deltaP `-2.0226` edge `-0.121` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
