# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T23:22:37.291848+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10906`

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

- `market_context_high->commodity_4h` score `1.2399` n `148` status `ready` deltaP `15.1532` edge `0.0696` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8116` n `160` status `ready` deltaP `10.5801` edge `0.0314` maxDD `-0.7439`
- `market_context_high->metal_24h` score `0.5485` n `127` status `ready` deltaP `3.151` edge `0.0823` maxDD `-2.2743`
- `market_context_high->fx_24h` score `0.4482` n `127` status `ready` deltaP `18.318` edge `0.022` maxDD `-1.9329`
- `market_context_high->equity_24h` score `0.1827` n `127` status `ready` deltaP `3.002` edge `0.3012` maxDD `-21.1456`
- `market_context_high->index_24h` score `-0.2046` n `127` status `ready` deltaP `3.1824` edge `0.1057` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.4956` n `160` status `ready` deltaP `1.7777` edge `-0.0036` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.68` n `148` status `ready` deltaP `-2.5008` edge `-0.01` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.6952` n `148` status `ready` deltaP `3.0735` edge `-0.0031` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.7065` n `160` status `ready` deltaP `-3.9371` edge `-0.0089` maxDD `-1.4345`
- `market_context_high->index_1h` score `-1.0278` n `160` status `ready` deltaP `-4.7904` edge `-0.006` maxDD `-0.8168`
- `market_context_high->metal_4h` score `-1.1005` n `148` status `ready` deltaP `-2.6491` edge `-0.0197` maxDD `-2.9647`
- `market_context_high->equity_1h` score `-1.1907` n `160` status `ready` deltaP `-1.8001` edge `-0.0002` maxDD `-4.6286`
- `market_context_high->crypto_alt_1h` score `-1.3574` n `160` status `ready` deltaP `-9.0606` edge `-0.0369` maxDD `-3.4713`
- `market_context_high->equity_4h` score `-2.7086` n `148` status `ready` deltaP `-3.1929` edge `-0.0707` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.54` n `160` status `ready` deltaP `-11.3211` edge `-0.0632` maxDD `-9.1728`
- `market_context_high->crypto_major_24h` score `-4.1497` n `127` status `ready` deltaP `1.9671` edge `-0.1095` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-4.1942` n `148` status `ready` deltaP `-9.4307` edge `-0.121` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-4.7564` n `127` status `ready` deltaP `-13.6142` edge `-0.1613` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.6056` n `160` status `ready` deltaP `-5.625` edge `-0.5506` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
