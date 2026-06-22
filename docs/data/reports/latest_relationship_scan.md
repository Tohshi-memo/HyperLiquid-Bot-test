# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-22T07:52:28.899680+00:00`
- Price records: `672`
- Market context records: `4396`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11063`

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

- `risk_on_high->unknown_4h` score `133.1971` n `44` status `ready` deltaP `-0.3742` edge `11.2841` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `133.1971` n `44` status `ready` deltaP `-0.3742` edge `11.2841` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `32.8063` n `224` status `ready` deltaP `2.7561` edge `2.8651` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `11.4821` n `215` status `ready` deltaP `4.7738` edge `1.468` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.1678` n `44` status `ready` deltaP `34.77` edge `0.0369` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.1678` n `44` status `ready` deltaP `34.77` edge `0.0369` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.9874` n `44` status `ready` deltaP `-15.3567` edge `0.5468` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.9874` n `44` status `ready` deltaP `-15.3567` edge `0.5468` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `1.9619` n `44` status `ready` deltaP `18.3066` edge `0.108` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.9619` n `44` status `ready` deltaP `18.3066` edge `0.108` maxDD `-2.6576`
- `risk_on_high->equity_24h` score `1.7661` n `44` status `ready` deltaP `20.4861` edge `0.0106` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.7661` n `44` status `ready` deltaP `20.4861` edge `0.0106` maxDD `0.0`
- `risk_on_high->index_24h` score `1.4111` n `44` status `ready` deltaP `23.2639` edge `-0.0375` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.4111` n `44` status `ready` deltaP `23.2639` edge `-0.0375` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.7642` n `49` status `ready` deltaP `12.3519` edge `0.0203` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.7642` n `49` status `ready` deltaP `12.3519` edge `0.0203` maxDD `-0.7834`
- `risk_on_high->metal_4h` score `0.2822` n `44` status `ready` deltaP `5.5709` edge `0.0326` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.2822` n `44` status `ready` deltaP `5.5709` edge `0.0326` maxDD `-1.3516`
- `risk_on_high->fx_1h` score `0.2405` n `49` status `ready` deltaP `6.0002` edge `0.003` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.2405` n `49` status `ready` deltaP `6.0002` edge `0.003` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
