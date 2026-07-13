# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T03:22:26.994043+00:00`
- Price records: `672`
- Market context records: `6565`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9886`

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

- `market_context_high->unknown_24h` score `6.2498` n `144` status `ready` deltaP `11.032` edge `0.7773` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.7297` n `210` status `ready` deltaP `-5.2736` edge `0.2694` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3881` n `144` status `ready` deltaP `13.3492` edge `0.2135` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3548` n `210` status `ready` deltaP `0.8458` edge `-0.0004` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.3783` n `210` status `ready` deltaP `7.3489` edge `0.0291` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.4309` n `210` status `ready` deltaP `6.9368` edge `0.0298` maxDD `-5.8368`
- `market_context_high->index_1h` score `-0.5469` n `210` status `ready` deltaP `-0.3838` edge `0.0044` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.5894` n `210` status `ready` deltaP `-0.398` edge `-0.0046` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.7005` n `207` status `ready` deltaP `8.6714` edge `0.0111` maxDD `-4.3645`
- `market_context_high->crypto_major_4h` score `-1.0868` n `207` status `ready` deltaP `8.7037` edge `0.0692` maxDD `-12.6576`
- `market_context_high->equity_1h` score `-1.1117` n `210` status `ready` deltaP `2.2317` edge `0.0035` maxDD `-4.2147`
- `market_context_high->metal_1h` score `-1.2235` n `210` status `ready` deltaP `-3.1414` edge `-0.0003` maxDD `-2.1239`
- `market_context_high->crypto_alt_4h` score `-1.2235` n `207` status `ready` deltaP `6.0386` edge `0.0747` maxDD `-14.7452`
- `market_context_high->commodity_4h` score `-1.3862` n `207` status `ready` deltaP `-2.3471` edge `-0.0126` maxDD `-5.6246`
- `market_context_high->unknown_4h` score `-1.394` n `207` status `ready` deltaP `-15.945` edge `0.2307` maxDD `-10.5788`
- `market_context_high->fx_4h` score `-1.7849` n `207` status `ready` deltaP `-0.5293` edge `-0.0041` maxDD `-3.3635`
- `market_context_high->metal_4h` score `-1.8904` n `207` status `ready` deltaP `-0.812` edge `0.026` maxDD `-4.3688`
- `market_context_high->metal_24h` score `-1.9465` n `144` status `ready` deltaP `6.0917` edge `0.0902` maxDD `-5.7746`
- `market_context_high->equity_4h` score `-3.6736` n `207` status `ready` deltaP `6.9234` edge `-0.0142` maxDD `-21.0469`
- `market_context_high->index_24h` score `-3.7641` n `144` status `ready` deltaP `1.4429` edge `-0.0012` maxDD `-10.7676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
