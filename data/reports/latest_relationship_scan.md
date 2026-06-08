# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T02:52:26.659550+00:00`
- Price records: `672`
- Market context records: `3241`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9724`

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

- `market_context_high->crypto_alt_24h` score `14.2329` n `103` status `ready` deltaP `18.4769` edge `2.6857` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `13.6474` n `103` status `ready` deltaP `49.0359` edge `0.8532` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.6143` n `103` status `ready` deltaP `31.8366` edge `0.8444` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.5444` n `103` status `ready` deltaP `19.222` edge `1.5525` maxDD `-53.663`
- `risk_on_high->crypto_major_1h` score `2.6297` n `31` status `ready` deltaP `10.8267` edge `0.3719` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.6297` n `31` status `ready` deltaP `10.8267` edge `0.3719` maxDD `-5.8885`
- `market_context_high->crypto_major_24h` score `2.4578` n `103` status `ready` deltaP `22.5475` edge `2.2347` maxDD `-152.2601`
- `market_context_high->commodity_4h` score `1.8606` n `139` status `ready` deltaP `17.1258` edge `0.1367` maxDD `-3.9989`
- `risk_on_high->crypto_alt_1h` score `0.7487` n `31` status `ready` deltaP `4.0081` edge `0.213` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.7487` n `31` status `ready` deltaP `4.0081` edge `0.213` maxDD `-8.1649`
- `risk_on_high->metal_1h` score `0.4623` n `31` status `ready` deltaP `7.9148` edge `0.075` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.4623` n `31` status `ready` deltaP `7.9148` edge `0.075` maxDD `-1.4793`
- `risk_on_high->equity_1h` score `0.3352` n `31` status `ready` deltaP `2.6608` edge `0.1156` maxDD `-3.5625`
- `risk_on_and_context->equity_1h` score `0.3352` n `31` status `ready` deltaP `2.6608` edge `0.1156` maxDD `-3.5625`
- `risk_on_high->index_1h` score `-0.104` n `31` status `ready` deltaP `0.1835` edge `0.0478` maxDD `-1.3216`
- `risk_on_and_context->index_1h` score `-0.104` n `31` status `ready` deltaP `0.1835` edge `0.0478` maxDD `-1.3216`
- `market_context_high->commodity_1h` score `-0.3934` n `151` status `ready` deltaP `3.7921` edge `0.0235` maxDD `-2.5251`
- `market_context_high->index_1h` score `-0.4778` n `151` status `ready` deltaP `4.1143` edge `0.0176` maxDD `-4.5023`
- `market_context_high->unknown_4h` score `-0.5806` n `139` status `ready` deltaP `9.2604` edge `0.0904` maxDD `-15.1257`
- `market_context_high->crypto_major_1h` score `-0.7356` n `151` status `ready` deltaP `4.3324` edge `0.1031` maxDD `-15.1032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
