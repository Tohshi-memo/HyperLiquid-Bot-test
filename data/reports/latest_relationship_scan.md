# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T02:52:15.618202+00:00`
- Price records: `672`
- Market context records: `1179`
- Flow alert records: `5298`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `19.6485` n `144` status `ready` deltaP `44.9652` edge `1.4508` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `9.2966` n `144` status `ready` deltaP `22.2223` edge `0.8282` maxDD `-15.1306`
- `market_context_high->metal_24h` score `5.1836` n `144` status `ready` deltaP `-2.7778` edge `0.6172` maxDD `-6.3373`
- `market_context_high->equity_24h` score `4.9617` n `144` status `ready` deltaP `17.8819` edge `0.4586` maxDD `-10.4803`
- `market_context_high->index_24h` score `4.3783` n `144` status `ready` deltaP `17.5347` edge `0.3174` maxDD `-3.8883`
- `market_context_high->equity_4h` score `2.7389` n `149` status `ready` deltaP `14.1707` edge `0.2001` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.2387` n `149` status `ready` deltaP `10.1736` edge `0.1037` maxDD `-2.1308`
- `market_context_high->unknown_4h` score `0.9722` n `149` status `ready` deltaP `5.9799` edge `0.1628` maxDD `-6.7322`
- `market_context_high->index_1h` score `0.6895` n `149` status `ready` deltaP `9.3819` edge `0.0266` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.4423` n `149` status `ready` deltaP `3.858` edge `0.0489` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.0406` n `149` status `ready` deltaP `7.6307` edge `-0.0001` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `-0.0003` n `149` status `ready` deltaP `7.9616` edge `0.139` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `-0.1277` n `149` status `ready` deltaP `5.55` edge `0.0232` maxDD `-4.1256`
- `market_context_high->metal_1h` score `-0.1413` n `149` status `ready` deltaP `7.9151` edge `-0.0035` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.351` n `149` status `ready` deltaP `1.1363` edge `0.0317` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.927` n `149` status `ready` deltaP `-4.5845` edge `-0.0075` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-1.1021` n `149` status `ready` deltaP `-5.2136` edge `-0.0069` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.3945` n `149` status `ready` deltaP `3.4222` edge `0.0949` maxDD `-16.7194`
- `market_context_high->unknown_24h` score `-1.5172` n `144` status `ready` deltaP `4.3403` edge `0.1176` maxDD `-10.1706`
- `market_context_high->fx_24h` score `-1.6416` n `144` status `ready` deltaP `3.2986` edge `0.0027` maxDD `-11.8118`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
