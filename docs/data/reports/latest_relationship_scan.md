# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T09:37:27.716428+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11190`

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

- `news_risk_high->unknown_1h` score `443.0597` n `82` status `ready` deltaP `-5.999` edge `37.0038` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `20.3033` n `82` status `ready` deltaP `41.781` edge `1.4622` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.4477` n `82` status `ready` deltaP `34.9848` edge `1.3678` maxDD `-9.098`
- `news_risk_high->equity_24h` score `12.0834` n `82` status `ready` deltaP `35.4844` edge `0.9484` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.2392` n `82` status `ready` deltaP `59.3199` edge `0.3088` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `7.0207` n `85` status `ready` deltaP `40.1042` edge `0.3177` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.2203` n `41` status `ready` deltaP `40.1042` edge `0.251` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2203` n `41` status `ready` deltaP `40.1042` edge `0.251` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.8037` n `82` status `ready` deltaP `34.989` edge `0.2958` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `5.1488` n `41` status `ready` deltaP `57.6304` edge `0.0491` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.1488` n `41` status `ready` deltaP `57.6304` edge `0.0491` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.6228` n `85` status `ready` deltaP `53.0106` edge `0.0534` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9427` n `52` status `ready` deltaP `26.2899` edge `0.0216` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9427` n `52` status `ready` deltaP `26.2899` edge `0.0216` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.743` n `137` status `ready` deltaP `21.6998` edge `0.0424` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.6939` n `137` status `ready` deltaP `12.2132` edge `0.0141` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.663` n `82` status `ready` deltaP `16.311` edge `0.0391` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3239` n `137` status `ready` deltaP `11.9881` edge `0.0092` maxDD `-0.1412`
- `market_context_high->fx_1h` score `0.183` n `137` status `ready` deltaP `5.811` edge `0.0023` maxDD `-0.063`
- `risk_on_high->commodity_1h` score `0.1785` n `52` status `ready` deltaP `6.5984` edge `0.0061` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
