# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T21:37:25.684960+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9172`

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

- `news_risk_high->crypto_major_24h` score `24.3934` n `98` status `ready` deltaP `12.617` edge `2.6345` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.3355` n `98` status `ready` deltaP `15.0935` edge `2.0821` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.6042` n `101` status `ready` deltaP `20.7483` edge `0.3663` maxDD `-7.675`
- `market_context_high->unknown_4h` score `4.5064` n `44` status `ready` deltaP `-0.4158` edge `0.3933` maxDD `-0.5326`
- `news_risk_high->crypto_major_4h` score `3.7177` n `101` status `ready` deltaP `20.4434` edge `0.2993` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.2728` n `44` status `ready` deltaP `33.9385` edge `0.0598` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `2.8229` n `101` status `ready` deltaP `16.6805` edge `0.1706` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1707` n `101` status `ready` deltaP `18.7763` edge `0.108` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.0206` n `98` status `ready` deltaP `22.775` edge `0.1096` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.9411` n `53` status `ready` deltaP `13.7329` edge `0.0048` maxDD `-0.1012`
- `news_risk_high->metal_1h` score `0.6377` n `101` status `ready` deltaP `14.7477` edge `0.015` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.6216` n `101` status `ready` deltaP `17.2512` edge `0.0422` maxDD `-2.0994`
- `market_context_high->fx_4h` score `0.5332` n `44` status `ready` deltaP `13.7611` edge `0.0043` maxDD `-0.2144`
- `news_risk_high->equity_24h` score `0.4414` n `98` status `ready` deltaP `16.3974` edge `0.0684` maxDD `-4.941`
- `market_context_high->commodity_1h` score `0.4259` n `53` status `ready` deltaP `9.1798` edge `0.0209` maxDD `-0.1998`
- `news_risk_high->fx_4h` score `0.2285` n `101` status `ready` deltaP `8.9456` edge `0.023` maxDD `-0.421`
- `news_risk_high->equity_1h` score `0.1921` n `101` status `ready` deltaP `5.0646` edge `0.0228` maxDD `-0.9112`
- `market_context_high->metal_1h` score `0.1359` n `53` status `ready` deltaP `6.005` edge `0.0097` maxDD `-0.2519`
- `news_risk_high->metal_24h` score `0.0957` n `98` status `ready` deltaP `14.9837` edge `-0.0032` maxDD `-2.4203`
- `news_risk_high->fx_1h` score `-0.2783` n `101` status `ready` deltaP `2.244` edge `0.0062` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
