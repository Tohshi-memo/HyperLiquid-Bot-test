# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T03:37:38.904809+00:00`
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

- `market_context_high->unknown_1h` score `15789.3274` n `85` status `ready` deltaP `2.2437` edge `1315.7785` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `10596.0406` n `83` status `ready` deltaP `3.3977` edge `882.9946` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1337.8042` n `31` status `ready` deltaP `4.0274` edge `111.4744` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1184.1599` n `31` status `ready` deltaP `3.7864` edge `98.6604` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.5743` n `31` status `ready` deltaP `37.9869` edge `0.7595` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0409` n `31` status `ready` deltaP `25.8457` edge `0.8348` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.6298` n `31` status `ready` deltaP `14.3391` edge `0.8961` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.9893` n `31` status `ready` deltaP `19.9874` edge `0.2179` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4212` n `31` status `ready` deltaP `35.8527` edge `0.0721` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.719` n `31` status `ready` deltaP `31.8428` edge `0.0228` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4797` n `31` status `ready` deltaP `10.0106` edge `0.2973` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.118` n `31` status `ready` deltaP `8.9627` edge `0.2475` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5462` n `31` status `ready` deltaP `29.2833` edge `0.0309` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.5191` n `31` status `ready` deltaP `20.894` edge `0.1112` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.8407` n `31` status `ready` deltaP `18.2779` edge `0.0257` maxDD `-0.5151`
- `market_context_high->fx_4h` score `0.0573` n `83` status `ready` deltaP `10.7718` edge `0.0136` maxDD `-0.5784`
- `market_context_high->metal_1h` score `-0.068` n `85` status `ready` deltaP `4.5016` edge `0.0131` maxDD `-1.4794`
- `news_risk_high->commodity_1h` score `-0.1064` n `31` status `ready` deltaP `0.932` edge `0.0111` maxDD `-0.0947`
- `market_context_high->index_1h` score `-0.2609` n `85` status `ready` deltaP `2.9623` edge `0.0041` maxDD `-0.9806`
- `market_context_high->commodity_1h` score `-1.0601` n `85` status `ready` deltaP `-3.9257` edge `-0.0162` maxDD `-3.1494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
