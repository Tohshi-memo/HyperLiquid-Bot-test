# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T17:07:29.069363+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13296`

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

- `market_context_high->unknown_24h` score `17793.5016` n `56` status `ready` deltaP `10.2093` edge `1482.7439` maxDD `-0.613`
- `risk_on_high->unknown_24h` score `7945.0071` n `37` status `ready` deltaP `11.0298` edge `662.0169` maxDD `-0.1869`
- `risk_on_and_context->unknown_24h` score `7945.0071` n `37` status `ready` deltaP `11.0298` edge `662.0169` maxDD `-0.1869`
- `news_risk_high->unknown_1h` score `421.8687` n `82` status `ready` deltaP `-5.1008` edge `35.2319` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.6325` n `82` status `ready` deltaP `36.0302` edge `1.3613` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.3988` n `82` status `ready` deltaP `38.0236` edge `1.4268` maxDD `-9.098`
- `news_risk_high->equity_24h` score `9.0048` n `82` status `ready` deltaP `26.2363` edge `0.7535` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.9999` n `82` status `ready` deltaP `50.0084` edge `0.2676` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.641` n `82` status `ready` deltaP `25.1052` edge `0.2648` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `4.3382` n `37` status `ready` deltaP `39.8276` edge `0.096` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.3382` n `37` status `ready` deltaP `39.8276` edge `0.096` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.2938` n `56` status `ready` deltaP `39.8276` edge `0.0923` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `3.0745` n `37` status `ready` deltaP `7.1575` edge `0.469` maxDD `-6.8038`
- `risk_on_and_context->crypto_alt_24h` score `3.0745` n `37` status `ready` deltaP `7.1575` edge `0.469` maxDD `-6.8038`
- `market_context_high->crypto_alt_24h` score `2.8667` n `56` status `ready` deltaP `6.6748` edge `0.4781` maxDD `-9.406`
- `market_context_high->metal_24h` score `0.6843` n `56` status `ready` deltaP `8.9902` edge `0.1212` maxDD `-1.4721`
- `news_risk_high->index_4h` score `0.3966` n `82` status `ready` deltaP `12.0427` edge `0.0334` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.1992` n `62` status `ready` deltaP `8.3694` edge `0.1372` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.1992` n `62` status `ready` deltaP `8.3694` edge `0.1372` maxDD `-6.7304`
- `risk_on_high->fx_1h` score `0.1866` n `71` status `ready` deltaP `5.6169` edge `0.0035` maxDD `-0.0318`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
