# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T15:52:25.779047+00:00`
- Price records: `672`
- Market context records: `4327`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10794`

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

- `risk_on_high->unknown_4h` score `130.7902` n `44` status `ready` deltaP `-1.1364` edge `11.0886` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.7902` n `44` status `ready` deltaP `-1.1364` edge `11.0886` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `31.2243` n `225` status `ready` deltaP `3.3713` edge `2.7375` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `10.7623` n `225` status `ready` deltaP `1.0556` edge `1.4328` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.7159` n `44` status `ready` deltaP `32.331` edge `0.0155` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.7159` n `44` status `ready` deltaP `32.331` edge `0.0155` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.3531` n `44` status `ready` deltaP `-20.565` edge `0.5002` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.3531` n `44` status `ready` deltaP `-20.565` edge `0.5002` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `2.2521` n `44` status `ready` deltaP `22.9167` edge `0.0349` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.2521` n `44` status `ready` deltaP `22.9167` edge `0.0349` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.7789` n `44` status `ready` deltaP `17.8493` edge `0.0958` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.7789` n `44` status `ready` deltaP `17.8493` edge `0.0958` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.3787` n `44` status `ready` deltaP `7.7436` edge `0.0029` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.3787` n `44` status `ready` deltaP `7.7436` edge `0.0029` maxDD `-0.1704`
- `risk_on_high->metal_4h` score `0.3013` n `44` status `ready` deltaP `5.1136` edge `0.0381` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.3013` n `44` status `ready` deltaP `5.1136` edge `0.0381` maxDD `-1.3516`
- `risk_on_high->crypto_major_1h` score `0.2213` n `44` status `ready` deltaP `8.0975` edge `0.0286` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2213` n `44` status `ready` deltaP `8.0975` edge `0.0286` maxDD `-2.3372`
- `risk_on_high->index_24h` score `0.2061` n `44` status `ready` deltaP `19.2708` edge `-0.1113` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.2061` n `44` status `ready` deltaP `19.2708` edge `-0.1113` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
