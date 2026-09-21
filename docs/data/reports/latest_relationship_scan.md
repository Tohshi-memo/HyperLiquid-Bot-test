# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T14:37:43.549641+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8604`

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

- `market_context_high->unknown_4h` score `30.9901` n `58` status `ready` deltaP `1.23` edge `2.5893` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `19.3615` n `101` status `ready` deltaP `6.9289` edge `2.2531` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `13.3819` n `101` status `ready` deltaP `7.314` edge `1.5545` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.4373` n `101` status `ready` deltaP `16.6324` edge `0.2965` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.1483` n `101` status `ready` deltaP `19.9861` edge `0.2549` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.42` n `101` status `ready` deltaP `14.8841` edge `0.149` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.7703` n `101` status `ready` deltaP `16.5308` edge `0.0896` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.4142` n `101` status `ready` deltaP `24.2385` edge `0.1503` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.73` n `58` status `ready` deltaP `5.2602` edge `0.0511` maxDD `-0.36`
- `market_context_high->index_1h` score `0.5759` n `58` status `ready` deltaP `9.0801` edge `0.013` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.4963` n `101` status `ready` deltaP `13.4004` edge `0.0122` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.4085` n `58` status `ready` deltaP `9.5241` edge `0.0062` maxDD `-0.1854`
- `news_risk_high->metal_4h` score `0.3065` n `101` status `ready` deltaP `14.8122` edge `0.0322` maxDD `-2.0994`
- `news_risk_high->fx_4h` score `0.2757` n `101` status `ready` deltaP `9.2504` edge `0.0249` maxDD `-0.421`
- `market_context_high->index_4h` score `0.2584` n `58` status `ready` deltaP `13.5618` edge `0.0064` maxDD `-1.0949`
- `market_context_high->metal_1h` score `0.2183` n `58` status `ready` deltaP `4.9505` edge `0.016` maxDD `-0.1314`
- `news_risk_high->fx_1h` score `-0.1405` n `101` status `ready` deltaP `3.8907` edge `0.0067` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.3448` n `101` status `ready` deltaP `0.873` edge `0.006` maxDD `-0.9112`
- `market_context_high->fx_4h` score `-0.4568` n `58` status `ready` deltaP `1.0565` edge `-0.0032` maxDD `-0.6588`
- `news_risk_high->metal_24h` score `-0.4651` n `101` status `ready` deltaP `8.9091` edge `-0.0346` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
