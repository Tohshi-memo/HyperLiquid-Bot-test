# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T05:52:28.121830+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9286`

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

- `news_risk_high->crypto_major_24h` score `40.8437` n `81` status `ready` deltaP `16.9367` edge `3.4575` maxDD `-10.3413`
- `news_risk_high->crypto_alt_24h` score `37.4596` n `81` status `ready` deltaP `29.0316` edge `3.066` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.1676` n `79` status `ready` deltaP `36.6474` edge `0.4055` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `6.28` n `81` status `ready` deltaP `33.2755` edge `0.3151` maxDD `-0.4217`
- `news_risk_high->crypto_alt_4h` score `6.2674` n `98` status `ready` deltaP `23.4476` edge `0.4869` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.8912` n `98` status `ready` deltaP `23.1427` edge `0.3791` maxDD `-8.0625`
- `market_context_high->unknown_4h` score `4.0629` n `82` status `ready` deltaP `0.6097` edge `0.3495` maxDD `-0.5326`
- `market_context_high->commodity_4h` score `3.8306` n `82` status `ready` deltaP `34.1464` edge `0.1049` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.4247` n `98` status `ready` deltaP `19.0731` edge `0.2048` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6501` n `98` status `ready` deltaP `21.3186` edge `0.131` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.3639` n `82` status `ready` deltaP `31.25` edge `0.006` maxDD `-0.0543`
- `market_context_high->commodity_1h` score `1.8117` n `82` status `ready` deltaP `20.4761` edge `0.0355` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.4623` n `81` status `ready` deltaP `22.3765` edge `0.0571` maxDD `-2.4203`
- `market_context_high->fx_24h` score `0.9687` n `79` status `ready` deltaP `14.3592` edge `-0.0108` maxDD `-0.0027`
- `news_risk_high->metal_4h` score `0.8978` n `98` status `ready` deltaP `20.0441` edge `0.0466` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.7566` n `98` status `ready` deltaP `16.0546` edge `0.0162` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.6092` n `82` status `ready` deltaP `10.9136` edge `0.0038` maxDD `-0.063`
- `news_risk_high->equity_1h` score `0.3552` n `98` status `ready` deltaP `5.7681` edge `0.0317` maxDD `-0.9112`
- `news_risk_high->commodity_24h` score `0.3294` n `81` status `ready` deltaP `17.2068` edge `0.0581` maxDD `-3.4467`
- `news_risk_high->fx_4h` score `-0.1427` n `98` status `ready` deltaP `4.4705` edge `0.0219` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
