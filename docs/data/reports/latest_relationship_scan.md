# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T11:37:25.350526+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11573`

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

- `market_context_high->equity_24h` score `5.9461` n `82` status `ready` deltaP `2.1892` edge `0.7869` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.7963` n `82` status `ready` deltaP `13.8381` edge `0.2817` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.6274` n `82` status `ready` deltaP `32.7151` edge `0.0647` maxDD `-1.9329`
- `market_context_high->commodity_4h` score `1.4288` n `103` status `ready` deltaP `13.5241` edge `0.0962` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.1641` n `82` status `ready` deltaP `7.3679` edge `0.1992` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `0.9926` n `103` status `ready` deltaP `11.5371` edge `0.0401` maxDD `-0.7439`
- `market_context_high->equity_1h` score `-0.4029` n `103` status `ready` deltaP `4.0478` edge `0.0223` maxDD `-4.6286`
- `market_context_high->index_1h` score `-0.4968` n `103` status `ready` deltaP `-3.3341` edge `-0.0067` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.4986` n `103` status `ready` deltaP `2.0551` edge `-0.0057` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.578` n `103` status `ready` deltaP `-0.5091` edge `-0.0102` maxDD `-1.1743`
- `market_context_high->metal_1h` score `-0.6646` n `103` status `ready` deltaP `-4.459` edge `-0.0059` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.8651` n `103` status `ready` deltaP `1.1751` edge `-0.0046` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.0819` n `103` status `ready` deltaP `-3.6778` edge `-0.0133` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.7571` n `103` status `ready` deltaP `3.9605` edge `-0.0391` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.8606` n `103` status `ready` deltaP `-10.2799` edge `-0.0236` maxDD `-2.3669`
- `market_context_high->crypto_major_1h` score `-2.3834` n `103` status `ready` deltaP `-7.2859` edge `-0.0504` maxDD `-4.6382`
- `market_context_high->crypto_major_24h` score `-2.6317` n `82` status `ready` deltaP `7.0249` edge `-0.1348` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-3.7642` n `82` status `ready` deltaP `-22.3916` edge `-0.189` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.9375` n `103` status `ready` deltaP `-9.6644` edge `-0.0985` maxDD `-6.5487`
- `market_context_high->crypto_major_4h` score `-7.5954` n `103` status `ready` deltaP `-12.2721` edge `-0.212` maxDD `-18.1307`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
