# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T21:52:31.283746+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3336`

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

- `news_risk_high->unknown_1h` score `3216.0516` n `31` status `ready` deltaP `2.0813` edge `268.008` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3193.0842` n `31` status `ready` deltaP `4.3962` edge `266.0667` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `28.3284` n `31` status `ready` deltaP `37.5` edge `2.1107` maxDD `0.0`
- `news_risk_high->equity_24h` score `25.5014` n `31` status `ready` deltaP `36.6319` edge `1.8809` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `22.1864` n `31` status `ready` deltaP `36.8056` edge `1.6035` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.9386` n `31` status `ready` deltaP `24.3214` edge `0.7531` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.6167` n `31` status `ready` deltaP `35.8527` edge `0.5271` maxDD `-2.178`
- `news_risk_high->metal_24h` score `6.4938` n `31` status `ready` deltaP `23.1799` edge `0.4141` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.4053` n `31` status `ready` deltaP `17.3879` edge `0.847` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.964` n `31` status `ready` deltaP `42.0587` edge `0.1461` maxDD `-0.0262`
- `news_risk_high->index_24h` score `4.5105` n `31` status `ready` deltaP `38.0208` edge `0.1224` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.2061` n `31` status `ready` deltaP `18.7898` edge `0.1606` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0471` n `31` status `ready` deltaP `34.1759` edge `0.0521` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5632` n `31` status `ready` deltaP `30.6452` edge `0.0178` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.2296` n `31` status `ready` deltaP `7.6154` edge `0.2812` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0282` n `31` status `ready` deltaP `10.7591` edge `0.224` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.3545` n `31` status `ready` deltaP `27.3372` edge `0.0193` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.7566` n `31` status `ready` deltaP `13.7293` edge `0.0612` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.2716` n `31` status `ready` deltaP `10.1986` edge `0.0066` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4167` n `31` status `ready` deltaP `-2.3614` edge `0.0072` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
