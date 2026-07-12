# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T05:52:26.553894+00:00`
- Price records: `672`
- Market context records: `6468`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5907`

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

- `news_risk_high->crypto_alt_24h` score `12.1744` n `32` status `ready` deltaP `32.2917` edge `0.814` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `6.8951` n `153` status `ready` deltaP `16.0233` edge `0.7978` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.3479` n `32` status `ready` deltaP `52.6042` edge `0.1783` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0962` n `32` status `ready` deltaP `42.6067` edge `0.0619` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.8638` n `32` status `ready` deltaP `14.5833` edge `0.4761` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `3.3986` n `32` status `ready` deltaP `30.7292` edge `0.0989` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.8311` n `38` status `ready` deltaP `22.9121` edge `0.0179` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.5554` n `172` status `ready` deltaP `-5.6364` edge `0.2573` maxDD `-3.2083`
- `news_risk_high->crypto_major_1h` score `0.5605` n `38` status `ready` deltaP `4.9007` edge `0.0929` maxDD `-2.6299`
- `market_context_high->commodity_24h` score `0.3884` n `153` status `ready` deltaP `7.1385` edge `0.1716` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.3673` n `172` status `ready` deltaP `10.5821` edge `0.0277` maxDD `-0.4108`
- `market_context_high->unknown_4h` score `0.2813` n `172` status `ready` deltaP `-15.0879` edge `0.3646` maxDD `-10.5788`
- `market_context_high->crypto_alt_4h` score `0.1` n `172` status `ready` deltaP `7.6361` edge `0.1128` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.0687` n `38` status `ready` deltaP `1.5837` edge `0.0492` maxDD `-2.0756`
- `market_context_high->metal_4h` score `0.0567` n `172` status `ready` deltaP `10.5218` edge `0.0434` maxDD `-2.7056`
- `news_risk_high->index_24h` score `-0.4626` n `32` status `ready` deltaP `4.6875` edge `-0.0034` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.5435` n `172` status `ready` deltaP `1.0479` edge `0.0011` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.5699` n `172` status `ready` deltaP `6.7675` edge `0.0517` maxDD `-8.2573`
- `market_context_high->commodity_1h` score `-0.5923` n `172` status `ready` deltaP `-0.4839` edge `-0.0044` maxDD `-2.1314`
- `news_risk_high->unknown_1h` score `-0.6332` n `38` status `ready` deltaP `4.0025` edge `-0.0423` maxDD `-0.9718`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
