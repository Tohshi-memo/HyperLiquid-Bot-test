# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T09:37:27.354507+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11572`

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

- `market_context_high->equity_24h` score `6.108` n `81` status `ready` deltaP `1.9483` edge `0.802` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.7297` n `81` status `ready` deltaP `12.6158` edge `0.2843` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.7201` n `81` status `ready` deltaP `33.6034` edge `0.0665` maxDD `-1.9329`
- `market_context_high->commodity_4h` score `1.4872` n `103` status `ready` deltaP `14.1339` edge `0.097` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.152` n `81` status `ready` deltaP `7.0216` edge `0.2005` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `1.0609` n `103` status `ready` deltaP `12.2856` edge `0.0408` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.3609` n `103` status `ready` deltaP `4.4969` edge `0.0228` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.496` n `103` status `ready` deltaP `-3.3341` edge `-0.0066` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5118` n `103` status `ready` deltaP `1.9054` edge `-0.0058` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.5527` n `103` status `ready` deltaP `-0.0518` edge `-0.01` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6646` n `103` status `ready` deltaP `-4.459` edge `-0.0059` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.9285` n `103` status `ready` deltaP `0.4129` edge `-0.0048` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0811` n `103` status `ready` deltaP `-3.6778` edge `-0.0132` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.7159` n `103` status `ready` deltaP `4.2653` edge `-0.0377` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.7995` n `103` status `ready` deltaP `-9.6811` edge `-0.0225` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.2947` n `103` status `ready` deltaP `-6.3877` edge `-0.049` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-2.6723` n `81` status `ready` deltaP `6.6937` edge `-0.1378` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.7691` n `103` status `ready` deltaP `-8.4448` edge `-0.0926` maxDD `-6.5487`
- `market_context_high->crypto_alt_24h` score `-3.7802` n `81` status `ready` deltaP `-22.8202` edge `-0.1882` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-7.4354` n `103` status `ready` deltaP `-11.0526` edge `-0.2068` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
