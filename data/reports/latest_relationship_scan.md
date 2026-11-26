# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T03:37:38.236666+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3911`

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

- `market_context_high->unknown_1h` score `37616.7454` n `39` status `ready` deltaP `0.3915` edge `3134.7356` maxDD `-0.4209`
- `news_risk_high->unknown_4h` score `3196.8377` n `31` status `ready` deltaP `3.3291` edge `266.3866` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `886.7893` n `31` status `ready` deltaP `1.6322` edge `73.9058` maxDD `-0.7395`
- `news_risk_high->equity_24h` score `43.2396` n `31` status `ready` deltaP `49.3056` edge `3.2746` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `40.5899` n `31` status `ready` deltaP `50.1736` edge `3.048` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `35.2651` n `31` status `ready` deltaP `49.4792` edge `2.6089` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.8067` n `31` status `ready` deltaP `26.6079` edge `0.8102` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `10.6541` n `31` status `ready` deltaP `35.8535` edge `0.6763` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.1905` n `31` status `ready` deltaP `37.2247` edge `0.6491` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.0664` n `31` status `ready` deltaP `50.6944` edge `0.2509` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7788` n `31` status `ready` deltaP `17.2354` edge `0.8959` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.3631` n `31` status `ready` deltaP `45.8782` edge `0.1539` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6247` n `31` status `ready` deltaP `19.9874` edge `0.1875` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3244` n `31` status `ready` deltaP `36.1576` edge `0.062` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.683` n `31` status `ready` deltaP `31.8428` edge `0.0198` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.4442` n `39` status `ready` deltaP `29.9172` edge `0.0327` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.4345` n `31` status `ready` deltaP `9.8609` edge `0.2925` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2331` n `31` status `ready` deltaP `12.5555` edge `0.2383` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4815` n `31` status `ready` deltaP `29.1336` edge `0.0236` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.1297` n `31` status `ready` deltaP `16.9305` edge `0.0877` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
