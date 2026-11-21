# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T21:52:26.030020+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `32`

- Symbol pattern count: `3610`

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

- `market_context_high->unknown_1h` score `9975.2045` n `126` status `ready` deltaP `1.314` edge `831.2781` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6019.3787` n `126` status `ready` deltaP `-1.0767` edge `501.6526` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.3067` n `126` status `ready` deltaP `2.4546` edge `0.0108` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4525` n `126` status `ready` deltaP `0.1639` edge `0.0021` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.9746` n `126` status `ready` deltaP `5.5458` edge `0.0187` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4406` n `126` status `ready` deltaP `-9.405` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.878` n `126` status `ready` deltaP `-6.1169` edge `0.0016` maxDD `-1.794`
- `market_context_high->equity_1h` score `-2.2926` n `126` status `ready` deltaP `2.3952` edge `-0.0011` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.4476` n `126` status `ready` deltaP `-10.1678` edge `-0.023` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.8824` n `126` status `ready` deltaP `-8.5196` edge `-0.0201` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.5161` n `126` status `ready` deltaP `-0.884` edge `-0.0553` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-4.1898` n `126` status `ready` deltaP `-7.188` edge `-0.0735` maxDD `-13.8848`
- `market_context_high->fx_24h` score `-6.2948` n `126` status `ready` deltaP `-11.4335` edge `-0.0024` maxDD `-7.0088`
- `market_context_high->crypto_major_4h` score `-6.8254` n `126` status `ready` deltaP `-7.3582` edge `-0.1331` maxDD `-47.4317`
- `market_context_high->commodity_4h` score `-7.1255` n `126` status `ready` deltaP `-21.4068` edge `-0.0818` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-8.08` n `126` status `ready` deltaP `4.9603` edge `0.1032` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-10.9691` n `126` status `ready` deltaP `-7.0534` edge `-0.1858` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-13.1435` n `126` status `ready` deltaP `13.4921` edge `0.285` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.8411` n `126` status `ready` deltaP `-26.1409` edge `-0.1187` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-16.2089` n `126` status `ready` deltaP `2.2569` edge `0.0251` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
