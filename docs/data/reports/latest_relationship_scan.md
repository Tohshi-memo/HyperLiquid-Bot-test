# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T23:37:30.875546+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5036`

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

- `market_context_high->unknown_1h` score `97.9351` n `97` status `ready` deltaP `0.1389` edge `8.2018` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `86.6714` n `97` status `ready` deltaP `2.7564` edge `7.2354` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `9.9312` n `65` status `ready` deltaP `34.5333` edge `0.6177` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `7.5573` n `46` status `ready` deltaP `27.1512` edge `0.514` maxDD `-4.5519`
- `news_risk_high->crypto_alt_4h` score `7.0377` n `65` status `ready` deltaP `22.378` edge `0.5717` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `6.7762` n `46` status `ready` deltaP `20.7126` edge `0.5539` maxDD `-8.1838`
- `news_risk_high->equity_24h` score `5.5308` n `65` status `ready` deltaP `18.1518` edge `0.3499` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.2646` n `97` status `ready` deltaP `18.5143` edge `0.3023` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.6456` n `65` status `ready` deltaP `25.6944` edge `0.1325` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.2847` n `65` status `ready` deltaP `23.0159` edge `0.1813` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.0664` n `65` status `ready` deltaP `33.5906` edge `0.0578` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.7362` n `65` status `ready` deltaP `11.3634` edge `0.1878` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.3183` n `65` status `ready` deltaP `20.7552` edge `0.0964` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1549` n `65` status `ready` deltaP `26.5154` edge `0.0178` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `1.9978` n `97` status `ready` deltaP `14.2818` edge `0.1163` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.575` n `65` status `ready` deltaP `5.3178` edge `0.1477` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.4638` n `97` status `ready` deltaP `25.5831` edge `0.0271` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.3837` n `46` status `ready` deltaP `25.7096` edge `0.1078` maxDD `-1.8102`
- `market_context_high->crypto_alt_4h` score `1.1509` n `97` status `ready` deltaP `4.2337` edge `0.2466` maxDD `-7.6465`
- `market_context_high->fx_1h` score `0.9516` n `97` status `ready` deltaP `14.8666` edge `0.0066` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
