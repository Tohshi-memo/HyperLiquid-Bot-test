# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T01:37:24.276515+00:00`
- Price records: `672`
- Market context records: `7622`
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

- `market_context_high->equity_24h` score `0.7209` n `145` status `ready` deltaP `16.9771` edge `0.4698` maxDD `-34.5784`
- `market_context_high->unknown_24h` score `0.2949` n `146` status `ready` deltaP `10.664` edge `0.0715` maxDD `-4.775`
- `market_context_high->index_1h` score `0.0547` n `146` status `ready` deltaP `6.6622` edge `0.0105` maxDD `-0.8324`
- `market_context_high->commodity_24h` score `0.0432` n `145` status `ready` deltaP `13.7619` edge `0.0702` maxDD `-7.0012`
- `market_context_high->crypto_major_1h` score `-0.183` n `146` status `ready` deltaP `7.7065` edge `0.0212` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.2381` n `146` status `ready` deltaP `1.9051` edge `0.02` maxDD `-2.7243`
- `market_context_high->commodity_1h` score `-0.2984` n `146` status `ready` deltaP `3.0297` edge `-0.0014` maxDD `-1.5641`
- `market_context_high->fx_24h` score `-0.3479` n `145` status `ready` deltaP `9.2803` edge `0.0179` maxDD `-3.0343`
- `market_context_high->commodity_4h` score `-0.377` n `146` status `ready` deltaP `4.6647` edge `0.012` maxDD `-2.2943`
- `market_context_high->equity_1h` score `-0.5041` n `146` status `ready` deltaP `5.5268` edge `0.0499` maxDD `-7.7764`
- `market_context_high->index_4h` score `-0.6224` n `146` status `ready` deltaP `9.2162` edge `0.0289` maxDD `-3.2774`
- `market_context_high->fx_1h` score `-0.651` n `146` status `ready` deltaP `-0.4217` edge `-0.0015` maxDD `-0.6615`
- `market_context_high->metal_1h` score `-0.652` n `146` status `ready` deltaP `1.0889` edge `0.0137` maxDD `-1.0307`
- `market_context_high->crypto_alt_4h` score `-0.9409` n `146` status `ready` deltaP `3.197` edge `0.057` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.1862` n `146` status `ready` deltaP `8.217` edge `0.0609` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.4559` n `146` status `ready` deltaP `-0.3855` edge `-0.0564` maxDD `-1.3217`
- `market_context_high->equity_4h` score `-1.4962` n `146` status `ready` deltaP `2.061` edge `0.2088` maxDD `-20.4824`
- `market_context_high->metal_4h` score `-1.6314` n `146` status `ready` deltaP `-1.2133` edge `0.0446` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-1.9876` n `146` status `ready` deltaP `-3.2772` edge `0.0927` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.574` n `146` status `ready` deltaP `-6.3529` edge `-0.0037` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
