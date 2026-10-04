# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T21:37:30.464389+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5012`

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

- `market_context_high->unknown_1h` score `97.2776` n `97` status `ready` deltaP `-0.1605` edge `8.149` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `78.7106` n `97` status `ready` deltaP `2.7564` edge `6.572` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.2496` n `65` status `ready` deltaP `35.7528` edge `0.6361` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `8.2696` n `46` status `ready` deltaP `28.5401` edge `0.5641` maxDD `-4.5519`
- `market_context_high->crypto_alt_24h` score `7.6638` n `46` status `ready` deltaP `22.1015` edge `0.6186` maxDD `-8.1838`
- `news_risk_high->crypto_alt_4h` score `7.3129` n `65` status `ready` deltaP `23.5976` edge `0.5865` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `6.1939` n `65` status `ready` deltaP `19.5406` edge `0.3959` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.583` n `97` status `ready` deltaP `19.7338` edge `0.3207` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.7546` n `65` status `ready` deltaP `26.5625` edge `0.1358` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.5875` n `65` status `ready` deltaP `24.2354` edge `0.1984` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.1808` n `65` status `ready` deltaP `34.8101` edge `0.0592` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.7446` n `65` status `ready` deltaP `11.3634` edge `0.1885` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.4888` n `65` status `ready` deltaP `21.8223` edge `0.1035` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1681` n `65` status `ready` deltaP `26.6651` edge `0.0179` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `2.0062` n `97` status `ready` deltaP `14.2818` edge `0.117` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.5894` n `65` status `ready` deltaP `5.6172` edge `0.1469` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.4262` n `97` status `ready` deltaP `25.2782` edge `0.026` maxDD `-0.3868`
- `market_context_high->crypto_alt_4h` score `1.4261` n `97` status `ready` deltaP `5.4533` edge `0.2614` maxDD `-7.6465`
- `market_context_high->fx_24h` score `1.37` n `46` status `ready` deltaP `25.536` edge `0.1072` maxDD `-1.8102`
- `market_context_high->fx_1h` score `0.9252` n `97` status `ready` deltaP `14.5672` edge `0.0064` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
