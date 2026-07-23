# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T02:52:24.409060+00:00`
- Price records: `672`
- Market context records: `7627`
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

- `market_context_high->equity_24h` score `0.4908` n `145` status `ready` deltaP `16.9771` edge `0.4403` maxDD `-34.5784`
- `market_context_high->index_1h` score `0.0843` n `146` status `ready` deltaP `7.1126` edge `0.0113` maxDD `-0.8324`
- `market_context_high->unknown_24h` score `-0.023` n `146` status `ready` deltaP `9.796` edge `0.0508` maxDD `-4.775`
- `market_context_high->commodity_24h` score `-0.1045` n `145` status `ready` deltaP `12.8908` edge `0.0637` maxDD `-7.0012`
- `market_context_high->crypto_major_1h` score `-0.1292` n `146` status `ready` deltaP `8.3053` edge `0.0241` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.1711` n `146` status `ready` deltaP `2.6536` edge `0.0236` maxDD `-2.7243`
- `market_context_high->commodity_1h` score `-0.3257` n `146` status `ready` deltaP `2.5792` edge `-0.0019` maxDD `-1.5641`
- `market_context_high->fx_24h` score `-0.3527` n `145` status `ready` deltaP `9.2803` edge `0.0175` maxDD `-3.0343`
- `market_context_high->equity_1h` score `-0.4393` n `146` status `ready` deltaP `6.1274` edge `0.0542` maxDD `-7.7764`
- `market_context_high->commodity_4h` score `-0.4597` n `146` status `ready` deltaP `3.9002` edge `0.0102` maxDD `-2.2943`
- `market_context_high->index_4h` score `-0.6399` n `146` status `ready` deltaP `8.9103` edge `0.0287` maxDD `-3.2774`
- `market_context_high->fx_1h` score `-0.651` n `146` status `ready` deltaP `-0.4217` edge `-0.0015` maxDD `-0.6615`
- `market_context_high->metal_1h` score `-0.6785` n `146` status `ready` deltaP `0.6398` edge `0.0133` maxDD `-1.0307`
- `market_context_high->crypto_alt_4h` score `-0.8748` n `146` status `ready` deltaP `3.8068` edge `0.0614` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.1233` n `146` status `ready` deltaP `8.8268` edge `0.0649` maxDD `-14.4206`
- `market_context_high->equity_4h` score `-1.4686` n `146` status `ready` deltaP `2.3669` edge `0.2103` maxDD `-20.4824`
- `market_context_high->unknown_1h` score `-1.5458` n `146` status `ready` deltaP `-1.134` edge `-0.0589` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.6622` n `146` status `ready` deltaP `-1.6706` edge `0.0437` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-2.025` n `146` status `ready` deltaP `-3.2772` edge `0.0879` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.5728` n `146` status `ready` deltaP `-6.3529` edge `-0.0036` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
