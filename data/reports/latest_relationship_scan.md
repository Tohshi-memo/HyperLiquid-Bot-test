# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T23:22:31.356905+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10503`

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

- `news_risk_high->unknown_4h` score `372.167` n `83` status `ready` deltaP `-20.7483` edge `31.2417` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `17.9043` n `83` status `ready` deltaP `40.9555` edge `1.3569` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `16.3746` n `83` status `ready` deltaP `33.0217` edge `1.3439` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `12.6226` n `83` status `ready` deltaP `42.2545` edge `0.9476` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `6.9832` n `52` status `ready` deltaP `40.625` edge `0.3111` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.9832` n `52` status `ready` deltaP `40.625` edge `0.3111` maxDD `0.0`
- `news_risk_high->index_24h` score `6.8495` n `83` status `ready` deltaP `47.6845` edge `0.2705` maxDD `-0.075`
- `market_context_high->commodity_24h` score `5.6841` n `149` status `ready` deltaP `33.9136` edge `0.3001` maxDD `-0.8682`
- `news_risk_high->metal_24h` score `5.0998` n `83` status `ready` deltaP `32.6849` edge `0.2525` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.4216` n `52` status `ready` deltaP `32.1047` edge `-0.008` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4216` n `52` status `ready` deltaP `32.1047` edge `-0.008` maxDD `-0.0054`
- `risk_on_high->commodity_4h` score `2.3874` n `52` status `ready` deltaP `29.6435` edge `0.0363` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.3874` n `52` status `ready` deltaP `29.6435` edge `0.0363` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.2871` n `149` status `ready` deltaP `26.1458` edge `0.0581` maxDD `-0.345`
- `market_context_high->fx_24h` score `2.2867` n `149` status `ready` deltaP `29.3298` edge `0.0166` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `0.9827` n `149` status `ready` deltaP `15.0133` edge `0.0195` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.4052` n `83` status `ready` deltaP `12.1933` edge `0.0335` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3594` n `52` status `ready` deltaP `8.0954` edge `0.0112` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3594` n `52` status `ready` deltaP `8.0954` edge `0.0112` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1949` n `52` status `ready` deltaP `7.0129` edge `0.0088` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
