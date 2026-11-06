# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T18:22:27.341912+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4091`

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

- `news_risk_high->equity_4h` score `2.4892` n `97` status `ready` deltaP `17.0103` edge `0.2963` maxDD `-4.2454`
- `news_risk_high->index_4h` score `1.0838` n `97` status `ready` deltaP `16.3644` edge `0.029` maxDD `-0.4888`
- `news_risk_high->equity_1h` score `0.6656` n `97` status `ready` deltaP `6.1022` edge `0.0996` maxDD `-1.396`
- `news_risk_high->equity_24h` score `0.3915` n `97` status `ready` deltaP `29.3305` edge `1.0133` maxDD `-86.0244`
- `news_risk_high->index_1h` score `0.3286` n `97` status `ready` deltaP `11.8896` edge `0.0082` maxDD `-0.2931`
- `news_risk_high->index_24h` score `-0.2116` n `97` status `ready` deltaP `2.9928` edge `0.1459` maxDD `-6.6786`
- `news_risk_high->crypto_major_4h` score `-0.2623` n `97` status `ready` deltaP `2.8021` edge `0.1163` maxDD `-9.1553`
- `news_risk_high->metal_1h` score `-0.2669` n `97` status `ready` deltaP `0.6482` edge `-0.0028` maxDD `-0.5256`
- `news_risk_high->fx_1h` score `-0.2862` n `97` status `ready` deltaP `0.4476` edge `0.0003` maxDD `-0.1984`
- `news_risk_high->crypto_alt_1h` score `-0.5669` n `97` status `ready` deltaP `2.761` edge `0.0317` maxDD `-5.8225`
- `news_risk_high->crypto_alt_4h` score `-0.5951` n `97` status `ready` deltaP `1.3578` edge `0.1783` maxDD `-14.0916`
- `news_risk_high->fx_4h` score `-0.7159` n `97` status `ready` deltaP `-1.7994` edge `-0.0031` maxDD `-0.4682`
- `news_risk_high->crypto_major_1h` score `-0.7772` n `97` status `ready` deltaP `-2.0943` edge `0.0082` maxDD `-4.1772`
- `news_risk_high->metal_4h` score `-0.7793` n `97` status `ready` deltaP `2.3605` edge `-0.0251` maxDD `-1.5773`
- `news_risk_high->fx_24h` score `-1.4947` n `97` status `ready` deltaP `-11.1169` edge `0.0118` maxDD `-0.313`
- `news_risk_high->metal_24h` score `-2.8077` n `97` status `ready` deltaP `4.9117` edge `-0.2031` maxDD `-8.5019`
- `news_risk_high->commodity_1h` score `-3.2962` n `97` status `ready` deltaP `-18.9225` edge `-0.0144` maxDD `-3.0639`
- `news_risk_high->commodity_4h` score `-4.7744` n `97` status `ready` deltaP `-27.0587` edge `-0.0175` maxDD `-7.3313`
- `news_risk_high->crypto_major_24h` score `-6.0419` n `97` status `ready` deltaP `-13.9774` edge `0.1689` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-9.6846` n `97` status `ready` deltaP `-24.8459` edge `-0.0127` maxDD `-32.9634`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
