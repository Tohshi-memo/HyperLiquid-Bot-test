# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T00:07:29.610586+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10145`

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

- `market_context_high->unknown_1h` score `83.9024` n `47` status `ready` deltaP `9.5172` edge `6.9355` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `46.9625` n `47` status `ready` deltaP `30.4226` edge `3.75` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.9772` n `47` status `ready` deltaP `24.782` edge `2.4542` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.7011` n `47` status `ready` deltaP `34.0684` edge `1.9502` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `9.9369` n `114` status `ready` deltaP `-1.1398` edge `0.8601` maxDD `-0.9543`
- `market_context_high->index_24h` score `8.1332` n `47` status `ready` deltaP `37.7142` edge `0.4393` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.3723` n `47` status `ready` deltaP `36.7945` edge `0.1429` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.3969` n `69` status `ready` deltaP `31.5897` edge `0.1073` maxDD `-1.7857`
- `news_risk_high->crypto_alt_1h` score `2.9943` n `114` status `ready` deltaP `15.4297` edge `0.1976` maxDD `-1.7416`
- `market_context_high->index_4h` score `2.9341` n `47` status `ready` deltaP `33.7215` edge `0.0351` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.4083` n `47` status `ready` deltaP `17.1445` edge `0.1282` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.0768` n `114` status `ready` deltaP `15.343` edge `0.1267` maxDD `-2.4737`
- `news_risk_high->metal_1h` score `1.2997` n `114` status `ready` deltaP `17.3285` edge `0.0213` maxDD `-0.6142`
- `market_context_high->index_1h` score `0.9571` n `47` status `ready` deltaP `14.6101` edge `0.0102` maxDD `-0.2275`
- `news_risk_high->fx_4h` score `0.9228` n `102` status `ready` deltaP `16.6188` edge `0.0297` maxDD `-0.421`
- `market_context_high->equity_1h` score `0.9055` n `47` status `ready` deltaP `11.3167` edge `0.0403` maxDD `-1.5564`
- `news_risk_high->crypto_major_4h` score `0.4271` n `102` status `ready` deltaP `10.5063` edge `0.1787` maxDD `-13.719`
- `news_risk_high->crypto_alt_4h` score `0.223` n `102` status `ready` deltaP `5.1919` edge `0.2291` maxDD `-15.9436`
- `market_context_high->fx_1h` score `0.1907` n `47` status `ready` deltaP `6.9658` edge `0.0051` maxDD `-0.1854`
- `market_context_high->crypto_alt_4h` score `0.1899` n `47` status `ready` deltaP `6.9441` edge `0.0363` maxDD `-3.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
