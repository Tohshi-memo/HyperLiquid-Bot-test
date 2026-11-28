# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T22:07:32.311334+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7448`

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

- `market_context_high->fx_1h` score `0.8266` n `72` status `ready` deltaP `13.3982` edge `0.0017` maxDD `-0.1042`
- `market_context_high->fx_4h` score `0.5741` n `68` status `ready` deltaP `11.7198` edge `0.0093` maxDD `-0.1673`
- `market_context_high->metal_1h` score `0.2163` n `72` status `ready` deltaP `6.9444` edge `0.004` maxDD `-0.2485`
- `market_context_high->commodity_1h` score `-0.0467` n `72` status `ready` deltaP `3.0772` edge `0.0081` maxDD `-0.4347`
- `market_context_high->equity_1h` score `-0.2243` n `72` status `ready` deltaP `5.9381` edge `-0.0081` maxDD `-2.1532`
- `market_context_high->metal_4h` score `-0.3904` n `68` status `ready` deltaP `2.0804` edge `0.0083` maxDD `-0.4441`
- `market_context_high->index_1h` score `-0.4628` n `72` status `ready` deltaP `-1.0479` edge `-0.003` maxDD `-0.2813`
- `market_context_high->crypto_major_1h` score `-1.2212` n `72` status `ready` deltaP `-4.4661` edge `0.0007` maxDD `-7.5329`
- `market_context_high->equity_4h` score `-3.7208` n `68` status `ready` deltaP `-17.6471` edge `-0.1557` maxDD `-6.9605`
- `market_context_high->commodity_4h` score `-3.8533` n `68` status `ready` deltaP `-23.1169` edge `-0.0092` maxDD `-2.9572`
- `market_context_high->index_4h` score `-4.2769` n `68` status `ready` deltaP `-23.9867` edge `-0.0217` maxDD `-0.984`
- `market_context_high->crypto_alt_1h` score `-4.3862` n `72` status `ready` deltaP `-9.3563` edge `-0.1078` maxDD `-11.9607`
- `market_context_high->crypto_major_4h` score `-9.3666` n `68` status `ready` deltaP `-10.1776` edge `-0.2622` maxDD `-22.7068`
- `market_context_high->crypto_alt_4h` score `-19.8479` n `68` status `ready` deltaP `-33.6621` edge `-0.6701` maxDD `-49.4247`
- `market_context_high->unknown_4h` score `-545.5599` n `68` status `ready` deltaP `4.4745` edge `-45.4882` maxDD `-0.063`
- `market_context_high->unknown_1h` score `-1312.0747` n `72` status `ready` deltaP `1.4388` edge `-109.3375` maxDD `-0.2652`
- `news_risk_high->unknown_1h` score `2902.3289` n `25` status `thin_sample` deltaP `8.3832` edge `290.177` maxDD `0.0`
- `news_risk_high->unknown_4h` score `233.8013` n `25` status `thin_sample` deltaP `5.9451` edge `23.3405` maxDD `0.0`
- `risk_on_high->unknown_4h` score `27.3031` n `2` status `thin_sample` deltaP `5.9451` edge `34.0892` maxDD `0.0`
- `risk_on_and_context->unknown_4h` score `27.3031` n `2` status `thin_sample` deltaP `5.9451` edge `34.0892` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
