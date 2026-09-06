# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T12:37:25.428205+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10703`

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

- `risk_on_high->unknown_24h` score `59.1521` n `110` status `ready` deltaP `20.2494` edge `4.82` maxDD `-0.7193`
- `risk_on_and_context->unknown_24h` score `59.1521` n `110` status `ready` deltaP `20.2494` edge `4.82` maxDD `-0.7193`
- `risk_on_high->crypto_major_24h` score `4.5921` n `110` status `ready` deltaP `17.4369` edge `0.9582` maxDD `-45.3415`
- `risk_on_and_context->crypto_major_24h` score `4.5921` n `110` status `ready` deltaP `17.4369` edge `0.9582` maxDD `-45.3415`
- `market_context_high->equity_24h` score `1.0211` n `196` status `ready` deltaP `12.6559` edge `0.3247` maxDD `-15.5851`
- `risk_on_high->index_1h` score `-0.1164` n `143` status `ready` deltaP `4.9475` edge `-0.0032` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1164` n `143` status `ready` deltaP `4.9475` edge `-0.0032` maxDD `-0.5764`
- `risk_on_high->metal_1h` score `-0.1539` n `143` status `ready` deltaP `7.7405` edge `-0.0001` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.1539` n `143` status `ready` deltaP `7.7405` edge `-0.0001` maxDD `-1.699`
- `risk_on_high->equity_1h` score `-0.4663` n `143` status `ready` deltaP `6.1022` edge `-0.013` maxDD `-2.6638`
- `risk_on_and_context->equity_1h` score `-0.4663` n `143` status `ready` deltaP `6.1022` edge `-0.013` maxDD `-2.6638`
- `risk_on_high->crypto_alt_1h` score `-0.4675` n `143` status `ready` deltaP `1.3547` edge `0.0537` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.4675` n `143` status `ready` deltaP `1.3547` edge `0.0537` maxDD `-5.4685`
- `risk_on_high->commodity_1h` score `-0.5757` n `143` status `ready` deltaP `0.356` edge `0.0` maxDD `-1.0281`
- `risk_on_and_context->commodity_1h` score `-0.5757` n `143` status `ready` deltaP `0.356` edge `0.0` maxDD `-1.0281`
- `market_context_high->commodity_1h` score `-0.7911` n `250` status `ready` deltaP `0.1126` edge `-0.0017` maxDD `-1.5315`
- `risk_on_high->crypto_major_1h` score `-0.8309` n `143` status `ready` deltaP `0.5036` edge `0.0202` maxDD `-7.4065`
- `risk_on_and_context->crypto_major_1h` score `-0.8309` n `143` status `ready` deltaP `0.5036` edge `0.0202` maxDD `-7.4065`
- `market_context_high->metal_1h` score `-0.9247` n `250` status `ready` deltaP `3.7964` edge `-0.0066` maxDD `-2.9947`
- `market_context_high->index_1h` score `-1.0913` n `250` status `ready` deltaP `2.8048` edge `0.0008` maxDD `-3.1683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
