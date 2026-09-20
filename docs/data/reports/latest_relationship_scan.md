# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T23:07:29.897620+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9028`

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

- `news_risk_high->crypto_major_24h` score `24.6653` n `98` status `ready` deltaP `12.7906` edge `2.656` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.2935` n `98` status `ready` deltaP `15.0935` edge `2.0786` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.6064` n `101` status `ready` deltaP `20.5958` edge `0.3675` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.7633` n `101` status `ready` deltaP `20.4434` edge `0.3031` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.727` n `101` status `ready` deltaP `16.3811` edge `0.1646` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.058` n `101` status `ready` deltaP `18.1775` edge `0.1026` maxDD `-2.8494`
- `market_context_high->commodity_4h` score `1.4364` n `43` status `ready` deltaP `29.3747` edge `0.0271` maxDD `-1.1027`
- `market_context_high->fx_1h` score `1.3591` n `51` status `ready` deltaP `18.058` edge `0.0108` maxDD `-0.1012`
- `news_risk_high->commodity_24h` score `0.9842` n `98` status `ready` deltaP `22.2541` edge `0.1084` maxDD `-3.4467`
- `news_risk_high->metal_1h` score `0.6329` n `101` status `ready` deltaP `14.7477` edge `0.0146` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.6106` n `101` status `ready` deltaP `17.0988` edge `0.0423` maxDD `-2.0994`
- `market_context_high->fx_4h` score `0.3844` n `43` status `ready` deltaP `10.848` edge `0.0052` maxDD `-0.2586`
- `news_risk_high->equity_24h` score `0.3048` n `98` status `ready` deltaP `15.5293` edge `0.0628` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.2957` n `51` status `ready` deltaP `6.2639` edge `0.0152` maxDD `-0.2519`
- `news_risk_high->fx_4h` score `0.2383` n `101` status `ready` deltaP `9.098` edge `0.0228` maxDD `-0.421`
- `news_risk_high->equity_1h` score `0.0998` n `101` status `ready` deltaP `4.4658` edge `0.0191` maxDD `-0.9112`
- `news_risk_high->metal_24h` score `0.0217` n `98` status `ready` deltaP `14.1157` edge `-0.0069` maxDD `-2.4203`
- `market_context_high->index_1h` score `0.013` n `51` status `ready` deltaP `3.2553` edge `0.0076` maxDD `-0.2572`
- `market_context_high->equity_1h` score `-0.1946` n `51` status `ready` deltaP `-0.0381` edge `0.0098` maxDD `-1.0927`
- `market_context_high->commodity_1h` score `-0.2715` n `51` status `ready` deltaP `2.4921` edge `-0.0038` maxDD `-1.1427`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
