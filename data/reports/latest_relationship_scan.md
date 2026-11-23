# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T09:22:28.721079+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4494`

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

- `market_context_high->unknown_1h` score `19463.1703` n `71` status `ready` deltaP `1.4295` edge `1621.9375` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `12907.0599` n `71` status `ready` deltaP `3.8539` edge `1075.5765` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1303.1891` n `31` status `ready` deltaP `3.4286` edge `108.5938` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1158.2616` n `31` status `ready` deltaP `4.8535` edge `96.4951` maxDD `-0.119`
- `news_risk_high->equity_4h` score `10.7936` n `31` status `ready` deltaP `34.6332` edge `0.7168` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.2798` n `31` status `ready` deltaP `22.797` edge `0.7917` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.2511` n `31` status `ready` deltaP `12.0525` edge `0.8628` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.7052` n `31` status `ready` deltaP `18.6401` edge `0.2032` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4298` n `31` status `ready` deltaP `36.0051` edge `0.0718` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6639` n `31` status `ready` deltaP `31.244` edge `0.0222` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3309` n `31` status `ready` deltaP `8.813` edge `0.2862` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9279` n `31` status `ready` deltaP `7.316` edge `0.2341` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5189` n `31` status `ready` deltaP `28.9839` edge `0.0294` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4072` n `31` status `ready` deltaP `19.522` edge `0.106` maxDD `-0.7918`
- `market_context_high->fx_4h` score `1.1067` n `71` status `ready` deltaP `19.8557` edge `0.0186` maxDD `-0.3661`
- `news_risk_high->commodity_4h` score `0.8484` n `31` status `ready` deltaP `18.1255` edge `0.0277` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0309` n `31` status `ready` deltaP `1.5308` edge `0.0134` maxDD `-0.0947`
- `market_context_high->index_1h` score `-0.2883` n `71` status `ready` deltaP `-0.1054` edge `0.001` maxDD `-0.9806`
- `market_context_high->metal_1h` score `-0.3872` n `71` status `ready` deltaP `1.2693` edge `0.0111` maxDD `-1.4794`
- `market_context_high->commodity_1h` score `-0.8395` n `71` status `ready` deltaP `-1.7859` edge `-0.0122` maxDD `-2.3485`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
