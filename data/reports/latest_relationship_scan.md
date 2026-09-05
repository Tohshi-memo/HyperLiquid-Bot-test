# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T03:07:26.047625+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10466`

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

- `risk_on_high->unknown_4h` score `19.6048` n `133` status `ready` deltaP `7.779` edge `1.6437` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.6048` n `133` status `ready` deltaP `7.779` edge `1.6437` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `9.1072` n `217` status `ready` deltaP `8.2156` edge `0.7737` maxDD `-2.563`
- `news_risk_high->crypto_alt_24h` score `7.0618` n `38` status `ready` deltaP `24.9817` edge `0.4489` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.9953` n `38` status `ready` deltaP `23.0628` edge `0.1834` maxDD `-0.0034`
- `news_risk_high->crypto_major_4h` score `3.531` n `38` status `ready` deltaP `15.7172` edge `0.232` maxDD `-1.0693`
- `news_risk_high->metal_4h` score `2.2336` n `38` status `ready` deltaP `22.6573` edge `0.0572` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.8848` n `38` status `ready` deltaP `11.7538` edge `0.0988` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.6497` n `38` status `ready` deltaP `14.0167` edge `0.0831` maxDD `-0.7924`
- `news_risk_high->index_1h` score `1.3` n `38` status `ready` deltaP `16.3253` edge `0.0129` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `1.2679` n `38` status `ready` deltaP `15.1907` edge `0.0237` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `1.1889` n `38` status `ready` deltaP `5.9486` edge `0.0777` maxDD `-0.4628`
- `news_risk_high->crypto_alt_4h` score `0.9526` n `38` status `ready` deltaP `7.5979` edge `0.0616` maxDD `-1.296`
- `news_risk_high->crypto_alt_1h` score `0.8507` n `38` status `ready` deltaP `7.9184` edge `0.0446` maxDD `-0.7867`
- `risk_on_high->metal_1h` score `0.1451` n `133` status `ready` deltaP `13.311` edge `0.0011` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1451` n `133` status `ready` deltaP `13.311` edge `0.0011` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `0.059` n `38` status `ready` deltaP `7.3196` edge `0.0034` maxDD `-0.9036`
- `news_risk_high->fx_24h` score `0.0365` n `38` status `ready` deltaP `10.8004` edge `0.0368` maxDD `-3.1274`
- `risk_on_high->index_1h` score `-0.1886` n `133` status `ready` deltaP `3.5433` edge `-0.0033` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1886` n `133` status `ready` deltaP `3.5433` edge `-0.0033` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
