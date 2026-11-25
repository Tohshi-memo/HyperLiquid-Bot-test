# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T04:07:28.303339+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4080`

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

- `market_context_high->unknown_1h` score `32250.8101` n `45` status `ready` deltaP `2.1656` edge `2687.5625` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21974.2921` n `45` status `ready` deltaP `3.1776` edge `1831.1837` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1015.8551` n `31` status `ready` deltaP `2.3807` edge `84.6563` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `721.3446` n `31` status `ready` deltaP `4.3962` edge `60.0884` maxDD `-0.1191`
- `news_risk_high->equity_24h` score `39.2292` n `31` status `ready` deltaP `44.4444` edge `2.9728` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `39.0287` n `31` status `ready` deltaP `50.1736` edge `2.9179` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `35.4114` n `31` status `ready` deltaP `49.1319` edge `2.6234` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `12.0074` n `31` status `ready` deltaP `28.1323` edge `0.9001` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.2214` n `31` status `ready` deltaP `41.2355` edge `0.6877` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.6625` n `31` status `ready` deltaP `35.7003` edge `0.6986` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5053` n `31` status `ready` deltaP `18.6074` edge `0.9799` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.9439` n `31` status `ready` deltaP `43.9236` edge `0.2025` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.3924` n `31` status `ready` deltaP `45.7045` edge `0.1575` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7064` n `31` status `ready` deltaP `19.0892` edge `0.2003` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.2083` n `31` status `ready` deltaP `34.4808` edge `0.0635` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7166` n `31` status `ready` deltaP `12.1064` edge `0.3137` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.604` n `31` status `ready` deltaP `30.7949` edge `0.0202` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.5968` n `45` status `ready` deltaP `31.7649` edge `0.0331` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.3642` n `31` status `ready` deltaP `12.2561` edge `0.2571` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5804` n `31` status `ready` deltaP `30.0318` edge `0.0303` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
