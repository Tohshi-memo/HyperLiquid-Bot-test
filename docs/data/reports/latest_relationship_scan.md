# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T06:22:26.444671+00:00`
- Price records: `672`
- Market context records: `6161`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11132`

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

- `news_risk_high->crypto_alt_24h` score `12.4059` n `31` status `ready` deltaP `42.6863` edge `0.764` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.4842` n `31` status `ready` deltaP `65.8621` edge `0.1846` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1944` n `32` status `ready` deltaP `43.6553` edge `0.0631` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4278` n `32` status `ready` deltaP `29.1916` edge `0.0216` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.6674` n `195` status `ready` deltaP `1.104` edge `0.2324` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.2207` n `32` status `ready` deltaP `13.0801` edge `0.116` maxDD `-2.0691`
- `news_risk_high->crypto_major_24h` score `1.1545` n `31` status `ready` deltaP `15.2058` edge `0.1246` maxDD `-4.2368`
- `news_risk_high->crypto_alt_1h` score `0.626` n `32` status `ready` deltaP `8.3271` edge `0.0709` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.1693` n `195` status `ready` deltaP `-0.9091` edge `0.2734` maxDD `-11.925`
- `market_context_high->metal_24h` score `0.0229` n `195` status `ready` deltaP `19.9779` edge `0.1266` maxDD `-11.8809`
- `market_context_high->equity_4h` score `0.0154` n `195` status `ready` deltaP `3.0303` edge `0.0728` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.1237` n `31` status `ready` deltaP `8.8042` edge `0.0126` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2521` n `195` status `ready` deltaP `1.8839` edge `-0.0003` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.576` n `195` status `ready` deltaP `4.1842` edge `0.017` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7188` n `195` status `ready` deltaP `-1.6897` edge `-0.004` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7629` n `32` status `ready` deltaP `-2.994` edge `-0.0281` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.808` n `195` status `ready` deltaP `2.3906` edge `-0.0034` maxDD `-2.0564`
- `news_risk_high->commodity_24h` score `-0.8713` n `31` status `ready` deltaP `11.2848` edge `-0.1273` maxDD `-0.3101`
- `market_context_high->equity_1h` score `-0.9006` n `195` status `ready` deltaP `-1.9062` edge `0.0088` maxDD `-4.2573`
- `market_context_high->crypto_alt_1h` score `-0.9499` n `195` status `ready` deltaP `3.3111` edge `0.0314` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
