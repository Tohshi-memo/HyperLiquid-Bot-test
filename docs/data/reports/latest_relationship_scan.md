# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T22:22:26.809737+00:00`
- Price records: `672`
- Market context records: `7607`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14551`

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

- `market_context_high->equity_24h` score `1.2107` n `145` status `ready` deltaP `16.9771` edge `0.5326` maxDD `-34.5784`
- `market_context_high->unknown_24h` score `1.0778` n `146` status `ready` deltaP `12.921` edge `0.1217` maxDD `-4.775`
- `market_context_high->commodity_24h` score `0.4572` n `145` status `ready` deltaP `16.0267` edge `0.0896` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.1148` n `146` status `ready` deltaP `7.5631` edge `0.0122` maxDD `-0.8324`
- `market_context_high->commodity_4h` score `-0.1435` n `146` status `ready` deltaP `6.6525` edge `0.0182` maxDD `-2.2943`
- `market_context_high->crypto_major_1h` score `-0.1487` n `146` status `ready` deltaP `8.0059` edge `0.0236` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2279` n `146` status `ready` deltaP `2.0548` edge `0.0203` maxDD `-2.7243`
- `market_context_high->commodity_1h` score `-0.2367` n `146` status `ready` deltaP `4.0807` edge `-0.0005` maxDD `-1.5641`
- `market_context_high->fx_24h` score `-0.3263` n `145` status `ready` deltaP `9.2803` edge `0.0197` maxDD `-3.0343`
- `market_context_high->equity_1h` score `-0.4065` n `146` status `ready` deltaP `6.5779` edge `0.0554` maxDD `-7.7764`
- `market_context_high->index_4h` score `-0.5464` n `146` status `ready` deltaP `10.2865` edge `0.0315` maxDD `-3.2774`
- `market_context_high->metal_1h` score `-0.6037` n `146` status `ready` deltaP `1.8374` edge `0.0149` maxDD `-1.0307`
- `market_context_high->fx_1h` score `-0.6534` n `146` status `ready` deltaP `-0.4217` edge `-0.0017` maxDD `-0.6615`
- `market_context_high->crypto_alt_4h` score `-0.9124` n `146` status `ready` deltaP `3.6543` edge `0.0576` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.0391` n `146` status `ready` deltaP `9.7414` edge `0.0696` maxDD `-14.4206`
- `market_context_high->equity_4h` score `-1.3457` n `146` status `ready` deltaP `3.5901` edge `0.2179` maxDD `-20.4824`
- `market_context_high->unknown_1h` score `-1.5206` n `146` status `ready` deltaP `-0.6849` edge `-0.0598` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.5961` n `146` status `ready` deltaP `-0.9084` edge `0.0471` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-1.7299` n `146` status `ready` deltaP `-1.3675` edge `0.113` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.5654` n `146` status `ready` deltaP `-6.2` edge `-0.004` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
