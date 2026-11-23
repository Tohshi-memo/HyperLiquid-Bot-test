# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T02:07:28.582254+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5282`

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

- `market_context_high->unknown_1h` score `14949.7472` n `89` status `ready` deltaP `0.666` edge `1245.824` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `9648.9979` n `89` status `ready` deltaP `-1.3668` edge `804.1228` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1354.9809` n `31` status `ready` deltaP `4.3268` edge `112.9038` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1195.3482` n `31` status `ready` deltaP `4.3962` edge `99.5887` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.7419` n `31` status `ready` deltaP `38.5966` edge `0.7694` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0419` n `31` status `ready` deltaP `25.6933` edge `0.8359` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.6539` n `31` status `ready` deltaP `14.3391` edge `0.8992` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.9486` n `31` status `ready` deltaP `19.688` edge `0.2165` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.499` n `31` status `ready` deltaP `36.6149` edge `0.0735` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7034` n `31` status `ready` deltaP `31.6931` edge `0.0225` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4735` n `31` status `ready` deltaP `9.8609` edge `0.2975` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.069` n `31` status `ready` deltaP `8.5136` edge `0.2442` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.554` n `31` status `ready` deltaP `29.433` edge `0.0309` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.5412` n `31` status `ready` deltaP `21.1988` edge `0.112` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.7958` n `31` status `ready` deltaP `17.8206` edge `0.023` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0909` n `31` status `ready` deltaP `1.0817` edge `0.0114` maxDD `-0.0947`
- `market_context_high->fx_4h` score `-0.335` n `89` status `ready` deltaP `8.0313` edge `0.0106` maxDD `-0.9003`
- `market_context_high->metal_1h` score `-0.3627` n `89` status `ready` deltaP `2.4305` edge `0.0054` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.4051` n `89` status `ready` deltaP `1.6097` edge `0.0011` maxDD `-0.9806`
- `market_context_high->metal_4h` score `-1.2764` n `89` status `ready` deltaP `3.7287` edge `0.0092` maxDD `-6.9009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
