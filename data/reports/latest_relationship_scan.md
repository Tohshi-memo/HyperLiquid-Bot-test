# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T22:07:26.117118+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9170`

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

- `news_risk_high->crypto_major_24h` score `24.4841` n `98` status `ready` deltaP `12.7906` edge `2.6409` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.2839` n `98` status `ready` deltaP `15.0935` edge `2.0778` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.5548` n `101` status `ready` deltaP `20.5958` edge `0.3632` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.7021` n `101` status `ready` deltaP `20.4434` edge `0.298` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `2.9036` n `44` status `ready` deltaP `31.8182` edge `0.0457` maxDD `-0.2685`
- `news_risk_high->crypto_alt_1h` score `2.7522` n `101` status `ready` deltaP `16.5308` edge `0.1657` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1275` n `101` status `ready` deltaP `18.6266` edge `0.1054` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.0085` n `98` status `ready` deltaP `22.6013` edge `0.1092` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.8548` n `51` status `ready` deltaP `12.6248` edge `0.005` maxDD `-0.1012`
- `news_risk_high->metal_1h` score `0.6365` n `101` status `ready` deltaP `14.7477` edge `0.0149` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.6228` n `101` status `ready` deltaP `17.2512` edge `0.0423` maxDD `-2.0994`
- `market_context_high->fx_4h` score `0.4108` n `44` status `ready` deltaP `11.6408` edge `0.0033` maxDD `-0.2586`
- `market_context_high->commodity_1h` score `0.4065` n `51` status `ready` deltaP `9.7364` edge `0.0147` maxDD `-0.1998`
- `news_risk_high->equity_24h` score `0.4023` n `98` status `ready` deltaP `16.2237` edge `0.0663` maxDD `-4.941`
- `news_risk_high->fx_4h` score `0.2407` n `101` status `ready` deltaP `9.098` edge `0.023` maxDD `-0.421`
- `news_risk_high->equity_1h` score `0.1657` n `101` status `ready` deltaP `4.9149` edge `0.0216` maxDD `-0.9112`
- `market_context_high->metal_1h` score `0.1641` n `51` status `ready` deltaP `6.2639` edge `0.0116` maxDD `-0.2519`
- `news_risk_high->metal_24h` score `0.0765` n `98` status `ready` deltaP `14.8101` edge `-0.0045` maxDD `-2.4203`
- `news_risk_high->fx_1h` score `-0.2651` n `101` status `ready` deltaP `2.3937` edge `0.0063` maxDD `-0.2147`
- `market_context_high->index_1h` score `-0.3596` n `51` status `ready` deltaP `-2.178` edge `-0.0005` maxDD `-0.4865`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
