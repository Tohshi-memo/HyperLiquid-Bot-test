# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T03:07:30.055368+00:00`
- Price records: `672`
- Market context records: `8474`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5828`

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

- `news_risk_high->unknown_24h` score `6266.8061` n `52` status `ready` deltaP `44.0438` edge `521.9823` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.2751` n `61` status `ready` deltaP `22.7434` edge `0.431` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.2202` n `61` status `ready` deltaP `18.4751` edge `0.0809` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.814` n `64` status `ready` deltaP `16.701` edge `0.0875` maxDD `-2.4803`
- `news_risk_high->crypto_alt_4h` score `1.2876` n `61` status `ready` deltaP `16.7933` edge `0.1923` maxDD `-5.8012`
- `news_risk_high->crypto_major_4h` score `1.2618` n `61` status `ready` deltaP `6.9972` edge `0.1845` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `0.6019` n `64` status `ready` deltaP `10.058` edge `0.0628` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3384` n `64` status `ready` deltaP `7.064` edge `0.0475` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.1173` n `64` status `ready` deltaP `5.8851` edge `0.0039` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0536` n `61` status `ready` deltaP `11.6429` edge `0.0226` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0387` n `64` status `ready` deltaP `4.2197` edge `0.0085` maxDD `-0.5338`
- `news_risk_high->metal_1h` score `-0.2701` n `64` status `ready` deltaP `1.9087` edge `0.0051` maxDD `-0.5599`
- `news_risk_high->metal_4h` score `-0.4726` n `61` status `ready` deltaP `-2.0742` edge `0.0217` maxDD `-0.7801`
- `news_risk_high->commodity_1h` score `-1.5022` n `64` status `ready` deltaP `-2.3578` edge `-0.0309` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5585` n `52` status `ready` deltaP `-27.7244` edge `-0.0462` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.42` n `61` status `ready` deltaP `-18.5526` edge `-0.1639` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.2624` n `52` status `ready` deltaP `-36.6186` edge `-0.2507` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.9198` n `52` status `ready` deltaP `-13.3013` edge `-0.394` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-14.3219` n `52` status `ready` deltaP `-34.6688` edge `-0.4121` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-40.3326` n `52` status `ready` deltaP `-30.008` edge `-1.7085` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
