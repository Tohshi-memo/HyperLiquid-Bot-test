# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T10:22:29.563363+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8380`

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

- `market_context_high->unknown_4h` score `39.6048` n `149` status `ready` deltaP `-0.311` edge `3.3258` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.4835` n `52` status `ready` deltaP `-7.5516` edge `1.1965` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.4835` n `52` status `ready` deltaP `-7.5516` edge `1.1965` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.8672` n `52` status `ready` deltaP `50.0` edge `0.4056` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8672` n `52` status `ready` deltaP `50.0` edge `0.4056` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5681` n `149` status `ready` deltaP `43.2886` edge `0.3946` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `3.0116` n `85` status `ready` deltaP `19.9157` edge `0.4684` maxDD `-12.8718`
- `risk_on_high->commodity_4h` score `2.8341` n `52` status `ready` deltaP `32.6923` edge `0.0532` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8341` n `52` status `ready` deltaP `32.6923` edge `0.0532` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7338` n `149` status `ready` deltaP `29.1946` edge `0.075` maxDD `-0.345`
- `news_risk_high->equity_4h` score `1.3124` n `85` status `ready` deltaP `16.7772` edge `0.1401` maxDD `-3.3619`
- `market_context_high->commodity_1h` score `1.1193` n `149` status `ready` deltaP `16.2109` edge `0.0229` maxDD `-0.3491`
- `risk_on_high->fx_24h` score `0.9518` n `52` status `ready` deltaP `18.563` edge `-0.0402` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `0.9518` n `52` status `ready` deltaP `18.563` edge `-0.0402` maxDD `-0.0054`
- `market_context_high->fx_24h` score `0.817` n `149` status `ready` deltaP `15.7881` edge `-0.0156` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.496` n `52` status `ready` deltaP `9.293` edge `0.0146` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.496` n `52` status `ready` deltaP `9.293` edge `0.0146` maxDD `-0.1507`
- `news_risk_high->fx_4h` score `0.3325` n `85` status `ready` deltaP `9.2844` edge `0.0254` maxDD `-0.2398`
- `news_risk_high->equity_1h` score `0.2865` n `95` status `ready` deltaP `9.9905` edge `0.0223` maxDD `-1.8403`
- `market_context_high->fx_1h` score `-0.0682` n `149` status `ready` deltaP `2.556` edge `0.0` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
