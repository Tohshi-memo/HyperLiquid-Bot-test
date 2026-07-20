# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T18:50:10.407988+00:00`
- Price records: `672`
- Market context records: `7381`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14654`

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

- `risk_on_high->crypto_major_4h` score `6.1514` n `32` status `ready` deltaP `35.4421` edge `0.2956` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.1514` n `32` status `ready` deltaP `35.4421` edge `0.2956` maxDD `-0.8742`
- `risk_on_high->unknown_4h` score `4.9305` n `32` status `ready` deltaP `15.5488` edge `0.3502` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.9305` n `32` status `ready` deltaP `15.5488` edge `0.3502` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.8186` n `32` status `ready` deltaP `28.2774` edge `0.2374` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.8186` n `32` status `ready` deltaP `28.2774` edge `0.2374` maxDD `-0.9492`
- `risk_on_high->crypto_major_1h` score `1.0765` n `32` status `ready` deltaP `19.0307` edge `0.0356` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.0765` n `32` status `ready` deltaP `19.0307` edge `0.0356` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.3676` n `32` status `ready` deltaP `5.0488` edge `0.0249` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.3676` n `32` status `ready` deltaP `5.0488` edge `0.0249` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.1062` n `32` status `ready` deltaP `3.4535` edge `0.0283` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1062` n `32` status `ready` deltaP `3.4535` edge `0.0283` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `-0.0394` n `32` status `ready` deltaP `-0.5988` edge `0.036` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `-0.0394` n `32` status `ready` deltaP `-0.5988` edge `0.036` maxDD `-0.9651`
- `market_context_high->fx_1h` score `-0.1835` n `130` status `ready` deltaP `3.8277` edge `-0.0001` maxDD `-0.5822`
- `risk_on_high->metal_4h` score `-0.2664` n `32` status `ready` deltaP `-1.372` edge `0.0693` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.2664` n `32` status `ready` deltaP `-1.372` edge `0.0693` maxDD `-0.5882`
- `market_context_high->commodity_1h` score `-0.6034` n `130` status `ready` deltaP `-1.9704` edge `-0.007` maxDD `-1.5775`
- `market_context_high->commodity_4h` score `-0.7112` n `129` status `ready` deltaP `-0.1707` edge `0.0068` maxDD `-2.4139`
- `market_context_high->unknown_4h` score `-0.838` n `129` status `ready` deltaP `3.4848` edge `0.1052` maxDD `-6.2031`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
