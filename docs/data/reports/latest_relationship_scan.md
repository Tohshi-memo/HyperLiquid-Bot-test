# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T15:37:33.601693+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3491`

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

- `news_risk_high->unknown_1h` score `3223.5816` n `31` status `ready` deltaP `1.9316` edge `268.6365` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3216.9283` n `31` status `ready` deltaP `3.4815` edge `268.0598` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `33.0808` n `31` status `ready` deltaP `41.8403` edge `2.4778` maxDD `0.0`
- `news_risk_high->equity_24h` score `31.6446` n `31` status `ready` deltaP `40.9722` edge `2.3639` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `27.0073` n `31` status `ready` deltaP `41.1458` edge `1.9763` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.3795` n `31` status `ready` deltaP `25.6933` edge `0.7807` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.8143` n `31` status `ready` deltaP `37.682` edge `0.6147` maxDD `-2.178`
- `news_risk_high->metal_24h` score `7.7698` n `31` status `ready` deltaP `27.5202` edge `0.4915` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.798` n `31` status `ready` deltaP `18.7598` edge `0.8882` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.3917` n `31` status `ready` deltaP `42.3611` edge `0.1669` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.8203` n `31` status `ready` deltaP `40.3226` edge `0.1457` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7086` n `31` status `ready` deltaP `20.7359` edge `0.1895` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.2958` n `31` status `ready` deltaP `36.31` edge `0.0586` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7572` n `31` status `ready` deltaP `32.741` edge `0.02` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4681` n `31` status `ready` deltaP `9.8609` edge `0.2968` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2183` n `31` status `ready` deltaP `12.5555` edge `0.2364` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4129` n `31` status `ready` deltaP `28.0857` edge `0.0218` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.93` n `31` status `ready` deltaP `14.9488` edge `0.0753` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.3743` n `31` status `ready` deltaP `11.723` edge `0.0096` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4251` n `31` status `ready` deltaP `-2.5111` edge `0.0075` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
