# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T10:37:18.310736+00:00`
- Price records: `672`
- Market context records: `1834`
- Flow alert records: `7178`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4488`

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

- `market_context_high->crypto_alt_4h` score `6.935` n `193` status `ready` deltaP `22.8729` edge `0.5399` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.5563` n `178` status `ready` deltaP `25.8544` edge `0.6166` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.4614` n `193` status `ready` deltaP `26.4683` edge `0.4866` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.4193` n `193` status `ready` deltaP `16.9902` edge `0.4574` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.4875` n `178` status `ready` deltaP `17.6947` edge `0.2955` maxDD `-4.1604`
- `market_context_high->equity_4h` score `2.949` n `193` status `ready` deltaP `16.4705` edge `0.2454` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.7315` n `178` status `ready` deltaP `14.56` edge `0.6626` maxDD `-35.8966`
- `market_context_high->equity_24h` score `1.8947` n `178` status `ready` deltaP `15.0202` edge `0.5476` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.8408` n `193` status `ready` deltaP `12.2046` edge `0.0976` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.3894` n `196` status `ready` deltaP `5.8903` edge `0.0918` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.2127` n `196` status `ready` deltaP `5.7742` edge `0.0906` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `0.1277` n `178` status `ready` deltaP `18.8593` edge `0.7435` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.0689` n `178` status `ready` deltaP `12.1294` edge `0.0183` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1251` n `196` status `ready` deltaP `4.1336` edge `0.0414` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.5295` n `196` status `ready` deltaP `3.0399` edge `0.0308` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.6314` n `196` status `ready` deltaP `5.0745` edge `0.0188` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.6392` n `193` status `ready` deltaP `12.5735` edge `0.1321` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.6477` n `196` status `ready` deltaP `-0.3758` edge `0.0117` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7402` n `196` status `ready` deltaP `-4.5857` edge `-0.0011` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0627` n `193` status `ready` deltaP `-5.8993` edge `-0.0081` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
