# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T23:37:34.316025+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5108`

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

- `market_context_high->unknown_1h` score `13130.1611` n `99` status `ready` deltaP `0.939` edge `1094.19` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `8870.4941` n `94` status `ready` deltaP `-0.8886` edge `739.2443` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1372.6222` n `31` status `ready` deltaP `3.5783` edge `114.3789` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1211.547` n `31` status `ready` deltaP `4.3962` edge `100.9386` maxDD `-0.119`
- `news_risk_high->equity_4h` score `12.1614` n `31` status `ready` deltaP `40.121` edge `0.7942` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0807` n `31` status `ready` deltaP `25.9982` edge `0.8371` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.7677` n `31` status `ready` deltaP `15.1013` edge `0.9087` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `4.0781` n `31` status `ready` deltaP `20.1371` edge `0.2243` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.6726` n `31` status `ready` deltaP `38.1393` edge `0.0778` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7693` n `31` status `ready` deltaP `32.2919` edge `0.024` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5203` n `31` status `ready` deltaP `10.1603` edge `0.3015` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1251` n `31` status `ready` deltaP `8.813` edge `0.2494` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.6915` n `31` status `ready` deltaP `22.7232` edge `0.1211` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.5828` n `31` status `ready` deltaP `29.7324` edge `0.0326` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7567` n `31` status `ready` deltaP `17.6682` edge `0.019` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0789` n `31` status `ready` deltaP `1.2314` edge `0.0114` maxDD `-0.0947`
- `market_context_high->index_1h` score `-0.609` n `99` status `ready` deltaP `0.1315` edge `-0.0028` maxDD `-1.2394`
- `market_context_high->metal_1h` score `-0.7471` n `99` status `ready` deltaP `0.9934` edge `-0.0024` maxDD `-2.6517`
- `market_context_high->fx_4h` score `-1.0665` n `94` status `ready` deltaP `1.5471` edge `0.0051` maxDD `-1.1716`
- `market_context_high->fx_1h` score `-1.2808` n `99` status `ready` deltaP `-9.5204` edge `-0.0011` maxDD `-0.3731`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
