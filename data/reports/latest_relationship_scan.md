# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T04:07:26.570692+00:00`
- Price records: `672`
- Market context records: `4896`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8584`

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

- `market_context_high->unknown_1h` score `15.0031` n `110` status `ready` deltaP `9.423` edge `1.2292` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.5278` n `110` status `ready` deltaP `23.1624` edge `0.6927` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.5134` n `110` status `ready` deltaP `21.3609` edge `0.5356` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.4394` n `110` status `ready` deltaP `18.9495` edge `0.5327` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.3344` n `91` status `ready` deltaP `24.2541` edge `0.3171` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.1101` n `110` status `ready` deltaP `7.9102` edge `0.106` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8984` n `110` status `ready` deltaP `12.439` edge `0.1704` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5565` n `110` status `ready` deltaP `11.5355` edge `0.0407` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4765` n `110` status `ready` deltaP `6.6195` edge `0.1208` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4316` n `110` status `ready` deltaP `8.3206` edge `0.1021` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2168` n `110` status `ready` deltaP `4.2352` edge `0.0593` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.2258` n `110` status `ready` deltaP `-0.2042` edge `0.0304` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2308` n `110` status `ready` deltaP `3.1328` edge `0.0155` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.525` n `110` status `ready` deltaP `-0.4382` edge `0.0111` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.7201` n `110` status `ready` deltaP `0.1524` edge `0.0037` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.8342` n `110` status `ready` deltaP `6.577` edge `0.0053` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3609` n `110` status `ready` deltaP `-7.1666` edge `-0.0043` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.6081` n `91` status `ready` deltaP `-3.7317` edge `-0.0081` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.5494` n `91` status `ready` deltaP `-5.2351` edge `-0.1398` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-4.6476` n `91` status `ready` deltaP `16.0618` edge `0.0165` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
