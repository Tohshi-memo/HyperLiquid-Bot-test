# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T00:37:23.453593+00:00`
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

- `news_risk_high->crypto_major_24h` score `24.8309` n `98` status `ready` deltaP `12.7906` edge `2.6698` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.2803` n `98` status `ready` deltaP `15.0935` edge `2.0775` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.688` n `101` status `ready` deltaP `20.5958` edge `0.3743` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.8509` n `101` status `ready` deltaP `20.4434` edge `0.3104` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.6958` n `101` status `ready` deltaP `16.3811` edge `0.162` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.9836` n `101` status `ready` deltaP `17.8781` edge `0.0984` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `0.9865` n `98` status `ready` deltaP `22.2541` edge `0.1087` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.9562` n `52` status `ready` deltaP `7.7729` edge `0.0532` maxDD `-0.36`
- `market_context_high->fx_4h` score `0.9246` n `42` status `ready` deltaP `14.322` edge `0.0098` maxDD `-0.2586`
- `market_context_high->index_1h` score `0.7768` n `52` status `ready` deltaP `11.216` edge `0.0155` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.7394` n `52` status `ready` deltaP `11.3427` edge `0.0081` maxDD `-0.1012`
- `news_risk_high->metal_1h` score `0.646` n `101` status `ready` deltaP `14.8974` edge `0.0147` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.568` n `101` status `ready` deltaP `16.6415` edge `0.0418` maxDD `-2.0994`
- `market_context_high->commodity_4h` score `0.3969` n `42` status `ready` deltaP `20.1147` edge `-0.0103` maxDD `-2.4997`
- `market_context_high->metal_1h` score `0.2251` n `52` status `ready` deltaP `5.3201` edge `0.0141` maxDD `-0.1314`
- `news_risk_high->fx_4h` score `0.1969` n `101` status `ready` deltaP `8.6407` edge `0.0224` maxDD `-0.421`
- `news_risk_high->equity_24h` score `0.1959` n `98` status `ready` deltaP `15.0085` edge `0.0572` maxDD `-4.941`
- `news_risk_high->equity_1h` score `-0.0069` n `101` status `ready` deltaP `3.7173` edge `0.0152` maxDD `-0.9112`
- `market_context_high->index_4h` score `-0.0175` n `42` status `ready` deltaP `10.2061` edge `-0.0066` maxDD `-1.0949`
- `news_risk_high->metal_24h` score `-0.0577` n `98` status `ready` deltaP `13.2476` edge `-0.0113` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
