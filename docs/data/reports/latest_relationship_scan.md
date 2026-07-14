# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T14:07:37.645135+00:00`
- Price records: `672`
- Market context records: `6715`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11792`

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

- `market_context_high->unknown_24h` score `1.4531` n `176` status `ready` deltaP `2.7935` edge `0.5429` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.0508` n `176` status `ready` deltaP `8.4003` edge `0.0365` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.0236` n `176` status `ready` deltaP `5.7975` edge `0.0358` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3477` n `176` status `ready` deltaP `0.4831` edge `0.0007` maxDD `-0.5468`
- `market_context_high->commodity_24h` score `-0.4954` n `176` status `ready` deltaP `7.9704` edge `0.0924` maxDD `-5.2791`
- `market_context_high->index_1h` score `-0.5562` n `176` status `ready` deltaP `-0.2688` edge `0.0019` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.646` n `176` status `ready` deltaP `-0.4525` edge `-0.0115` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.6739` n `176` status `ready` deltaP `-4.6918` edge `-0.0026` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-0.9324` n `176` status `ready` deltaP `4.0045` edge `-0.0017` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.0552` n `176` status `ready` deltaP `8.5781` edge `-0.0045` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2138` n `176` status `ready` deltaP `7.5388` edge `0.0005` maxDD `-2.1765`
- `market_context_high->unknown_1h` score `-1.3682` n `176` status `ready` deltaP `-8.6724` edge `0.0339` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6946` n `176` status `ready` deltaP `-4.0604` edge `-0.0412` maxDD `-5.5853`
- `market_context_high->crypto_major_4h` score `-1.9485` n `176` status `ready` deltaP `6.0976` edge `0.041` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.1002` n `176` status `ready` deltaP `4.5038` edge `0.0409` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.4518` n `176` status `ready` deltaP `-4.9474` edge `0.0047` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.6025` n `176` status `ready` deltaP `6.8182` edge `-0.0804` maxDD `-27.1529`
- `market_context_high->unknown_4h` score `-4.0158` n `176` status `ready` deltaP `-17.8493` edge `0.0209` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.2664` n `176` status `ready` deltaP `-7.8756` edge `0.0006` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-7.1502` n `176` status `ready` deltaP `-6.8656` edge `-0.0224` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
