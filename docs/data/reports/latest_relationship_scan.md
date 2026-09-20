# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T15:07:30.094536+00:00`
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

- `news_risk_high->crypto_major_24h` score `22.4502` n `98` status `ready` deltaP `8.2767` edge `2.5015` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.1697` n `98` status `ready` deltaP `14.7463` edge `2.0706` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `9.0055` n `54` status `ready` deltaP `0.8468` edge `0.7598` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.9873` n `101` status `ready` deltaP `23.1873` edge `0.4653` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.526` n `101` status `ready` deltaP `21.9678` edge `0.3565` maxDD `-8.0625`
- `market_context_high->commodity_24h` score `4.4382` n `43` status `ready` deltaP `26.0498` edge `0.2487` maxDD `-0.8682`
- `market_context_high->commodity_4h` score `4.3799` n `54` status `ready` deltaP `37.5169` edge `0.1282` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.0641` n `101` status `ready` deltaP `16.6805` edge `0.1907` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.2499` n `101` status `ready` deltaP `18.4769` edge `0.1166` maxDD `-2.8494`
- `market_context_high->fx_4h` score `1.8026` n `54` status `ready` deltaP `23.9894` edge `0.0118` maxDD `-0.0543`
- `market_context_high->fx_24h` score `1.7638` n `43` status `ready` deltaP `19.723` edge `0.0197` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.2879` n `54` status `ready` deltaP `14.5709` edge `0.0377` maxDD `-0.2012`
- `news_risk_high->commodity_24h` score `1.0698` n `98` status `ready` deltaP `22.775` edge `0.1159` maxDD `-3.4467`
- `news_risk_high->metal_4h` score `0.7286` n `101` status `ready` deltaP `18.3183` edge `0.044` maxDD `-2.0994`
- `market_context_high->fx_1h` score `0.6409` n `54` status `ready` deltaP `10.3238` edge `0.0062` maxDD `-0.063`
- `news_risk_high->equity_24h` score `0.6233` n `98` status `ready` deltaP `16.571` edge `0.0824` maxDD `-4.941`
- `news_risk_high->metal_1h` score `0.6173` n `101` status `ready` deltaP `14.4483` edge `0.0153` maxDD `-0.8144`
- `market_context_high->metal_1h` score `0.415` n `54` status `ready` deltaP `10.2129` edge `0.0075` maxDD `-0.4568`
- `news_risk_high->metal_24h` score `0.2398` n `98` status `ready` deltaP `15.5046` edge `0.0118` maxDD `-2.4203`
- `news_risk_high->equity_1h` score `0.2209` n `101` status `ready` deltaP `5.2143` edge `0.0242` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
