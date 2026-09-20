# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T14:22:26.369626+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9386`

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

- `news_risk_high->crypto_major_24h` score `22.1901` n `98` status `ready` deltaP `7.7559` edge `2.4833` maxDD `-46.1999`
- `market_context_high->unknown_4h` score `20.7864` n `57` status `ready` deltaP `1.1392` edge `1.7396` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `20.0845` n `98` status `ready` deltaP `14.7463` edge `2.0635` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `5.9945` n `101` status `ready` deltaP `23.1873` edge `0.4659` maxDD `-7.675`
- `market_context_high->commodity_24h` score `4.8535` n `46` status `ready` deltaP `27.5665` edge `0.2732` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `4.52` n `101` status `ready` deltaP `21.9678` edge `0.356` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.3907` n `57` status `ready` deltaP `38.1017` edge `0.1252` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.1361` n `101` status `ready` deltaP `17.1296` edge `0.1937` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.2907` n `101` status `ready` deltaP `18.7763` edge `0.118` maxDD `-2.8494`
- `market_context_high->fx_4h` score `1.8508` n `57` status `ready` deltaP `24.7567` edge `0.0107` maxDD `-0.0543`
- `market_context_high->fx_24h` score `1.6911` n `46` status `ready` deltaP `19.3539` edge `0.0161` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.4367` n `57` status `ready` deltaP `16.1756` edge `0.0394` maxDD `-0.2012`
- `news_risk_high->commodity_24h` score `1.0573` n `98` status `ready` deltaP `22.775` edge `0.1143` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.7746` n `57` status `ready` deltaP `12.026` edge `0.006` maxDD `-0.063`
- `news_risk_high->metal_4h` score `0.703` n `101` status `ready` deltaP `18.0134` edge `0.0439` maxDD `-2.0994`
- `news_risk_high->equity_24h` score `0.6665` n `98` status `ready` deltaP `16.571` edge `0.086` maxDD `-4.941`
- `news_risk_high->metal_1h` score `0.6413` n `101` status `ready` deltaP `14.7477` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->metal_24h` score `0.2585` n `98` status `ready` deltaP `15.5046` edge `0.0142` maxDD `-2.4203`
- `market_context_high->metal_1h` score `0.2532` n `57` status `ready` deltaP `7.2959` edge `0.0062` maxDD `-0.4568`
- `news_risk_high->equity_1h` score `0.2364` n `101` status `ready` deltaP `5.364` edge `0.0245` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
