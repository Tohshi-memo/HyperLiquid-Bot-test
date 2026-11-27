# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T07:22:27.080803+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3564`

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

- `news_risk_high->unknown_1h` score `3225.2965` n `31` status `ready` deltaP `1.6322` edge `268.7814` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3181.6978` n `31` status `ready` deltaP `3.7864` edge `265.1219` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `21.4161` n `31` status `ready` deltaP `31.0764` edge `1.5775` maxDD `0.0`
- `news_risk_high->equity_24h` score `19.2132` n `31` status `ready` deltaP `30.5556` edge `1.3974` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.1747` n `31` status `ready` deltaP `30.2083` edge `1.1465` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.029` n `31` status `ready` deltaP `22.4921` edge `0.6895` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.8944` n `31` status `ready` deltaP `31.8893` edge `0.41` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.757` n `31` status `ready` deltaP `15.4062` edge `0.7771` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.4384` n `31` status `ready` deltaP `18.4924` edge `0.3574` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.637` n `31` status `ready` deltaP `38.5865` edge `0.142` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.4358` n `31` status `ready` deltaP `32.1181` edge `0.0722` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.6545` n `31` status `ready` deltaP `16.3946` edge `0.1306` maxDD `-0.1621`
- `news_risk_high->index_4h` score `2.6454` n `31` status `ready` deltaP `30.6698` edge `0.042` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.4122` n `31` status `ready` deltaP `29.1482` edge `0.0152` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0784` n `31` status `ready` deltaP `6.8669` edge `0.2668` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.859` n `31` status `ready` deltaP `9.7112` edge `0.2093` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1566` n `31` status `ready` deltaP `25.0917` edge `0.0089` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.4482` n `31` status `ready` deltaP `12.5098` edge `0.0298` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `-0.1106` n `31` status `ready` deltaP `5.473` edge `-0.0109` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.6707` n `31` status `ready` deltaP `-5.056` edge `0.004` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
