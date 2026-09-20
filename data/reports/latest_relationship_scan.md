# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T09:07:27.783570+00:00`
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

- `news_risk_high->crypto_major_24h` score `35.91` n `85` status `ready` deltaP `14.7222` edge `3.1878` maxDD `-19.1423`
- `news_risk_high->crypto_alt_24h` score `33.8519` n `85` status `ready` deltaP `24.3852` edge `2.8005` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `9.4549` n `69` status `ready` deltaP `2.0546` edge `0.7892` maxDD `-0.5326`
- `market_context_high->commodity_24h` score `6.5649` n `66` status `ready` deltaP `34.1541` edge `0.3719` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.2134` n `98` status `ready` deltaP `23.4476` edge `0.4824` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6712` n `98` status `ready` deltaP `22.8378` edge `0.3628` maxDD `-8.0625`
- `news_risk_high->equity_24h` score `4.6698` n `85` status `ready` deltaP `28.7439` edge `0.2411` maxDD `-1.4861`
- `market_context_high->commodity_4h` score `4.1155` n `69` status `ready` deltaP `36.0419` edge `0.116` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.0533` n `101` status `ready` deltaP `16.6805` edge `0.1898` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.2871` n `101` status `ready` deltaP `18.7763` edge `0.1177` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.2822` n `69` status `ready` deltaP `29.9443` edge `0.0079` maxDD `-0.0543`
- `market_context_high->commodity_1h` score `2.0225` n `72` status `ready` deltaP `22.006` edge `0.0387` maxDD `-0.3491`
- `market_context_high->fx_24h` score `1.2325` n `66` status `ready` deltaP `16.3667` edge `-0.0022` maxDD `-0.0027`
- `news_risk_high->metal_24h` score `0.8314` n `85` status `ready` deltaP `21.5707` edge `0.0472` maxDD `-2.4203`
- `news_risk_high->metal_4h` score `0.7859` n `98` status `ready` deltaP `18.8246` edge `0.0454` maxDD `-2.0994`
- `market_context_high->fx_1h` score `0.7567` n `72` status `ready` deltaP `12.6664` edge `0.0044` maxDD `-0.063`
- `news_risk_high->metal_1h` score `0.6664` n `101` status `ready` deltaP `15.0471` edge `0.0154` maxDD `-0.8144`
- `news_risk_high->commodity_24h` score `0.546` n `85` status `ready` deltaP `18.7174` edge `0.0758` maxDD `-3.4467`
- `news_risk_high->equity_1h` score `0.3179` n `101` status `ready` deltaP `6.2622` edge `0.0253` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `-0.0793` n `98` status `ready` deltaP `5.2327` edge `0.0221` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
