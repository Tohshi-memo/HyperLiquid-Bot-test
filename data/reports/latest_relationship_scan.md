# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T05:37:26.194074+00:00`
- Price records: `672`
- Market context records: `7639`
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

- `market_context_high->index_1h` score `0.0523` n `146` status `ready` deltaP `6.512` edge `0.0112` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.1129` n `146` status `ready` deltaP `8.455` edge `0.0252` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.1804` n `146` status `ready` deltaP `2.5039` edge `0.0234` maxDD `-2.7243`
- `market_context_high->equity_24h` score `-0.2543` n `145` status `ready` deltaP `16.6287` edge `0.3471` maxDD `-34.5784`
- `market_context_high->fx_24h` score `-0.3515` n `145` status `ready` deltaP `9.2803` edge `0.0176` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.3624` n `146` status `ready` deltaP `1.9786` edge `-0.0026` maxDD `-1.5641`
- `market_context_high->commodity_24h` score `-0.4558` n `145` status `ready` deltaP `10.9744` edge `0.0472` maxDD `-7.0012`
- `market_context_high->equity_1h` score `-0.476` n `146` status `ready` deltaP `5.5268` edge `0.0535` maxDD `-7.7764`
- `market_context_high->commodity_4h` score `-0.6315` n `146` status `ready` deltaP `2.2182` edge `0.0071` maxDD `-2.2943`
- `market_context_high->index_4h` score `-0.6612` n `146` status `ready` deltaP `8.6045` edge `0.028` maxDD `-3.2774`
- `market_context_high->metal_1h` score `-0.6769` n `146` status `ready` deltaP `0.6398` edge `0.0135` maxDD `-1.0307`
- `market_context_high->unknown_24h` score `-0.6894` n `146` status `ready` deltaP `7.8862` edge `0.008` maxDD `-4.775`
- `market_context_high->fx_1h` score `-0.7134` n `146` status `ready` deltaP `-1.1724` edge `-0.0017` maxDD `-0.6615`
- `market_context_high->crypto_alt_4h` score `-0.8811` n `146` status `ready` deltaP `3.8068` edge `0.0606` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.0517` n `146` status `ready` deltaP `9.589` edge `0.069` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.4439` n `146` status `ready` deltaP `-0.3855` edge `-0.0554` maxDD `-1.3217`
- `market_context_high->equity_4h` score `-1.5062` n `146` status `ready` deltaP `2.214` edge `0.2065` maxDD `-20.4824`
- `market_context_high->metal_4h` score `-1.7403` n `146` status `ready` deltaP `-2.7376` edge `0.0408` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-2.128` n `146` status `ready` deltaP `-3.2772` edge `0.0747` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.5752` n `146` status `ready` deltaP `-6.3529` edge `-0.0038` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
