# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-19T17:28:54.060586+00:00`
- Price records: `672`
- Market context records: `4123`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10016`

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

- `risk_on_high->unknown_4h` score `145.3597` n `40` status `ready` deltaP `-8.9168` edge `12.3546` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.3597` n `40` status `ready` deltaP `-8.9168` edge `12.3546` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `39.2314` n `199` status `ready` deltaP `1.64` edge `3.4163` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `14.2194` n `198` status `ready` deltaP `-10.0631` edge `1.6554` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `11.3502` n `198` status `ready` deltaP `-2.2754` edge `1.504` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.7838` n `40` status `ready` deltaP `36.4805` edge `-0.0065` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.7838` n `40` status `ready` deltaP `36.4805` edge `-0.0065` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `1.6603` n `40` status `ready` deltaP `18.3771` edge `0.0824` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6603` n `40` status `ready` deltaP `18.3771` edge `0.0824` maxDD `-2.6576`
- `risk_on_high->metal_4h` score `0.5056` n `40` status `ready` deltaP `11.2781` edge `0.0232` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.5056` n `40` status `ready` deltaP `11.2781` edge `0.0232` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.2855` n `40` status `ready` deltaP `11.0629` edge `-0.011` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.2855` n `40` status `ready` deltaP `11.0629` edge `-0.011` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `0.2358` n `40` status `ready` deltaP `11.1078` edge `0.0104` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2358` n `40` status `ready` deltaP `11.1078` edge `0.0104` maxDD `-2.3372`
- `risk_on_high->metal_24h` score `0.1734` n `40` status `ready` deltaP `-19.7189` edge `0.2151` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `0.1734` n `40` status `ready` deltaP `-19.7189` edge `0.2151` maxDD `-1.9133`
- `risk_on_high->fx_4h` score `0.0711` n `40` status `ready` deltaP `9.8238` edge `0.0027` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0711` n `40` status `ready` deltaP `9.8238` edge `0.0027` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0256` n `40` status `ready` deltaP `3.8024` edge `0.0009` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
