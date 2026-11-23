# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T02:22:29.214456+00:00`
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

- `market_context_high->unknown_1h` score `15147.9636` n `88` status `ready` deltaP `0.5511` edge `1262.3428` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `9795.9288` n `88` status `ready` deltaP `-0.485` edge `816.357` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1346.4129` n `31` status `ready` deltaP `4.3268` edge `112.1898` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1191.6184` n `31` status `ready` deltaP `4.2437` edge `99.2789` maxDD `-0.119`
- `news_risk_high->equity_4h` score `11.7201` n `31` status `ready` deltaP `38.4442` edge `0.7686` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0721` n `31` status `ready` deltaP `25.8457` edge `0.8374` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.6712` n `31` status `ready` deltaP `14.4915` edge `0.9004` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.9726` n `31` status `ready` deltaP `19.8377` edge `0.2175` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.4856` n `31` status `ready` deltaP `36.4625` edge `0.0734` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7178` n `31` status `ready` deltaP `31.8428` edge `0.0227` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4953` n `31` status `ready` deltaP `10.0106` edge `0.2993` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0923` n `31` status `ready` deltaP `8.6633` edge `0.2462` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5563` n `31` status `ready` deltaP `29.433` edge `0.0312` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.5318` n `31` status `ready` deltaP `21.0464` edge `0.1118` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.7997` n `31` status `ready` deltaP `17.8206` edge `0.0235` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0909` n `31` status `ready` deltaP `1.0817` edge `0.0114` maxDD `-0.0947`
- `market_context_high->fx_4h` score `-0.2699` n `88` status `ready` deltaP `8.4535` edge `0.0112` maxDD `-0.8394`
- `market_context_high->metal_1h` score `-0.3162` n `88` status `ready` deltaP `2.9668` edge `0.0057` maxDD `-1.4794`
- `market_context_high->index_1h` score `-0.4417` n `88` status `ready` deltaP `1.1976` edge `0.0008` maxDD `-0.9806`
- `market_context_high->metal_4h` score `-1.2572` n `88` status `ready` deltaP `4.0743` edge `0.0085` maxDD `-6.9009`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
