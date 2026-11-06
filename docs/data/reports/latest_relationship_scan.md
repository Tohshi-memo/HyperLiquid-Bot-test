# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T19:07:32.806215+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4095`

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

- `news_risk_high->equity_4h` score `2.2898` n `94` status `ready` deltaP `16.4147` edge `0.2747` maxDD `-4.2454`
- `news_risk_high->index_4h` score `1.0184` n `94` status `ready` deltaP `15.8018` edge `0.0273` maxDD `-0.4888`
- `news_risk_high->equity_1h` score `0.7995` n `94` status `ready` deltaP `7.4627` edge `0.1077` maxDD `-1.396`
- `news_risk_high->index_1h` score `0.4162` n `94` status `ready` deltaP `13.3488` edge `0.0097` maxDD `-0.2931`
- `news_risk_high->equity_24h` score `-0.0941` n `94` status `ready` deltaP `28.5409` edge `0.9563` maxDD `-86.0244`
- `news_risk_high->crypto_major_4h` score `-0.1718` n `94` status `ready` deltaP `3.957` edge `0.1202` maxDD `-9.1553`
- `news_risk_high->metal_1h` score `-0.1961` n `94` status `ready` deltaP `1.8442` edge `-0.0017` maxDD `-0.5256`
- `news_risk_high->index_24h` score `-0.343` n `94` status `ready` deltaP `1.5451` edge `0.1446` maxDD `-6.6786`
- `news_risk_high->fx_1h` score `-0.3568` n `94` status `ready` deltaP `-0.8504` edge `-0.0001` maxDD `-0.1984`
- `news_risk_high->crypto_alt_1h` score `-0.3707` n `94` status `ready` deltaP `3.9241` edge `0.0491` maxDD `-5.8225`
- `news_risk_high->fx_4h` score `-0.514` n `94` status `ready` deltaP `-0.0227` edge `-0.0023` maxDD `-0.4086`
- `news_risk_high->crypto_major_1h` score `-0.5935` n `94` status `ready` deltaP `-1.0957` edge `0.0251` maxDD `-4.1772`
- `news_risk_high->crypto_alt_4h` score `-0.7483` n `94` status `ready` deltaP `0.3016` edge `0.1657` maxDD `-14.0916`
- `news_risk_high->metal_4h` score `-0.8626` n `94` status `ready` deltaP `1.0444` edge `-0.027` maxDD `-1.5773`
- `news_risk_high->fx_24h` score `-1.3844` n `94` status `ready` deltaP `-10.8908` edge `0.0151` maxDD `-0.2958`
- `news_risk_high->metal_24h` score `-2.8501` n `94` status `ready` deltaP `4.5761` edge `-0.2063` maxDD `-8.5019`
- `news_risk_high->commodity_1h` score `-3.3047` n `94` status `ready` deltaP `-19.2986` edge `-0.0144` maxDD `-2.9201`
- `news_risk_high->commodity_4h` score `-4.5451` n `94` status `ready` deltaP `-26.8909` edge `-0.0116` maxDD `-6.3641`
- `news_risk_high->crypto_major_24h` score `-6.2727` n `94` status `ready` deltaP `-15.596` edge `0.1501` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-9.4995` n `94` status `ready` deltaP `-25.1355` edge `-0.0123` maxDD `-31.6068`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
