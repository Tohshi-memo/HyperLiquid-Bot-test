# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T04:37:27.439397+00:00`
- Price records: `672`
- Market context records: `4279`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10816`

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

- `risk_on_high->unknown_4h` score `130.4614` n `44` status `ready` deltaP `-2.9657` edge `11.0734` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.4614` n `44` status `ready` deltaP `-2.9657` edge `11.0734` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `27.784` n `236` status `ready` deltaP `1.8574` edge `2.4609` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `8.818` n `236` status `ready` deltaP `0.0775` edge `1.2773` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `7.7008` n `200` status `ready` deltaP `-8.9097` edge `1.1045` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `2.1323` n `44` status `ready` deltaP `32.0261` edge `-0.0311` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.1323` n `44` status `ready` deltaP `32.0261` edge `-0.0311` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.8268` n `44` status `ready` deltaP `14.648` edge `0.0378` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.8268` n `44` status `ready` deltaP `14.648` edge `0.0378` maxDD `-2.6576`
- `risk_on_high->metal_24h` score `0.7989` n `40` status `ready` deltaP `-23.125` edge `0.318` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `0.7989` n `40` status `ready` deltaP `-23.125` edge `0.318` maxDD `-1.9133`
- `risk_on_high->fx_1h` score `0.4734` n `44` status `ready` deltaP `8.7915` edge `0.0038` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.4734` n `44` status `ready` deltaP `8.7915` edge `0.0038` maxDD `-0.1704`
- `risk_on_high->equity_24h` score `0.4209` n `40` status `ready` deltaP `22.9167` edge `-0.1177` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.4209` n `40` status `ready` deltaP `22.9167` edge `-0.1177` maxDD `0.0`
- `risk_on_high->crypto_major_1h` score `0.0856` n `44` status `ready` deltaP `7.4987` edge `0.0152` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0856` n `44` status `ready` deltaP `7.4987` edge `0.0152` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0415` n `44` status `ready` deltaP `8.9385` edge `0.0048` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0415` n `44` status `ready` deltaP `8.9385` edge `0.0048` maxDD `-0.3925`
- `risk_on_high->equity_1h` score `-0.0453` n `44` status `ready` deltaP `6.9271` edge `-0.011` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
