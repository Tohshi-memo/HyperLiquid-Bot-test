# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T20:52:29.697442+00:00`
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

- `market_context_high->unknown_1h` score `97.454` n `97` status `ready` deltaP `-0.1605` edge `8.1637` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `78.719` n `97` status `ready` deltaP `2.7564` edge `6.5727` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.3317` n `65` status `ready` deltaP `36.2101` edge `0.6399` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `8.5321` n `46` status `ready` deltaP `29.061` edge `0.5825` maxDD `-4.5519`
- `market_context_high->crypto_alt_24h` score `7.9898` n `46` status `ready` deltaP `22.6223` edge `0.6423` maxDD `-8.1838`
- `news_risk_high->crypto_alt_4h` score `7.3335` n `65` status `ready` deltaP `23.75` edge `0.5872` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `6.4588` n `65` status `ready` deltaP `20.0615` edge `0.4145` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.6652` n `97` status `ready` deltaP `20.1911` edge `0.3245` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.7877` n `65` status `ready` deltaP `26.7361` edge `0.1374` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.6697` n `65` status `ready` deltaP `24.6928` edge `0.2022` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.2234` n `65` status `ready` deltaP `35.2674` edge `0.0597` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8022` n `65` status `ready` deltaP `11.6628` edge `0.1913` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.5518` n `65` status `ready` deltaP `22.2796` edge `0.1057` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1956` n `65` status `ready` deltaP `26.9645` edge `0.0182` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `2.0637` n `97` status `ready` deltaP `14.5812` edge `0.1198` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.5834` n `65` status `ready` deltaP `5.4675` edge `0.1474` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `1.4467` n `97` status `ready` deltaP `5.6057` edge `0.2621` maxDD `-7.6465`
- `market_context_high->fx_4h` score `1.3958` n `97` status `ready` deltaP `24.9733` edge `0.0255` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.3669` n `46` status `ready` deltaP `25.536` edge `0.1068` maxDD `-1.8102`
- `market_context_high->fx_1h` score `0.9121` n `97` status `ready` deltaP `14.4175` edge `0.0063` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
