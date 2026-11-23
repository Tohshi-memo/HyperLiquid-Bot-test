# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T08:52:29.481604+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4548`

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

- `market_context_high->unknown_1h` score `18856.5972` n `73` status `ready` deltaP `1.661` edge `1571.3882` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `12473.634` n `73` status `ready` deltaP `3.9697` edge `1039.4569` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1317.1487` n `31` status `ready` deltaP `3.4286` edge `109.7571` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1172.3508` n `31` status `ready` deltaP `4.8535` edge `97.6692` maxDD `-0.119`
- `news_risk_high->equity_4h` score `10.9056` n `31` status `ready` deltaP `34.9381` edge `0.7241` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.339` n `31` status `ready` deltaP `23.1018` edge `0.7946` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.2911` n `31` status `ready` deltaP `12.3574` edge `0.8659` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.7651` n `31` status `ready` deltaP `18.9395` edge `0.2062` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4614` n `31` status `ready` deltaP `36.31` edge `0.0724` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6902` n `31` status `ready` deltaP `31.5434` edge `0.0224` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3675` n `31` status `ready` deltaP `9.1124` edge `0.2889` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9458` n `31` status `ready` deltaP `7.4657` edge `0.2354` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.522` n `31` status `ready` deltaP `28.9839` edge `0.0298` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4088` n `31` status `ready` deltaP `19.522` edge `0.1062` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.8452` n `31` status `ready` deltaP `18.1255` edge `0.0273` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.6173` n `73` status `ready` deltaP `18.0421` edge `0.0176` maxDD `-0.3661`
- `news_risk_high->commodity_1h` score `-0.0249` n `31` status `ready` deltaP `1.5308` edge `0.0139` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.2531` n `73` status `ready` deltaP `2.7356` edge `0.0125` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.4095` n `73` status `ready` deltaP `-1.1566` edge `0.0008` maxDD `-0.9806`
- `market_context_high->commodity_1h` score `-0.9793` n `73` status `ready` deltaP `-3.0207` edge `-0.0178` maxDD `-2.6753`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
