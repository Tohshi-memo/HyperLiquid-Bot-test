# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T19:07:43.849734+00:00`
- Price records: `672`
- Market context records: `4342`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10810`

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

- `risk_on_high->unknown_4h` score `130.9793` n `44` status `ready` deltaP `-0.5266` edge `11.1003` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.9793` n `44` status `ready` deltaP `-0.5266` edge `11.1003` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `30.9185` n `226` status `ready` deltaP `3.524` edge `2.711` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `11.5421` n `222` status `ready` deltaP `2.0738` edge `1.491` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.0246` n `44` status `ready` deltaP `33.5505` edge `0.0331` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.0246` n `44` status `ready` deltaP `33.5505` edge `0.0331` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.6003` n `44` status `ready` deltaP `-18.4817` edge `0.518` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.6003` n `44` status `ready` deltaP `-18.4817` edge `0.518` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `2.0714` n `44` status `ready` deltaP `21.5278` edge `0.0291` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.0714` n `44` status `ready` deltaP `21.5278` edge `0.0291` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.7113` n `44` status `ready` deltaP `17.5444` edge `0.0922` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.7113` n `44` status `ready` deltaP `17.5444` edge `0.0922` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.459` n `44` status `ready` deltaP `8.6418` edge `0.0036` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.459` n `44` status `ready` deltaP `8.6418` edge `0.0036` maxDD `-0.1704`
- `risk_on_high->metal_4h` score `0.4374` n `44` status `ready` deltaP `6.4856` edge `0.0464` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.4374` n `44` status `ready` deltaP `6.4856` edge `0.0464` maxDD `-1.3516`
- `risk_on_high->index_24h` score `0.3885` n `44` status `ready` deltaP `19.2708` edge `-0.0961` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.3885` n `44` status `ready` deltaP `19.2708` edge `-0.0961` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.2724` n `44` status `ready` deltaP `8.4241` edge `0.0055` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.2724` n `44` status `ready` deltaP `8.4241` edge `0.0055` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
