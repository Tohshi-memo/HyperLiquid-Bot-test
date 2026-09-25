# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T03:22:31.393476+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11053`

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

- `market_context_high->unknown_1h` score `86.7692` n `47` status `ready` deltaP `9.3675` edge `7.1754` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `48.3617` n `47` status `ready` deltaP `30.4226` edge `3.8666` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.6624` n `47` status `ready` deltaP `24.782` edge `2.5113` maxDD `-2.7051`
- `market_context_high->equity_24h` score `26.0806` n `47` status `ready` deltaP `34.7628` edge `1.9772` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.2827` n `47` status `ready` deltaP `39.1031` edge `0.4425` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.5923` n `47` status `ready` deltaP `38.7042` edge `0.1485` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.3358` n `58` status `ready` deltaP `30.7651` edge `0.1077` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.9619` n `47` status `ready` deltaP `33.8739` edge `0.0364` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.5379` n `47` status `ready` deltaP `17.1445` edge `0.139` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `1.0912` n `116` status `ready` deltaP `9.457` edge `0.1113` maxDD `-4.0061`
- `news_risk_high->crypto_major_1h` score `1.0667` n `116` status `ready` deltaP `11.5528` edge `0.0731` maxDD `-2.8981`
- `news_risk_high->metal_1h` score `1.0152` n `116` status `ready` deltaP `14.237` edge `0.0182` maxDD `-0.6142`
- `market_context_high->index_1h` score `0.9343` n `47` status `ready` deltaP `14.3107` edge `0.0103` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9259` n `47` status `ready` deltaP `11.3167` edge `0.042` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `0.6988` n `47` status `ready` deltaP `8.0111` edge `0.0716` maxDD `-3.3417`
- `market_context_high->fx_1h` score `0.3416` n `47` status `ready` deltaP `8.6125` edge `0.0067` maxDD `-0.1854`
- `market_context_high->metal_1h` score `-0.0162` n `47` status `ready` deltaP `2.8284` edge `0.0107` maxDD `-0.1976`
- `news_risk_high->fx_4h` score `-0.0523` n `104` status `ready` deltaP `8.5483` edge `0.0131` maxDD `-1.1434`
- `news_risk_high->equity_1h` score `-0.0854` n `116` status `ready` deltaP `3.1179` edge `0.0301` maxDD `-2.6402`
- `market_context_high->crypto_major_1h` score `-0.2116` n `47` status `ready` deltaP `1.7582` edge `0.0524` maxDD `-4.5405`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
