# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T21:07:35.874322+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9645`

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

- `market_context_high->unknown_1h` score `84.7255` n `47` status `ready` deltaP `10.116` edge `7.0001` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `45.5009` n `47` status `ready` deltaP `30.4226` edge `3.6282` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.2068` n `47` status `ready` deltaP `24.782` edge `2.39` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.1216` n `47` status `ready` deltaP `31.9851` edge `1.9158` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.9221` n `47` status `ready` deltaP `35.6309` edge `0.4356` maxDD `-0.3705`
- `news_risk_high->unknown_1h` score `5.9373` n `114` status `ready` deltaP `-4.0498` edge `0.5462` maxDD `-0.9543`
- `market_context_high->metal_24h` score `4.0857` n `47` status `ready` deltaP `34.7112` edge `0.1329` maxDD `-0.2401`
- `news_risk_high->crypto_alt_1h` score `3.2188` n `114` status `ready` deltaP `15.4297` edge `0.2144` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.9145` n `47` status `ready` deltaP `33.4166` edge `0.0355` maxDD `-0.2323`
- `news_risk_high->crypto_major_4h` score `2.7526` n `105` status `ready` deltaP `17.6902` edge `0.3246` maxDD `-13.719`
- `news_risk_high->crypto_alt_4h` score `2.6978` n `105` status `ready` deltaP `9.232` edge `0.4084` maxDD `-15.9436`
- `news_risk_high->crypto_major_1h` score `2.4055` n `114` status `ready` deltaP `16.0705` edge `0.141` maxDD `-1.8141`
- `market_context_high->equity_4h` score `2.3745` n `47` status `ready` deltaP `16.992` edge `0.1264` maxDD `-1.3444`
- `news_risk_high->commodity_24h` score `2.1602` n `81` status `ready` deltaP `22.6852` edge `0.0886` maxDD `-1.7857`
- `news_risk_high->crypto_major_24h` score `1.741` n `81` status `ready` deltaP `-3.9351` edge `1.1537` maxDD `-63.6743`
- `news_risk_high->fx_4h` score `1.6455` n `105` status `ready` deltaP `23.7936` edge `0.0421` maxDD `-0.421`
- `news_risk_high->metal_1h` score `1.5188` n `114` status `ready` deltaP `19.511` edge `0.025` maxDD `-0.6142`
- `market_context_high->index_1h` score `1.0242` n `47` status `ready` deltaP `15.3586` edge `0.0108` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9714` n `47` status `ready` deltaP `11.9155` edge `0.0418` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.8102` n `81` status `ready` deltaP `23.2061` edge `0.094` maxDD `-7.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
