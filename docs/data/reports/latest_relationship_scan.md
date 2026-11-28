# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T02:52:32.415498+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3248`

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

- `news_risk_high->unknown_1h` score `3312.1141` n `31` status `ready` deltaP `1.6322` edge `276.0162` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3174.7975` n `31` status `ready` deltaP `3.4815` edge `264.5489` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `17.9585` n `31` status `ready` deltaP `28.5962` edge `1.3059` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.4276` n `31` status `ready` deltaP `26.6898` edge `0.8577` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.3201` n `31` status `ready` deltaP `23.9168` edge `0.7839` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.0609` n `31` status `ready` deltaP `18.6811` edge `0.5509` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `4.99` n `31` status `ready` deltaP `28.0783` edge `0.2767` maxDD `-2.178`
- `news_risk_high->fx_24h` score `4.7186` n `31` status `ready` deltaP `38.6762` edge `0.1482` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `4.3669` n `31` status `ready` deltaP `13.272` edge `0.6131` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `3.3464` n `31` status `ready` deltaP `12.1877` edge `0.2251` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.1765` n `31` status `ready` deltaP `27.1637` edge `0.0263` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.175` n `31` status `ready` deltaP `26.753` edge `0.0114` maxDD `-0.0136`
- `news_risk_high->index_24h` score `2.1632` n `31` status `ready` deltaP `24.6101` edge `0.0162` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.116` n `31` status `ready` deltaP `14.1491` edge `0.1007` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.7401` n `31` status `ready` deltaP `4.7711` edge `0.2374` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.5909` n `31` status `ready` deltaP `7.9148` edge `0.1869` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.0811` n `31` status `ready` deltaP `23.7444` edge `0.0082` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3516` n `31` status `ready` deltaP `8.8267` edge `0.026` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.2008` n `31` status `ready` deltaP `9.461` edge `0.0184` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3711` n `31` status `ready` deltaP `-2.5111` edge `0.012` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
