# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T08:22:28.282746+00:00`
- Price records: `672`
- Market context records: `4294`
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

- `risk_on_high->unknown_4h` score `130.4446` n `44` status `ready` deltaP `-2.9657` edge `11.072` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.4446` n `44` status `ready` deltaP `-2.9657` edge `11.072` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `27.7719` n `236` status `ready` deltaP `2.1568` edge `2.4579` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `8.8012` n `236` status `ready` deltaP `0.0775` edge `1.2759` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `6.7362` n `203` status `ready` deltaP `-7.8878` edge `1.0173` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `1.9711` n `44` status `ready` deltaP `30.8066` edge `-0.0364` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.9711` n `44` status `ready` deltaP `30.8066` edge `-0.0364` maxDD `-0.044`
- `risk_on_high->metal_24h` score `1.4475` n `40` status `ready` deltaP `-21.7361` edge `0.3919` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `1.4475` n `40` status `ready` deltaP `-21.7361` edge `0.3919` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `1.1133` n `40` status `ready` deltaP `22.9167` edge `-0.06` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.1133` n `40` status `ready` deltaP `22.9167` edge `-0.06` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.0806` n `44` status `ready` deltaP `16.02` edge `0.0498` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.0806` n `44` status `ready` deltaP `16.02` edge `0.0498` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.4338` n `44` status `ready` deltaP `8.3424` edge `0.0035` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.4338` n `44` status `ready` deltaP `8.3424` edge `0.0035` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.183` n `44` status `ready` deltaP `8.3969` edge `0.0217` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.183` n `44` status `ready` deltaP `8.3969` edge `0.0217` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0107` n `44` status `ready` deltaP `8.4811` edge `0.0039` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0107` n `44` status `ready` deltaP `8.4811` edge `0.0039` maxDD `-0.3925`
- `risk_on_high->equity_1h` score `-0.0489` n `44` status `ready` deltaP `6.6277` edge `-0.0093` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
