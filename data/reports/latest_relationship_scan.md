# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T10:37:26.979594+00:00`
- Price records: `672`
- Market context records: `4304`
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

- `risk_on_high->unknown_4h` score `130.6284` n `44` status `ready` deltaP `-1.8986` edge `11.0802` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.6284` n `44` status `ready` deltaP `-1.8986` edge `11.0802` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `27.8762` n `236` status `ready` deltaP `3.055` edge `2.4606` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `8.985` n `236` status `ready` deltaP `1.1446` edge `1.2841` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `5.2026` n `207` status `ready` deltaP `-7.8879` edge `0.8895` maxDD `-24.2693`
- `risk_on_high->metal_24h` score `1.9141` n `40` status `ready` deltaP `-20.1736` edge `0.4413` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `1.9141` n `40` status `ready` deltaP `-20.1736` edge `0.4413` maxDD `-1.9133`
- `risk_on_high->equity_4h` score `1.9126` n `44` status `ready` deltaP `30.0444` edge `-0.0362` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.9126` n `44` status `ready` deltaP `30.0444` edge `-0.0362` maxDD `-0.044`
- `risk_on_high->equity_24h` score `1.5717` n `40` status `ready` deltaP `22.9167` edge `-0.0218` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.5717` n `40` status `ready` deltaP `22.9167` edge `-0.0218` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.0962` n `44` status `ready` deltaP `16.02` edge `0.0511` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.0962` n `44` status `ready` deltaP `16.02` edge `0.0511` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.4554` n `44` status `ready` deltaP `8.6418` edge `0.0033` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.4554` n `44` status `ready` deltaP `8.6418` edge `0.0033` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.1581` n `44` status `ready` deltaP `8.2472` edge `0.0195` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.1581` n `44` status `ready` deltaP `8.2472` edge `0.0195` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0029` n `44` status `ready` deltaP `8.4811` edge `0.0029` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0029` n `44` status `ready` deltaP `8.4811` edge `0.0029` maxDD `-0.3925`
- `risk_on_high->equity_1h` score `-0.0657` n `44` status `ready` deltaP `6.6277` edge `-0.0107` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
