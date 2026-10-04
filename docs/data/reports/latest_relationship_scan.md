# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T08:52:28.187239+00:00`
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

- `market_context_high->unknown_4h` score `204.0653` n `65` status `ready` deltaP `8.1755` edge `16.9653` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `162.6011` n `77` status `ready` deltaP `1.7323` edge `13.58` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `13.3055` n `46` status `ready` deltaP `30.8681` edge `1.0303` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `12.3985` n `46` status `ready` deltaP `37.3106` edge `0.8497` maxDD `-4.5519`
- `news_risk_high->crypto_major_4h` score `11.1072` n `65` status `ready` deltaP `40.1736` edge `0.6781` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `10.7364` n `59` status `ready` deltaP `27.709` edge `0.72` maxDD `-0.1353`
- `news_risk_high->crypto_alt_4h` score `7.4527` n `65` status `ready` deltaP `24.0549` edge `0.5951` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.3319` n `65` status `ready` deltaP `23.2505` edge `0.443` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.4497` n `65` status `ready` deltaP `20.978` edge `0.4432` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.6623` n `59` status `ready` deltaP `31.3692` edge `0.1794` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.9969` n `65` status `ready` deltaP `27.7415` edge `0.2094` maxDD `-2.9013`
- `market_context_high->equity_24h` score `3.7623` n `46` status `ready` deltaP `8.4017` edge `0.3572` maxDD `-6.3081`
- `news_risk_high->index_4h` score `3.2318` n `65` status `ready` deltaP `35.2674` edge `0.0604` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9808` n `65` status `ready` deltaP `12.8604` edge `0.1982` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.7152` n `77` status `ready` deltaP `18.1352` edge `0.1504` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.5268` n `65` status `ready` deltaP `21.5174` edge `0.1087` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.2184` n `65` status `ready` deltaP `27.2639` edge `0.0181` maxDD `-0.1997`
- `market_context_high->crypto_alt_1h` score `2.1468` n `77` status `ready` deltaP `13.4906` edge `0.1636` maxDD `-3.6376`
- `news_risk_high->crypto_alt_1h` score `1.5164` n `65` status `ready` deltaP `4.4196` edge `0.1488` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.2657` n `46` status `ready` deltaP `23.8603` edge `0.105` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
