# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T15:37:40.932208+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5913`

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

- `market_context_high->crypto_alt_24h` score `12.1346` n `39` status `ready` deltaP `52.3771` edge `0.6794` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `11.4701` n `39` status `ready` deltaP `53.6458` edge `0.5982` maxDD `0.0`
- `news_risk_high->equity_4h` score `1.112` n `31` status `ready` deltaP `-7.2777` edge `0.2096` maxDD `-2.8064`
- `news_risk_high->commodity_1h` score `0.9599` n `31` status `ready` deltaP `20.1371` edge `0.01` maxDD `-0.6947`
- `news_risk_high->fx_24h` score `0.9461` n `31` status `ready` deltaP `12.192` edge `0.0628` maxDD `-1.5526`
- `market_context_high->commodity_4h` score `0.3702` n `46` status `ready` deltaP `5.4878` edge `0.0955` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.3587` n `47` status `ready` deltaP `7.7143` edge `0.032` maxDD `-1.3282`
- `news_risk_high->commodity_4h` score `0.2925` n `31` status `ready` deltaP `13.5523` edge `-0.0159` maxDD `-1.6728`
- `news_risk_high->index_4h` score `0.1462` n `31` status `ready` deltaP `-0.3688` edge `0.0527` maxDD `-0.3783`
- `news_risk_high->fx_4h` score `0.1391` n `31` status `ready` deltaP `4.8928` edge `0.0355` maxDD `-0.356`
- `market_context_high->fx_1h` score `0.0989` n `47` status `ready` deltaP `8.345` edge `-0.0082` maxDD `-0.7804`
- `news_risk_high->index_1h` score `-0.0571` n `31` status `ready` deltaP `2.7429` edge `-0.0058` maxDD `-0.5845`
- `market_context_high->fx_4h` score `-0.0622` n `46` status `ready` deltaP `12.9573` edge `-0.0059` maxDD `-1.8531`
- `news_risk_high->crypto_alt_1h` score `-0.1034` n `31` status `ready` deltaP `10.3921` edge `-0.0185` maxDD `-3.1233`
- `news_risk_high->fx_1h` score `-0.2599` n `31` status `ready` deltaP `-0.7147` edge `0.0026` maxDD `-0.1588`
- `news_risk_high->metal_1h` score `-0.5732` n `31` status `ready` deltaP `-2.2117` edge `-0.0011` maxDD `-0.5538`
- `market_context_high->fx_24h` score `-0.5907` n `39` status `ready` deltaP `1.1084` edge `0.0398` maxDD `-2.3798`
- `news_risk_high->metal_4h` score `-0.9209` n `31` status `ready` deltaP `-4.0765` edge `-0.015` maxDD `-0.7654`
- `news_risk_high->crypto_major_1h` score `-0.9546` n `31` status `ready` deltaP `2.062` edge `-0.0641` maxDD `-3.762`
- `news_risk_high->index_24h` score `-1.161` n `31` status `ready` deltaP `7.4429` edge `-0.106` maxDD `-3.7303`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
