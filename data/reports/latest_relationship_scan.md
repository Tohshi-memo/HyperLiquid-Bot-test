# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T21:07:31.396281+00:00`
- Price records: `672`
- Market context records: `7601`
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

- `market_context_high->unknown_24h` score `1.041` n `146` status `ready` deltaP `13.104` edge `0.1268` maxDD `-5.1929`
- `market_context_high->equity_24h` score `0.8725` n `145` status `ready` deltaP `16.9771` edge `0.5367` maxDD `-38.3748`
- `market_context_high->commodity_24h` score `0.5065` n `145` status `ready` deltaP `16.2081` edge `0.0925` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.0847` n `147` status `ready` deltaP `7.0448` edge `0.0118` maxDD `-0.8324`
- `market_context_high->commodity_4h` score `-0.1317` n `147` status `ready` deltaP `6.965` edge `0.0186` maxDD `-2.4139`
- `market_context_high->crypto_major_1h` score `-0.1524` n `147` status `ready` deltaP `7.9046` edge `0.0238` maxDD `-4.0162`
- `market_context_high->commodity_1h` score `-0.2092` n `147` status `ready` deltaP `4.4402` edge `0.0008` maxDD `-1.5775`
- `market_context_high->crypto_alt_1h` score `-0.2284` n `147` status `ready` deltaP `2.0001` edge `0.0206` maxDD `-2.7243`
- `market_context_high->fx_24h` score `-0.3251` n `145` status `ready` deltaP `9.2803` edge `0.0198` maxDD `-3.0343`
- `market_context_high->equity_1h` score `-0.4556` n `147` status `ready` deltaP `6.5147` edge `0.0544` maxDD `-7.8324`
- `market_context_high->index_4h` score `-0.593` n `147` status `ready` deltaP `9.7423` edge `0.0308` maxDD `-3.4082`
- `market_context_high->metal_1h` score `-0.6402` n `147` status `ready` deltaP `1.2118` edge `0.0144` maxDD `-1.0307`
- `market_context_high->fx_1h` score `-0.6735` n `147` status `ready` deltaP `-0.6588` edge `-0.0018` maxDD `-0.6615`
- `market_context_high->crypto_alt_4h` score `-1.0071` n `147` status `ready` deltaP `3.1432` edge `0.0556` maxDD `-9.7866`
- `market_context_high->unknown_1h` score `-1.0129` n `147` status `ready` deltaP `-1.0204` edge `-0.0607` maxDD `-1.3217`
- `market_context_high->crypto_major_4h` score `-1.1159` n `147` status `ready` deltaP `9.1837` edge `0.0677` maxDD `-14.7592`
- `market_context_high->equity_4h` score `-1.4548` n `147` status `ready` deltaP `3.3982` edge `0.2158` maxDD `-20.9976`
- `market_context_high->metal_4h` score `-1.6251` n `147` status `ready` deltaP `-1.2206` edge `0.0461` maxDD `-4.7051`
- `market_context_high->metal_24h` score `-1.8258` n `146` status `ready` deltaP `-1.1843` edge `0.1146` maxDD `-8.2622`
- `market_context_high->fx_4h` score `-2.5846` n `147` status `ready` deltaP `-6.4376` edge `-0.004` maxDD `-2.1439`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
