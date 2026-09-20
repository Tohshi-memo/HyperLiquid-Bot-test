# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T09:37:26.120846+00:00`
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

- `news_risk_high->crypto_major_24h` score `33.5939` n `87` status `ready` deltaP `13.2303` edge `3.0583` maxDD `-22.7611`
- `news_risk_high->crypto_alt_24h` score `32.2034` n `87` status `ready` deltaP `22.3839` edge `2.6848` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `11.9657` n `67` status `ready` deltaP `1.9248` edge `0.9993` maxDD `-0.5326`
- `market_context_high->commodity_24h` score `6.4094` n `64` status `ready` deltaP `33.6806` edge `0.3621` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.2194` n `98` status `ready` deltaP `23.4476` edge `0.4829` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6399` n `98` status `ready` deltaP `22.6854` edge `0.3612` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.0699` n `67` status `ready` deltaP `35.6526` edge `0.1148` maxDD `-0.0659`
- `news_risk_high->equity_24h` score `4.025` n `87` status `ready` deltaP `26.6344` edge `0.2156` maxDD `-1.9528`
- `news_risk_high->crypto_alt_1h` score `3.0294` n `101` status `ready` deltaP `16.5308` edge `0.1888` maxDD `-2.058`
- `market_context_high->fx_4h` score `2.2571` n `67` status `ready` deltaP `29.555` edge `0.0084` maxDD `-0.0543`
- `news_risk_high->crypto_major_1h` score `2.2451` n `101` status `ready` deltaP `18.4769` edge `0.1162` maxDD `-2.8494`
- `market_context_high->commodity_1h` score `1.8638` n `72` status `ready` deltaP `20.7668` edge `0.0379` maxDD `-0.3491`
- `market_context_high->fx_24h` score `1.2817` n `64` status `ready` deltaP `16.6667` edge `-0.0001` maxDD `-0.0027`
- `news_risk_high->metal_24h` score `0.8119` n `87` status `ready` deltaP `21.7373` edge `0.0436` maxDD `-2.4203`
- `news_risk_high->metal_4h` score `0.7591` n `98` status `ready` deltaP `18.5197` edge `0.0452` maxDD `-2.0994`
- `market_context_high->fx_1h` score `0.6575` n `72` status `ready` deltaP `11.4272` edge `0.0044` maxDD `-0.063`
- `news_risk_high->metal_1h` score `0.6413` n `101` status `ready` deltaP `14.7477` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->commodity_24h` score `0.627` n `87` status `ready` deltaP `19.4205` edge `0.0815` maxDD `-3.4467`
- `news_risk_high->equity_1h` score `0.2963` n `101` status `ready` deltaP `6.1125` edge `0.0245` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `-0.0793` n `98` status `ready` deltaP `5.2327` edge `0.0221` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
