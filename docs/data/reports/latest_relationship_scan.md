# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T09:52:30.015695+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9300`

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

- `news_risk_high->crypto_major_24h` score `32.4968` n `88` status `ready` deltaP `12.5158` edge `2.9977` maxDD `-24.5125`
- `news_risk_high->crypto_alt_24h` score `31.1968` n `88` status `ready` deltaP `21.5909` edge `2.6269` maxDD `-10.6883`
- `market_context_high->unknown_4h` score `13.3379` n `66` status `ready` deltaP `1.8569` edge `1.1141` maxDD `-0.5326`
- `market_context_high->commodity_24h` score `6.3344` n `63` status `ready` deltaP `33.4326` edge `0.3575` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.2496` n `98` status `ready` deltaP `23.6` edge `0.4844` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6411` n `98` status `ready` deltaP `22.6854` edge `0.3613` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.0464` n `66` status `ready` deltaP `35.449` edge `0.1142` maxDD `-0.0659`
- `news_risk_high->equity_24h` score `3.7123` n `88` status `ready` deltaP `25.6156` edge `0.2036` maxDD `-2.201`
- `news_risk_high->crypto_alt_1h` score `3.0066` n `101` status `ready` deltaP `16.3811` edge `0.1879` maxDD `-2.058`
- `market_context_high->fx_4h` score `2.2444` n `66` status `ready` deltaP `29.3514` edge `0.0087` maxDD `-0.0543`
- `news_risk_high->crypto_major_1h` score `2.2212` n `101` status `ready` deltaP `18.3272` edge `0.1152` maxDD `-2.8494`
- `market_context_high->commodity_1h` score `1.705` n `72` status `ready` deltaP `19.5276` edge `0.0371` maxDD `-0.3491`
- `market_context_high->fx_24h` score `1.3092` n `63` status `ready` deltaP `16.8155` edge `0.0012` maxDD `-0.0027`
- `news_risk_high->metal_24h` score `0.8002` n `88` status `ready` deltaP `21.8119` edge `0.0416` maxDD `-2.4203`
- `news_risk_high->metal_4h` score `0.7457` n `98` status `ready` deltaP `18.3673` edge `0.0451` maxDD `-2.0994`
- `news_risk_high->commodity_24h` score `0.6665` n `88` status `ready` deltaP `19.7601` edge `0.0843` maxDD `-3.4467`
- `news_risk_high->metal_1h` score `0.6281` n `101` status `ready` deltaP `14.598` edge `0.0152` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.5572` n `72` status `ready` deltaP `10.188` edge `0.0043` maxDD `-0.063`
- `news_risk_high->equity_1h` score `0.2807` n `101` status `ready` deltaP `5.9628` edge `0.0242` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `-0.0793` n `98` status `ready` deltaP `5.2327` edge `0.0221` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
