# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T20:37:25.041565+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4914`

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

- `market_context_high->unknown_1h` score `12012.4161` n `106` status `ready` deltaP `-0.9915` edge `1001.0611` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7465.1777` n `106` status `ready` deltaP `-2.2694` edge `622.1438` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1392.0538` n `31` status `ready` deltaP `3.8777` edge `115.9962` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1215.3193` n `31` status `ready` deltaP `3.9388` edge `101.256` maxDD `-0.119`
- `news_risk_high->equity_4h` score `12.104` n `31` status `ready` deltaP `40.2734` edge `0.7884` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0079` n `31` status `ready` deltaP `25.3884` edge `0.8351` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.8008` n `31` status `ready` deltaP `15.5586` edge `0.9099` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.987` n `31` status `ready` deltaP `19.5383` edge `0.2207` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.5534` n `31` status `ready` deltaP `36.9198` edge `0.076` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7226` n `31` status `ready` deltaP `31.8428` edge `0.0231` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4806` n `31` status `ready` deltaP `9.7112` edge `0.2994` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0884` n `31` status `ready` deltaP `8.6633` edge `0.2457` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.6236` n `31` status `ready` deltaP `21.8086` edge `0.1185` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.5649` n `31` status `ready` deltaP `29.433` edge `0.0323` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7786` n `31` status `ready` deltaP `17.6682` edge `0.0218` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0549` n `31` status `ready` deltaP `1.5308` edge `0.0114` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.2787` n `106` status `ready` deltaP `3.3527` edge `0.0084` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3939` n `106` status `ready` deltaP `2.141` edge `0.0016` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.2215` n `106` status `ready` deltaP `-8.6262` edge `-0.0013` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.5196` n `106` status `ready` deltaP `-0.3164` edge `0.0045` maxDD `-1.444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
