# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T07:52:29.741865+00:00`
- Price records: `672`
- Market context records: `4292`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10730`

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

- `risk_on_high->unknown_4h` score `130.4662` n `44` status `ready` deltaP `-2.9657` edge `11.0738` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.4662` n `44` status `ready` deltaP `-2.9657` edge `11.0738` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `27.7911` n `236` status `ready` deltaP `2.1568` edge `2.4595` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `8.8228` n `236` status `ready` deltaP `0.0775` edge `1.2777` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `7.6409` n `201` status `ready` deltaP `-7.7089` edge `1.0915` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `2.0075` n `44` status `ready` deltaP `31.1114` edge `-0.0354` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.0075` n `44` status `ready` deltaP `31.1114` edge `-0.0354` maxDD `-0.044`
- `risk_on_high->metal_24h` score `1.3413` n `40` status `ready` deltaP `-22.0833` edge `0.3806` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `1.3413` n `40` status `ready` deltaP `-22.0833` edge `0.3806` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `1.0432` n `44` status `ready` deltaP `15.8675` edge `0.0477` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.0432` n `44` status `ready` deltaP `15.8675` edge `0.0477` maxDD `-2.6576`
- `risk_on_high->equity_24h` score `1.0161` n `40` status `ready` deltaP `22.9167` edge `-0.0681` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.0161` n `40` status `ready` deltaP `22.9167` edge `-0.0681` maxDD `0.0`
- `risk_on_high->fx_1h` score `0.4087` n `44` status `ready` deltaP `8.043` edge `0.0034` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.4087` n `44` status `ready` deltaP `8.043` edge `0.0034` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.1511` n `44` status `ready` deltaP `8.0975` edge `0.0196` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.1511` n `44` status `ready` deltaP `8.0975` edge `0.0196` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0202` n `44` status `ready` deltaP `8.6336` edge `0.0041` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0202` n `44` status `ready` deltaP `8.6336` edge `0.0041` maxDD `-0.3925`
- `risk_on_high->equity_1h` score `-0.0597` n `44` status `ready` deltaP `6.478` edge `-0.0092` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
