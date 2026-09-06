# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T12:22:26.105152+00:00`
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

- `risk_on_high->unknown_24h` score `56.5846` n `111` status `ready` deltaP `20.3313` edge `4.6055` maxDD `-0.7193`
- `risk_on_and_context->unknown_24h` score `56.5846` n `111` status `ready` deltaP `20.3313` edge `4.6055` maxDD `-0.7193`
- `risk_on_high->crypto_major_24h` score `2.618` n `111` status `ready` deltaP `16.9717` edge `0.9366` maxDD `-46.7952`
- `risk_on_and_context->crypto_major_24h` score `2.618` n `111` status `ready` deltaP `16.9717` edge `0.9366` maxDD `-46.7952`
- `market_context_high->equity_24h` score `0.8195` n `196` status `ready` deltaP `12.3193` edge `0.321` maxDD `-16.1204`
- `risk_on_high->index_1h` score `-0.101` n `144` status `ready` deltaP `5.2437` edge `-0.0032` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.101` n `144` status `ready` deltaP `5.2437` edge `-0.0032` maxDD `-0.5764`
- `risk_on_high->metal_1h` score `-0.1365` n `144` status `ready` deltaP `8.0464` edge `0.0001` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.1365` n `144` status `ready` deltaP `8.0464` edge `0.0001` maxDD `-1.699`
- `risk_on_high->crypto_alt_1h` score `-0.451` n `144` status `ready` deltaP `1.5012` edge `0.0541` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.451` n `144` status `ready` deltaP `1.5012` edge `0.0541` maxDD `-5.4685`
- `risk_on_high->equity_1h` score `-0.4519` n `144` status `ready` deltaP `6.3498` edge `-0.0128` maxDD `-2.6638`
- `risk_on_and_context->equity_1h` score `-0.4519` n `144` status `ready` deltaP `6.3498` edge `-0.0128` maxDD `-2.6638`
- `risk_on_high->commodity_1h` score `-0.5624` n `144` status `ready` deltaP `0.5073` edge `0.0001` maxDD `-1.0281`
- `risk_on_and_context->commodity_1h` score `-0.5624` n `144` status `ready` deltaP `0.5073` edge `0.0001` maxDD `-1.0281`
- `market_context_high->commodity_1h` score `-0.7711` n `250` status `ready` deltaP `0.3629` edge `-0.0017` maxDD `-1.5315`
- `risk_on_high->crypto_major_1h` score `-0.7997` n `144` status `ready` deltaP `0.8192` edge `0.0221` maxDD `-7.4065`
- `risk_on_and_context->crypto_major_1h` score `-0.7997` n `144` status `ready` deltaP `0.8192` edge `0.0221` maxDD `-7.4065`
- `market_context_high->metal_1h` score `-0.9247` n `250` status `ready` deltaP `3.7964` edge `-0.0066` maxDD `-2.9947`
- `market_context_high->index_1h` score `-1.0925` n `250` status `ready` deltaP `2.8048` edge `0.0007` maxDD `-3.1683`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
