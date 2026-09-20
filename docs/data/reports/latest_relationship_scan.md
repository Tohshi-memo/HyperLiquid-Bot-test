# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T09:22:32.448777+00:00`
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

- `news_risk_high->crypto_major_24h` score `34.6599` n `86` status `ready` deltaP `13.9656` edge `3.119` maxDD `-21.2358`
- `news_risk_high->crypto_alt_24h` score `33.0069` n `86` status `ready` deltaP `23.3729` edge `2.741` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `10.6786` n `68` status `ready` deltaP `1.9906` edge `0.8916` maxDD `-0.5326`
- `market_context_high->commodity_24h` score `6.4802` n `65` status `ready` deltaP `33.921` edge `0.3664` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.2134` n `98` status `ready` deltaP `23.4476` edge `0.4824` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6592` n `98` status `ready` deltaP `22.8378` edge `0.3618` maxDD `-8.0625`
- `news_risk_high->equity_24h` score `4.3351` n `86` status `ready` deltaP `27.6769` edge `0.2277` maxDD `-1.7433`
- `market_context_high->commodity_4h` score `4.0965` n `68` status `ready` deltaP `35.8501` edge `0.1157` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.0342` n `101` status `ready` deltaP `16.5308` edge `0.1892` maxDD `-2.058`
- `market_context_high->fx_4h` score `2.2693` n `68` status `ready` deltaP `29.7525` edge `0.0081` maxDD `-0.0543`
- `news_risk_high->crypto_major_1h` score `2.2631` n `101` status `ready` deltaP `18.6266` edge `0.1167` maxDD `-2.8494`
- `market_context_high->commodity_1h` score `1.9174` n `72` status `ready` deltaP `20.7668` edge `0.0382` maxDD `-0.3491`
- `market_context_high->fx_24h` score `1.2578` n `65` status `ready` deltaP `16.5171` edge `-0.0011` maxDD `-0.0027`
- `news_risk_high->metal_24h` score `0.8234` n `86` status `ready` deltaP `21.657` edge `0.0456` maxDD `-2.4203`
- `news_risk_high->metal_4h` score `0.7725` n `98` status `ready` deltaP `18.6722` edge `0.0453` maxDD `-2.0994`
- `market_context_high->fx_1h` score `0.7579` n `72` status `ready` deltaP `12.6664` edge `0.0045` maxDD `-0.063`
- `news_risk_high->metal_1h` score `0.6532` n `101` status `ready` deltaP `14.8974` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->commodity_24h` score `0.5871` n `86` status `ready` deltaP `19.073` edge `0.0787` maxDD `-3.4467`
- `news_risk_high->equity_1h` score `0.3095` n `101` status `ready` deltaP `6.2622` edge `0.0246` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `-0.0793` n `98` status `ready` deltaP `5.2327` edge `0.0221` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
