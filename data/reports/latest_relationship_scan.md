# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T07:37:16.356099+00:00`
- Price records: `672`
- Market context records: `1925`
- Flow alert records: `7440`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6020`

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

- `market_context_high->crypto_alt_4h` score `7.5702` n `204` status `ready` deltaP `23.6729` edge `0.5875` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.0894` n `204` status `ready` deltaP `28.8588` edge `0.523` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.7272` n `204` status `ready` deltaP `17.2345` edge `0.3981` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.441` n `204` status `ready` deltaP `15.0706` edge `0.2124` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `0.7671` n `216` status `ready` deltaP `8.6605` edge `0.1048` maxDD `-3.2225`
- `market_context_high->unknown_24h` score `0.6189` n `196` status `ready` deltaP `13.818` edge `0.4915` maxDD `-35.8966`
- `market_context_high->crypto_alt_1h` score `0.5744` n `216` status `ready` deltaP `7.6403` edge `0.1083` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.3942` n `196` status `ready` deltaP `12.2626` edge `0.1937` maxDD `-12.7414`
- `market_context_high->index_4h` score `0.3812` n `204` status `ready` deltaP `9.6993` edge `0.076` maxDD `-3.7119`
- `market_context_high->index_24h` score `0.2102` n `196` status `ready` deltaP `4.2233` edge `0.1122` maxDD `-4.1604`
- `market_context_high->equity_1h` score `-0.1219` n `216` status `ready` deltaP `5.0427` edge `0.0356` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2381` n `196` status `ready` deltaP `10.1793` edge `0.0172` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.613` n `216` status `ready` deltaP `0.4935` edge `0.0088` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.6438` n `216` status `ready` deltaP `5.1065` edge `0.017` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6834` n `216` status `ready` deltaP `-3.7176` edge `0.0004` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-0.8617` n `204` status `ready` deltaP `-3.2341` edge `-0.0001` maxDD `-1.1056`
- `market_context_high->metal_4h` score `-0.9` n `204` status `ready` deltaP `10.4674` edge `0.1244` maxDD `-12.5349`
- `market_context_high->unknown_1h` score `-1.1845` n `216` status `ready` deltaP `2.1125` edge `-0.0176` maxDD `-3.6151`
- `market_context_high->equity_24h` score `-1.3952` n `196` status `ready` deltaP `6.4166` edge `0.3308` maxDD `-33.1875`
- `market_context_high->commodity_1h` score `-2.0298` n `216` status `ready` deltaP `0.9398` edge `-0.0107` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
