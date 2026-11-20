# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T17:07:37.762608+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2726`

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

- `market_context_high->unknown_1h` score `10170.8896` n `126` status `ready` deltaP `1.7632` edge `847.5822` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6466.9694` n `122` status `ready` deltaP `0.6072` edge `538.9385` maxDD `-0.6076`
- `market_context_high->crypto_major_24h` score `4.8332` n `107` status `ready` deltaP `27.4257` edge `1.1498` maxDD `-50.7065`
- `market_context_high->crypto_alt_24h` score `1.6295` n `107` status `ready` deltaP `14.3156` edge `0.9524` maxDD `-66.63`
- `market_context_high->metal_1h` score `-0.1797` n `126` status `ready` deltaP `4.251` edge `0.0151` maxDD `-2.6517`
- `market_context_high->metal_4h` score `-0.2041` n `122` status `ready` deltaP `13.662` edge `0.0432` maxDD `-8.5022`
- `market_context_high->index_1h` score `-0.3108` n `126` status `ready` deltaP `2.8585` edge `0.0023` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.3711` n `126` status `ready` deltaP `-8.5068` edge `-0.0016` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.9283` n `126` status `ready` deltaP `5.6886` edge `0.0073` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-2.0037` n `122` status `ready` deltaP `-8.2192` edge `-0.0005` maxDD `-1.794`
- `market_context_high->crypto_major_4h` score `-2.0731` n `122` status `ready` deltaP `1.6169` edge `0.2165` maxDD `-32.7781`
- `market_context_high->index_4h` score `-2.0941` n `122` status `ready` deltaP `-2.6715` edge `-0.0123` maxDD `-5.5517`
- `market_context_high->commodity_1h` score `-2.1481` n `126` status `ready` deltaP `-7.0241` edge `-0.019` maxDD `-4.3877`
- `market_context_high->crypto_major_1h` score `-2.5314` n `126` status `ready` deltaP `2.11` edge `0.0068` maxDD `-13.8788`
- `market_context_high->crypto_alt_4h` score `-2.7942` n `122` status `ready` deltaP `2.684` edge `0.1383` maxDD `-34.4869`
- `market_context_high->crypto_alt_1h` score `-3.1032` n `126` status `ready` deltaP `-3.4455` edge `-0.0079` maxDD `-13.8848`
- `market_context_high->metal_24h` score `-5.761` n `107` status `ready` deltaP `13.2139` edge `0.1048` maxDD `-43.8379`
- `market_context_high->fx_24h` score `-6.7004` n `107` status `ready` deltaP `-18.0994` edge `-0.0104` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.9755` n `122` status `ready` deltaP `-20.9716` edge `-0.0722` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-12.5509` n `122` status `ready` deltaP `-5.6277` edge `-0.1288` maxDD `-60.0342`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
