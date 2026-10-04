# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T08:23:04.348869+00:00`
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

- `market_context_high->unknown_4h` score `215.8001` n `63` status `ready` deltaP `7.9801` edge `17.9445` maxDD `-0.4822`
- `market_context_high->unknown_1h` score `170.9371` n `75` status `ready` deltaP `1.3513` edge `14.2772` maxDD `-0.983`
- `market_context_high->crypto_alt_24h` score `13.6116` n `46` status `ready` deltaP `31.2147` edge `1.0535` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `12.6158` n `46` status `ready` deltaP `37.6573` edge `0.8655` maxDD `-4.5519`
- `news_risk_high->crypto_major_4h` score `11.1168` n `65` status `ready` deltaP `40.1736` edge `0.6789` maxDD `-0.6258`
- `news_risk_high->equity_24h` score `10.8854` n `59` status `ready` deltaP `28.0557` edge `0.7301` maxDD `-0.1353`
- `news_risk_high->crypto_alt_4h` score `7.4915` n `65` status `ready` deltaP `24.3598` edge `0.5963` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.291` n `63` status `ready` deltaP `22.4691` edge `0.4448` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.4706` n `63` status `ready` deltaP `20.5503` edge `0.4478` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.7021` n `59` status `ready` deltaP `31.7158` edge `0.1804` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.9713` n `65` status `ready` deltaP `27.4367` edge `0.2093` maxDD `-2.9013`
- `market_context_high->equity_24h` score `3.9113` n `46` status `ready` deltaP `8.7484` edge `0.3673` maxDD `-6.3081`
- `news_risk_high->index_4h` score `3.2318` n `65` status `ready` deltaP `35.2674` edge `0.0604` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `3.0179` n `65` status `ready` deltaP `13.1598` edge `0.1993` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.6842` n `75` status `ready` deltaP `17.6727` edge `0.1509` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.5524` n `65` status `ready` deltaP `21.8223` edge `0.1088` maxDD `-0.993`
- `market_context_high->crypto_alt_1h` score `2.2442` n `75` status `ready` deltaP `14.1078` edge `0.1676` maxDD `-3.6376`
- `news_risk_high->index_1h` score `2.2064` n `65` status `ready` deltaP `27.1142` edge `0.0181` maxDD `-0.1997`
- `news_risk_high->crypto_alt_1h` score `1.5379` n `65` status `ready` deltaP `4.5693` edge `0.1496` maxDD `-2.4854`
- `market_context_high->fx_24h` score `1.2657` n `46` status `ready` deltaP `23.8603` edge `0.105` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
