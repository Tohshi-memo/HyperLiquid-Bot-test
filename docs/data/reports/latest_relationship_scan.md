# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T03:52:27.203442+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3652`

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

- `news_risk_high->unknown_1h` score `3312.7177` n `31` status `ready` deltaP `1.4825` edge `276.0675` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3178.5357` n `31` status `ready` deltaP `3.634` edge `264.8594` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `18.3512` n `31` status `ready` deltaP `29.2894` edge `1.334` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.6612` n `31` status `ready` deltaP `27.2097` edge `0.8737` maxDD `0.0`
- `news_risk_high->equity_24h` score `11.2973` n `31` status `ready` deltaP `23.9168` edge `0.782` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.0911` n `31` status `ready` deltaP `18.8336` edge `0.5524` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `4.9438` n `31` status `ready` deltaP `27.621` edge `0.2759` maxDD `-2.178`
- `news_risk_high->fx_24h` score `4.7282` n `31` status `ready` deltaP `38.6762` edge `0.149` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `4.3699` n `31` status `ready` deltaP `13.1196` edge `0.6145` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `3.344` n `31` status `ready` deltaP `12.1877` edge `0.2249` maxDD `-0.1986`
- `news_risk_high->index_1h` score `2.169` n `31` status `ready` deltaP `26.753` edge `0.0109` maxDD `-0.0136`
- `news_risk_high->index_24h` score `2.1656` n `31` status `ready` deltaP `24.6101` edge `0.0164` maxDD `0.0`
- `news_risk_high->index_4h` score `2.1643` n `31` status `ready` deltaP `27.0112` edge `0.0263` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.0296` n `31` status `ready` deltaP `13.9994` edge `0.0945` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.6161` n `31` status `ready` deltaP `4.7711` edge `0.2215` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.4871` n `31` status `ready` deltaP `7.9148` edge `0.1736` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.0585` n `31` status `ready` deltaP `23.445` edge `0.0073` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.3523` n `31` status `ready` deltaP `8.8267` edge `0.0261` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.2024` n `31` status `ready` deltaP `9.461` edge `0.0186` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3998` n `31` status `ready` deltaP `-2.8105` edge `0.0116` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
