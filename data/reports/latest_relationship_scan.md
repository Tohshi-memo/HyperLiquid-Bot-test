# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T13:37:30.767854+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5016`

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

- `market_context_high->unknown_4h` score `117.511` n `84` status `ready` deltaP `2.3011` edge `9.8084` maxDD `-0.4928`
- `market_context_high->unknown_1h` score `98.151` n `96` status `ready` deltaP `-0.7921` edge `8.226` maxDD `-0.9839`
- `market_context_high->crypto_alt_24h` score `10.9714` n `46` status `ready` deltaP `27.657` edge `0.8572` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `10.6029` n `46` status `ready` deltaP `34.0957` edge `0.7215` maxDD `-4.5519`
- `news_risk_high->crypto_major_4h` score `10.5663` n `65` status `ready` deltaP `37.5821` edge `0.6503` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `8.8847` n `65` status `ready` deltaP `25.0962` edge `0.5831` maxDD `-0.1344`
- `news_risk_high->crypto_alt_4h` score `7.2377` n `65` status `ready` deltaP `23.9024` edge `0.5782` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `5.7896` n `84` status `ready` deltaP `25.0363` edge `0.3859` maxDD `-3.294`
- `news_risk_high->index_24h` score `4.0752` n `65` status `ready` deltaP `28.125` edge `0.1521` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8116` n `65` status `ready` deltaP `25.9123` edge `0.2059` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.066` n `65` status `ready` deltaP `33.2857` edge `0.0598` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9448` n `65` status `ready` deltaP `12.7107` edge `0.1962` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.5512` n `65` status `ready` deltaP `21.8223` edge `0.1087` maxDD `-0.993`
- `market_context_high->equity_24h` score `2.3434` n `46` status `ready` deltaP `5.163` edge `0.26` maxDD `-6.264`
- `market_context_high->crypto_major_1h` score `2.1794` n `96` status `ready` deltaP `15.3069` edge `0.1246` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.0962` n `65` status `ready` deltaP `25.7669` edge `0.0179` maxDD `-0.1997`
- `market_context_high->crypto_alt_4h` score `1.9008` n `84` status `ready` deltaP `5.8072` edge `0.2861` maxDD `-7.6465`
- `news_risk_high->crypto_alt_1h` score `1.5606` n `65` status `ready` deltaP `5.1681` edge `0.1475` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.3599` n `46` status `ready` deltaP `25.536` edge `0.1059` maxDD `-1.8102`
- `market_context_high->fx_1h` score `0.9903` n `96` status `ready` deltaP `15.3505` edge `0.0066` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
