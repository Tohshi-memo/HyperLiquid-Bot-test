# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T10:37:31.039530+00:00`
- Price records: `672`
- Market context records: `4199`
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

- `risk_on_high->unknown_4h` score `145.2808` n `40` status `ready` deltaP `-8.6585` edge `12.3463` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.2808` n `40` status `ready` deltaP `-8.6585` edge `12.3463` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `32.5719` n `209` status `ready` deltaP `1.3316` edge `2.8634` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `10.2816` n `202` status `ready` deltaP `-3.2872` edge `1.4217` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `8.3626` n `198` status `ready` deltaP `-12.5772` edge `1.1841` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.3653` n `40` status `ready` deltaP `4.5987` edge `0.3946` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.3653` n `40` status `ready` deltaP `4.5987` edge `0.3946` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `2.2067` n `40` status `ready` deltaP `31.9512` edge `-0.0244` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.2067` n `40` status `ready` deltaP `31.9512` edge `-0.0244` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.7808` n `40` status `ready` deltaP `14.2683` edge `0.0365` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.7808` n `40` status `ready` deltaP `14.2683` edge `0.0365` maxDD `-2.6576`
- `risk_on_high->metal_4h` score `0.1653` n `40` status `ready` deltaP `8.9634` edge `-0.005` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1653` n `40` status `ready` deltaP `8.9634` edge `-0.005` maxDD `-1.3516`
- `risk_on_high->fx_4h` score `0.0666` n `40` status `ready` deltaP `9.4817` edge `0.0044` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0666` n `40` status `ready` deltaP `9.4817` edge `0.0044` maxDD `-0.3925`
- `risk_on_high->equity_1h` score `0.0578` n `40` status `ready` deltaP `9.2665` edge `-0.018` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.0578` n `40` status `ready` deltaP `9.2665` edge `-0.018` maxDD `-0.7834`
- `risk_on_high->fx_1h` score `0.0412` n `40` status `ready` deltaP `4.1018` edge `0.0009` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0412` n `40` status `ready` deltaP `4.1018` edge `0.0009` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `-0.0197` n `40` status `ready` deltaP `8.7126` edge `-0.0064` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
