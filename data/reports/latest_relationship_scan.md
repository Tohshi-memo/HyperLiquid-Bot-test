# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T03:37:28.184534+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11824`

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

- `market_context_high->unknown_24h` score `15.1808` n `88` status `ready` deltaP `15.0094` edge `1.1693` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.6637` n `90` status `ready` deltaP `2.3577` edge `0.5558` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5495` n `90` status `ready` deltaP `16.9276` edge `0.1009` maxDD `-2.7703`
- `market_context_high->metal_24h` score `1.3745` n `88` status `ready` deltaP `3.488` edge `0.2698` maxDD `-2.6802`
- `market_context_high->fx_24h` score `1.106` n `88` status `ready` deltaP `26.5151` edge `0.0856` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.3313` n `90` status `ready` deltaP `6.0911` edge `0.0286` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1279` n `90` status `ready` deltaP `7.3054` edge `-0.0032` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.0585` n `90` status `ready` deltaP `13.0048` edge `0.0068` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5846` n `90` status `ready` deltaP `-2.0559` edge `-0.0118` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6609` n `90` status `ready` deltaP `-1.3539` edge `-0.0223` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7217` n `90` status `ready` deltaP `3.3367` edge `0.0087` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-0.8572` n `88` status `ready` deltaP `5.4767` edge `-0.0021` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-0.8824` n `90` status `ready` deltaP `-3.3566` edge `-0.0197` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.3091` n `90` status `ready` deltaP `1.8089` edge `-0.0409` maxDD `-5.7857`
- `market_context_high->index_24h` score `-1.7996` n `88` status `ready` deltaP `-6.1553` edge `0.0298` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.8918` n `90` status `ready` deltaP `2.8543` edge `-0.108` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1828` n `90` status `ready` deltaP `-13.3502` edge `-0.0654` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.2752` n `90` status `ready` deltaP `2.1989` edge `-0.2429` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.4584` n `90` status `ready` deltaP `-11.5602` edge `-0.0738` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.9557` n `88` status `ready` deltaP `5.4451` edge `-0.1319` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
