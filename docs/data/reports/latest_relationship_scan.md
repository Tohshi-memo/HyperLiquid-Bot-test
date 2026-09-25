# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T06:52:33.257632+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11254`

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

- `market_context_high->unknown_1h` score `84.9393` n `47` status `ready` deltaP `8.4693` edge `7.0289` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `49.5696` n `47` status `ready` deltaP `30.5962` edge `3.9661` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.2012` n `47` status `ready` deltaP `24.782` edge `2.5562` maxDD `-2.7051`
- `market_context_high->equity_24h` score `26.0266` n `47` status `ready` deltaP `34.7628` edge `1.9727` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.1578` n `47` status `ready` deltaP `37.8878` edge `0.4402` maxDD `-0.3705`
- `news_risk_high->unknown_1h` score `5.6431` n `116` status `ready` deltaP `4.1039` edge `0.4568` maxDD `-0.4452`
- `market_context_high->metal_24h` score `4.7653` n `47` status `ready` deltaP `40.2667` edge `0.1525` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.7311` n `54` status `ready` deltaP `30.3819` edge `0.1432` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.9059` n `47` status `ready` deltaP `33.2641` edge `0.0358` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.5341` n `47` status `ready` deltaP `16.992` edge `0.1397` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.2196` n `47` status `ready` deltaP `9.8404` edge `0.1028` maxDD `-3.3417`
- `news_risk_high->crypto_alt_1h` score `1.0552` n `116` status `ready` deltaP `10.1693` edge `0.1112` maxDD `-4.2849`
- `market_context_high->equity_1h` score `0.9762` n `47` status `ready` deltaP `11.7658` edge `0.0432` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.9595` n `47` status `ready` deltaP `14.6101` edge `0.0104` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.4027` n `47` status `ready` deltaP `9.361` edge `0.0068` maxDD `-0.1854`
- `news_risk_high->crypto_major_1h` score `0.1829` n `116` status `ready` deltaP `5.8538` edge `0.0509` maxDD `-3.3083`
- `market_context_high->metal_1h` score `0.0624` n `47` status `ready` deltaP `4.026` edge `0.0128` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `0.025` n `116` status `ready` deltaP `8.5381` edge `0.0081` maxDD `-0.7016`
- `market_context_high->crypto_major_1h` score `-0.0594` n `47` status `ready` deltaP `2.9558` edge `0.0571` maxDD `-4.5405`
- `market_context_high->metal_4h` score `-0.1981` n `47` status `ready` deltaP `-1.9525` edge `0.026` maxDD `-0.404`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
