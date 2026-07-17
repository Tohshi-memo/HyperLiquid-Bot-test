# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T16:07:36.519345+00:00`
- Price records: `672`
- Market context records: `7045`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `market_context_high->fx_4h` score `0.1575` n `202` status `ready` deltaP `14.0184` edge `0.0105` maxDD `-0.9333`
- `market_context_high->crypto_alt_1h` score `-0.3105` n `202` status `ready` deltaP `1.8186` edge `0.0345` maxDD `-4.5815`
- `market_context_high->fx_1h` score `-0.3184` n `202` status `ready` deltaP `2.533` edge `0.0017` maxDD `-0.276`
- `market_context_high->crypto_major_1h` score `-0.5696` n `202` status `ready` deltaP `4.0523` edge `0.0352` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-0.7324` n `202` status `ready` deltaP `-2.7405` edge `-0.014` maxDD `-1.9306`
- `market_context_high->index_1h` score `-0.7488` n `202` status `ready` deltaP `-0.4017` edge `-0.0022` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.7955` n `202` status `ready` deltaP `-3.5098` edge `-0.0018` maxDD `-2.1427`
- `market_context_high->unknown_1h` score `-0.9455` n `202` status `ready` deltaP `-2.4056` edge `0.0124` maxDD `-2.3457`
- `market_context_high->unknown_4h` score `-1.5748` n `202` status `ready` deltaP `-6.0462` edge `0.0969` maxDD `-6.6924`
- `market_context_high->equity_1h` score `-1.8061` n `202` status `ready` deltaP `4.2954` edge `-0.0179` maxDD `-14.716`
- `market_context_high->index_4h` score `-2.0808` n `202` status `ready` deltaP `3.9649` edge `-0.0233` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-2.0862` n `202` status `ready` deltaP `3.6691` edge `0.0064` maxDD `-5.5324`
- `market_context_high->commodity_4h` score `-2.1403` n `202` status `ready` deltaP `-4.3091` edge `-0.0336` maxDD `-2.9494`
- `market_context_high->commodity_24h` score `-2.2069` n `200` status `ready` deltaP `-0.2292` edge `-0.0515` maxDD `-4.4704`
- `market_context_high->crypto_alt_4h` score `-2.53` n `202` status `ready` deltaP `3.0865` edge `0.0336` maxDD `-22.2831`
- `market_context_high->unknown_24h` score `-2.6638` n `200` status `ready` deltaP `-11.2083` edge `0.2409` maxDD `-22.9487`
- `market_context_high->crypto_major_4h` score `-2.752` n `202` status `ready` deltaP `4.6848` edge `0.0444` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.5957` n `200` status `ready` deltaP `-0.9792` edge `-0.0104` maxDD `-3.9503`
- `market_context_high->equity_4h` score `-7.4578` n `202` status `ready` deltaP `4.2321` edge `-0.0973` maxDD `-63.963`
- `market_context_high->metal_24h` score `-14.8695` n `200` status `ready` deltaP `-16.0972` edge `-0.0758` maxDD `-44.1476`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
