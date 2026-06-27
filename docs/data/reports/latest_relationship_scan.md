# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T19:37:30.895515+00:00`
- Price records: `672`
- Market context records: `4965`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `17.8866` n `99` status `ready` deltaP `8.0612` edge `1.4869` maxDD `-1.674`
- `market_context_high->unknown_4h` score `12.0911` n `94` status `ready` deltaP `28.5612` edge `0.8686` maxDD `-1.7801`
- `market_context_high->crypto_major_4h` score `7.4322` n `94` status `ready` deltaP `22.0452` edge `0.5948` maxDD `-7.1265`
- `market_context_high->crypto_alt_4h` score `7.1466` n `94` status `ready` deltaP `22.4961` edge `0.5808` maxDD `-7.8181`
- `market_context_high->unknown_24h` score `5.8082` n `91` status `ready` deltaP `27.1463` edge `0.3373` maxDD `-1.4072`
- `market_context_high->equity_4h` score `1.7627` n `94` status `ready` deltaP `14.4363` edge `0.1888` maxDD `-6.3852`
- `market_context_high->metal_4h` score `1.5521` n `94` status `ready` deltaP `12.4806` edge `0.1207` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `1.1493` n `99` status `ready` deltaP `7.727` edge `0.1481` maxDD `-5.6406`
- `market_context_high->equity_1h` score `1.0616` n `99` status `ready` deltaP `10.3067` edge `0.0771` maxDD `-2.5875`
- `market_context_high->index_4h` score `0.9654` n `94` status `ready` deltaP `12.3184` edge `0.0445` maxDD `-0.6938`
- `market_context_high->crypto_alt_1h` score `0.5834` n `99` status `ready` deltaP `9.035` edge `0.1168` maxDD `-5.5126`
- `market_context_high->metal_1h` score `0.1334` n `99` status `ready` deltaP `4.9961` edge `0.0358` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.3981` n `99` status `ready` deltaP `1.7768` edge `0.0126` maxDD `-0.7054`
- `market_context_high->commodity_1h` score `-0.4247` n `99` status `ready` deltaP `0.6184` edge `0.0074` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.9941` n `94` status `ready` deltaP `7.0186` edge `-0.0051` maxDD `-4.9624`
- `market_context_high->fx_4h` score `-1.1081` n `94` status `ready` deltaP `-6.0781` edge `-0.0045` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-1.5532` n `99` status `ready` deltaP `-9.7442` edge `-0.0045` maxDD `-0.4646`
- `market_context_high->fx_24h` score `-1.5583` n `91` status `ready` deltaP `-2.3447` edge `-0.0132` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-3.9947` n `91` status `ready` deltaP `19.6485` edge `0.047` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-6.9982` n `91` status `ready` deltaP `-10.0351` edge `0.0292` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
