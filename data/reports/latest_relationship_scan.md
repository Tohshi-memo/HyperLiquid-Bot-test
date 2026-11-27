# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T12:07:29.241428+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2886`

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

- `news_risk_high->unknown_1h` score `3252.9109` n `31` status `ready` deltaP `1.4825` edge `271.0836` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3188.0002` n `31` status `ready` deltaP `3.7864` edge `265.6471` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `17.5402` n `31` status `ready` deltaP `27.7778` edge `1.2765` maxDD `0.0`
- `news_risk_high->equity_24h` score `15.5858` n `31` status `ready` deltaP `27.2569` edge `1.1171` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.9228` n `31` status `ready` deltaP `26.9097` edge `0.8975` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.2839` n `31` status `ready` deltaP `20.6628` edge `0.6396` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.3117` n `31` status `ready` deltaP `30.3649` edge `0.3716` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.2091` n `31` status `ready` deltaP `13.1196` edge `0.7221` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6358` n `31` status `ready` deltaP `38.5865` edge `0.1419` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `4.5181` n `31` status `ready` deltaP `15.1938` edge `0.3027` maxDD `-0.1986`
- `news_risk_high->index_24h` score `2.8456` n `31` status `ready` deltaP `28.8194` edge `0.045` maxDD `0.0`
- `news_risk_high->index_4h` score `2.5678` n `31` status `ready` deltaP `30.06` edge `0.0396` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.5441` n `31` status `ready` deltaP `15.9455` edge `0.1244` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3583` n `31` status `ready` deltaP `28.5494` edge `0.0147` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `1.9763` n `31` status `ready` deltaP `6.1184` edge `0.2587` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7943` n `31` status `ready` deltaP `9.4118` edge `0.203` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1621` n `31` status `ready` deltaP `25.0917` edge `0.0096` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.324` n `31` status `ready` deltaP `11.2903` edge `0.022` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.0443` n `31` status `ready` deltaP `6.9974` edge `-0.0012` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5689` n `31` status `ready` deltaP `-4.0081` edge `0.0055` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
