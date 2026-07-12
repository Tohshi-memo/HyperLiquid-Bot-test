# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T10:37:31.280152+00:00`
- Price records: `672`
- Market context records: `6489`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5869`

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

- `news_risk_high->crypto_alt_24h` score `12.7425` n `32` status `ready` deltaP `34.5486` edge `0.8463` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.489` n `32` status `ready` deltaP `53.9931` edge `0.1808` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.2546` n `159` status `ready` deltaP `15.5169` edge `0.7478` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.5151` n `32` status `ready` deltaP `17.8819` edge `0.5376` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.941` n `38` status `ready` deltaP `41.9127` edge `0.0536` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `2.9256` n `32` status `ready` deltaP `27.9514` edge `0.078` maxDD `-0.3101`
- `market_context_high->unknown_1h` score `2.8493` n `180` status `ready` deltaP `-4.2981` edge `0.3562` maxDD `-3.2083`
- `news_risk_high->fx_1h` score `1.843` n `38` status `ready` deltaP `23.0618` edge `0.0179` maxDD `-0.1113`
- `market_context_high->unknown_4h` score `0.7002` n `168` status `ready` deltaP `-14.7576` edge `0.3973` maxDD `-10.5788`
- `market_context_high->index_4h` score `0.659` n `168` status `ready` deltaP `13.9881` edge `0.0293` maxDD `-0.4108`
- `market_context_high->commodity_24h` score `0.6238` n `159` status `ready` deltaP `8.3563` edge `0.1831` maxDD `-5.2791`
- `news_risk_high->crypto_major_1h` score `0.5979` n `38` status `ready` deltaP `5.3498` edge `0.0947` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.5093` n `168` status `ready` deltaP `10.3223` edge `0.129` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.0921` n `38` status `ready` deltaP `1.7334` edge `0.0512` maxDD `-2.0756`
- `market_context_high->metal_4h` score `-0.0039` n `168` status `ready` deltaP `10.9539` edge `0.0438` maxDD `-2.7056`
- `news_risk_high->index_24h` score `-0.4493` n `32` status `ready` deltaP `4.6875` edge `-0.0017` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.4517` n `168` status `ready` deltaP `8.4857` edge `0.0554` maxDD `-8.2573`
- `market_context_high->metal_1h` score `-0.5546` n `180` status `ready` deltaP `0.835` edge `0.0011` maxDD `-1.8877`
- `market_context_high->crypto_alt_1h` score `-0.5634` n `180` status `ready` deltaP `6.324` edge `0.0169` maxDD `-5.8368`
- `market_context_high->commodity_1h` score `-0.6114` n `180` status `ready` deltaP `-1.0911` edge `-0.0028` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
