# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T10:22:34.115804+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4964`

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

- `market_context_high->unknown_4h` score `171.5245` n `71` status `ready` deltaP `8.6955` edge `14.2501` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `139.1998` n `83` status `ready` deltaP `2.765` edge `11.623` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `12.4827` n `46` status `ready` deltaP `29.914` edge `0.9681` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `11.783` n `46` status `ready` deltaP `36.3526` edge `0.8048` maxDD `-4.5519`
- `news_risk_high->crypto_major_4h` score `10.9766` n `65` status `ready` deltaP `39.4114` edge `0.6723` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `10.2775` n `59` status `ready` deltaP `26.7272` edge `0.6883` maxDD `-0.1353`
- `news_risk_high->crypto_alt_4h` score `7.3647` n `65` status `ready` deltaP `23.75` edge `0.5898` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.405` n `71` status `ready` deltaP `24.5685` edge `0.4403` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.6734` n `71` status `ready` deltaP `16.9894` edge `0.4051` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.5438` n `59` status `ready` deltaP `30.3819` edge `0.1761` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.9835` n `65` status `ready` deltaP `27.5891` edge `0.2093` maxDD `-2.9013`
- `market_context_high->equity_24h` score `3.3034` n `46` status `ready` deltaP `7.4199` edge `0.3255` maxDD `-6.3081`
- `news_risk_high->index_4h` score `3.205` n `65` status `ready` deltaP `34.9625` edge `0.0602` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9628` n `65` status `ready` deltaP `12.7107` edge `0.1977` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.7577` n `83` status `ready` deltaP `18.8461` edge `0.1492` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.5012` n `65` status `ready` deltaP `21.2125` edge `0.1086` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1705` n `65` status `ready` deltaP `26.6651` edge `0.0181` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.5883` n `65` status `ready` deltaP `5.0184` edge `0.1508` maxDD `-2.4854`
- `market_context_high->crypto_alt_1h` score `1.557` n `83` status `ready` deltaP `9.2075` edge `0.143` maxDD `-3.6376`
- `market_context_high->fx_24h` score `1.3214` n `46` status `ready` deltaP `24.8415` edge `0.1056` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
