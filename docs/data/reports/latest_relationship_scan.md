# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T03:37:29.352571+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10533`

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

- `news_risk_high->unknown_4h` score `382.4712` n `83` status `ready` deltaP `-20.9007` edge `32.1014` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `16.3374` n `83` status `ready` deltaP `38.0041` edge `1.246` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `14.9541` n `83` status `ready` deltaP `30.0703` edge `1.2452` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `11.1817` n `83` status `ready` deltaP `39.3031` edge `0.8472` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `7.7929` n `52` status `ready` deltaP `43.5764` edge `0.3589` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.7929` n `52` status `ready` deltaP `43.5764` edge `0.3589` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.4938` n `149` status `ready` deltaP `36.865` edge `0.3479` maxDD `-0.8682`
- `news_risk_high->index_24h` score `6.4502` n `83` status `ready` deltaP `44.7331` edge `0.2569` maxDD `-0.075`
- `news_risk_high->metal_24h` score `4.6398` n `83` status `ready` deltaP `31.9905` edge `0.2188` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.5922` n `52` status `ready` deltaP `33.6672` edge `-0.0042` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.5922` n `52` status `ready` deltaP `33.6672` edge `-0.0042` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.4573` n `149` status `ready` deltaP `30.8923` edge `0.0204` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.1894` n `52` status `ready` deltaP `27.8143` edge `0.032` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.1894` n `52` status `ready` deltaP `27.8143` edge `0.032` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.0892` n `149` status `ready` deltaP `24.3166` edge `0.0538` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8904` n `149` status `ready` deltaP `14.1151` edge `0.0178` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3666` n `83` status `ready` deltaP `11.736` edge `0.0316` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2672` n `52` status `ready` deltaP `7.1972` edge `0.0095` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2672` n `52` status `ready` deltaP `7.1972` edge `0.0095` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1459` n `52` status `ready` deltaP `6.2644` edge `0.0075` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
