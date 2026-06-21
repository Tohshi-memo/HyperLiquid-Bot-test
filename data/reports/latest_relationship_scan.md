# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T07:22:25.389199+00:00`
- Price records: `672`
- Market context records: `4290`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10690`

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

- `risk_on_high->unknown_4h` score `130.5542` n `44` status `ready` deltaP `-2.6608` edge `11.0791` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.5542` n `44` status `ready` deltaP `-2.6608` edge `11.0791` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `27.8859` n `236` status `ready` deltaP `2.4562` edge `2.4654` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `8.9108` n `236` status `ready` deltaP `0.3824` edge `1.283` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `8.1185` n `200` status `ready` deltaP `-7.6944` edge `1.1312` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `2.0039` n `44` status `ready` deltaP `31.1114` edge `-0.0357` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.0039` n `44` status `ready` deltaP `31.1114` edge `-0.0357` maxDD `-0.044`
- `risk_on_high->metal_24h` score `1.2395` n `40` status `ready` deltaP `-22.2569` edge `0.3687` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `1.2395` n `40` status `ready` deltaP `-22.2569` edge `0.3687` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `0.9972` n `44` status `ready` deltaP `15.5627` edge `0.0459` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.9972` n `44` status `ready` deltaP `15.5627` edge `0.0459` maxDD `-2.6576`
- `risk_on_high->equity_24h` score `0.9117` n `40` status `ready` deltaP `22.9167` edge `-0.0768` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.9117` n `40` status `ready` deltaP `22.9167` edge `-0.0768` maxDD `0.0`
- `risk_on_high->fx_1h` score `0.4075` n `44` status `ready` deltaP `8.043` edge `0.0033` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.4075` n `44` status `ready` deltaP `8.043` edge `0.0033` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.1394` n `44` status `ready` deltaP `7.9478` edge `0.0191` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.1394` n `44` status `ready` deltaP `7.9478` edge `0.0191` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0273` n `44` status `ready` deltaP `8.786` edge `0.004` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0273` n `44` status `ready` deltaP `8.786` edge `0.004` maxDD `-0.3925`
- `risk_on_high->equity_1h` score `-0.0441` n `44` status `ready` deltaP `6.6277` edge `-0.0089` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
