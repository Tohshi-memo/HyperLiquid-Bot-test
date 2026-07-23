# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T14:52:32.060570+00:00`
- Price records: `672`
- Market context records: `7679`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14675`

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

- `market_context_high->index_1h` score `0.0137` n `144` status `ready` deltaP `5.7245` edge `0.0115` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1363` n `144` status `ready` deltaP `8.3333` edge `0.023` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2268` n `144` status `ready` deltaP `2.1374` edge `0.0199` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.2591` n `143` status `ready` deltaP `10.0911` edge `0.0199` maxDD `-3.0343`
- `market_context_high->equity_1h` score `-0.369` n `144` status `ready` deltaP `4.9175` edge `0.0519` maxDD `-6.8928`
- `market_context_high->commodity_1h` score `-0.3866` n `144` status `ready` deltaP `0.9759` edge `-0.0028` maxDD `-1.2617`
- `market_context_high->metal_1h` score `-0.6184` n `144` status `ready` deltaP `1.3598` edge `0.0162` maxDD `-1.0307`
- `market_context_high->index_4h` score `-0.643` n `144` status `ready` deltaP `8.1804` edge `0.0298` maxDD `-3.0087`
- `market_context_high->commodity_4h` score `-0.6759` n `144` status `ready` deltaP `0.5415` edge `0.0019` maxDD `-1.2801`
- `market_context_high->crypto_alt_4h` score `-0.6883` n `144` status `ready` deltaP `3.9295` edge `0.0654` maxDD `-8.721`
- `market_context_high->fx_1h` score `-0.6899` n `144` status `ready` deltaP `-1.5202` edge `-0.002` maxDD `-0.6283`
- `market_context_high->crypto_major_4h` score `-1.1332` n `144` status `ready` deltaP `10.5691` edge `0.0766` maxDD `-12.3194`
- `market_context_high->commodity_24h` score `-1.3622` n `143` status `ready` deltaP `7.0844` edge `-0.0024` maxDD `-7.0012`
- `market_context_high->equity_4h` score `-1.3992` n `144` status `ready` deltaP `0.0128` edge `0.1882` maxDD `-17.4136`
- `market_context_high->unknown_1h` score `-1.5517` n `144` status `ready` deltaP `-1.838` edge `-0.0547` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.581` n `144` status `ready` deltaP `-1.9478` edge `0.0508` maxDD `-4.2407`
- `market_context_high->equity_24h` score `-1.6986` n `143` status `ready` deltaP `12.9858` edge `0.0722` maxDD `-25.4571`
- `market_context_high->metal_24h` score `-1.957` n `144` status `ready` deltaP `-2.4305` edge `0.0672` maxDD `-6.1515`
- `market_context_high->fx_4h` score `-2.6062` n `144` status `ready` deltaP `-6.7851` edge `-0.0048` maxDD `-2.0386`
- `market_context_high->index_24h` score `-3.5013` n `143` status `ready` deltaP `-21.3092` edge `-0.0384` maxDD `-6.8074`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
