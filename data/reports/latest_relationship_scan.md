# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T13:37:25.155795+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2634`

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

- `market_context_high->unknown_1h` score `10730.146` n `120` status `ready` deltaP `1.507` edge `894.1886` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7123.3992` n `112` status `ready` deltaP `0.7839` edge `593.6398` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `12.151` n `103` status `ready` deltaP `30.0752` edge `1.3026` maxDD `-34.2412`
- `market_context_high->crypto_alt_24h` score `6.4648` n `103` status `ready` deltaP `16.3481` edge `1.1014` maxDD `-48.732`
- `market_context_high->crypto_major_4h` score `1.3393` n `112` status `ready` deltaP `4.9652` edge `0.3604` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.046` n `112` status `ready` deltaP `6.0323` edge `0.2666` maxDD `-13.9055`
- `market_context_high->metal_4h` score `0.2408` n `112` status `ready` deltaP `15.8319` edge `0.0548` maxDD `-6.8892`
- `market_context_high->metal_1h` score `-0.1511` n `120` status `ready` deltaP `4.471` edge `0.0173` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3416` n `120` status `ready` deltaP `2.2056` edge `0.0027` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-1.1585` n `120` status `ready` deltaP `2.8243` edge `0.041` maxDD `-7.843`
- `market_context_high->fx_1h` score `-1.255` n `120` status `ready` deltaP `-7.1757` edge `-0.0008` maxDD `-0.4757`
- `market_context_high->equity_1h` score `-1.6006` n `120` status `ready` deltaP `5.005` edge `0.0194` maxDD `-11.559`
- `market_context_high->index_4h` score `-1.8622` n `112` status `ready` deltaP `-1.9164` edge `-0.0079` maxDD `-4.7608`
- `market_context_high->crypto_alt_1h` score `-1.9062` n `120` status `ready` deltaP `-3.009` edge `0.0188` maxDD `-8.2736`
- `market_context_high->commodity_1h` score `-2.0268` n `120` status `ready` deltaP `-5.9581` edge `-0.016` maxDD `-4.3877`
- `market_context_high->fx_4h` score `-2.2205` n `112` status `ready` deltaP `-12.2387` edge `-0.0015` maxDD `-1.794`
- `market_context_high->metal_24h` score `-4.8228` n `103` status `ready` deltaP `14.2664` edge `0.1164` maxDD `-39.0725`
- `market_context_high->fx_24h` score `-6.5876` n `103` status `ready` deltaP `-17.0341` edge `-0.0081` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-7.4056` n `112` status `ready` deltaP `-24.1725` edge `-0.0867` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-10.2978` n `112` status `ready` deltaP `-5.5314` edge `-0.0733` maxDD `-49.5043`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
