# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T11:52:24.402781+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `5558`

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

- `news_risk_high->unknown_1h` score `3390.5556` n `31` status `ready` deltaP `2.0813` edge `282.55` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3266.089` n `31` status `ready` deltaP `3.7864` edge `272.1545` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `23.1964` n `31` status `ready` deltaP `34.8354` edge `1.7008` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.9136` n `31` status `ready` deltaP `32.7556` edge `1.1911` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.6753` n `31` status `ready` deltaP `28.0763` edge `0.8691` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.9156` n `31` status `ready` deltaP `22.9494` edge `0.677` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `5.6696` n `31` status `ready` deltaP `17.2354` edge `0.7537` maxDD `-7.6714`
- `news_risk_high->equity_4h` score `5.5851` n `31` status `ready` deltaP `30.8222` edge `0.308` maxDD `-2.178`
- `news_risk_high->fx_24h` score `5.0268` n `31` status `ready` deltaP `41.4491` edge `0.1554` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.9265` n `31` status `ready` deltaP `16.6937` edge `0.2434` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.5086` n `31` status `ready` deltaP `30.6698` edge `0.0306` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.396` n `31` status `ready` deltaP `26.1698` edge `0.0252` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3367` n `31` status `ready` deltaP `28.6991` edge `0.0119` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.152` n `31` status `ready` deltaP `14.2988` edge `0.1027` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.9902` n `31` status `ready` deltaP `7.0166` edge `0.2545` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7849` n `31` status `ready` deltaP `9.5615` edge `0.2008` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1154` n `31` status `ready` deltaP `24.3432` edge `0.0086` maxDD `-0.2315`
- `market_context_high->metal_4h` score `0.9037` n `40` status `ready` deltaP `12.6524` edge `0.0321` maxDD `-0.2914`
- `news_risk_high->commodity_4h` score `0.4402` n `31` status `ready` deltaP `10.3511` edge `0.0272` maxDD `-0.5151`
- `market_context_high->fx_1h` score `0.3579` n `52` status `ready` deltaP `9.7651` edge `0.0022` maxDD `-0.0471`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
