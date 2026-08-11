# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T06:07:28.750342+00:00`
- Price records: `672`
- Market context records: `8640`
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

- `market_context_high->unknown_24h` score `34.0669` n `131` status `ready` deltaP `-17.7725` edge `3.2028` maxDD `-9.6329`
- `market_context_high->commodity_24h` score `0.7695` n `131` status `ready` deltaP `12.8821` edge `0.1774` maxDD `-8.5031`
- `market_context_high->commodity_1h` score `0.6561` n `180` status `ready` deltaP `9.3114` edge `0.0269` maxDD `-0.7439`
- `market_context_high->commodity_4h` score `0.637` n `169` status `ready` deltaP `10.3267` edge `0.0557` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.5356` n `131` status `ready` deltaP `17.6748` edge `0.0316` maxDD `-1.4613`
- `market_context_high->fx_1h` score `-0.2413` n `180` status `ready` deltaP `2.0925` edge `-0.0011` maxDD `-0.5028`
- `market_context_high->fx_4h` score `-0.2437` n `169` status `ready` deltaP `3.7683` edge `0.0041` maxDD `-0.504`
- `market_context_high->index_1h` score `-0.8491` n `180` status `ready` deltaP `-7.0758` edge `-0.004` maxDD `-0.948`
- `market_context_high->metal_1h` score `-0.9854` n `180` status `ready` deltaP `-7.2488` edge `-0.0144` maxDD `-2.0884`
- `market_context_high->index_4h` score `-1.3729` n `169` status `ready` deltaP `-2.6226` edge `-0.0075` maxDD `-1.4875`
- `market_context_high->equity_1h` score `-1.4708` n `180` status `ready` deltaP `-6.8662` edge `-0.0151` maxDD `-6.8818`
- `market_context_high->metal_24h` score `-2.5092` n `131` status `ready` deltaP `0.1704` edge `-0.0778` maxDD `-2.9283`
- `market_context_high->crypto_alt_1h` score `-2.6177` n `180` status `ready` deltaP `-9.1084` edge `-0.0389` maxDD `-6.4812`
- `market_context_high->crypto_major_1h` score `-3.4407` n `180` status `ready` deltaP `-7.8011` edge `-0.0443` maxDD `-11.9002`
- `market_context_high->metal_4h` score `-3.5477` n `169` status `ready` deltaP `-10.5374` edge `-0.049` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-3.9493` n `169` status `ready` deltaP `-12.1072` edge `-0.1147` maxDD `-15.8728`
- `market_context_high->index_24h` score `-4.3488` n `131` status `ready` deltaP `-14.3348` edge `-0.0573` maxDD `-6.7627`
- `market_context_high->crypto_alt_4h` score `-6.7741` n `169` status `ready` deltaP `-13.2906` edge `-0.1411` maxDD `-20.1177`
- `market_context_high->crypto_major_24h` score `-7.168` n `131` status `ready` deltaP `-15.8008` edge `-0.2365` maxDD `-33.5037`
- `market_context_high->crypto_alt_24h` score `-9.0166` n `131` status `ready` deltaP `-11.5137` edge `-0.1948` maxDD `-27.3857`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
