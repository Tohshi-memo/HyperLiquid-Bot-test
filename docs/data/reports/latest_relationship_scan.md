# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T03:52:32.266067+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9156`

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

- `news_risk_high->crypto_major_24h` score `40.4666` n `81` status `ready` deltaP `16.2423` edge `3.4307` maxDD `-10.3413`
- `news_risk_high->crypto_alt_24h` score `37.4915` n `81` status `ready` deltaP `29.2052` edge `3.0675` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `30.1179` n `89` status `ready` deltaP `-0.853` edge `2.5305` maxDD `-0.5326`
- `market_context_high->commodity_24h` score `7.5331` n `87` status `ready` deltaP `37.8113` edge `0.4282` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `6.4696` n `81` status `ready` deltaP `33.2755` edge `0.3309` maxDD `-0.4217`
- `news_risk_high->crypto_alt_4h` score `6.1138` n `98` status `ready` deltaP `23.4476` edge `0.4741` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.7844` n `98` status `ready` deltaP `23.1427` edge `0.3702` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.8843` n `89` status `ready` deltaP `35.2974` edge `0.1017` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.4175` n `98` status `ready` deltaP `19.0731` edge `0.2042` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6453` n `98` status `ready` deltaP `21.3186` edge `0.1306` maxDD `-2.8494`
- `market_context_high->commodity_1h` score `1.9306` n `90` status `ready` deltaP `22.1125` edge `0.0345` maxDD `-0.3491`
- `market_context_high->fx_4h` score `1.5353` n `89` status `ready` deltaP `23.7343` edge `0.0038` maxDD `-0.0601`
- `news_risk_high->metal_24h` score `1.4851` n `81` status `ready` deltaP `22.3765` edge `0.059` maxDD `-2.4203`
- `news_risk_high->metal_4h` score `0.8954` n `98` status `ready` deltaP `20.0441` edge `0.0464` maxDD `-2.0994`
- `market_context_high->fx_24h` score `0.8069` n `87` status `ready` deltaP `13.0867` edge `-0.0158` maxDD `-0.0027`
- `news_risk_high->metal_1h` score `0.7327` n `98` status `ready` deltaP `15.7552` edge `0.0162` maxDD `-0.8144`
- `news_risk_high->equity_1h` score `0.3971` n `98` status `ready` deltaP `6.2172` edge `0.0322` maxDD `-0.9112`
- `market_context_high->fx_1h` score `0.3848` n `90` status `ready` deltaP `8.2435` edge `0.0029` maxDD `-0.063`
- `news_risk_high->commodity_24h` score `0.2763` n `81` status `ready` deltaP `17.2068` edge `0.0513` maxDD `-3.4467`
- `news_risk_high->fx_4h` score `-0.0927` n `98` status `ready` deltaP `5.0803` edge `0.022` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
