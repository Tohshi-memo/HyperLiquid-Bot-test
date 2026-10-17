# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T15:37:23.174409+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9440`

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

- `risk_on_high->commodity_24h` score `6.9249` n `54` status `ready` deltaP `38.5017` edge `0.3204` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.9249` n `54` status `ready` deltaP `38.5017` edge `0.3204` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `3.3941` n `162` status `ready` deltaP `16.4465` edge `0.3844` maxDD `-9.2297`
- `risk_on_high->crypto_major_4h` score `1.3515` n `88` status `ready` deltaP `16.699` edge `0.2125` maxDD `-9.2297`
- `risk_on_and_context->crypto_major_4h` score `1.3515` n `88` status `ready` deltaP `16.699` edge `0.2125` maxDD `-9.2297`
- `market_context_high->crypto_alt_4h` score `0.8061` n `162` status `ready` deltaP `9.534` edge `0.4309` maxDD `-22.8492`
- `market_context_high->crypto_major_1h` score `0.4741` n `174` status `ready` deltaP `5.3703` edge `0.0926` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.0615` n `90` status `ready` deltaP `5.7057` edge `0.0055` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0615` n `90` status `ready` deltaP `5.7057` edge `0.0055` maxDD `-0.7394`
- `market_context_high->crypto_alt_1h` score `-0.0393` n `174` status `ready` deltaP `6.8432` edge `0.1011` maxDD `-7.3329`
- `market_context_high->metal_4h` score `-0.0461` n `162` status `ready` deltaP `8.4745` edge `0.0442` maxDD `-1.6961`
- `market_context_high->index_1h` score `-0.1897` n `174` status `ready` deltaP `6.8551` edge `0.0048` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2677` n `90` status `ready` deltaP `1.021` edge `-0.0031` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2677` n `90` status `ready` deltaP `1.021` edge `-0.0031` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3167` n `174` status `ready` deltaP `5.766` edge `0.0079` maxDD `-0.9556`
- `market_context_high->equity_1h` score `-0.3923` n `174` status `ready` deltaP `9.8581` edge `0.0377` maxDD `-7.2977`
- `risk_on_high->equity_1h` score `-0.4495` n `90` status `ready` deltaP `9.8198` edge `0.0267` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4495` n `90` status `ready` deltaP `9.8198` edge `0.0267` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.5048` n `90` status `ready` deltaP `0.7086` edge `0.0037` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5048` n `90` status `ready` deltaP `0.7086` edge `0.0037` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
