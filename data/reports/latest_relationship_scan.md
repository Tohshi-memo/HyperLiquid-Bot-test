# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T03:37:19.512886+00:00`
- Price records: `672`
- Market context records: `1182`
- Flow alert records: `5307`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `19.0633` n `144` status `ready` deltaP `44.4445` edge `1.4055` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `8.657` n `144` status `ready` deltaP `22.2223` edge `0.7749` maxDD `-15.1306`
- `market_context_high->metal_24h` score `4.7156` n `144` status `ready` deltaP `-2.7778` edge `0.5782` maxDD `-6.3373`
- `market_context_high->equity_24h` score `3.5134` n `144` status `ready` deltaP `16.3195` edge `0.3882` maxDD `-12.6703`
- `market_context_high->index_24h` score `3.3697` n `144` status `ready` deltaP `15.9723` edge `0.2655` maxDD `-4.627`
- `market_context_high->equity_4h` score `2.7361` n `146` status `ready` deltaP `14.4211` edge `0.1982` maxDD `-3.6396`
- `market_context_high->unknown_4h` score `1.8405` n `146` status `ready` deltaP `5.5546` edge `0.238` maxDD `-6.7322`
- `market_context_high->index_4h` score `1.1815` n `146` status `ready` deltaP `10.3137` edge `0.098` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.7394` n `146` status `ready` deltaP `9.9007` edge `0.0273` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3591` n `146` status `ready` deltaP `3.2237` edge `0.0462` maxDD `-1.3546`
- `market_context_high->fx_1h` score `-0.0018` n `146` status `ready` deltaP `6.8309` edge `-0.0002` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.0809` n `146` status `ready` deltaP `7.5364` edge `0.1315` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `-0.2001` n `146` status `ready` deltaP `4.8171` edge `0.0188` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.2143` n `146` status `ready` deltaP `7.6471` edge `-0.0078` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.3836` n `146` status `ready` deltaP `0.5394` edge `0.0315` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.8685` n `146` status `ready` deltaP `-4.4951` edge `-0.0062` maxDD `-3.3476`
- `market_context_high->fx_4h` score `-1.08` n `146` status `ready` deltaP `-5.1829` edge `-0.0068` maxDD `-1.4358`
- `market_context_high->fx_24h` score `-1.157` n `144` status `ready` deltaP `4.8611` edge `0.017` maxDD `-9.8188`
- `market_context_high->crypto_alt_4h` score `-1.3882` n `146` status `ready` deltaP `3.1072` edge `0.0978` maxDD `-16.7194`
- `market_context_high->unknown_24h` score `-1.8592` n `144` status `ready` deltaP `4.3403` edge `0.0891` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
