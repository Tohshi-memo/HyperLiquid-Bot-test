# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T07:07:25.515734+00:00`
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

- `news_risk_high->unknown_1h` score `3225.2233` n `31` status `ready` deltaP `1.6322` edge `268.7753` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3181.903` n `31` status `ready` deltaP `3.7864` edge `265.139` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `21.6196` n `31` status `ready` deltaP `31.25` edge `1.5933` maxDD `0.0`
- `news_risk_high->equity_24h` score `19.3975` n `31` status `ready` deltaP `30.7292` edge `1.4116` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.3494` n `31` status `ready` deltaP `30.3819` edge `1.1599` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.052` n `31` status `ready` deltaP `22.6445` edge `0.6904` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.933` n `31` status `ready` deltaP `32.0417` edge `0.4122` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.7774` n `31` status `ready` deltaP `15.5586` edge `0.7787` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.4811` n `31` status `ready` deltaP `18.666` edge `0.3598` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.6406` n `31` status `ready` deltaP `38.5865` edge `0.1423` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.4653` n `31` status `ready` deltaP `32.2917` edge `0.0735` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6588` n `31` status `ready` deltaP `30.8222` edge `0.0421` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.6233` n `31` status `ready` deltaP `16.2449` edge `0.129` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3978` n `31` status `ready` deltaP `28.9985` edge `0.015` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0784` n `31` status `ready` deltaP `6.8669` edge `0.2668` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8559` n `31` status `ready` deltaP `9.7112` edge `0.2089` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1543` n `31` status `ready` deltaP `25.0917` edge `0.0086` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.4482` n `31` status `ready` deltaP `12.5098` edge `0.0298` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `-0.1004` n `31` status `ready` deltaP `5.6255` edge `-0.0106` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.6695` n `31` status `ready` deltaP `-5.056` edge `0.0041` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
