# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T14:52:27.453846+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2590`

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

- `market_context_high->unknown_1h` score `12556.0786` n `104` status `ready` deltaP `0.3743` edge `1046.3572` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `8042.8486` n `102` status `ready` deltaP `-0.3736` edge `670.2683` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `25.204` n `88` status `ready` deltaP `46.1489` edge `1.852` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.6092` n `88` status `ready` deltaP `23.3586` edge `1.4719` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.8347` n `102` status `ready` deltaP `3.267` edge `0.413` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.1964` n `102` status `ready` deltaP `4.1816` edge `0.2794` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.5025` n `102` status `ready` deltaP `18.5348` edge `0.0473` maxDD `-5.9858`
- `market_context_high->metal_24h` score `0.3631` n `88` status `ready` deltaP `18.7184` edge `0.2143` maxDD `-14.7068`
- `market_context_high->crypto_major_1h` score `-0.1751` n `104` status `ready` deltaP `4.5313` edge `0.087` maxDD `-6.5061`
- `market_context_high->metal_1h` score `-0.1756` n `104` status `ready` deltaP `4.2549` edge `0.0156` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3201` n `104` status `ready` deltaP `2.2455` edge `0.0052` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-0.6915` n `104` status `ready` deltaP `-1.5373` edge `0.0438` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-0.9397` n `104` status `ready` deltaP `5.1301` edge `0.0232` maxDD `-10.8962`
- `market_context_high->index_4h` score `-1.2627` n `102` status `ready` deltaP `-3.6825` edge `-0.003` maxDD `-4.7471`
- `market_context_high->fx_1h` score `-1.5166` n `104` status `ready` deltaP `-10.6806` edge `-0.0007` maxDD `-0.3584`
- `market_context_high->fx_4h` score `-2.3677` n `102` status `ready` deltaP `-14.7537` edge `-0.0036` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4223` n `104` status `ready` deltaP `-9.7421` edge `-0.0291` maxDD `-3.9584`
- `market_context_high->fx_24h` score `-7.0611` n `88` status `ready` deltaP `-22.7273` edge `-0.0096` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.3854` n `102` status `ready` deltaP `-31.0049` edge `-0.1302` maxDD `-14.9509`
- `market_context_high->equity_4h` score `-9.4936` n `102` status `ready` deltaP `-8.5426` edge `-0.0665` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
