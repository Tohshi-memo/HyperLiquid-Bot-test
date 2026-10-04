# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T09:07:29.587351+00:00`
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

- `market_context_high->unknown_4h` score `198.2336` n `66` status `ready` deltaP `8.2687` edge `16.4787` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `158.4578` n `78` status `ready` deltaP `1.9154` edge `13.2335` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `13.2194` n `46` status `ready` deltaP `30.782` edge `1.0237` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `12.3313` n `46` status `ready` deltaP `37.2207` edge `0.8447` maxDD `-4.5519`
- `news_risk_high->crypto_major_4h` score `11.106` n `65` status `ready` deltaP `40.1736` edge `0.678` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `10.6709` n `59` status `ready` deltaP `27.5953` edge `0.7153` maxDD `-0.1353`
- `news_risk_high->crypto_alt_4h` score `7.4357` n `65` status `ready` deltaP `23.9024` edge `0.5947` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.3402` n `66` status `ready` deltaP `23.6235` edge `0.4412` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.4066` n `66` status `ready` deltaP `21.1751` edge `0.4383` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.6456` n `59` status `ready` deltaP `31.25` edge `0.1788` maxDD `0.0`
- `news_risk_high->equity_4h` score `4.0103` n `65` status `ready` deltaP `27.894` edge `0.2095` maxDD `-2.9013`
- `market_context_high->equity_24h` score `3.6968` n `46` status `ready` deltaP `8.288` edge `0.3525` maxDD `-6.3081`
- `news_risk_high->index_4h` score `3.2318` n `65` status `ready` deltaP `35.2674` edge `0.0604` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.994` n `65` status `ready` deltaP `13.0101` edge `0.1983` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.6263` n `78` status `ready` deltaP `17.3691` edge `0.1481` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.5146` n `65` status `ready` deltaP `21.3649` edge `0.1087` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.2064` n `65` status `ready` deltaP `27.1142` edge `0.0181` maxDD `-0.1997`
- `market_context_high->crypto_alt_1h` score `2.0451` n `78` status `ready` deltaP `12.7745` edge `0.1599` maxDD `-3.6376`
- `news_risk_high->crypto_alt_1h` score `1.5307` n `65` status `ready` deltaP `4.5693` edge `0.149` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.2732` n `46` status `ready` deltaP `23.9735` edge `0.1052` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
