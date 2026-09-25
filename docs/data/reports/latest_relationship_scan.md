# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T04:07:32.122698+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11109`

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

- `market_context_high->unknown_1h` score `86.7548` n `47` status `ready` deltaP `9.0681` edge `7.1762` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `48.6209` n `47` status `ready` deltaP `30.4226` edge `3.8882` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.786` n `47` status `ready` deltaP `24.782` edge `2.5216` maxDD `-2.7051`
- `market_context_high->equity_24h` score `26.0974` n `47` status `ready` deltaP `34.7628` edge `1.9786` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.2827` n `47` status `ready` deltaP `39.1031` edge `0.4425` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.6484` n `47` status `ready` deltaP `39.225` edge `0.1497` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.3264` n `55` status `ready` deltaP `30.483` edge `0.1088` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.9631` n `47` status `ready` deltaP `33.8739` edge `0.0365` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.5511` n `47` status `ready` deltaP `17.1445` edge `0.1401` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `1.0744` n `116` status `ready` deltaP `10.1693` edge `0.1128` maxDD `-4.2849`
- `market_context_high->index_1h` score `0.9463` n `47` status `ready` deltaP `14.4604` edge `0.0103` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9415` n `47` status `ready` deltaP `11.4664` edge `0.0423` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `0.8074` n `47` status `ready` deltaP `8.4684` edge `0.0776` maxDD `-3.3417`
- `news_risk_high->crypto_major_1h` score `0.7762` n `116` status `ready` deltaP `10.128` edge `0.0672` maxDD `-3.2695`
- `news_risk_high->metal_1h` score `0.6703` n `116` status `ready` deltaP `12.0999` edge `0.0162` maxDD `-0.6142`
- `market_context_high->fx_1h` score `0.3799` n `47` status `ready` deltaP `9.0616` edge `0.0069` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.0102` n `47` status `ready` deltaP `3.2775` edge `0.0111` maxDD `-0.1976`
- `news_risk_high->equity_1h` score `-0.158` n `116` status `ready` deltaP `2.4056` edge `0.0288` maxDD `-2.6402`
- `market_context_high->crypto_major_1h` score `-0.1721` n `47` status `ready` deltaP `2.0576` edge `0.0537` maxDD `-4.5405`
- `news_risk_high->index_1h` score `-0.2558` n `116` status `ready` deltaP `2.8133` edge `0.0056` maxDD `-0.5725`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
