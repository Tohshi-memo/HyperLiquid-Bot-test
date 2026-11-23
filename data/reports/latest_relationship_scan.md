# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T01:52:36.161782+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5282`

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

- `market_context_high->unknown_1h` score `14753.3462` n `90` status `ready` deltaP `0.7784` edge `1229.4565` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `9501.9147` n `90` status `ready` deltaP `-1.2669` edge `791.8652` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1360.6749` n `31` status `ready` deltaP `4.3268` edge `113.3783` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1195.3386` n `31` status `ready` deltaP `4.3962` edge `99.5879` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.7865` n `31` status `ready` deltaP `38.749` edge `0.7721` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0359` n `31` status `ready` deltaP `25.6933` edge `0.8354` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.6539` n `31` status `ready` deltaP `14.3391` edge `0.8992` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.9738` n `31` status `ready` deltaP `19.8377` edge `0.2176` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.516` n `31` status `ready` deltaP `36.7673` edge `0.0739` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7166` n `31` status `ready` deltaP `31.8428` edge `0.0226` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4704` n `31` status `ready` deltaP `9.8609` edge `0.2971` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0682` n `31` status `ready` deltaP `8.5136` edge `0.2441` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5547` n `31` status `ready` deltaP `29.433` edge `0.031` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.5546` n `31` status `ready` deltaP `21.3513` edge `0.1127` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.7935` n `31` status `ready` deltaP `17.8206` edge `0.0227` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0777` n `31` status `ready` deltaP `1.2314` edge `0.0115` maxDD `-0.0947`
- `market_context_high->fx_4h` score `-0.3933` n `90` status `ready` deltaP `7.622` edge `0.0104` maxDD `-0.9312`
- `market_context_high->metal_1h` score `-0.4322` n `90` status `ready` deltaP `1.9062` edge `0.0031` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.4429` n `90` status `ready` deltaP `1.1976` edge `0.0007` maxDD `-0.9806`
- `market_context_high->metal_4h` score `-1.332` n `90` status `ready` deltaP `3.3943` edge `0.0068` maxDD `-6.9009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
