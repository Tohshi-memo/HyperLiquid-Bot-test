# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T00:37:17.177473+00:00`
- Price records: `672`
- Market context records: `1992`
- Flow alert records: `7624`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7585`

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

- `market_context_high->crypto_major_4h` score `8.2049` n `227` status `ready` deltaP `28.7553` edge `0.5492` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `7.8439` n `227` status `ready` deltaP `24.0786` edge `0.6076` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `3.9366` n `227` status `ready` deltaP `15.8778` edge `0.3555` maxDD `-6.6644`
- `market_context_high->equity_4h` score `2.3745` n `227` status `ready` deltaP `14.6442` edge `0.2097` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.1896` n `192` status `ready` deltaP `16.2314` edge `0.6063` maxDD `-35.8966`
- `market_context_high->metal_24h` score `1.8032` n `192` status `ready` deltaP `16.7951` edge `0.2809` maxDD `-12.7414`
- `market_context_high->equity_24h` score `1.2484` n `192` status `ready` deltaP `15.1612` edge `0.4928` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `1.1998` n `227` status `ready` deltaP `10.6347` edge `0.1277` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.9777` n `227` status `ready` deltaP `8.9623` edge `0.1331` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `0.6547` n `192` status `ready` deltaP `20.2412` edge `0.7782` maxDD `-62.3533`
- `market_context_high->index_4h` score `0.5392` n `227` status `ready` deltaP `8.0363` edge `0.0728` maxDD `-2.8489`
- `market_context_high->fx_24h` score `0.4354` n `192` status `ready` deltaP `13.2491` edge `0.0254` maxDD `-1.1952`
- `market_context_high->index_24h` score `0.296` n `192` status `ready` deltaP `3.496` edge `0.1242` maxDD `-4.1604`
- `market_context_high->equity_1h` score `-0.1406` n `227` status `ready` deltaP `4.4284` edge `0.0376` maxDD `-2.6402`
- `market_context_high->fx_1h` score `-0.6298` n `227` status `ready` deltaP `-2.5983` edge `-0.0002` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6934` n `227` status `ready` deltaP `-0.3917` edge `0.008` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.9635` n `227` status `ready` deltaP `1.5076` edge `0.0` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.1747` n `227` status `ready` deltaP `1.4733` edge `-0.0249` maxDD `-3.2917`
- `market_context_high->fx_4h` score `-1.191` n `227` status `ready` deltaP `-9.1134` edge `-0.0038` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.9169` n `227` status `ready` deltaP `1.5504` edge `-0.0003` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
