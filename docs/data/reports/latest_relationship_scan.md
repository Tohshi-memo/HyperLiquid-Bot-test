# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T22:52:33.382270+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10431`

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

- `news_risk_high->unknown_4h` score `372.1768` n `83` status `ready` deltaP `-20.5958` edge `31.2415` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `17.9854` n `83` status `ready` deltaP `41.1291` edge `1.3625` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `16.4743` n `83` status `ready` deltaP `33.3689` edge `1.3499` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `12.786` n `83` status `ready` deltaP `42.6017` edge `0.9589` maxDD `-6.5262`
- `news_risk_high->index_24h` score `6.8953` n `83` status `ready` deltaP `48.0317` edge `0.272` maxDD `-0.075`
- `risk_on_high->commodity_24h` score `6.8822` n `52` status `ready` deltaP `40.2778` edge `0.305` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.8822` n `52` status `ready` deltaP `40.2778` edge `0.305` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.5831` n `149` status `ready` deltaP `33.5664` edge `0.294` maxDD `-0.8682`
- `news_risk_high->metal_24h` score `5.1418` n `83` status `ready` deltaP `32.6849` edge `0.256` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.4192` n `52` status `ready` deltaP `32.1047` edge `-0.0082` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4192` n `52` status `ready` deltaP `32.1047` edge `-0.0082` maxDD `-0.0054`
- `risk_on_high->commodity_4h` score `2.3922` n `52` status `ready` deltaP `29.6435` edge `0.0367` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.3922` n `52` status `ready` deltaP `29.6435` edge `0.0367` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.2919` n `149` status `ready` deltaP `26.1458` edge `0.0585` maxDD `-0.345`
- `market_context_high->fx_24h` score `2.2843` n `149` status `ready` deltaP `29.3298` edge `0.0164` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `0.9827` n `149` status `ready` deltaP `15.0133` edge `0.0195` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.4266` n `83` status `ready` deltaP `12.4982` edge `0.0342` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3594` n `52` status `ready` deltaP `8.0954` edge `0.0112` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3594` n `52` status `ready` deltaP `8.0954` edge `0.0112` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1879` n `52` status `ready` deltaP `6.8632` edge `0.0089` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
