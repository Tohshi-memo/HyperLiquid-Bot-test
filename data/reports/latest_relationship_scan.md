# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T16:52:27.024881+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3419`

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

- `news_risk_high->unknown_1h` score `3224.2296` n `31` status `ready` deltaP `2.231` edge `268.6885` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3217.5456` n `31` status `ready` deltaP `3.9388` edge `268.1082` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `32.0154` n `31` status `ready` deltaP `40.9722` edge `2.3948` maxDD `0.0`
- `news_risk_high->equity_24h` score `29.9743` n `31` status `ready` deltaP `40.1042` edge `2.2305` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `25.841` n `31` status `ready` deltaP `40.2778` edge `1.8849` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.3867` n `31` status `ready` deltaP `25.6933` edge `0.7813` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.6019` n `31` status `ready` deltaP `37.682` edge `0.597` maxDD `-2.178`
- `news_risk_high->metal_24h` score `7.4328` n `31` status `ready` deltaP `26.6521` edge `0.4692` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.7918` n `31` status `ready` deltaP `18.7598` edge `0.8874` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.1782` n `31` status `ready` deltaP `41.4931` edge `0.1549` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.7575` n `31` status `ready` deltaP `39.6282` edge `0.1451` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.5742` n `31` status `ready` deltaP `20.4365` edge `0.1803` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.2754` n `31` status `ready` deltaP `36.31` edge `0.0569` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7225` n `31` status `ready` deltaP `32.4416` edge `0.0191` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.433` n `31` status `ready` deltaP `9.5615` edge `0.2943` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1653` n `31` status `ready` deltaP `12.2561` edge `0.2316` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4199` n `31` status `ready` deltaP `28.2354` edge `0.0217` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.9079` n `31` status `ready` deltaP `14.644` edge `0.0745` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.3285` n `31` status `ready` deltaP `11.1133` edge `0.0078` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4275` n `31` status `ready` deltaP `-2.5111` edge `0.0073` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
