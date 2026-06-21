# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T13:52:32.797858+00:00`
- Price records: `672`
- Market context records: `4318`
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

- `risk_on_high->unknown_4h` score `130.7689` n `44` status `ready` deltaP `-0.8315` edge `11.0848` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.7689` n `44` status `ready` deltaP `-0.8315` edge `11.0848` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `29.153` n `232` status `ready` deltaP `3.4457` edge `2.5644` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `9.7017` n `232` status `ready` deltaP `1.598` edge `1.3408` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.3561` n `44` status `ready` deltaP `31.5688` edge `-0.0094` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.3561` n `44` status `ready` deltaP `31.5688` edge `-0.0094` maxDD `-0.044`
- `market_context_high->unknown_24h` score `2.2265` n `211` status `ready` deltaP `-7.2744` edge `0.6374` maxDD `-24.2693`
- `risk_on_high->metal_24h` score `2.1116` n `43` status `ready` deltaP `-21.0554` edge `0.4725` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.1116` n `43` status `ready` deltaP `-21.0554` edge `0.4725` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `1.9725` n `43` status `ready` deltaP `22.9167` edge `0.0116` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.9725` n `43` status `ready` deltaP `22.9167` edge `0.0116` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.5429` n `44` status `ready` deltaP `17.2395` edge `0.0802` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.5429` n `44` status `ready` deltaP `17.2395` edge `0.0802` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.3787` n `44` status `ready` deltaP `7.7436` edge `0.0029` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.3787` n `44` status `ready` deltaP `7.7436` edge `0.0029` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.1643` n `44` status `ready` deltaP `8.2472` edge `0.0203` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.1643` n `44` status `ready` deltaP `8.2472` edge `0.0203` maxDD `-2.3372`
- `risk_on_high->metal_4h` score `0.0369` n `44` status `ready` deltaP `4.199` edge `0.0103` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.0369` n `44` status `ready` deltaP `4.199` edge `0.0103` maxDD `-1.3516`
- `risk_on_high->fx_4h` score `0.0211` n `44` status `ready` deltaP `8.786` edge `0.0032` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
