# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-19T21:37:26.116847+00:00`
- Price records: `672`
- Market context records: `4142`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10032`

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

- `risk_on_high->unknown_4h` score `144.7472` n `40` status `ready` deltaP `-10.1829` edge `12.312` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `144.7472` n `40` status `ready` deltaP `-10.1829` edge `12.312` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `38.0846` n `202` status `ready` deltaP `1.3903` edge `3.3224` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `11.9381` n `198` status `ready` deltaP `-12.1492` edge `1.4792` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `9.7481` n `202` status `ready` deltaP `-4.8116` edge `1.3874` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.6084` n `40` status `ready` deltaP `35.4573` edge `-0.0143` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.6084` n `40` status `ready` deltaP `35.4573` edge `-0.0143` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `1.2739` n `40` status `ready` deltaP `17.0122` edge `0.0593` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.2739` n `40` status `ready` deltaP `17.0122` edge `0.0593` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `0.3733` n `40` status `ready` deltaP `-0.8462` edge `0.2649` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.3733` n `40` status `ready` deltaP `-0.8462` edge `0.2649` maxDD `-12.9187`
- `risk_on_high->equity_1h` score `0.2735` n `40` status `ready` deltaP `10.9132` edge `-0.011` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.2735` n `40` status `ready` deltaP `10.9132` edge `-0.011` maxDD `-0.7834`
- `risk_on_high->metal_4h` score `0.1868` n `40` status `ready` deltaP `9.4207` edge `-0.0053` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1868` n `40` status `ready` deltaP `9.4207` edge `-0.0053` maxDD `-1.3516`
- `risk_on_high->crypto_major_1h` score `0.1595` n `40` status `ready` deltaP `10.3593` edge `0.0056` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.1595` n `40` status `ready` deltaP `10.3593` edge `0.0056` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0328` n `40` status `ready` deltaP `9.1768` edge `0.0021` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0328` n `40` status `ready` deltaP `9.1768` edge `0.0021` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0241` n `40` status `ready` deltaP `3.8024` edge `0.0007` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
