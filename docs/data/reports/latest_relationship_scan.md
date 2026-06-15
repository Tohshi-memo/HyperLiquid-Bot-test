# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T23:22:33.591367+00:00`
- Price records: `672`
- Market context records: `4036`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10624`

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

- `risk_on_high->unknown_4h` score `145.7221` n `40` status `ready` deltaP `-7.1341` edge `12.3727` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `145.7221` n `40` status `ready` deltaP `-7.1341` edge `12.3727` maxDD `-10.864`
- `market_context_high->unknown_24h` score `46.8191` n `134` status `ready` deltaP `-6.8923` edge `4.3504` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `23.9228` n `153` status `ready` deltaP `2.0326` edge `2.5223` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `4.9299` n `40` status `ready` deltaP `36.0485` edge `0.1705` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.9299` n `40` status `ready` deltaP `36.0485` edge `0.1705` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.2367` n `40` status `ready` deltaP `36.0671` edge `0.034` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.2367` n `40` status `ready` deltaP `36.0671` edge `0.034` maxDD `-0.0446`
- `market_context_high->index_24h` score `2.7445` n `134` status `ready` deltaP `22.9972` edge `0.0966` maxDD `-1.3629`
- `market_context_high->equity_4h` score `1.7181` n `153` status `ready` deltaP `16.3449` edge `0.1623` maxDD `-6.9137`
- `market_context_high->metal_24h` score `1.5365` n `134` status `ready` deltaP `11.1811` edge `0.1522` maxDD `-4.8962`
- `market_context_high->equity_1h` score `1.1701` n `157` status `ready` deltaP `8.3814` edge `0.0976` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `0.9161` n `40` status `ready` deltaP `18.689` edge `0.0183` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.9161` n `40` status `ready` deltaP `18.689` edge `0.0183` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `0.56` n `40` status `ready` deltaP `2.643` edge `0.2572` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.56` n `40` status `ready` deltaP `2.643` edge `0.2572` maxDD `-12.9187`
- `market_context_high->metal_1h` score `0.42` n `157` status `ready` deltaP `10.0957` edge `0.0491` maxDD `-3.0049`
- `market_context_high->crypto_major_1h` score `0.4198` n `157` status `ready` deltaP `7.2896` edge `0.053` maxDD `-3.3288`
- `risk_on_high->equity_1h` score `0.4112` n `40` status `ready` deltaP `10.9132` edge `0.0006` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4112` n `40` status `ready` deltaP `10.9132` edge `0.0006` maxDD `-0.7937`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
