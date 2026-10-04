# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T19:07:42.156738+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5060`

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

- `market_context_high->unknown_1h` score `96.8672` n `97` status `ready` deltaP `-0.1605` edge `8.1148` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `78.5678` n `97` status `ready` deltaP `2.7564` edge `6.5601` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.4937` n `65` status `ready` deltaP `37.1248` edge `0.6473` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `9.0937` n `46` status `ready` deltaP `30.2762` edge `0.6212` maxDD `-4.5519`
- `market_context_high->crypto_alt_24h` score `8.807` n `46` status `ready` deltaP `23.8376` edge `0.7023` maxDD `-8.1838`
- `news_risk_high->crypto_alt_4h` score `7.4581` n `65` status `ready` deltaP `24.5122` edge `0.5925` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `7.0552` n `65` status `ready` deltaP `21.2768` edge `0.4561` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.8272` n `97` status `ready` deltaP `21.1058` edge `0.3319` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.8297` n `65` status `ready` deltaP `26.7361` edge `0.1409` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.7932` n `65` status `ready` deltaP `25.6074` edge `0.2064` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.2793` n `65` status `ready` deltaP `35.8771` edge `0.0603` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8789` n `65` status `ready` deltaP `12.2616` edge `0.1937` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.6538` n `65` status `ready` deltaP `23.1942` edge `0.1081` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1956` n `65` status `ready` deltaP `26.9645` edge `0.0182` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `2.1404` n `97` status `ready` deltaP `15.18` edge `0.1222` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.6505` n `65` status `ready` deltaP `5.9166` edge `0.15` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `1.5713` n `97` status `ready` deltaP `6.3679` edge `0.2674` maxDD `-7.6465`
- `market_context_high->fx_4h` score `1.3813` n `97` status `ready` deltaP `24.8209` edge `0.0253` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.3646` n `46` status `ready` deltaP `25.536` edge `0.1065` maxDD `-1.8102`
- `market_context_high->fx_1h` score `0.9636` n `97` status `ready` deltaP `15.0163` edge `0.0066` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
