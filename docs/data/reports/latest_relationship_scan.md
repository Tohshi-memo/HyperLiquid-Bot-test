# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T21:53:01.884732+00:00`
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

- `market_context_high->unknown_1h` score `97.3052` n `97` status `ready` deltaP `-0.1605` edge `8.1513` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `78.7094` n `97` status `ready` deltaP `2.7564` edge `6.5719` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.2218` n `65` status `ready` deltaP `35.6004` edge `0.6348` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `8.1837` n `46` status `ready` deltaP `28.3665` edge `0.5581` maxDD `-4.5519`
- `market_context_high->crypto_alt_24h` score `7.5551` n `46` status `ready` deltaP `21.9279` edge `0.6107` maxDD `-8.1838`
- `news_risk_high->crypto_alt_4h` score `7.2899` n `65` status `ready` deltaP `23.4451` edge `0.5856` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `6.1068` n `65` status `ready` deltaP `19.367` edge `0.3898` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.5552` n `97` status `ready` deltaP `19.5814` edge `0.3194` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.7486` n `65` status `ready` deltaP `26.5625` edge `0.1353` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.5537` n `65` status `ready` deltaP `24.083` edge `0.1966` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.1674` n `65` status `ready` deltaP `34.6576` edge `0.0591` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.7183` n `65` status `ready` deltaP `11.2137` edge `0.1873` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.478` n `65` status `ready` deltaP `21.8223` edge `0.1026` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1537` n `65` status `ready` deltaP `26.5154` edge `0.0177` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `1.9798` n `97` status `ready` deltaP `14.1321` edge `0.1158` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.5678` n `65` status `ready` deltaP `5.4675` edge `0.1461` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.4286` n `97` status `ready` deltaP `25.2782` edge `0.0262` maxDD `-0.3868`
- `market_context_high->crypto_alt_4h` score `1.4031` n `97` status `ready` deltaP `5.3008` edge `0.2605` maxDD `-7.6465`
- `market_context_high->fx_24h` score `1.37` n `46` status `ready` deltaP `25.536` edge `0.1072` maxDD `-1.8102`
- `market_context_high->fx_1h` score `0.9252` n `97` status `ready` deltaP `14.5672` edge `0.0064` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
