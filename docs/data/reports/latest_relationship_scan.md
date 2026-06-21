# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T11:07:30.988212+00:00`
- Price records: `672`
- Market context records: `4306`
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

- `risk_on_high->unknown_4h` score `130.6164` n `44` status `ready` deltaP `-1.8986` edge `11.0792` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.6164` n `44` status `ready` deltaP `-1.8986` edge `11.0792` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `27.893` n `236` status `ready` deltaP `3.2047` edge `2.461` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `8.973` n `236` status `ready` deltaP `1.1446` edge `1.2831` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `5.259` n `207` status `ready` deltaP `-7.8879` edge `0.8942` maxDD `-24.2693`
- `risk_on_high->metal_24h` score `2.0027` n `40` status `ready` deltaP `-20.0` edge `0.4515` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.0027` n `40` status `ready` deltaP `-20.0` edge `0.4515` maxDD `-1.9133`
- `risk_on_high->equity_4h` score `1.9247` n `44` status `ready` deltaP `30.1968` edge `-0.0362` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.9247` n `44` status `ready` deltaP `30.1968` edge `-0.0362` maxDD `-0.044`
- `risk_on_high->equity_24h` score `1.6593` n `40` status `ready` deltaP `22.9167` edge `-0.0145` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.6593` n `40` status `ready` deltaP `22.9167` edge `-0.0145` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.0708` n `44` status `ready` deltaP `15.8675` edge `0.05` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.0708` n `44` status `ready` deltaP `15.8675` edge `0.05` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.4566` n `44` status `ready` deltaP `8.6418` edge `0.0034` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.4566` n `44` status `ready` deltaP `8.6418` edge `0.0034` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.1596` n `44` status `ready` deltaP `8.2472` edge `0.0197` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.1596` n `44` status `ready` deltaP `8.2472` edge `0.0197` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0021` n `44` status `ready` deltaP `8.4811` edge `0.0028` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0021` n `44` status `ready` deltaP `8.4811` edge `0.0028` maxDD `-0.3925`
- `risk_on_high->equity_1h` score `-0.0501` n `44` status `ready` deltaP `6.6277` edge `-0.0094` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
