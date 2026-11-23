# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T02:37:27.394356+00:00`
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

- `market_context_high->unknown_1h` score `15356.6522` n `87` status `ready` deltaP `0.4336` edge `1279.7343` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `9949.2409` n `87` status `ready` deltaP `0.4205` edge `829.1228` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1343.5581` n `31` status `ready` deltaP `4.3268` edge `111.9519` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1190.7939` n `31` status `ready` deltaP `4.0913` edge `99.2112` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.7153` n `31` status `ready` deltaP `38.4442` edge `0.7682` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0975` n `31` status `ready` deltaP `25.9982` edge `0.8385` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.6838` n `31` status `ready` deltaP `14.644` edge `0.901` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `4.0133` n `31` status `ready` deltaP `19.9874` edge `0.2199` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.471` n `31` status `ready` deltaP `36.31` edge `0.0732` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7322` n `31` status `ready` deltaP `31.9925` edge `0.0229` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5203` n `31` status `ready` deltaP `10.1603` edge `0.3015` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1212` n `31` status `ready` deltaP `8.813` edge `0.2489` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.568` n `31` status `ready` deltaP `29.5827` edge `0.0317` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.5318` n `31` status `ready` deltaP `21.0464` edge `0.1118` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.8124` n `31` status `ready` deltaP `17.973` edge `0.0241` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0789` n `31` status `ready` deltaP `1.2314` edge `0.0114` maxDD `-0.0947`
- `market_context_high->fx_4h` score `-0.2032` n `87` status `ready` deltaP `8.8887` edge `0.0118` maxDD `-0.769`
- `market_context_high->metal_1h` score `-0.3583` n `87` status `ready` deltaP `2.5156` edge `0.0052` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.4805` n `87` status `ready` deltaP `0.7726` edge `0.0004` maxDD `-0.9806`
- `market_context_high->metal_4h` score `-1.3192` n `87` status `ready` deltaP `3.4343` edge `0.0076` maxDD `-6.9009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
