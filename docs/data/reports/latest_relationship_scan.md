# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T12:52:26.526782+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12978`

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

- `market_context_high->unknown_24h` score `17602.0077` n `57` status `ready` deltaP `11.7756` edge `1466.7699` maxDD `-0.4878`
- `news_risk_high->unknown_1h` score `412.8507` n `82` status `ready` deltaP `-4.8014` edge `34.4784` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `18.067` n `82` status `ready` deltaP `37.8512` edge `1.4003` maxDD `-9.098`
- `news_risk_high->crypto_alt_24h` score `18.059` n `82` status `ready` deltaP `33.9613` edge `1.3273` maxDD `-2.2369`
- `market_context_high->crypto_alt_24h` score `10.3459` n `57` status `ready` deltaP `24.7187` edge `0.7801` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `8.0611` n `82` status `ready` deltaP `23.3053` edge `0.6944` maxDD `-6.5742`
- `market_context_high->equity_24h` score `7.5752` n `57` status `ready` deltaP `41.5124` edge `0.4857` maxDD `-8.1614`
- `news_risk_high->index_24h` score `6.715` n `82` status `ready` deltaP `47.767` edge `0.2588` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.5672` n `82` status `ready` deltaP `24.2431` edge `0.2644` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.0418` n `57` status `ready` deltaP `39.8276` edge `0.0713` maxDD `0.0`
- `market_context_high->index_24h` score `3.9444` n `57` status `ready` deltaP `44.3225` edge `0.0788` maxDD `-1.3132`
- `market_context_high->metal_24h` score `1.2973` n `57` status `ready` deltaP `15.8349` edge `0.1227` maxDD `-1.2886`
- `risk_on_high->crypto_alt_4h` score `0.5103` n `65` status `ready` deltaP `11.3678` edge `0.1571` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.5103` n `65` status `ready` deltaP `11.3678` edge `0.1571` maxDD `-6.7304`
- `news_risk_high->index_4h` score `0.4243` n `82` status `ready` deltaP `12.4991` edge `0.0339` maxDD `-0.6935`
- `risk_on_high->fx_1h` score `0.0981` n `65` status `ready` deltaP `4.5532` edge `0.0034` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.0981` n `65` status `ready` deltaP `4.5532` edge `0.0034` maxDD `-0.0464`
- `risk_on_high->metal_1h` score `-0.0113` n `65` status `ready` deltaP `4.5117` edge `0.002` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0113` n `65` status `ready` deltaP `4.5117` edge `0.002` maxDD `-0.3081`
- `market_context_high->fx_1h` score `-0.0265` n `144` status `ready` deltaP `4.3288` edge `-0.0006` maxDD `-0.5323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
