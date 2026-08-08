# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T20:52:25.770683+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11607`

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

- `market_context_high->equity_24h` score `2.9664` n `103` status `ready` deltaP `4.5729` edge `0.5227` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.417` n `103` status `ready` deltaP `12.2118` edge `0.1776` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.6063` n `106` status `ready` deltaP `15.4279` edge `0.0983` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `1.0351` n `113` status `ready` deltaP `12.2331` edge `0.039` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.899` n `103` status `ready` deltaP `22.443` edge `0.0523` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.423` n `103` status `ready` deltaP `9.1002` edge `0.1467` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.5041` n `113` status `ready` deltaP `1.9262` edge `-0.0053` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5203` n `113` status `ready` deltaP `-3.1768` edge `-0.0066` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.6251` n `113` status `ready` deltaP `-3.6392` edge `-0.0063` maxDD `-0.9664`
- `market_context_high->equity_1h` score `-0.6307` n `113` status `ready` deltaP `2.0402` edge `0.0167` maxDD `-4.6286`
- `market_context_high->index_4h` score `-0.7057` n `106` status `ready` deltaP `-2.7237` edge `-0.0118` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.9048` n `106` status `ready` deltaP `0.7996` edge `-0.0054` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.077` n `106` status `ready` deltaP `-3.4946` edge `-0.0139` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.1574` n `113` status `ready` deltaP `-13.0743` edge `-0.0297` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-2.2642` n `106` status `ready` deltaP `0.1265` edge `-0.0558` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-2.7374` n `113` status `ready` deltaP `-9.4815` edge `-0.0579` maxDD `-5.2274`
- `market_context_high->crypto_major_24h` score `-3.6151` n `103` status `ready` deltaP `6.2197` edge `-0.0933` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.0846` n `103` status `ready` deltaP `-12.4461` edge `-0.1131` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.6784` n `106` status `ready` deltaP `-13.616` edge `-0.1339` maxDD `-6.5487`
- `market_context_high->unknown_1h` score `-8.1388` n `113` status `ready` deltaP `-3.2735` edge `-0.6117` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
