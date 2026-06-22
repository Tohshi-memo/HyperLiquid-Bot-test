# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-22T08:22:27.960160+00:00`
- Price records: `672`
- Market context records: `4398`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11123`

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

- `risk_on_high->unknown_4h` score `130.3738` n `45` status `ready` deltaP `0.4844` edge `11.0431` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.3738` n `45` status `ready` deltaP `0.4844` edge `11.0431` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `32.4976` n `225` status `ready` deltaP `2.7678` edge `2.8393` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `11.7336` n `217` status `ready` deltaP `5.0825` edge `1.4869` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.1678` n `45` status `ready` deltaP `34.5156` edge `0.0386` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.1678` n `45` status `ready` deltaP `34.5156` edge `0.0386` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.9859` n `44` status `ready` deltaP `-15.3567` edge `0.5466` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.9859` n `44` status `ready` deltaP `-15.3567` edge `0.5466` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `2.1602` n `45` status `ready` deltaP `18.7601` edge `0.1215` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.1602` n `45` status `ready` deltaP `18.7601` edge `0.1215` maxDD `-2.6576`
- `risk_on_high->equity_24h` score `1.7541` n `44` status `ready` deltaP `20.4861` edge `0.0096` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.7541` n `44` status `ready` deltaP `20.4861` edge `0.0096` maxDD `0.0`
- `risk_on_high->index_24h` score `1.4502` n `44` status `ready` deltaP `23.4375` edge `-0.0354` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.4502` n `44` status `ready` deltaP `23.4375` edge `-0.0354` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.799` n `49` status `ready` deltaP `12.6513` edge `0.0212` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.799` n `49` status `ready` deltaP `12.6513` edge `0.0212` maxDD `-0.7834`
- `risk_on_high->metal_4h` score `0.3227` n `45` status `ready` deltaP `6.1246` edge `0.0341` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.3227` n `45` status `ready` deltaP `6.1246` edge `0.0341` maxDD `-1.3516`
- `risk_on_high->fx_1h` score `0.2417` n `49` status `ready` deltaP `6.0002` edge `0.0031` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.2417` n `49` status `ready` deltaP `6.0002` edge `0.0031` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
