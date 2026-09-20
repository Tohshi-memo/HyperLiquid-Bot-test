# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T21:07:28.940018+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10660`

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

- `news_risk_high->crypto_major_24h` score `24.2979` n `98` status `ready` deltaP `12.4434` edge `2.6277` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.4046` n `98` status `ready` deltaP `15.2671` edge `2.0867` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `10.2496` n `44` status `ready` deltaP `-0.4158` edge `0.8719` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `4.6922` n `101` status `ready` deltaP `21.0532` edge `0.3716` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.7549` n `101` status `ready` deltaP `20.4434` edge `0.3024` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.6788` n `44` status `ready` deltaP `36.0587` edge `0.0795` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `2.8757` n `101` status `ready` deltaP `16.6805` edge `0.175` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.2019` n `101` status `ready` deltaP `18.7763` edge `0.1106` maxDD `-2.8494`
- `market_context_high->fx_4h` score `1.1993` n `44` status `ready` deltaP `18.0017` edge `0.0066` maxDD `-0.1333`
- `news_risk_high->commodity_24h` score `1.0237` n `98` status `ready` deltaP `22.775` edge `0.11` maxDD `-3.4467`
- `market_context_high->fx_1h` score `1.0128` n `55` status `ready` deltaP `14.5999` edge `0.005` maxDD `-0.1012`
- `news_risk_high->metal_1h` score `0.6413` n `101` status `ready` deltaP `14.7477` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.624` n `101` status `ready` deltaP `17.2512` edge `0.0424` maxDD `-2.0994`
- `market_context_high->commodity_1h` score `0.5671` n `55` status `ready` deltaP `10.3212` edge `0.0314` maxDD `-0.1998`
- `news_risk_high->equity_24h` score `0.4666` n `98` status `ready` deltaP `16.3974` edge `0.0705` maxDD `-4.941`
- `news_risk_high->equity_1h` score `0.2173` n `101` status `ready` deltaP `5.2143` edge `0.0239` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `0.2017` n `101` status `ready` deltaP `8.6407` edge `0.0228` maxDD `-0.421`
- `news_risk_high->metal_24h` score `0.1043` n `98` status `ready` deltaP `14.9837` edge `-0.0021` maxDD `-2.4203`
- `market_context_high->metal_1h` score `-0.0151` n `55` status `ready` deltaP `3.9467` edge `0.0057` maxDD `-0.3823`
- `news_risk_high->fx_1h` score `-0.3034` n `101` status `ready` deltaP `1.9446` edge `0.0061` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
