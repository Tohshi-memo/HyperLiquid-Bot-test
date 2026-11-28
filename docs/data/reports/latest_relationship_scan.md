# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T09:52:28.498297+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3714`

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

- `news_risk_high->unknown_1h` score `3388.5984` n `31` status `ready` deltaP `2.0813` edge `282.3869` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3250.225` n `31` status `ready` deltaP `3.7864` edge `270.8325` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `21.8519` n `31` status `ready` deltaP `33.4489` edge `1.598` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.7107` n `31` status `ready` deltaP `31.3692` edge `1.1001` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.229` n `31` status `ready` deltaP `26.8631` edge `0.84` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.3862` n `31` status `ready` deltaP `21.8823` edge `0.64` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.3679` n `31` status `ready` deltaP `29.9076` edge `0.296` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.2349` n `31` status `ready` deltaP `16.0159` edge `0.7061` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.972` n `31` status `ready` deltaP `40.9292` edge `0.1543` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.7508` n `31` status `ready` deltaP `15.3072` edge `0.238` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.393` n `31` status `ready` deltaP `29.4503` edge `0.0291` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.3359` n `31` status `ready` deltaP `25.8232` edge `0.0225` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3115` n `31` status `ready` deltaP `28.3997` edge `0.0118` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.1244` n `31` status `ready` deltaP `14.1491` edge `0.1014` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8718` n `31` status `ready` deltaP `6.1184` edge `0.2453` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7015` n `31` status `ready` deltaP `8.813` edge `0.1951` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1309` n `31` status `ready` deltaP `24.6426` edge `0.0086` maxDD `-0.2315`
- `market_context_high->fx_4h` score `0.7491` n `32` status `ready` deltaP `12.3476` edge `0.0183` maxDD `-0.0553`
- `news_risk_high->commodity_4h` score `0.3769` n `31` status `ready` deltaP `9.284` edge `0.0262` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3358` n `31` status `ready` deltaP `11.4427` edge `0.0225` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
