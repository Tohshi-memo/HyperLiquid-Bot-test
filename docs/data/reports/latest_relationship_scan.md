# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T19:37:30.446159+00:00`
- Price records: `672`
- Market context records: `4344`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11234`

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

- `risk_on_high->unknown_4h` score `131.1091` n `44` status `ready` deltaP `-0.3742` edge `11.1101` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `131.1091` n `44` status `ready` deltaP `-0.3742` edge `11.1101` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `31.2292` n `224` status `ready` deltaP `3.2079` edge `2.739` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `11.5125` n `221` status `ready` deltaP `2.0631` edge `1.4886` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.061` n `44` status `ready` deltaP `33.8553` edge `0.0341` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.061` n `44` status `ready` deltaP `33.8553` edge `0.0341` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.6347` n `44` status `ready` deltaP `-18.1344` edge `0.5201` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.6347` n `44` status `ready` deltaP `-18.1344` edge `0.5201` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `2.0172` n `44` status `ready` deltaP `21.1806` edge `0.0269` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.0172` n `44` status `ready` deltaP `21.1806` edge `0.0269` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.6689` n `44` status `ready` deltaP `17.2395` edge `0.0907` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6689` n `44` status `ready` deltaP `17.2395` edge `0.0907` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.4841` n `44` status `ready` deltaP `8.9412` edge `0.0037` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.4841` n `44` status `ready` deltaP `8.9412` edge `0.0037` maxDD `-0.1704`
- `risk_on_high->metal_4h` score `0.4453` n `44` status `ready` deltaP `6.638` edge `0.0464` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.4453` n `44` status `ready` deltaP `6.638` edge `0.0464` maxDD `-1.3516`
- `risk_on_high->index_24h` score `0.4089` n `44` status `ready` deltaP `19.2708` edge `-0.0944` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.4089` n `44` status `ready` deltaP `19.2708` edge `-0.0944` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.2844` n `44` status `ready` deltaP `8.4241` edge `0.0065` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.2844` n `44` status `ready` deltaP `8.4241` edge `0.0065` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
