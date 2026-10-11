# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T22:37:32.972514+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9132`

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

- `market_context_high->unknown_24h` score `1381.3161` n `40` status `ready` deltaP `-22.5694` edge `115.2965` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `46.1353` n `99` status `ready` deltaP `-4.1004` edge `3.93` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.8032` n `40` status `ready` deltaP `27.6736` edge `0.592` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.4156` n `40` status `ready` deltaP `52.4306` edge `0.1851` maxDD `0.0`
- `market_context_high->unknown_1h` score `3.8829` n `111` status `ready` deltaP `-2.3102` edge `0.3726` maxDD `-1.0231`
- `market_context_high->fx_24h` score `3.0363` n `40` status `ready` deltaP `34.5139` edge `0.0359` maxDD `-0.0374`
- `risk_on_high->commodity_1h` score `1.8749` n `32` status `ready` deltaP `23.3346` edge `0.0144` maxDD `-0.0975`
- `risk_on_and_context->commodity_1h` score `1.8749` n `32` status `ready` deltaP `23.3346` edge `0.0144` maxDD `-0.0975`
- `market_context_high->crypto_major_24h` score `1.3816` n `40` status `ready` deltaP `-21.1111` edge `0.5707` maxDD `-17.8526`
- `risk_on_high->crypto_alt_1h` score `1.0873` n `32` status `ready` deltaP `10.9843` edge `0.1217` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.0873` n `32` status `ready` deltaP `10.9843` edge `0.1217` maxDD `-2.4421`
- `risk_on_high->metal_1h` score `0.7526` n `32` status `ready` deltaP `13.5292` edge `0.0204` maxDD `-0.1286`
- `risk_on_and_context->metal_1h` score `0.7526` n `32` status `ready` deltaP `13.5292` edge `0.0204` maxDD `-0.1286`
- `market_context_high->commodity_4h` score `0.6526` n `99` status `ready` deltaP `13.4285` edge `0.0182` maxDD `-1.6002`
- `market_context_high->fx_4h` score `0.4789` n `99` status `ready` deltaP `9.9209` edge `0.0063` maxDD `-0.2692`
- `market_context_high->commodity_1h` score `0.325` n `111` status `ready` deltaP `7.3718` edge `0.0063` maxDD `-0.6025`
- `risk_on_high->crypto_major_1h` score `0.2562` n `32` status `ready` deltaP `3.125` edge `0.0773` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.2562` n `32` status `ready` deltaP `3.125` edge `0.0773` maxDD `-3.2233`
- `market_context_high->crypto_alt_1h` score `0.1139` n `111` status `ready` deltaP `4.8188` edge `0.0859` maxDD `-4.9401`
- `market_context_high->metal_4h` score `0.0196` n `99` status `ready` deltaP `8.0716` edge `0.0201` maxDD `-1.1153`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
