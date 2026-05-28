# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T07:52:22.523363+00:00`
- Price records: `672`
- Market context records: `2121`
- Flow alert records: `8003`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9149`

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

- `market_context_high->crypto_alt_4h` score `13.2197` n `160` status `ready` deltaP `37.2713` edge `0.9468` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.914` n `160` status `ready` deltaP `41.5091` edge `0.7691` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.0814` n `160` status `ready` deltaP `24.375` edge `0.4192` maxDD `-2.6599`
- `market_context_high->equity_4h` score `5.1007` n `160` status `ready` deltaP `26.311` edge `0.3591` maxDD `-5.0894`
- `market_context_high->metal_4h` score `3.2111` n `160` status `ready` deltaP `21.936` edge `0.2601` maxDD `-4.7664`
- `market_context_high->index_4h` score `3.1558` n `160` status `ready` deltaP `22.8963` edge `0.1787` maxDD `-1.8022`
- `news_risk_high->unknown_1h` score `2.9192` n `31` status `ready` deltaP `31.6255` edge `0.0627` maxDD `-1.7548`
- `market_context_high->crypto_major_1h` score `2.9113` n `160` status `ready` deltaP `16.7702` edge `0.194` maxDD `-2.3888`
- `market_context_high->index_24h` score `2.8926` n `159` status `ready` deltaP `12.4328` edge `0.281` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `2.75` n `160` status `ready` deltaP `14.0756` edge `0.2217` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.9423` n `159` status `ready` deltaP `23.8352` edge `0.4928` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.53` n `159` status `ready` deltaP `24.3216` edge `0.4974` maxDD `-35.8966`
- `news_risk_high->commodity_1h` score `1.1699` n `31` status `ready` deltaP `11.1406` edge `0.0912` maxDD `-2.1052`
- `market_context_high->crypto_major_24h` score `1.0506` n `159` status `ready` deltaP `20.412` edge `0.8572` maxDD `-62.3533`
- `market_context_high->equity_1h` score `0.6902` n `160` status `ready` deltaP `9.1879` edge `0.0751` maxDD `-2.6402`
- `market_context_high->metal_1h` score `0.4944` n `160` status `ready` deltaP `8.2485` edge `0.0532` maxDD `-2.3594`
- `news_risk_high->fx_1h` score `0.1884` n `31` status `ready` deltaP `5.1381` edge `0.0071` maxDD `-0.0524`
- `market_context_high->unknown_1h` score `0.1448` n `160` status `ready` deltaP `5.2545` edge `0.049` maxDD `-3.0902`
- `market_context_high->metal_24h` score `-0.0192` n `159` status `ready` deltaP `10.5994` edge `0.317` maxDD `-23.2095`
- `market_context_high->index_1h` score `-0.0646` n `160` status `ready` deltaP `3.6078` edge `0.0296` maxDD `-1.3898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
