# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T04:22:28.662809+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11113`

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

- `market_context_high->unknown_1h` score `86.7297` n `47` status `ready` deltaP `8.9184` edge `7.1751` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `48.7085` n `47` status `ready` deltaP `30.4226` edge `3.8955` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.8232` n `47` status `ready` deltaP `24.782` edge `2.5247` maxDD `-2.7051`
- `market_context_high->equity_24h` score `26.0998` n `47` status `ready` deltaP `34.7628` edge `1.9788` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.2815` n `47` status `ready` deltaP `39.1031` edge `0.4424` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.6683` n `47` status `ready` deltaP `39.3987` edge `0.1502` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.3339` n `54` status `ready` deltaP `30.3819` edge `0.1101` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.9643` n `47` status `ready` deltaP `33.8739` edge `0.0366` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.5595` n `47` status `ready` deltaP `17.1445` edge `0.1408` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `1.177` n `116` status `ready` deltaP `10.8817` edge `0.1166` maxDD `-4.2849`
- `market_context_high->index_1h` score `0.9595` n `47` status `ready` deltaP `14.6101` edge `0.0104` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.957` n `47` status `ready` deltaP `11.6161` edge `0.0426` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `0.8436` n `47` status `ready` deltaP `8.6209` edge `0.0796` maxDD `-3.3417`
- `news_risk_high->crypto_major_1h` score `0.6384` n `116` status `ready` deltaP `9.4157` edge `0.065` maxDD `-3.2991`
- `news_risk_high->metal_1h` score `0.5453` n `116` status `ready` deltaP `11.3876` edge `0.0147` maxDD `-0.6142`
- `market_context_high->fx_1h` score `0.3919` n `47` status `ready` deltaP `9.2113` edge `0.0069` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.0211` n `47` status `ready` deltaP `3.4272` edge `0.0115` maxDD `-0.1976`
- `market_context_high->crypto_major_1h` score `-0.1553` n `47` status `ready` deltaP `2.2073` edge `0.0541` maxDD `-4.5405`
- `news_risk_high->equity_1h` score `-0.2354` n `116` status `ready` deltaP `1.6932` edge `0.0271` maxDD `-2.6402`
- `news_risk_high->index_1h` score `-0.2968` n `116` status `ready` deltaP `2.101` edge `0.0051` maxDD `-0.5725`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
