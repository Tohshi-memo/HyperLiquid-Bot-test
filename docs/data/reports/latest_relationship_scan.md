# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T20:22:16.737514+00:00`
- Price records: `672`
- Market context records: `1151`
- Flow alert records: `5216`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8749`

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

- `market_context_high->crypto_major_24h` score `19.9672` n `151` status `ready` deltaP `43.8788` edge `1.4846` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `9.6848` n `151` status `ready` deltaP `20.2354` edge `0.8738` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.9191` n `151` status `ready` deltaP `19.7146` edge `0.6215` maxDD `-6.4404`
- `market_context_high->index_24h` score `6.2507` n `151` status `ready` deltaP `18.3257` edge `0.4545` maxDD `-3.4627`
- `market_context_high->metal_24h` score `5.7532` n `151` status `ready` deltaP `-1.7477` edge `0.6578` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.5773` n `167` status `ready` deltaP `12.5557` edge `0.1974` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.2292` n `167` status `ready` deltaP `9.725` edge `0.1059` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.5568` n `167` status `ready` deltaP `8.2335` edge `0.0232` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4978` n `167` status `ready` deltaP `4.0419` edge `0.0523` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `0.3278` n `167` status `ready` deltaP `9.8912` edge `0.1682` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `0.1527` n `167` status `ready` deltaP `7.7844` edge `0.0374` maxDD `-4.1256`
- `market_context_high->fx_1h` score `0.0579` n `167` status `ready` deltaP `7.485` edge `0.0005` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.2308` n `167` status `ready` deltaP `6.8863` edge `-0.0041` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2414` n `167` status `ready` deltaP `3.2934` edge `0.0422` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.7749` n `167` status `ready` deltaP `-2.3952` edge `-0.0026` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-0.8598` n `167` status `ready` deltaP `6.8634` edge `0.1405` maxDD `-16.7194`
- `market_context_high->fx_4h` score `-0.8737` n `167` status `ready` deltaP `-1.4651` edge `-0.0026` maxDD `-1.6381`
- `market_context_high->metal_4h` score `-2.3349` n `167` status `ready` deltaP `7.4294` edge `-0.0487` maxDD `-9.2991`
- `market_context_high->unknown_24h` score `-2.8023` n `151` status `ready` deltaP `4.5806` edge `0.0089` maxDD `-10.1706`
- `market_context_high->unknown_4h` score `-3.03` n `167` status `ready` deltaP `8.9327` edge `-0.1904` maxDD `-6.7322`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
