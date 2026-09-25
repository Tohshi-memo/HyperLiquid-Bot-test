# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T07:22:32.084380+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11302`

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
- `market_context_high->crypto_major_24h` score `49.7196` n `47` status `ready` deltaP `30.5962` edge `3.9786` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.248` n `47` status `ready` deltaP `24.782` edge `2.5601` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.9834` n `47` status `ready` deltaP `34.7628` edge `1.9691` maxDD `-2.1786`
- `market_context_high->index_24h` score `8.1193` n `47` status `ready` deltaP `37.5406` edge `0.4393` maxDD `-0.3705`
- `news_risk_high->unknown_1h` score `5.6431` n `116` status `ready` deltaP `4.1039` edge `0.4568` maxDD `-0.4452`
- `market_context_high->metal_24h` score `4.7641` n `47` status `ready` deltaP `40.2667` edge `0.1524` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.7047` n `53` status `ready` deltaP `30.2771` edge `0.1417` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.8767` n `47` status `ready` deltaP `32.9593` edge `0.0354` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.4857` n `47` status `ready` deltaP `16.6872` edge `0.1377` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.1894` n `47` status `ready` deltaP `9.688` edge `0.1013` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.9762` n `47` status `ready` deltaP `11.7658` edge `0.0432` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.961` n `116` status `ready` deltaP `9.457` edge `0.1081` maxDD `-4.2849`
- `market_context_high->index_1h` score `0.9595` n `47` status `ready` deltaP `14.6101` edge `0.0104` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.4314` n `47` status `ready` deltaP `9.6604` edge `0.0072` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.0726` n `47` status `ready` deltaP `4.1757` edge `0.0131` maxDD `-0.1976`
- `news_risk_high->crypto_major_1h` score `0.0285` n `116` status `ready` deltaP `4.4291` edge `0.0484` maxDD `-3.3776`
- `market_context_high->crypto_major_1h` score `-0.0283` n `47` status `ready` deltaP `3.2552` edge `0.0577` maxDD `-4.5405`
- `news_risk_high->metal_1h` score `-0.0286` n `116` status `ready` deltaP `7.8257` edge `0.0071` maxDD `-0.7016`
- `market_context_high->metal_4h` score `-0.1799` n `47` status `ready` deltaP `-1.6477` edge `0.0263` maxDD `-0.404`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
