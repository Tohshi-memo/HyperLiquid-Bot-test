# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T04:37:27.198695+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9986`

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

- `market_context_high->unknown_4h` score `49.5178` n `46` status `ready` deltaP `7.3171` edge `4.0777` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `35.7085` n `46` status `ready` deltaP `22.5619` edge `2.8409` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `20.1979` n `46` status `ready` deltaP `21.3542` edge `1.5408` maxDD `0.0`
- `market_context_high->equity_24h` score `17.405` n `46` status `ready` deltaP `15.7911` edge `1.3552` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `7.9914` n `101` status `ready` deltaP `-2.7933` edge `1.3704` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.6772` n `46` status `ready` deltaP `20.1314` edge `0.3476` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `3.7169` n `101` status `ready` deltaP `-2.4082` edge `0.8139` maxDD `-32.7147`
- `news_risk_high->commodity_24h` score `2.7653` n `101` status `ready` deltaP `33.9607` edge `0.2587` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.6843` n `101` status `ready` deltaP `13.2788` edge `0.2561` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.2486` n `101` status `ready` deltaP `13.6865` edge `0.1427` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.156` n `101` status `ready` deltaP `16.3276` edge `0.1966` maxDD `-8.0625`
- `market_context_high->index_4h` score `1.9725` n `46` status `ready` deltaP `23.3165` edge `0.0223` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.5748` n `101` status `ready` deltaP `15.4829` edge `0.0803` maxDD `-2.8494`
- `market_context_high->crypto_alt_4h` score `1.1287` n `46` status `ready` deltaP `8.974` edge `0.0937` maxDD `-2.7574`
- `market_context_high->equity_4h` score `1.0632` n `46` status `ready` deltaP `8.1389` edge `0.065` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.8653` n `46` status `ready` deltaP `6.9123` edge `0.0503` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.7851` n `101` status `ready` deltaP `14.4334` edge `0.0328` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6064` n `46` status `ready` deltaP `9.7566` edge `0.0108` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5562` n `101` status `ready` deltaP `13.9992` edge `0.0132` maxDD `-0.8144`
- `market_context_high->crypto_major_1h` score `0.487` n `46` status `ready` deltaP `0.9113` edge `0.0868` maxDD `-2.1836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
