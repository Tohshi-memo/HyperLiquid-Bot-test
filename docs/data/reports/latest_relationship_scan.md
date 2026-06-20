# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T07:52:25.933140+00:00`
- Price records: `672`
- Market context records: `4187`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10034`

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

- `risk_on_high->unknown_4h` score `144.8364` n `40` status `ready` deltaP `-9.878` edge `12.3174` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `144.8364` n `40` status `ready` deltaP `-9.878` edge `12.3174` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `35.0679` n `202` status `ready` deltaP `0.7914` edge `3.075` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `9.8373` n `202` status `ready` deltaP `-4.5067` edge `1.3928` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `8.5866` n `198` status `ready` deltaP `-12.8974` edge `1.2049` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.2175` n `40` status `ready` deltaP `4.1461` edge `0.3853` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.2175` n `40` status `ready` deltaP `4.1461` edge `0.3853` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `1.8239` n `40` status `ready` deltaP `31.0366` edge `-0.0502` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `1.8239` n `40` status `ready` deltaP `31.0366` edge `-0.0502` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.4996` n `40` status `ready` deltaP `13.9634` edge `0.0151` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.4996` n `40` status `ready` deltaP `13.9634` edge `0.0151` maxDD `-2.6576`
- `risk_on_high->fx_4h` score `0.1229` n `40` status `ready` deltaP `10.5488` edge `0.0045` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.1229` n `40` status `ready` deltaP `10.5488` edge `0.0045` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0934` n `40` status `ready` deltaP `5.0` edge `0.0016` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0934` n `40` status `ready` deltaP `5.0` edge `0.0016` maxDD `-0.1704`
- `risk_on_high->metal_4h` score `0.0849` n `40` status `ready` deltaP `8.811` edge `-0.0143` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.0849` n `40` status `ready` deltaP `8.811` edge `-0.0143` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `-0.0154` n `40` status `ready` deltaP `9.1168` edge `-0.0231` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `-0.0154` n `40` status `ready` deltaP `9.1168` edge `-0.0231` maxDD `-0.7834`
- `risk_on_high->crypto_major_1h` score `-0.0564` n `40` status `ready` deltaP `8.7126` edge `-0.0111` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
