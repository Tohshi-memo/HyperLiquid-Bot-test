# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T18:02:55.013698+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10842`

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

- `market_context_high->equity_24h` score `2.2163` n `111` status `ready` deltaP `3.4019` edge `0.468` maxDD `-21.1456`
- `market_context_high->metal_24h` score `1.851` n `111` status `ready` deltaP `8.4366` edge `0.1556` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.3162` n `143` status `ready` deltaP `16.2716` edge `0.0685` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8672` n `143` status `ready` deltaP `11.5898` edge `0.0293` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.6241` n `111` status `ready` deltaP `20.4861` edge `0.0301` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.2229` n `111` status `ready` deltaP `6.1984` edge `0.1404` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.4067` n `143` status `ready` deltaP `2.948` edge `-0.004` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.4486` n `143` status `ready` deltaP `-1.9921` edge `-0.0053` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.6636` n `143` status `ready` deltaP `3.6938` edge `-0.0046` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6822` n `143` status `ready` deltaP `-4.738` edge `-0.0063` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.9622` n `143` status `ready` deltaP `-1.5254` edge `-0.0095` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.9768` n `143` status `ready` deltaP `-0.7862` edge `0.0067` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0272` n `143` status `ready` deltaP `-1.9657` edge `-0.0177` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.0846` n `143` status `ready` deltaP `-11.4809` edge `-0.033` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.6262` n `143` status `ready` deltaP `-2.0286` edge `-0.0716` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.3544` n `143` status `ready` deltaP `-12.4838` edge `-0.0641` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-4.062` n `143` status `ready` deltaP `-9.0387` edge `-0.1126` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.3519` n `111` status `ready` deltaP `0.9244` edge `-0.1194` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-6.0834` n `111` status `ready` deltaP `-17.286` edge `-0.2474` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.8292` n `143` status `ready` deltaP `-6.2435` edge `-0.5661` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
