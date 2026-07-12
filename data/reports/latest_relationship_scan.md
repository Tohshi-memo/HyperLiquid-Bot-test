# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T12:07:30.017632+00:00`
- Price records: `672`
- Market context records: `6496`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5862`

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

- `news_risk_high->crypto_alt_24h` score `12.8323` n `32` status `ready` deltaP `34.6512` edge `0.8531` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.4876` n `32` status `ready` deltaP `53.8995` edge `0.1813` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.2412` n `155` status `ready` deltaP `14.5547` edge `0.7531` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.6611` n `32` status `ready` deltaP `18.8312` edge `0.55` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.9213` n `38` status `ready` deltaP `41.6807` edge `0.0535` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.8096` n `180` status `ready` deltaP `-4.7039` edge `0.3556` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.7626` n `32` status `ready` deltaP `27.0093` edge `0.0707` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.843` n `38` status `ready` deltaP `23.0618` edge `0.0179` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `0.855` n `155` status `ready` deltaP `9.7311` edge `0.1932` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.7393` n `169` status `ready` deltaP `14.9766` edge `0.0294` maxDD `-0.4108`
- `market_context_high->crypto_alt_4h` score `0.6242` n `169` status `ready` deltaP `10.9031` edge `0.1347` maxDD `-6.7632`
- `market_context_high->unknown_4h` score `0.6196` n `169` status `ready` deltaP `-14.8946` edge `0.3915` maxDD `-10.5788`
- `news_risk_high->crypto_major_1h` score `0.5738` n `38` status `ready` deltaP `5.2001` edge `0.0926` maxDD `-2.6299`
- `news_risk_high->crypto_alt_1h` score `0.0859` n `38` status `ready` deltaP `1.7334` edge `0.0504` maxDD `-2.0756`
- `market_context_high->metal_4h` score `-0.378` n `169` status `ready` deltaP `8.928` edge `0.0428` maxDD `-2.7056`
- `news_risk_high->index_24h` score `-0.4173` n `32` status `ready` deltaP `5.1235` edge `-0.0005` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.4335` n `169` status `ready` deltaP `8.656` edge `0.0566` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.5013` n `180` status `ready` deltaP `-1.4704` edge `-0.0021` maxDD `-0.8555`
- `market_context_high->crypto_alt_1h` score `-0.5463` n `180` status `ready` deltaP `6.324` edge `0.0191` maxDD `-5.8368`
- `market_context_high->crypto_major_1h` score `-0.5686` n `180` status `ready` deltaP `6.1943` edge `0.0124` maxDD `-6.7936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
