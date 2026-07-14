# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T09:52:28.687040+00:00`
- Price records: `672`
- Market context records: `6697`
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

- `market_context_high->unknown_24h` score `0.7999` n `185` status `ready` deltaP `0.2505` edge `0.4761` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.1857` n `185` status `ready` deltaP `9.0435` edge `0.0495` maxDD `-4.2122`
- `market_context_high->commodity_24h` score `0.1426` n `185` status `ready` deltaP `9.6012` edge `0.1347` maxDD `-5.2791`
- `market_context_high->crypto_alt_1h` score `0.0824` n `185` status `ready` deltaP `5.9832` edge `0.0434` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3925` n `185` status `ready` deltaP `-0.0453` edge `0.0002` maxDD `-0.6845`
- `market_context_high->unknown_1h` score `-0.5238` n `185` status `ready` deltaP `-6.6071` edge `0.0905` maxDD `-3.2083`
- `market_context_high->index_1h` score `-0.5308` n `185` status `ready` deltaP `-0.0041` edge `0.0034` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.5615` n `185` status `ready` deltaP `-3.189` edge `0.0018` maxDD `-1.2017`
- `market_context_high->commodity_1h` score `-0.664` n `185` status `ready` deltaP `-0.6781` edge `-0.0123` maxDD `-2.1314`
- `market_context_high->equity_1h` score `-0.999` n `185` status `ready` deltaP `2.9479` edge `-0.0002` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.0019` n `185` status `ready` deltaP `9.1685` edge `-0.0016` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.3309` n `185` status `ready` deltaP `7.0327` edge `-0.0011` maxDD `-2.9797`
- `market_context_high->crypto_major_4h` score `-1.6216` n `185` status `ready` deltaP `7.2833` edge `0.075` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.8013` n `185` status `ready` deltaP `-5.4252` edge `-0.0453` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.8643` n `185` status `ready` deltaP `5.0659` edge `0.0674` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.2819` n `185` status `ready` deltaP `-3.3759` edge `0.016` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-4.0772` n `185` status `ready` deltaP `-17.4159` edge `0.0129` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.7301` n `185` status `ready` deltaP `-9.5617` edge `-0.0028` maxDD `-7.5435`
- `market_context_high->equity_4h` score `-5.4904` n `185` status `ready` deltaP `5.9666` edge `-0.0704` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-7.0966` n `185` status `ready` deltaP `-7.0955` edge `-0.014` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
