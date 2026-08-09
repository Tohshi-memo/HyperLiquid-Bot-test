# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T14:03:21.205951+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10809`

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

- `market_context_high->equity_24h` score `3.8213` n `103` status `ready` deltaP `4.3993` edge `0.5951` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.414` n `103` status `ready` deltaP `9.9549` edge `0.1924` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.202` n `143` status `ready` deltaP `15.2045` edge `0.0661` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7773` n `143` status `ready` deltaP `10.6916` edge `0.0278` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7146` n `103` status `ready` deltaP `21.4013` edge `0.0356` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.441` n `103` status `ready` deltaP `7.0169` edge `0.1629` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3481` n `143` status `ready` deltaP `3.6965` edge `-0.0041` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.3668` n `143` status `ready` deltaP `-0.4951` edge `-0.0048` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.5077` n `143` status `ready` deltaP `5.523` edge `-0.0038` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6815` n `143` status `ready` deltaP `-4.738` edge `-0.0062` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.8026` n `143` status `ready` deltaP `0.3039` edge `-0.0084` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.9085` n `143` status `ready` deltaP `-0.1873` edge `0.0084` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-0.9916` n `143` status `ready` deltaP `-1.3559` edge `-0.0172` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.9192` n `143` status `ready` deltaP `-10.2833` edge `-0.0272` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.4079` n `143` status `ready` deltaP `-0.1993` edge `-0.0656` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.1879` n `143` status `ready` deltaP `-10.9868` edge `-0.0602` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-3.6831` n `143` status `ready` deltaP `-7.3619` edge `-0.0922` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.0121` n `103` status `ready` deltaP `2.053` edge `-0.0986` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-6.2471` n `103` status `ready` deltaP `-17.3072` edge `-0.2609` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.7897` n `143` status `ready` deltaP `-5.7944` edge `-0.5658` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
