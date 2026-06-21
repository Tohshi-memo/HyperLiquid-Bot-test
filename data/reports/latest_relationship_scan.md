# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T17:37:30.889714+00:00`
- Price records: `672`
- Market context records: `4335`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10810`

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

- `risk_on_high->unknown_4h` score `130.9179` n `44` status `ready` deltaP `-0.6791` edge `11.0962` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.9179` n `44` status `ready` deltaP `-0.6791` edge `11.0962` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `30.931` n `226` status `ready` deltaP `3.5306` edge `2.712` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `11.0114` n `224` status `ready` deltaP `1.3502` edge `1.4516` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.9029` n `44` status `ready` deltaP `33.0932` edge `0.026` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.9029` n `44` status `ready` deltaP `33.0932` edge `0.026` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.5099` n `44` status `ready` deltaP `-19.3497` edge `0.5122` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.5099` n `44` status `ready` deltaP `-19.3497` edge `0.5122` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `2.2376` n `44` status `ready` deltaP `22.5694` edge `0.036` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.2376` n `44` status `ready` deltaP `22.5694` edge `0.036` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.6883` n `44` status `ready` deltaP `17.3919` edge `0.0913` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6883` n `44` status `ready` deltaP `17.3919` edge `0.0913` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.4446` n `44` status `ready` deltaP `8.4921` edge `0.0034` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.4446` n `44` status `ready` deltaP `8.4921` edge `0.0034` maxDD `-0.1704`
- `risk_on_high->metal_4h` score `0.405` n `44` status `ready` deltaP `6.0282` edge `0.0453` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.405` n `44` status `ready` deltaP `6.0282` edge `0.0453` maxDD `-1.3516`
- `risk_on_high->index_24h` score `0.3261` n `44` status `ready` deltaP `19.2708` edge `-0.1013` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.3261` n `44` status `ready` deltaP `19.2708` edge `-0.1013` maxDD `0.0`
- `risk_on_high->crypto_major_1h` score `0.2298` n `44` status `ready` deltaP `8.2472` edge `0.0287` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2298` n `44` status `ready` deltaP `8.2472` edge `0.0287` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
