# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T08:52:28.814732+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9292`

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

- `news_risk_high->crypto_major_24h` score `37.2242` n `84` status `ready` deltaP `15.501` edge `3.2601` maxDD `-16.9138`
- `news_risk_high->crypto_alt_24h` score `34.7624` n `84` status `ready` deltaP `25.4216` edge `2.8653` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `8.3246` n `70` status `ready` deltaP `2.1167` edge `0.6946` maxDD `-0.5326`
- `market_context_high->commodity_24h` score `6.631` n `67` status `ready` deltaP `34.3802` edge `0.3759` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.2146` n `98` status `ready` deltaP `23.4476` edge `0.4825` maxDD `-7.675`
- `news_risk_high->equity_24h` score `5.0156` n `84` status `ready` deltaP `29.8363` edge `0.255` maxDD `-1.2088`
- `news_risk_high->crypto_major_4h` score `4.682` n `98` status `ready` deltaP `22.8378` edge `0.3637` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.1376` n `70` status `ready` deltaP `36.2283` edge `0.1166` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.0581` n `101` status `ready` deltaP `16.6805` edge `0.1902` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.2979` n `101` status `ready` deltaP `18.7763` edge `0.1186` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.2947` n `70` status `ready` deltaP `30.1307` edge `0.0077` maxDD `-0.0543`
- `market_context_high->commodity_1h` score `2.1277` n `72` status `ready` deltaP `23.2452` edge `0.0392` maxDD `-0.3491`
- `market_context_high->fx_24h` score `1.2109` n `67` status `ready` deltaP `16.2158` edge `-0.003` maxDD `-0.0027`
- `news_risk_high->metal_24h` score `0.8406` n `84` status `ready` deltaP `21.4782` edge `0.049` maxDD `-2.4203`
- `news_risk_high->metal_4h` score `0.7993` n `98` status `ready` deltaP `18.9771` edge `0.0455` maxDD `-2.0994`
- `market_context_high->fx_1h` score `0.7579` n `72` status `ready` deltaP `12.6664` edge `0.0045` maxDD `-0.063`
- `news_risk_high->metal_1h` score `0.6664` n `101` status `ready` deltaP `15.0471` edge `0.0154` maxDD `-0.8144`
- `news_risk_high->commodity_24h` score `0.5044` n `84` status `ready` deltaP `18.3532` edge `0.0729` maxDD `-3.4467`
- `news_risk_high->equity_1h` score `0.3275` n `101` status `ready` deltaP `6.2622` edge `0.0261` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `-0.0793` n `98` status `ready` deltaP `5.2327` edge `0.0221` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
