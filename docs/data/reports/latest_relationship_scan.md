# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T06:07:23.499051+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11803`

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

- `risk_on_high->unknown_1h` score `4.2711` n `35` status `ready` deltaP `2.4893` edge `0.3788` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `4.2711` n `35` status `ready` deltaP `2.4893` edge `0.3788` maxDD `-0.8243`
- `market_context_high->commodity_24h` score `2.4944` n `77` status `ready` deltaP `27.2277` edge `0.1127` maxDD `-1.908`
- `market_context_high->crypto_major_24h` score `2.1377` n `77` status `ready` deltaP `5.4902` edge `0.2792` maxDD `-5.6792`
- `market_context_high->index_24h` score `1.4745` n `77` status `ready` deltaP `21.7014` edge `-0.0218` maxDD `0.0`
- `market_context_high->equity_24h` score `1.3235` n `77` status `ready` deltaP `15.6453` edge `0.0269` maxDD `-0.6726`
- `risk_on_high->crypto_major_1h` score `1.0828` n `35` status `ready` deltaP `11.9589` edge `0.0411` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.0828` n `35` status `ready` deltaP `11.9589` edge `0.0411` maxDD `-1.1144`
- `risk_on_high->equity_1h` score `1.0067` n `35` status `ready` deltaP `14.4055` edge `0.0422` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `1.0067` n `35` status `ready` deltaP `14.4055` edge `0.0422` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.8692` n `35` status `ready` deltaP `14.5424` edge `0.013` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.8692` n `35` status `ready` deltaP `14.5424` edge `0.013` maxDD `-0.3343`
- `market_context_high->commodity_4h` score `0.5756` n `108` status `ready` deltaP `11.4611` edge `0.0513` maxDD `-1.3135`
- `risk_on_high->fx_1h` score `0.0445` n `35` status `ready` deltaP `3.9863` edge `0.0019` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.0445` n `35` status `ready` deltaP `3.9863` edge `0.0019` maxDD `-0.1547`
- `market_context_high->metal_4h` score `-0.1508` n `108` status `ready` deltaP `16.8529` edge `0.0158` maxDD `-4.5909`
- `risk_on_high->commodity_1h` score `-0.2384` n `35` status `ready` deltaP `-0.6672` edge `0.0115` maxDD `-0.4871`
- `risk_on_and_context->commodity_1h` score `-0.2384` n `35` status `ready` deltaP `-0.6672` edge `0.0115` maxDD `-0.4871`
- `market_context_high->fx_1h` score `-0.3123` n `120` status `ready` deltaP `-0.2994` edge `-0.001` maxDD `-0.2968`
- `market_context_high->crypto_major_4h` score `-0.3886` n `108` status `ready` deltaP `4.782` edge `0.0391` maxDD `-4.6638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
