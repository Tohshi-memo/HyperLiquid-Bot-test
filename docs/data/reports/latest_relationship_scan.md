# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T17:07:26.183174+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10441`

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

- `risk_on_high->unknown_24h` score `283.1178` n `100` status `ready` deltaP `23.4375` edge `23.4369` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `283.1178` n `100` status `ready` deltaP `23.4375` edge `23.4369` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `18.5586` n `100` status `ready` deltaP `33.3056` edge `1.4436` maxDD `-6.8602`
- `risk_on_and_context->crypto_major_24h` score `18.5586` n `100` status `ready` deltaP `33.3056` edge `1.4436` maxDD `-6.8602`
- `risk_on_high->crypto_alt_24h` score `13.6372` n `100` status `ready` deltaP `31.4653` edge `0.9328` maxDD `-0.1572`
- `risk_on_and_context->crypto_alt_24h` score `13.6372` n `100` status `ready` deltaP `31.4653` edge `0.9328` maxDD `-0.1572`
- `market_context_high->crypto_alt_24h` score `7.7769` n `212` status `ready` deltaP `24.4464` edge `0.5426` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.6038` n `117` status `ready` deltaP `29.8728` edge `0.305` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.6038` n `117` status `ready` deltaP `29.8728` edge `0.305` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.9341` n `117` status `ready` deltaP `26.286` edge `0.3218` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.9341` n `117` status `ready` deltaP `26.286` edge `0.3218` maxDD `-3.8693`
- `market_context_high->equity_24h` score `4.4293` n `212` status `ready` deltaP `16.6667` edge `0.258` maxDD `0.0`
- `risk_on_high->equity_24h` score `3.6985` n `100` status `ready` deltaP `16.6667` edge `0.1971` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.6985` n `100` status `ready` deltaP `16.6667` edge `0.1971` maxDD `0.0`
- `risk_on_high->index_24h` score `2.0745` n `100` status `ready` deltaP `18.1806` edge `0.0559` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.0745` n `100` status `ready` deltaP `18.1806` edge `0.0559` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.3194` n `212` status `ready` deltaP `12.69` edge `0.0647` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.9992` n `117` status `ready` deltaP `4.6958` edge `0.0872` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9992` n `117` status `ready` deltaP `4.6958` edge `0.0872` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.6612` n `100` status `ready` deltaP `16.9583` edge `0.0873` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
