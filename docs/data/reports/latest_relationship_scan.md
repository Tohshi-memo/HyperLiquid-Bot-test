# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T18:52:48.641071+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8730`

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

- `market_context_high->unknown_24h` score `1531.279` n `117` status `ready` deltaP `11.0847` edge `127.5707` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `28.7655` n `117` status `ready` deltaP `-0.3583` edge `2.4534` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.0705` n `62` status `ready` deltaP `32.7892` edge `0.5576` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.1908` n `62` status `ready` deltaP `18.9713` edge `0.4405` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.0928` n `62` status `ready` deltaP `21.6495` edge `0.1134` maxDD `0.0`
- `news_risk_high->equity_24h` score `2.6965` n `62` status `ready` deltaP `7.8096` edge `0.1826` maxDD `-0.1298`
- `news_risk_high->index_4h` score `2.5063` n `62` status `ready` deltaP `28.3438` edge `0.0461` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.3256` n `117` status `ready` deltaP `12.6486` edge `0.2059` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `1.8496` n `62` status `ready` deltaP `7.0311` edge `0.1428` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8175` n `62` status `ready` deltaP `23.2278` edge `0.0116` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.4257` n `62` status `ready` deltaP `14.8801` edge `0.0794` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.1963` n `62` status `ready` deltaP `17.437` edge `0.0787` maxDD `-0.993`
- `news_risk_high->commodity_24h` score `0.9726` n `62` status `ready` deltaP `29.0711` edge `0.0875` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.8678` n `117` status `ready` deltaP `19.1982` edge `0.02` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `0.7672` n `117` status `ready` deltaP `13.4003` edge `0.0446` maxDD `-1.6002`
- `market_context_high->fx_1h` score `0.6893` n `117` status `ready` deltaP `12.0938` edge `0.0052` maxDD `-0.271`
- `news_risk_high->crypto_alt_1h` score `0.6452` n `62` status `ready` deltaP `2.4097` edge `0.0896` maxDD `-2.4854`
- `market_context_high->commodity_1h` score `0.5141` n `117` status `ready` deltaP `9.9596` edge `0.0161` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.066` n `117` status `ready` deltaP `-1.9413` edge `0.1908` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.1079` n `62` status `ready` deltaP `4.3558` edge `0.0038` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
