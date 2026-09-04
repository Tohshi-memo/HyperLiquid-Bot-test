# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T13:07:27.739359+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11316`

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

- `risk_on_high->unknown_4h` score `20.023` n `133` status `ready` deltaP `7.3216` edge `1.6816` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.023` n `133` status `ready` deltaP `7.3216` edge `1.6816` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `11.996` n `133` status `ready` deltaP `-1.2033` edge `1.0654` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `11.996` n `133` status `ready` deltaP `-1.2033` edge `1.0654` maxDD `-1.95`
- `market_context_high->unknown_4h` score `10.974` n `197` status `ready` deltaP `9.0658` edge `0.9236` maxDD `-2.563`
- `market_context_high->unknown_1h` score `8.0824` n `209` status `ready` deltaP `-1.0666` edge `0.7437` maxDD `-2.0446`
- `news_risk_high->commodity_4h` score `1.4174` n `61` status `ready` deltaP `11.9552` edge `0.0585` maxDD `-0.2737`
- `news_risk_high->commodity_24h` score `0.842` n `61` status `ready` deltaP `10.3427` edge `0.0185` maxDD `-0.0495`
- `market_context_high->equity_24h` score `0.7934` n `167` status `ready` deltaP `14.547` edge `0.4037` maxDD `-20.7654`
- `risk_on_high->metal_1h` score `0.188` n `133` status `ready` deltaP `13.311` edge `0.0066` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.188` n `133` status `ready` deltaP `13.311` edge `0.0066` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0159` n `61` status `ready` deltaP `5.4309` edge `-0.0029` maxDD `-0.8275`
- `news_risk_high->commodity_1h` score `-0.098` n `61` status `ready` deltaP `5.2592` edge `0.0014` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1676` n `133` status `ready` deltaP `3.693` edge `-0.0016` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1676` n `133` status `ready` deltaP `3.693` edge `-0.0016` maxDD `-0.5605`
- `risk_on_high->crypto_alt_1h` score `-0.3204` n `133` status `ready` deltaP `3.7031` edge `0.0503` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.3204` n `133` status `ready` deltaP `3.7031` edge `0.0503` maxDD `-5.4685`
- `risk_on_high->commodity_1h` score `-0.4205` n `133` status `ready` deltaP `0.107` edge `-0.0001` maxDD `-1.0281`
- `risk_on_and_context->commodity_1h` score `-0.4205` n `133` status `ready` deltaP `0.107` edge `-0.0001` maxDD `-1.0281`
- `risk_on_high->equity_1h` score `-0.4578` n `133` status `ready` deltaP `4.3155` edge `0.0` maxDD `-2.6638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
