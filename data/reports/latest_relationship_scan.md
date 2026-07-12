# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T07:07:35.071773+00:00`
- Price records: `672`
- Market context records: `6474`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5847`

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

- `news_risk_high->crypto_alt_24h` score `12.3986` n `32` status `ready` deltaP `33.1597` edge `0.8269` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `7.0846` n `153` status `ready` deltaP `16.8914` edge `0.8078` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.4119` n `32` status `ready` deltaP `53.2986` edge `0.179` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1461` n `32` status `ready` deltaP `43.2165` edge `0.062` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `4.0673` n `32` status `ready` deltaP `15.4514` edge `0.4964` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `3.2584` n `32` status `ready` deltaP `29.8611` edge `0.093` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.8311` n `38` status `ready` deltaP `22.9121` edge `0.0179` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.7318` n `172` status `ready` deltaP `-5.1873` edge `0.269` maxDD `-3.2083`
- `news_risk_high->crypto_major_1h` score `0.6089` n `38` status `ready` deltaP `5.3498` edge `0.0961` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.4331` n `172` status `ready` deltaP `11.3443` edge `0.0281` maxDD `-0.4108`
- `market_context_high->unknown_4h` score `0.3041` n `172` status `ready` deltaP `-15.0879` edge `0.3665` maxDD `-10.5788`
- `market_context_high->commodity_24h` score `0.2482` n `153` status `ready` deltaP `6.2704` edge `0.1657` maxDD `-5.2791`
- `market_context_high->crypto_alt_4h` score `0.1702` n `172` status `ready` deltaP `8.0934` edge `0.1156` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.1155` n `38` status `ready` deltaP `2.0328` edge `0.0522` maxDD `-2.0756`
- `market_context_high->metal_4h` score `0.0945` n `172` status `ready` deltaP `10.9791` edge `0.0435` maxDD `-2.7056`
- `news_risk_high->unknown_1h` score `-0.4568` n `38` status `ready` deltaP `4.4516` edge `-0.0306` maxDD `-0.9718`
- `news_risk_high->index_24h` score `-0.4626` n `32` status `ready` deltaP `4.6875` edge `-0.0034` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.5038` n `172` status `ready` deltaP `1.7964` edge `0.0012` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.5162` n `172` status `ready` deltaP `7.5297` edge `0.0535` maxDD `-8.2573`
- `market_context_high->commodity_1h` score `-0.6001` n `172` status `ready` deltaP `-0.6336` edge `-0.0044` maxDD `-2.1314`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
