# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T00:07:26.562772+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8733`

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

- `market_context_high->equity_24h` score `3.0972` n `103` status `ready` deltaP `4.5729` edge `0.5336` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.5005` n `103` status `ready` deltaP `12.3854` edge `0.1834` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.624` n `114` status `ready` deltaP `15.9045` edge `0.0966` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8902` n `126` status `ready` deltaP `10.8117` edge `0.0364` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8666` n `103` status `ready` deltaP `22.2694` edge `0.0493` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.462` n `103` status `ready` deltaP `9.1002` edge `0.1517` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.4342` n `126` status `ready` deltaP `2.6804` edge `-0.0045` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.4913` n `126` status `ready` deltaP `-2.6185` edge `-0.0066` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.5868` n `126` status `ready` deltaP `-2.8728` edge `-0.0065` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.6365` n `114` status `ready` deltaP `-1.2891` edge `-0.0125` maxDD `-1.1743`
- `market_context_high->fx_4h` score `-0.6372` n `114` status `ready` deltaP `3.9634` edge `-0.0042` maxDD `-1.6928`
- `market_context_high->equity_1h` score `-0.7926` n `126` status `ready` deltaP `1.2617` edge `0.0084` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.146` n `114` status `ready` deltaP `-4.4903` edge `-0.0161` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.2586` n `126` status `ready` deltaP `-13.2354` edge `-0.0358` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.3037` n `114` status `ready` deltaP `0.698` edge `-0.0629` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.1498` n `126` status `ready` deltaP `-11.0802` edge `-0.0674` maxDD `-6.3636`
- `market_context_high->crypto_major_24h` score `-3.7963` n `103` status `ready` deltaP `6.2197` edge `-0.1084` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.447` n `103` status `ready` deltaP `-12.4461` edge `-0.1433` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.7631` n `114` status `ready` deltaP `-13.19` edge `-0.1438` maxDD `-6.5487`
- `market_context_high->unknown_1h` score `-8.307` n `126` status `ready` deltaP `-5.1659` edge `-0.6131` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
