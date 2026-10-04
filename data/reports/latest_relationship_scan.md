# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T16:37:32.391931+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5042`

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

- `market_context_high->unknown_1h` score `96.2252` n `97` status `ready` deltaP `-0.6096` edge `8.0643` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `80.8228` n `96` status `ready` deltaP `2.1595` edge `6.752` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.6375` n `65` status `ready` deltaP `37.887` edge `0.6542` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `9.7343` n `46` status `ready` deltaP `25.5737` edge `0.768` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `9.6934` n `46` status `ready` deltaP `32.0123` edge `0.6596` maxDD `-4.5519`
- `news_risk_high->equity_24h` score `7.8517` n `65` status `ready` deltaP `23.0129` edge `0.5109` maxDD `-0.1344`
- `news_risk_high->crypto_alt_4h` score `7.4738` n `65` status `ready` deltaP `24.6646` edge `0.5928` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `4.956` n `96` status `ready` deltaP `21.621` edge `0.3392` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.8825` n `65` status `ready` deltaP `26.7361` edge `0.1453` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8454` n `65` status `ready` deltaP `26.0647` edge `0.2077` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.2074` n `65` status `ready` deltaP `34.9625` edge `0.0604` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8693` n `65` status `ready` deltaP `12.4113` edge `0.1919` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.6524` n `65` status `ready` deltaP `23.0418` edge `0.109` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1585` n `65` status `ready` deltaP `26.5154` edge `0.0181` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `2.1308` n `97` status `ready` deltaP `15.3297` edge `0.1204` maxDD `-2.2692`
- `market_context_high->crypto_alt_4h` score `1.5829` n `96` status `ready` deltaP `6.1229` edge `0.27` maxDD `-7.6465`
- `news_risk_high->crypto_alt_1h` score `1.5798` n `65` status `ready` deltaP `5.4675` edge `0.1471` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.5178` n `96` status `ready` deltaP `26.4228` edge `0.026` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.363` n `46` status `ready` deltaP `25.536` edge `0.1063` maxDD `-1.8102`
- `market_context_high->equity_24h` score `1.3104` n `46` status `ready` deltaP `3.0797` edge `0.1878` maxDD `-6.264`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
