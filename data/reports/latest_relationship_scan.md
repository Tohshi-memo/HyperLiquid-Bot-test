# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T03:22:26.769917+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6597`

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

- `market_context_high->equity_24h` score `10.9726` n `32` status `ready` deltaP `18.0556` edge `1.0313` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.885` n `32` status `ready` deltaP `9.5486` edge `0.2355` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.5192` n `32` status `ready` deltaP `18.2292` edge `0.1195` maxDD `-2.3671`
- `market_context_high->equity_1h` score `1.0432` n `69` status `ready` deltaP `5.2699` edge `0.1715` maxDD `-5.5762`
- `market_context_high->metal_1h` score `0.9666` n `69` status `ready` deltaP `11.72` edge `0.0352` maxDD `-0.6226`
- `market_context_high->fx_24h` score `0.647` n `32` status `ready` deltaP `10.4167` edge `-0.0067` maxDD `-0.0397`
- `market_context_high->metal_4h` score `0.5026` n `57` status `ready` deltaP `8.2745` edge `0.0618` maxDD `-1.2025`
- `market_context_high->commodity_4h` score `0.2424` n `57` status `ready` deltaP `1.3372` edge `0.0585` maxDD `-1.1102`
- `market_context_high->commodity_1h` score `0.0929` n `69` status `ready` deltaP `6.9774` edge `0.02` maxDD `-1.7019`
- `market_context_high->index_4h` score `-0.0371` n `57` status `ready` deltaP `10.7937` edge `0.0178` maxDD `-2.4279`
- `market_context_high->index_1h` score `-0.2463` n `69` status `ready` deltaP `2.3713` edge `0.022` maxDD `-0.6664`
- `market_context_high->crypto_alt_1h` score `-0.4561` n `69` status `ready` deltaP `11.7612` edge `0.0524` maxDD `-10.1421`
- `market_context_high->fx_1h` score `-0.941` n `69` status `ready` deltaP `-11.5638` edge `-0.0041` maxDD `-0.4893`
- `market_context_high->fx_4h` score `-1.1789` n `57` status `ready` deltaP `-4.3806` edge `-0.0025` maxDD `-1.2219`
- `market_context_high->metal_24h` score `-1.5028` n `32` status `ready` deltaP `1.0417` edge `-0.1443` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-1.7797` n `69` status `ready` deltaP `2.8682` edge `-0.0374` maxDD `-11.7911`
- `market_context_high->equity_4h` score `-4.2526` n `57` status `ready` deltaP `5.9853` edge `-0.0163` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-4.6942` n `32` status `ready` deltaP `-4.8611` edge `0.0055` maxDD `-23.1423`
- `market_context_high->crypto_alt_4h` score `-7.6529` n `57` status `ready` deltaP `4.8352` edge `-0.2031` maxDD `-30.6833`
- `market_context_high->crypto_alt_24h` score `-8.8378` n `32` status `ready` deltaP `-18.75` edge `-0.1536` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
