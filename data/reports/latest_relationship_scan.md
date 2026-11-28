# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T09:07:28.484746+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3712`

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

- `news_risk_high->unknown_1h` score `3375.1332` n `31` status `ready` deltaP `1.7819` edge `281.2668` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3244.2022` n `31` status `ready` deltaP `3.7864` edge `270.3306` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `21.4059` n `31` status `ready` deltaP `32.9289` edge `1.5643` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.3079` n `31` status `ready` deltaP `30.8492` edge `1.07` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.0555` n `31` status `ready` deltaP `26.3432` edge `0.829` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.2514` n `31` status `ready` deltaP `21.5775` edge `0.6308` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.3087` n `31` status `ready` deltaP `29.6027` edge `0.2931` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.1043` n `31` status `ready` deltaP `15.5586` edge `0.6924` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.9244` n `31` status `ready` deltaP `40.4093` edge `0.1538` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.6792` n `31` status `ready` deltaP `14.7873` edge `0.2355` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.3504` n `31` status `ready` deltaP `28.993` edge `0.0286` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.31` n `31` status `ready` deltaP `25.6499` edge `0.0215` maxDD `0.0`
- `news_risk_high->index_1h` score `2.2876` n `31` status `ready` deltaP `28.1003` edge `0.0118` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.1088` n `31` status `ready` deltaP `13.9994` edge `0.1011` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8484` n `31` status `ready` deltaP `5.819` edge `0.2443` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6891` n `31` status `ready` deltaP `8.6633` edge `0.1945` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1146` n `31` status `ready` deltaP `24.3432` edge `0.0085` maxDD `-0.2315`
- `market_context_high->fx_1h` score `0.4583` n `41` status `ready` deltaP `8.5366` edge `0.0027` maxDD `-0.0466`
- `news_risk_high->commodity_4h` score `0.35` n `31` status `ready` deltaP `8.8267` edge `0.0258` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3319` n `31` status `ready` deltaP `11.4427` edge `0.022` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
