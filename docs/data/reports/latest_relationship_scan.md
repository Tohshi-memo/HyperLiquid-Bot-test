# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T16:07:22.305255+00:00`
- Price records: `672`
- Market context records: `3089`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6911`

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

- `market_context_high->crypto_alt_24h` score `16.9528` n `86` status `ready` deltaP `12.7664` edge `2.5295` maxDD `-26.6275`
- `market_context_high->commodity_24h` score `15.075` n `86` status `ready` deltaP `45.6113` edge `0.995` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `14.1624` n `86` status `ready` deltaP `21.3098` edge `1.0846` maxDD `-1.7175`
- `market_context_high->index_24h` score `11.9031` n `86` status `ready` deltaP `34.6939` edge `0.942` maxDD `-11.5093`
- `market_context_high->equity_24h` score `9.3049` n `86` status `ready` deltaP `22.6179` edge `1.4766` maxDD `-30.0893`
- `market_context_high->commodity_4h` score `2.974` n `120` status `ready` deltaP `18.1402` edge `0.1727` maxDD `-1.9973`
- `market_context_high->unknown_4h` score `0.0746` n `120` status `ready` deltaP `3.6077` edge `0.0875` maxDD `-3.7602`
- `market_context_high->commodity_1h` score `-0.1453` n `125` status `ready` deltaP `0.6527` edge `0.0258` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.5239` n `125` status `ready` deltaP `3.497` edge `0.0158` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.7687` n `125` status `ready` deltaP `3.6467` edge `0.0901` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-1.0277` n `86` status `ready` deltaP `0.8277` edge `-0.0053` maxDD `-0.5357`
- `market_context_high->fx_1h` score `-1.1778` n `125` status `ready` deltaP `-8.8024` edge `-0.0022` maxDD `-0.3147`
- `market_context_high->equity_1h` score `-1.2416` n `125` status `ready` deltaP `-1.4994` edge `-0.0006` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3219` n `120` status `ready` deltaP `-11.8801` edge `-0.0059` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4353` n `120` status `ready` deltaP `9.3293` edge `0.0447` maxDD `-17.6057`
- `market_context_high->unknown_1h` score `-1.5765` n `125` status `ready` deltaP `1.3078` edge `-0.0356` maxDD `-5.6925`
- `market_context_high->crypto_major_1h` score `-2.0156` n `125` status `ready` deltaP `-0.012` edge `0.0584` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.3384` n `125` status `ready` deltaP `-6.6599` edge `-0.0111` maxDD `-7.4828`
- `market_context_high->crypto_alt_4h` score `-3.2779` n `120` status `ready` deltaP `16.5955` edge `0.2736` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.8145` n `120` status `ready` deltaP `8.0284` edge `-0.0187` maxDD `-36.242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
