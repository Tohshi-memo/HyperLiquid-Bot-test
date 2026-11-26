# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T16:07:29.519282+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3455`

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

- `news_risk_high->unknown_1h` score `3223.8852` n `31` status `ready` deltaP `1.9316` edge `268.6618` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3217.0891` n `31` status `ready` deltaP `3.4815` edge `268.0732` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `32.6486` n `31` status `ready` deltaP `41.4931` edge `2.4441` maxDD `0.0`
- `news_risk_high->equity_24h` score `30.9988` n `31` status `ready` deltaP `40.625` edge `2.3124` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `26.5319` n `31` status `ready` deltaP `40.7986` edge `1.939` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.3903` n `31` status `ready` deltaP `25.6933` edge `0.7816` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.7339` n `31` status `ready` deltaP `37.682` edge `0.608` maxDD `-2.178`
- `news_risk_high->metal_24h` score `7.6376` n `31` status `ready` deltaP `27.173` edge `0.4828` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.7996` n `31` status `ready` deltaP `18.7598` edge `0.8884` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.3087` n `31` status `ready` deltaP `42.0139` edge `0.1623` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.7889` n `31` status `ready` deltaP `39.9754` edge `0.1454` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.651` n `31` status `ready` deltaP `20.5862` edge `0.1857` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.2874` n `31` status `ready` deltaP `36.31` edge `0.0579` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7393` n `31` status `ready` deltaP `32.5913` edge `0.0195` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4431` n `31` status `ready` deltaP `9.7112` edge `0.2946` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1887` n `31` status `ready` deltaP `12.4058` edge `0.2336` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4199` n `31` status `ready` deltaP `28.2354` edge `0.0217` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.9197` n `31` status `ready` deltaP `14.7964` edge `0.075` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.3522` n `31` status `ready` deltaP `11.4182` edge `0.0088` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4407` n `31` status `ready` deltaP `-2.6608` edge `0.0072` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
