# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T01:22:27.866299+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9142`

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

- `news_risk_high->crypto_major_24h` score `24.8489` n `98` status `ready` deltaP `12.7906` edge `2.6713` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.2419` n `98` status `ready` deltaP `15.0935` edge `2.0743` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.6832` n `101` status `ready` deltaP `20.5958` edge `0.3739` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.8329` n `101` status `ready` deltaP `20.4434` edge `0.3089` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.709` n `101` status `ready` deltaP `16.3811` edge `0.1631` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.974` n `101` status `ready` deltaP `17.8781` edge `0.0976` maxDD `-2.8494`
- `market_context_high->equity_1h` score `1.2825` n `55` status `ready` deltaP `9.7659` edge `0.0671` maxDD `-0.36`
- `news_risk_high->commodity_24h` score `0.9974` n `98` status `ready` deltaP `22.2541` edge `0.1101` maxDD `-3.4467`
- `market_context_high->fx_4h` score `0.9542` n `43` status `ready` deltaP `14.7369` edge `0.0095` maxDD `-0.2586`
- `market_context_high->index_1h` score `0.9458` n `55` status `ready` deltaP `13.209` edge `0.0163` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.646` n `101` status `ready` deltaP `14.8974` edge `0.0147` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.5486` n `101` status `ready` deltaP `16.489` edge `0.0412` maxDD `-2.0994`
- `market_context_high->crypto_major_1h` score `0.4707` n `55` status `ready` deltaP `0.9744` edge `0.1046` maxDD `-2.7494`
- `market_context_high->metal_1h` score `0.3159` n `55` status `ready` deltaP `5.9145` edge `0.0177` maxDD `-0.1314`
- `market_context_high->fx_1h` score `0.3046` n `55` status `ready` deltaP `8.2254` edge `0.0062` maxDD `-0.1854`
- `news_risk_high->equity_24h` score `0.1719` n `98` status `ready` deltaP `15.0085` edge `0.0552` maxDD `-4.941`
- `news_risk_high->fx_4h` score `0.1713` n `101` status `ready` deltaP `8.3358` edge `0.0223` maxDD `-0.421`
- `market_context_high->commodity_4h` score `0.0991` n `43` status `ready` deltaP `18.509` edge `-0.0244` maxDD `-3.2363`
- `market_context_high->index_4h` score `0.041` n `43` status `ready` deltaP `10.9259` edge `-0.0039` maxDD `-1.0949`
- `news_risk_high->equity_1h` score `-0.0069` n `101` status `ready` deltaP `3.7173` edge `0.0152` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
