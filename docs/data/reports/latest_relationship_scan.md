# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-19T22:07:31.050081+00:00`
- Price records: `672`
- Market context records: `4145`
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

- `risk_on_high->unknown_4h` score `144.734` n `40` status `ready` deltaP `-10.1829` edge `12.3109` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `144.734` n `40` status `ready` deltaP `-10.1829` edge `12.3109` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `36.2462` n `202` status `ready` deltaP `1.2406` edge `3.1702` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `11.6635` n `198` status `ready` deltaP `-12.4018` edge `1.458` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `9.7349` n `202` status `ready` deltaP `-4.8116` edge `1.3863` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.582` n `40` status `ready` deltaP `35.4573` edge `-0.0165` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.582` n `40` status `ready` deltaP `35.4573` edge `-0.0165` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `1.2499` n `40` status `ready` deltaP `17.0122` edge `0.0573` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.2499` n `40` status `ready` deltaP `17.0122` edge `0.0573` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `0.4744` n `40` status `ready` deltaP `-0.6173` edge `0.2718` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.4744` n `40` status `ready` deltaP `-0.6173` edge `0.2718` maxDD `-12.9187`
- `risk_on_high->equity_1h` score `0.2831` n `40` status `ready` deltaP `11.0629` edge `-0.0112` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.2831` n `40` status `ready` deltaP `11.0629` edge `-0.0112` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `0.1579` n `40` status `ready` deltaP `10.3593` edge `0.0054` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.1579` n `40` status `ready` deltaP `10.3593` edge `0.0054` maxDD `-2.3372`
- `risk_on_high->metal_4h` score `0.1452` n `40` status `ready` deltaP `9.1159` edge `-0.0086` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1452` n `40` status `ready` deltaP `9.1159` edge `-0.0086` maxDD `-1.3516`
- `risk_on_high->fx_4h` score `0.051` n `40` status `ready` deltaP `9.4817` edge `0.0024` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.051` n `40` status `ready` deltaP `9.4817` edge `0.0024` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0233` n `40` status `ready` deltaP `3.8024` edge `0.0006` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
