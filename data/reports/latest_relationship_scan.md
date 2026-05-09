# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-09T06:52:15.499453+00:00`
- Price records: `672`
- Market context records: `839`
- Flow alert records: `2357`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1278`

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

- `market_context_high->crypto_major_24h` score `11.8939` n `154` status `ready` deltaP `28.4474` edge `0.8349` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `4.953` n `154` status `ready` deltaP `7.1631` edge `0.3698` maxDD `-0.0508`
- `risk_on_high->equity_4h` score `3.4698` n `33` status `ready` deltaP `9.5806` edge `0.2618` maxDD `-0.9217`
- `risk_on_and_context->equity_4h` score `3.4698` n `33` status `ready` deltaP `9.5806` edge `0.2618` maxDD `-0.9217`
- `risk_on_high->index_4h` score `2.5154` n `33` status `ready` deltaP `14.2692` edge `0.1233` maxDD `-0.038`
- `risk_on_and_context->index_4h` score `2.5154` n `33` status `ready` deltaP `14.2692` edge `0.1233` maxDD `-0.038`
- `risk_on_high->crypto_major_4h` score `2.4451` n `33` status `ready` deltaP `18.593` edge `0.117` maxDD `-0.9758`
- `risk_on_and_context->crypto_major_4h` score `2.4451` n `33` status `ready` deltaP `18.593` edge `0.117` maxDD `-0.9758`
- `risk_on_high->crypto_alt_4h` score `2.0984` n `33` status `ready` deltaP `18.5006` edge `0.072` maxDD `-0.6377`
- `risk_on_and_context->crypto_alt_4h` score `2.0984` n `33` status `ready` deltaP `18.5006` edge `0.072` maxDD `-0.6377`
- `risk_on_high->metal_1h` score `1.0644` n `33` status `ready` deltaP `12.5114` edge `0.0283` maxDD `-0.5074`
- `risk_on_and_context->metal_1h` score `1.0644` n `33` status `ready` deltaP `12.5114` edge `0.0283` maxDD `-0.5074`
- `risk_on_high->commodity_4h` score `0.8286` n `33` status `ready` deltaP `5.363` edge `0.1536` maxDD `-1.3162`
- `risk_on_and_context->commodity_4h` score `0.8286` n `33` status `ready` deltaP `5.363` edge `0.1536` maxDD `-1.3162`
- `risk_on_high->commodity_1h` score `0.3211` n `33` status `ready` deltaP `8.4377` edge `0.0225` maxDD `-0.6739`
- `risk_on_and_context->commodity_1h` score `0.3211` n `33` status `ready` deltaP `8.4377` edge `0.0225` maxDD `-0.6739`
- `risk_on_high->fx_1h` score `0.2174` n `33` status `ready` deltaP `7.4987` edge `0.0014` maxDD `-0.2147`
- `risk_on_and_context->fx_1h` score `0.2174` n `33` status `ready` deltaP `7.4987` edge `0.0014` maxDD `-0.2147`
- `risk_on_high->crypto_major_1h` score `-0.1877` n `33` status `ready` deltaP `4.1327` edge `-0.0212` maxDD `-1.0995`
- `risk_on_and_context->crypto_major_1h` score `-0.1877` n `33` status `ready` deltaP `4.1327` edge `-0.0212` maxDD `-1.0995`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
