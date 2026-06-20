# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T10:22:26.298311+00:00`
- Price records: `672`
- Market context records: `4198`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10050`

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

- `risk_on_high->unknown_4h` score `145.217` n `40` status `ready` deltaP `-8.811` edge `12.342` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.217` n `40` status `ready` deltaP `-8.811` edge `12.342` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `32.5587` n `209` status `ready` deltaP `1.1819` edge `2.8633` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `10.2178` n `202` status `ready` deltaP `-3.4397` edge `1.4174` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `8.3963` n `198` status `ready` deltaP `-12.6068` edge `1.1871` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.3379` n `40` status `ready` deltaP `4.4658` edge `0.3932` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.3379` n `40` status `ready` deltaP `4.4658` edge `0.3932` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `2.1861` n `40` status `ready` deltaP `31.7988` edge `-0.0251` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.1861` n `40` status `ready` deltaP `31.7988` edge `-0.0251` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.759` n `40` status `ready` deltaP `14.1159` edge `0.0357` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.759` n `40` status `ready` deltaP `14.1159` edge `0.0357` maxDD `-2.6576`
- `risk_on_high->metal_4h` score `0.1638` n `40` status `ready` deltaP `8.9634` edge `-0.0052` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1638` n `40` status `ready` deltaP `8.9634` edge `-0.0052` maxDD `-1.3516`
- `risk_on_high->fx_4h` score `0.0674` n `40` status `ready` deltaP `9.4817` edge `0.0045` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0674` n `40` status `ready` deltaP `9.4817` edge `0.0045` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0404` n `40` status `ready` deltaP `4.1018` edge `0.0008` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0404` n `40` status `ready` deltaP `4.1018` edge `0.0008` maxDD `-0.1704`
- `risk_on_high->equity_1h` score `0.0362` n `40` status `ready` deltaP `9.1168` edge `-0.0188` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.0362` n `40` status `ready` deltaP `9.1168` edge `-0.0188` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `-0.0377` n `40` status `ready` deltaP `8.5629` edge `-0.0077` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
