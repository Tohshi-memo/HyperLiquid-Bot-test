# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T22:37:26.489207+00:00`
- Price records: `672`
- Market context records: `6025`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11124`

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

- `news_risk_high->fx_24h` score `7.8097` n `30` status `ready` deltaP `70.4861` edge `0.1809` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2893` n `30` status `ready` deltaP `44.4207` edge `0.0659` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.1132` n `30` status `ready` deltaP `27.9861` edge `0.0934` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.2562` n `30` status `ready` deltaP `27.0758` edge `0.0214` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.6951` n `206` status `ready` deltaP `9.2514` edge `0.1713` maxDD `-2.671`
- `market_context_high->equity_24h` score `1.5983` n `180` status `ready` deltaP `29.7223` edge `0.5519` maxDD `-31.6107`
- `news_risk_high->crypto_major_1h` score `0.8419` n `30` status `ready` deltaP `10.3393` edge `0.0857` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2372` n `30` status `ready` deltaP `5.4691` edge `0.0401` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1483` n `30` status `ready` deltaP `9.2361` edge `0.0446` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3659` n `206` status `ready` deltaP `4.0288` edge `0.0061` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.4024` n `30` status `ready` deltaP `1.5369` edge `-0.0252` maxDD `-1.2643`
- `market_context_high->index_24h` score `-0.4312` n `180` status `ready` deltaP `5.3472` edge `0.0791` maxDD `-5.6021`
- `market_context_high->fx_1h` score `-0.5762` n `206` status `ready` deltaP `-0.141` edge `-0.0014` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.626` n `206` status `ready` deltaP `-1.0842` edge `-0.0003` maxDD `-0.5708`
- `news_risk_high->crypto_alt_24h` score `-0.8778` n `30` status `ready` deltaP `22.5` edge `-0.2084` maxDD `-0.5131`
- `market_context_high->metal_4h` score `-0.8899` n `206` status `ready` deltaP `5.2481` edge `0.0096` maxDD `-3.4996`
- `market_context_high->index_4h` score `-0.8977` n `206` status `ready` deltaP `2.8727` edge `0.0191` maxDD `-1.9335`
- `market_context_high->equity_1h` score `-0.9509` n `206` status `ready` deltaP `1.0799` edge `0.0264` maxDD `-4.3608`
- `market_context_high->crypto_alt_1h` score `-0.9693` n `206` status `ready` deltaP `3.6568` edge `0.0266` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9758` n `206` status `ready` deltaP `3.8021` edge `0.0263` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
