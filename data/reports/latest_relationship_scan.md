# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T11:52:25.995790+00:00`
- Price records: `672`
- Market context records: `6706`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->unknown_24h` score `1.2563` n `179` status `ready` deltaP `1.9174` edge `0.5235` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.1996` n `179` status `ready` deltaP `9.3567` edge `0.0492` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `0.1328` n `179` status `ready` deltaP `6.3736` edge `0.045` maxDD `-3.7803`
- `market_context_high->commodity_24h` score `-0.2489` n `179` status `ready` deltaP `8.5322` edge `0.1092` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.358` n `179` status `ready` deltaP `0.3011` edge `0.0006` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.5588` n `179` status `ready` deltaP `-0.4984` edge `0.0031` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.628` n `179` status `ready` deltaP `-4.2886` edge `0.0006` maxDD `-1.2017`
- `market_context_high->commodity_1h` score `-0.6612` n `179` status `ready` deltaP `-0.6699` edge `-0.012` maxDD `-2.1314`
- `market_context_high->unknown_1h` score `-0.8902` n `179` status `ready` deltaP `-7.3922` edge `0.0652` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-0.9056` n `179` status `ready` deltaP `3.9198` edge `0.0011` maxDD `-3.8827`
- `market_context_high->index_4h` score `-0.9691` n `179` status `ready` deltaP `9.7246` edge `-0.0011` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.2347` n `179` status `ready` deltaP `7.4439` edge `0.0002` maxDD `-2.3168`
- `market_context_high->crypto_major_4h` score `-1.6829` n `179` status `ready` deltaP `7.0344` edge `0.0688` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.7889` n `179` status `ready` deltaP `-5.2604` edge `-0.0453` maxDD `-5.5853`
- `market_context_high->crypto_alt_4h` score `-1.897` n `179` status `ready` deltaP `5.3073` edge `0.0616` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.3599` n `179` status `ready` deltaP `-4.1857` edge `0.0114` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-3.8637` n `179` status `ready` deltaP `-16.833` edge `0.0268` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.3872` n `179` status `ready` deltaP `-8.4565` edge `0.0005` maxDD `-6.1111`
- `market_context_high->equity_4h` score `-5.4181` n `179` status `ready` deltaP `6.7805` edge `-0.0698` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-7.0532` n `179` status `ready` deltaP `-6.155` edge `-0.0147` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
