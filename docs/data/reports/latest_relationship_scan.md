# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T07:22:27.911446+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `137.0629` n `128` status `ready` deltaP `-28.102` edge `11.9005` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.3698` n `32` status `ready` deltaP `-41.3832` edge `4.6291` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.3698` n `32` status `ready` deltaP `-41.3832` edge `4.6291` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `11.9385` n `36` status `ready` deltaP `21.2882` edge `0.8909` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.5028` n `36` status `ready` deltaP `38.6606` edge `0.3675` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.0338` n `128` status `ready` deltaP `28.5054` edge `0.2352` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.6099` n `32` status `ready` deltaP `30.8492` edge `0.1785` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.6099` n `32` status `ready` deltaP `30.8492` edge `0.1785` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.1159` n `32` status `ready` deltaP `27.5076` edge `0.4599` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.1159` n `32` status `ready` deltaP `27.5076` edge `0.4599` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.1577` n `36` status `ready` deltaP `25.4766` edge `0.0933` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.8031` n `32` status `ready` deltaP `20.1341` edge `0.1176` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.8031` n `32` status `ready` deltaP `20.1341` edge `0.1176` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `1.8552` n `128` status `ready` deltaP `18.5716` edge `0.0779` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.7736` n `36` status `ready` deltaP `20.4718` edge `0.0245` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6734` n `36` status `ready` deltaP `7.7728` edge `0.1195` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2414` n `32` status `ready` deltaP `13.1446` edge `0.0391` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2414` n `32` status `ready` deltaP `13.1446` edge `0.0391` maxDD `-0.1957`
- `market_context_high->commodity_1h` score `0.6048` n `128` status `ready` deltaP `8.4571` edge `0.0237` maxDD `-0.3742`
- `risk_on_high->fx_4h` score `0.5751` n `32` status `ready` deltaP `7.0253` edge `0.0152` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
