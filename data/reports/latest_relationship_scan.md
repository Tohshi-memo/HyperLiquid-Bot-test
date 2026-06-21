# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T12:22:30.181117+00:00`
- Price records: `672`
- Market context records: `4312`
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

- `risk_on_high->unknown_4h` score `130.7024` n `44` status `ready` deltaP `-1.2888` edge `11.0823` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.7024` n `44` status `ready` deltaP `-1.2888` edge `11.0823` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `27.9733` n `236` status `ready` deltaP `3.8035` edge `2.4637` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `9.059` n `236` status `ready` deltaP `1.7544` edge `1.2862` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `5.8573` n `209` status `ready` deltaP `-7.5782` edge `0.942` maxDD `-24.2693`
- `risk_on_high->metal_24h` score `2.2085` n `40` status `ready` deltaP `-19.1319` edge `0.4721` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.2085` n `40` status `ready` deltaP `-19.1319` edge `0.4721` maxDD `-1.9133`
- `risk_on_high->equity_4h` score `2.0901` n `44` status `ready` deltaP `30.959` edge `-0.0275` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.0901` n `44` status `ready` deltaP `30.959` edge `-0.0275` maxDD `-0.044`
- `risk_on_high->equity_24h` score `1.8225` n `40` status `ready` deltaP `22.9167` edge `-0.0009` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.8225` n `40` status `ready` deltaP `22.9167` edge `-0.0009` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.2889` n `44` status `ready` deltaP `16.6297` edge `0.0631` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.2889` n `44` status `ready` deltaP `16.6297` edge `0.0631` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.4027` n `44` status `ready` deltaP `8.043` edge `0.0029` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.4027` n `44` status `ready` deltaP `8.043` edge `0.0029` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.2103` n `44` status `ready` deltaP `8.6963` edge `0.0232` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2103` n `44` status `ready` deltaP `8.6963` edge `0.0232` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `-0.0074` n `44` status `ready` deltaP `8.3287` edge `0.0026` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `-0.0074` n `44` status `ready` deltaP `8.3287` edge `0.0026` maxDD `-0.3925`
- `risk_on_high->equity_1h` score `-0.0166` n `44` status `ready` deltaP `7.0768` edge `-0.0096` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
