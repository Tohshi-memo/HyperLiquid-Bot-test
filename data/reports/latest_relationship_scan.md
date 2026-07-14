# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T17:07:29.500745+00:00`
- Price records: `672`
- Market context records: `6728`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11720`

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

- `market_context_high->unknown_24h` score `1.3673` n `176` status `ready` deltaP `2.7935` edge `0.5319` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `-0.0006` n `176` status `ready` deltaP `7.9512` edge `0.0329` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1076` n `176` status `ready` deltaP `5.3484` edge `0.0318` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.347` n `176` status `ready` deltaP `0.4831` edge `0.0008` maxDD `-0.5468`
- `market_context_high->commodity_24h` score `-0.3838` n `176` status `ready` deltaP `7.9704` edge `0.1017` maxDD `-5.2791`
- `market_context_high->index_1h` score `-0.5773` n `176` status `ready` deltaP `-0.5682` edge `0.0012` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6227` n `176` status `ready` deltaP `-0.1531` edge `-0.0105` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.6443` n `176` status `ready` deltaP `-4.3924` edge `-0.0008` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.0404` n `176` status `ready` deltaP `3.7051` edge `-0.0087` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.1995` n `176` status `ready` deltaP `6.7489` edge `-0.0108` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2154` n `176` status `ready` deltaP `7.5388` edge `0.0003` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.5216` n `176` status `ready` deltaP `-2.3836` edge `-0.0302` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.942` n `176` status `ready` deltaP `-7.7742` edge `-0.0199` maxDD `-3.2083`
- `market_context_high->crypto_major_4h` score `-2.1849` n `176` status `ready` deltaP `5.9451` edge `0.0117` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.3827` n `176` status `ready` deltaP `3.4368` edge `0.0118` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.6035` n `176` status `ready` deltaP `-6.3193` edge `-0.0056` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.9077` n `176` status `ready` deltaP `5.5987` edge `-0.1114` maxDD `-27.1529`
- `market_context_high->unknown_4h` score `-4.0354` n `176` status `ready` deltaP `-18.1541` edge `0.0213` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.3575` n `176` status `ready` deltaP `-8.7437` edge `-0.0012` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-7.5736` n `176` status `ready` deltaP `-8.9489` edge `-0.0628` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
