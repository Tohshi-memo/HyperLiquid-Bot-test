# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T11:52:30.538577+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8658`

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

- `news_risk_high->unknown_4h` score `384.5772` n `83` status `ready` deltaP `-21.8153` edge `32.283` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `12.8719` n `83` status `ready` deltaP `32.2749` edge `0.9954` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `12.2925` n `83` status `ready` deltaP `24.3411` edge `1.0616` maxDD `-13.2931`
- `risk_on_high->commodity_24h` score `9.1464` n `52` status `ready` deltaP `49.3056` edge `0.4335` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.1464` n `52` status `ready` deltaP `49.3056` edge `0.4335` maxDD `0.0`
- `news_risk_high->equity_24h` score `8.831` n `83` status `ready` deltaP `33.5739` edge `0.6895` maxDD `-6.5262`
- `market_context_high->commodity_24h` score `7.8473` n `149` status `ready` deltaP `42.5942` edge `0.4225` maxDD `-0.8682`
- `news_risk_high->index_24h` score `5.7591` n `83` status `ready` deltaP `39.0039` edge `0.2375` maxDD `-0.075`
- `news_risk_high->metal_24h` score `3.9862` n `83` status `ready` deltaP `31.4696` edge `0.1678` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.6619` n `52` status `ready` deltaP `31.3203` edge `0.048` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6619` n `52` status `ready` deltaP `31.3203` edge `0.048` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5617` n `149` status `ready` deltaP `27.8226` edge `0.0698` maxDD `-0.345`
- `risk_on_high->fx_24h` score `2.4456` n `52` status `ready` deltaP `32.1047` edge `-0.006` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4456` n `52` status `ready` deltaP `32.1047` edge `-0.006` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.3107` n `149` status `ready` deltaP `29.3298` edge `0.0186` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.0821` n `149` status `ready` deltaP `16.0612` edge `0.0208` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.4589` n `52` status `ready` deltaP `9.1433` edge `0.0125` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4589` n `52` status `ready` deltaP `9.1433` edge `0.0125` maxDD `-0.1507`
- `news_risk_high->index_4h` score `0.1782` n `83` status `ready` deltaP `9.2969` edge `0.0237` maxDD `-0.6935`
- `market_context_high->fx_1h` score `0.0711` n `149` status `ready` deltaP `4.9512` edge `0.0019` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
