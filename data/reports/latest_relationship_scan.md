# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T07:07:29.539555+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11645`

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

- `market_context_high->crypto_major_24h` score `2.2585` n `74` status `ready` deltaP `5.3843` edge `0.2731` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `1.0324` n `74` status `ready` deltaP `13.0474` edge `0.2287` maxDD `-4.666`
- `market_context_high->equity_1h` score `0.9068` n `97` status `ready` deltaP `8.4265` edge `0.0498` maxDD `-0.4329`
- `market_context_high->metal_4h` score `0.5841` n `93` status `ready` deltaP `12.9836` edge `0.0197` maxDD `-1.273`
- `market_context_high->index_1h` score `0.5704` n `97` status `ready` deltaP `11.9035` edge `0.0069` maxDD `-0.0982`
- `market_context_high->unknown_1h` score `0.5136` n `97` status `ready` deltaP `9.3108` edge `0.0034` maxDD `-0.4807`
- `market_context_high->crypto_major_4h` score `0.3118` n `93` status `ready` deltaP `8.081` edge `0.0882` maxDD `-3.1677`
- `market_context_high->crypto_alt_4h` score `0.2738` n `93` status `ready` deltaP `10.3675` edge `0.0977` maxDD `-5.5373`
- `market_context_high->unknown_24h` score `0.1277` n `74` status `ready` deltaP `14.633` edge `-0.0681` maxDD `-0.1719`
- `market_context_high->metal_1h` score `-0.1288` n `97` status `ready` deltaP `3.1591` edge `0.0069` maxDD `-0.4291`
- `market_context_high->commodity_4h` score `-0.2138` n `93` status `ready` deltaP `6.2435` edge `0.016` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.2664` n `93` status `ready` deltaP `2.3914` edge `0.0004` maxDD `-0.3734`
- `market_context_high->equity_4h` score `-0.2799` n `93` status `ready` deltaP `0.8294` edge `0.0616` maxDD `-2.5696`
- `market_context_high->crypto_alt_1h` score `-0.305` n `97` status `ready` deltaP `2.8597` edge `0.022` maxDD `-2.413`
- `market_context_high->fx_1h` score `-0.4533` n `97` status `ready` deltaP `-3.4416` edge `0.001` maxDD `-0.2273`
- `market_context_high->index_4h` score `-0.486` n `93` status `ready` deltaP `1.5588` edge `0.0103` maxDD `-0.2286`
- `market_context_high->crypto_major_1h` score `-0.5099` n `97` status `ready` deltaP `0.9306` edge `0.0129` maxDD `-2.7581`
- `market_context_high->metal_24h` score `-0.7875` n `74` status `ready` deltaP `-0.6815` edge `0.0472` maxDD `-4.1564`
- `market_context_high->commodity_1h` score `-0.9408` n `97` status `ready` deltaP `-7.732` edge `-0.0078` maxDD `-1.5684`
- `market_context_high->index_24h` score `-2.8282` n `74` status `ready` deltaP `-8.2042` edge `-0.1344` maxDD `-6.5461`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
