# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T07:22:31.128023+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5234`

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

- `market_context_high->unknown_1h` score `17199.4448` n `79` status `ready` deltaP `2.1356` edge `1433.289` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `11282.4494` n `79` status `ready` deltaP `3.672` edge `940.1935` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1314.0359` n `31` status `ready` deltaP `3.2789` edge `109.4987` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1168.1476` n `31` status `ready` deltaP `4.2437` edge `97.323` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.076` n `31` status `ready` deltaP `35.8527` edge `0.7322` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.4634` n `31` status `ready` deltaP `23.7116` edge `0.8009` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.3139` n `31` status `ready` deltaP `12.5098` edge `0.8678` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.7807` n `31` status `ready` deltaP `18.9395` edge `0.2075` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4736` n `31` status `ready` deltaP `36.4625` edge `0.0724` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6651` n `31` status `ready` deltaP `31.244` edge `0.0223` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3909` n `31` status `ready` deltaP `9.4118` edge `0.2899` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.97` n `31` status `ready` deltaP `7.7651` edge `0.2365` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4987` n `31` status `ready` deltaP `28.6845` edge `0.0288` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4088` n `31` status `ready` deltaP `19.522` edge `0.1062` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.8367` n `31` status `ready` deltaP `18.1255` edge `0.0262` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.3687` n `79` status `ready` deltaP `13.762` edge `0.0149` maxDD `-0.4165`
- `news_risk_high->commodity_1h` score `-0.0154` n `31` status `ready` deltaP `1.6805` edge `0.0137` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.1061` n `79` status `ready` deltaP `3.8581` edge `0.0125` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.1961` n `79` status `ready` deltaP `2.4975` edge `0.0038` maxDD `-0.9806`
- `market_context_high->metal_4h` score `-0.7828` n `79` status `ready` deltaP `8.8646` edge `0.0161` maxDD `-6.9009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
