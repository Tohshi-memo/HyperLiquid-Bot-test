# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T20:22:23.986122+00:00`
- Price records: `672`
- Market context records: `3108`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6925`

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

- `market_context_high->crypto_alt_24h` score `16.0412` n `88` status `ready` deltaP `13.6048` edge `2.5263` maxDD `-36.168`
- `market_context_high->commodity_24h` score `14.8756` n `88` status `ready` deltaP `45.8491` edge `0.9768` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `13.9109` n `88` status `ready` deltaP `22.5063` edge `1.058` maxDD `-1.9039`
- `market_context_high->index_24h` score `10.3108` n `88` status `ready` deltaP `31.692` edge `0.9034` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.6203` n `88` status `ready` deltaP `16.2406` edge `1.3501` maxDD `-41.1024`
- `market_context_high->commodity_4h` score `2.9918` n `120` status `ready` deltaP `17.9878` edge `0.1752` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `-0.0957` n `126` status `ready` deltaP `1.3782` edge `0.0251` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.5134` n `126` status `ready` deltaP `3.6831` edge `0.0159` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.5618` n `88` status `ready` deltaP `4.0562` edge `-0.0011` maxDD `-0.4876`
- `market_context_high->fx_1h` score `-0.8147` n `126` status `ready` deltaP `-8.7753` edge `-0.005` maxDD `-0.6094`
- `market_context_high->crypto_alt_1h` score `-0.826` n `126` status `ready` deltaP `3.1889` edge `0.0858` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.1417` n `126` status `ready` deltaP `-0.4943` edge `0.0055` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3122` n `120` status `ready` deltaP `-12.1138` edge `-0.0031` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4392` n `120` status `ready` deltaP `9.3293` edge `0.0442` maxDD `-17.6057`
- `market_context_high->unknown_4h` score `-1.8416` n `120` status `ready` deltaP `4.8984` edge `0.0156` maxDD `-13.8046`
- `market_context_high->metal_1h` score `-2.3508` n `126` status `ready` deltaP `-6.9195` edge `-0.0104` maxDD `-7.4828`
- `market_context_high->crypto_major_1h` score `-2.377` n `126` status `ready` deltaP `-2.1885` edge `0.0428` maxDD `-15.1032`
- `market_context_high->unknown_1h` score `-2.9347` n `126` status `ready` deltaP `2.1576` edge `-0.0563` maxDD `-14.2111`
- `market_context_high->crypto_alt_4h` score `-3.9336` n `120` status `ready` deltaP `12.2053` edge `0.2188` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-4.0641` n `120` status `ready` deltaP `5.9146` edge `-0.0299` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
