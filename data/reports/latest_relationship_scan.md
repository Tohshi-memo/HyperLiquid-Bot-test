# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T10:54:41.055695+00:00`
- Price records: `672`
- Market context records: `6702`
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

- `market_context_high->unknown_24h` score `0.9436` n `183` status `ready` deltaP `0.794` edge `0.4909` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.1737` n `183` status `ready` deltaP `9.009` edge `0.0482` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `0.0742` n `183` status `ready` deltaP `5.925` edge `0.0431` maxDD `-3.7803`
- `market_context_high->commodity_24h` score `-0.0148` n `183` status `ready` deltaP `9.2527` edge `0.1239` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3717` n `183` status `ready` deltaP `0.1456` edge `0.0005` maxDD `-0.5971`
- `market_context_high->unknown_1h` score `-0.4985` n `183` status `ready` deltaP `-6.6809` edge `0.0931` maxDD `-3.2083`
- `market_context_high->index_1h` score `-0.5487` n `183` status `ready` deltaP `-0.3182` edge `0.0032` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.571` n `183` status `ready` deltaP `-3.3425` edge `0.0016` maxDD `-1.2017`
- `market_context_high->commodity_1h` score `-0.662` n `183` status `ready` deltaP `-0.6397` edge `-0.0123` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.9913` n `183` status `ready` deltaP `9.3729` edge `-0.0016` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.0285` n `183` status `ready` deltaP `2.6987` edge `-0.001` maxDD `-3.8827`
- `market_context_high->fx_4h` score `-1.3063` n `183` status `ready` deltaP `6.9547` edge `-0.0009` maxDD `-2.7017`
- `market_context_high->crypto_major_4h` score `-1.6338` n `183` status `ready` deltaP `7.1988` edge `0.074` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.8286` n `183` status `ready` deltaP `-5.7094` edge `-0.0469` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.8467` n `183` status `ready` deltaP `5.4328` edge `0.0672` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.2885` n `183` status `ready` deltaP `-3.4278` edge `0.0155` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-4.005` n `183` status `ready` deltaP `-17.2789` edge `0.018` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.611` n `183` status `ready` deltaP `-9.2014` edge `-0.0022` maxDD `-6.9902`
- `market_context_high->equity_4h` score `-5.5155` n `183` status `ready` deltaP `5.9535` edge `-0.0724` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-7.0876` n `183` status `ready` deltaP `-6.8022` edge `-0.0148` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
