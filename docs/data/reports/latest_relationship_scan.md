# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T22:52:26.671996+00:00`
- Price records: `672`
- Market context records: `4873`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7594`

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

- `market_context_high->unknown_1h` score `15.3066` n `110` status `ready` deltaP `10.1715` edge `1.2495` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.6442` n `110` status `ready` deltaP `23.1624` edge `0.7024` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.4436` n `110` status `ready` deltaP `21.2084` edge `0.5308` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.136` n `110` status `ready` deltaP `18.1873` edge `0.5125` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.238` n `91` status `ready` deltaP `25.6429` edge `0.2998` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.2486` n `110` status `ready` deltaP `9.2822` edge `0.1084` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8773` n `110` status `ready` deltaP `12.439` edge `0.1677` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5557` n `110` status `ready` deltaP `11.5355` edge `0.0406` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4718` n `110` status `ready` deltaP `6.4698` edge `0.1212` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.455` n `110` status `ready` deltaP `8.4703` edge `0.1041` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2145` n `110` status `ready` deltaP `4.2352` edge `0.059` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.1596` n `110` status `ready` deltaP `0.9934` edge `0.0309` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2106` n `110` status `ready` deltaP `3.5819` edge `0.0151` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4861` n `110` status `ready` deltaP `0.3103` edge `0.0111` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.6261` n `110` status `ready` deltaP `1.6768` edge `0.0056` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.929` n `110` status `ready` deltaP `5.6624` edge `0.0035` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.349` n `110` status `ready` deltaP `-7.0169` edge `-0.0043` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.8392` n `91` status `ready` deltaP `-6.3359` edge `-0.01` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.6611` n `91` status `ready` deltaP `-6.7976` edge `-0.1437` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.1457` n `91` status `ready` deltaP `12.416` edge `-0.0007` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
