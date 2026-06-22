# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-22T13:52:30.238813+00:00`
- Price records: `672`
- Market context records: `4420`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11123`

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

- `risk_on_high->unknown_4h` score `123.0056` n `49` status `ready` deltaP `2.8061` edge `10.4136` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `123.0056` n `49` status `ready` deltaP `2.8061` edge `10.4136` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `31.2685` n `232` status `ready` deltaP `2.434` edge `2.7391` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `14.463` n `231` status `ready` deltaP `5.4654` edge `1.7118` maxDD `-35.7719`
- `risk_on_high->unknown_24h` score `4.5132` n `44` status `ready` deltaP `19.3813` edge `0.326` maxDD `-4.9954`
- `risk_on_and_context->unknown_24h` score `4.5132` n `44` status `ready` deltaP `19.3813` edge `0.326` maxDD `-4.9954`
- `risk_on_high->equity_4h` score `3.0754` n `49` status `ready` deltaP `32.7153` edge `0.0429` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.0754` n `49` status `ready` deltaP `32.7153` edge `0.0429` maxDD `-0.044`
- `risk_on_high->metal_24h` score `3.0615` n `44` status `ready` deltaP `-15.3567` edge `0.5563` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `3.0615` n `44` status `ready` deltaP `-15.3567` edge `0.5563` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `2.2516` n `49` status `ready` deltaP `20.0224` edge `0.1207` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.2516` n `49` status `ready` deltaP `20.0224` edge `0.1207` maxDD `-2.6576`
- `risk_on_high->index_24h` score `1.761` n `44` status `ready` deltaP `23.4375` edge `-0.0095` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.761` n `44` status `ready` deltaP `23.4375` edge `-0.0095` maxDD `0.0`
- `risk_on_high->equity_24h` score `1.62` n `44` status `ready` deltaP `19.9653` edge `0.0019` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.62` n `44` status `ready` deltaP `19.9653` edge `0.0019` maxDD `0.0`
- `risk_on_high->metal_4h` score `1.0241` n `49` status `ready` deltaP `9.361` edge `0.0565` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.0241` n `49` status `ready` deltaP `9.361` edge `0.0565` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.5797` n `49` status `ready` deltaP `11.0046` edge `0.0139` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.5797` n `49` status `ready` deltaP `11.0046` edge `0.0139` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
