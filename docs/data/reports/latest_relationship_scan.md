# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T15:22:31.756378+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9991`

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

- `risk_on_high->unknown_24h` score `130.5247` n `108` status `ready` deltaP `23.8426` edge `10.7291` maxDD `-0.2126`
- `risk_on_and_context->unknown_24h` score `130.5247` n `108` status `ready` deltaP `23.8426` edge `10.7291` maxDD `-0.2126`
- `risk_on_high->crypto_major_24h` score `11.4469` n `108` status `ready` deltaP `24.2477` edge `1.1993` maxDD `-25.8971`
- `risk_on_and_context->crypto_major_24h` score `11.4469` n `108` status `ready` deltaP `24.2477` edge `1.1993` maxDD `-25.8971`
- `market_context_high->equity_24h` score `3.2743` n `196` status `ready` deltaP `16.3584` edge `0.3595` maxDD `-8.989`
- `risk_on_high->crypto_alt_24h` score `2.8175` n `108` status `ready` deltaP `12.5` edge `0.538` maxDD `-23.257`
- `risk_on_and_context->crypto_alt_24h` score `2.8175` n `108` status `ready` deltaP `12.5` edge `0.538` maxDD `-23.257`
- `market_context_high->crypto_alt_24h` score `1.2703` n `196` status `ready` deltaP `14.8242` edge `0.4189` maxDD `-24.6164`
- `risk_on_high->equity_24h` score `0.8656` n `108` status `ready` deltaP `8.044` edge `0.2142` maxDD `-8.989`
- `risk_on_and_context->equity_24h` score `0.8656` n `108` status `ready` deltaP `8.044` edge `0.2142` maxDD `-8.989`
- `risk_on_high->index_1h` score `-0.062` n `133` status `ready` deltaP `5.9486` edge `-0.0029` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.062` n `133` status `ready` deltaP `5.9486` edge `-0.0029` maxDD `-0.5764`
- `risk_on_high->crypto_alt_1h` score `-0.1389` n `133` status `ready` deltaP `3.2574` edge `0.0684` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.1389` n `133` status `ready` deltaP `3.2574` edge `0.0684` maxDD `-5.4685`
- `risk_on_high->metal_1h` score `-0.2396` n `133` status `ready` deltaP `6.3775` edge `-0.002` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.2396` n `133` status `ready` deltaP `6.3775` edge `-0.002` maxDD `-1.699`
- `market_context_high->index_24h` score `-0.3421` n `196` status `ready` deltaP `13.8818` edge `0.0761` maxDD `-5.439`
- `risk_on_high->equity_1h` score `-0.4042` n `133` status `ready` deltaP `7.1767` edge `-0.0122` maxDD `-2.6638`
- `risk_on_and_context->equity_1h` score `-0.4042` n `133` status `ready` deltaP `7.1767` edge `-0.0122` maxDD `-2.6638`
- `risk_on_high->commodity_1h` score `-0.5163` n `133` status `ready` deltaP `1.0085` edge `0.0006` maxDD `-1.0281`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
