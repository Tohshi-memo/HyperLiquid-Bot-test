# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T21:52:34.883362+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2748`

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

- `market_context_high->unknown_1h` score `10140.0101` n `126` status `ready` deltaP `1.4638` edge `845.0109` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6182.8137` n `126` status `ready` deltaP `-0.3145` edge `515.2671` maxDD `-0.7759`
- `market_context_high->crypto_major_24h` score `3.6463` n `108` status `ready` deltaP `26.794` edge `1.0956` maxDD `-57.8734`
- `market_context_high->metal_1h` score `-0.1929` n `126` status `ready` deltaP `3.9516` edge `0.0154` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2469` n `126` status `ready` deltaP `3.7567` edge `0.0045` maxDD `-1.2295`
- `market_context_high->crypto_alt_24h` score `-0.3451` n `108` status `ready` deltaP `13.8311` edge `0.8691` maxDD `-72.5383`
- `market_context_high->metal_4h` score `-0.4831` n `126` status `ready` deltaP `12.2531` edge `0.037` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.3963` n `126` status `ready` deltaP `-8.8062` edge `-0.0017` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.7412` n `126` status `ready` deltaP `6.1377` edge `0.0199` maxDD `-13.1399`
- `market_context_high->fx_4h` score `-1.9895` n `126` status `ready` deltaP `-7.9462` edge `-0.0005` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.2356` n `126` status `ready` deltaP `-7.6229` edge `-0.0223` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.2814` n `126` status `ready` deltaP `-2.1172` edge `-0.0127` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.36` n `126` status `ready` deltaP `3.1579` edge `0.0141` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.0696` n `126` status `ready` deltaP `-2.9964` edge `-0.0081` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-4.1915` n `126` status `ready` deltaP `0.8735` edge `0.1497` maxDD `-47.4317`
- `market_context_high->metal_24h` score `-5.7182` n `108` status `ready` deltaP `12.963` edge `0.1264` maxDD `-45.1471`
- `market_context_high->fx_24h` score `-6.8305` n `108` status `ready` deltaP `-19.5602` edge `-0.0115` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-6.9632` n `126` status `ready` deltaP `-20.1873` edge `-0.0764` maxDD `-15.5426`
- `market_context_high->crypto_alt_4h` score `-7.1902` n `126` status `ready` deltaP `1.4832` edge `0.0722` maxDD `-46.5016`
- `market_context_high->index_24h` score `-13.0188` n `108` status `ready` deltaP `-26.3888` edge `-0.146` maxDD `-31.7046`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
