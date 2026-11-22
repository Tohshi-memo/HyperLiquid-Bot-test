# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T05:22:29.599620+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4590`

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

- `market_context_high->unknown_1h` score `10146.4595` n `122` status `ready` deltaP `1.0209` edge `845.5513` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6148.7148` n `122` status `ready` deltaP `-0.8796` edge `512.4293` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.1766` n `122` status `ready` deltaP `4.6407` edge `0.0129` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4368` n `122` status `ready` deltaP `1.4258` edge `0.0028` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.8181` n `122` status `ready` deltaP `8.2692` edge `0.0206` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.414` n `122` status `ready` deltaP `-9.0729` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.7803` n `122` status `ready` deltaP `-4.2933` edge `0.0018` maxDD `-1.7803`
- `market_context_high->equity_1h` score `-1.9259` n `122` status `ready` deltaP `4.783` edge `0.0052` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.3869` n `122` status `ready` deltaP `-9.3796` edge `-0.0232` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.7888` n `122` status `ready` deltaP `-7.2446` edge `-0.0208` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.0197` n `122` status `ready` deltaP `0.4565` edge `-0.0312` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-4.0242` n `122` status `ready` deltaP `-7.6691` edge `-0.0565` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-5.6493` n `122` status `ready` deltaP `-3.566` edge `-0.0076` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-5.7762` n `122` status `ready` deltaP `-7.8921` edge `-0.0009` maxDD `-6.8933`
- `market_context_high->crypto_alt_4h` score `-6.1905` n `122` status `ready` deltaP `-3.7185` edge `-0.0876` maxDD `-46.5016`
- `market_context_high->commodity_4h` score `-6.924` n `122` status `ready` deltaP `-19.1423` edge `-0.0809` maxDD `-15.4791`
- `market_context_high->metal_24h` score `-8.3599` n `122` status `ready` deltaP `2.4362` edge `0.0967` maxDD `-52.1012`
- `market_context_high->crypto_major_24h` score `-13.3018` n `122` status `ready` deltaP `12.113` edge `0.2739` maxDD `-152.134`
- `market_context_high->index_24h` score `-15.1977` n `122` status `ready` deltaP `-28.6174` edge `-0.1319` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.947` n `122` status `ready` deltaP `3.2901` edge `0.0518` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
