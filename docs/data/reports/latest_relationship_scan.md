# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T09:22:25.774045+00:00`
- Price records: `672`
- Market context records: `2750`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `7.1182` n `120` status `ready` deltaP `14.8958` edge `0.5267` maxDD `-1.6255`
- `market_context_high->crypto_alt_24h` score `5.3069` n `120` status `ready` deltaP `11.2847` edge `0.9545` maxDD `-19.9486`
- `market_context_high->unknown_4h` score `0.8881` n `143` status `ready` deltaP `6.0965` edge `0.1387` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.1815` n `143` status `ready` deltaP `11.3136` edge `0.032` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.146` n `143` status `ready` deltaP `3.3479` edge `0.0386` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1643` n `143` status `ready` deltaP `3.0506` edge `0.008` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5338` n `143` status `ready` deltaP `-0.4972` edge `0.0032` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.6469` n `143` status `ready` deltaP `5.9954` edge `0.0531` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7045` n `143` status `ready` deltaP `-0.5015` edge `-0.0024` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.708` n `143` status `ready` deltaP `-0.8458` edge `-0.0098` maxDD `-4.3601`
- `market_context_high->commodity_24h` score `-0.9173` n `120` status `ready` deltaP `5.4861` edge `0.1552` maxDD `-12.4171`
- `market_context_high->crypto_major_1h` score `-0.9378` n `143` status `ready` deltaP `3.797` edge `0.0414` maxDD `-9.622`
- `market_context_high->crypto_alt_4h` score `-1.0664` n `143` status `ready` deltaP `15.6011` edge `0.2412` maxDD `-28.7261`
- `market_context_high->fx_4h` score `-1.2015` n `143` status `ready` deltaP `-4.4027` edge `0.0071` maxDD `-0.5631`
- `market_context_high->equity_1h` score `-1.2016` n `143` status `ready` deltaP `-4.0858` edge `0.0104` maxDD `-2.6634`
- `market_context_high->fx_24h` score `-1.2388` n `120` status `ready` deltaP `0.1736` edge `-0.0172` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.6641` n `143` status `ready` deltaP `-0.6204` edge `-0.0172` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-1.9797` n `143` status `ready` deltaP `-1.0969` edge `-0.0197` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.3737` n `143` status `ready` deltaP `-2.1864` edge `-0.0347` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.4564` n `143` status `ready` deltaP `6.2948` edge `0.1337` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
