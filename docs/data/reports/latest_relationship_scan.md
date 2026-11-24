# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T19:52:29.116243+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4104`

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

- `market_context_high->unknown_1h` score `32268.395` n `45` status `ready` deltaP `1.4171` edge `2689.0329` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22072.0177` n `45` status `ready` deltaP `3.1776` edge `1839.3275` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1033.4401` n `31` status `ready` deltaP `1.6322` edge `86.1267` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `819.0702` n `31` status `ready` deltaP `4.3962` edge `68.2322` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.3975` n `31` status `ready` deltaP `50.1736` edge `2.8653` maxDD `0.0`
- `news_risk_high->equity_24h` score `36.6534` n `31` status `ready` deltaP `43.4028` edge `2.7651` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `33.8651` n `31` status `ready` deltaP `48.9583` edge `2.4957` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.6269` n `31` status `ready` deltaP `26.1506` edge `0.8816` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.0978` n `31` status `ready` deltaP `41.2355` edge `0.6774` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.2304` n `31` status `ready` deltaP `34.6332` edge `0.6697` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.2282` n `31` status `ready` deltaP `17.3879` edge `0.9525` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `6.0872` n `31` status `ready` deltaP `51.4337` edge `0.1772` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.4805` n `31` status `ready` deltaP `41.1458` edge `0.1824` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.4509` n `31` status `ready` deltaP `18.4904` edge `0.183` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0527` n `31` status `ready` deltaP `32.9564` edge `0.0607` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.7537` n `45` status `ready` deltaP `33.4417` edge `0.035` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.6433` n `31` status `ready` deltaP `11.9567` edge `0.3053` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5105` n `31` status `ready` deltaP `29.8967` edge `0.0184` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2964` n `31` status `ready` deltaP `11.6573` edge `0.2524` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.643` n `31` status `ready` deltaP `21.6562` edge `0.122` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
