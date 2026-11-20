# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T02:22:30.110583+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2778`

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

- `market_context_high->unknown_1h` score `12007.7288` n `108` status `ready` deltaP `1.2864` edge `1000.6553` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7456.1625` n `108` status `ready` deltaP `-0.0903` edge `621.3759` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `22.8468` n `89` status `ready` deltaP `41.2239` edge `1.6884` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.6285` n `89` status `ready` deltaP `24.9005` edge `1.4641` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.4024` n `108` status `ready` deltaP `3.7883` edge `0.3735` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `0.8581` n `108` status `ready` deltaP `5.0079` edge `0.2457` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.7359` n `108` status `ready` deltaP `20.0034` edge `0.0624` maxDD `-6.4211`
- `market_context_high->metal_24h` score `0.3894` n `89` status `ready` deltaP `18.6954` edge `0.2378` maxDD `-16.3989`
- `market_context_high->metal_1h` score `-0.0883` n `108` status `ready` deltaP `5.6886` edge `0.0212` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.1752` n `108` status `ready` deltaP `5.1453` edge `0.0829` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.2249` n `108` status `ready` deltaP `3.8645` edge `0.0066` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-0.6342` n `108` status `ready` deltaP `-1.3362` edge `0.0498` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-0.954` n `108` status `ready` deltaP `7.3908` edge `0.0491` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6337` n `108` status `ready` deltaP `-11.6988` edge `-0.0022` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.826` n `108` status `ready` deltaP `-2.2245` edge `-0.003` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.4199` n `108` status `ready` deltaP `-9.8193` edge `-0.028` maxDD `-3.9892`
- `market_context_high->fx_4h` score `-2.4205` n `108` status `ready` deltaP `-15.56` edge `-0.005` maxDD `-1.794`
- `market_context_high->fx_24h` score `-7.2954` n `89` status `ready` deltaP `-25.1014` edge `-0.0133` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.126` n `108` status `ready` deltaP `-29.2626` edge `-0.1128` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.2995` n `108` status `ready` deltaP `-6.8992` edge `-0.0468` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
