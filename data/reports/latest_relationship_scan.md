# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T16:22:31.762891+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `market_context_high->unknown_24h` score `126.4569` n `132` status `ready` deltaP `-33.2071` edge `11.0507` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.7904` n `32` status `ready` deltaP `-46.1806` edge `4.5868` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.7904` n `32` status `ready` deltaP `-46.1806` edge `4.5868` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.8914` n `36` status `ready` deltaP `11.2847` edge `0.787` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.3312` n `36` status `ready` deltaP `38.7195` edge `0.3528` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.751` n `32` status `ready` deltaP `32.1181` edge `0.1818` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.751` n `32` status `ready` deltaP `32.1181` edge `0.1818` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.4228` n `132` status `ready` deltaP `26.8151` edge `0.2183` maxDD `-0.9468`
- `risk_on_high->commodity_4h` score `2.8776` n `32` status `ready` deltaP `20.0457` edge `0.1244` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.8776` n `32` status `ready` deltaP `20.0457` edge `0.1244` maxDD `-0.1258`
- `risk_on_high->crypto_major_24h` score `2.2534` n `32` status `ready` deltaP `17.5347` edge `0.2876` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.2534` n `32` status `ready` deltaP `17.5347` edge `0.2876` maxDD `-6.2481`
- `news_risk_high->index_24h` score `2.1731` n `36` status `ready` deltaP `15.1042` edge `0.0804` maxDD `0.0`
- `news_risk_high->equity_1h` score `1.7669` n `36` status `ready` deltaP `8.8823` edge `0.1199` maxDD `-0.5496`
- `news_risk_high->index_4h` score `1.7467` n `36` status `ready` deltaP `20.376` edge `0.0229` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.5671` n `132` status `ready` deltaP `16.1631` edge `0.0735` maxDD `-1.0528`
- `risk_on_high->commodity_1h` score `1.321` n `32` status `ready` deltaP `13.9596` edge `0.0403` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.321` n `32` status `ready` deltaP `13.9596` edge `0.0403` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.1254` n `32` status `ready` deltaP `13.3681` edge `0.0231` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.1254` n `32` status `ready` deltaP `13.3681` edge `0.0231` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
