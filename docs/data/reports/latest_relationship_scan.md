# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T13:52:39.317082+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8542`

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

- `market_context_high->commodity_24h` score `1.8876` n `76` status `ready` deltaP `17.7368` edge `0.1242` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.5341` n `43` status `ready` deltaP `14.1348` edge `0.0081` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.5341` n `43` status `ready` deltaP `14.1348` edge `0.0081` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.4512` n `43` status `ready` deltaP `10.2368` edge `-0.0003` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.4512` n `43` status `ready` deltaP `10.2368` edge `-0.0003` maxDD `-0.4273`
- `market_context_high->crypto_major_1h` score `0.1698` n `80` status `ready` deltaP `3.256` edge `0.0882` maxDD `-3.7178`
- `market_context_high->crypto_major_4h` score `0.1461` n `77` status `ready` deltaP `3.3873` edge `0.3366` maxDD `-15.2359`
- `risk_on_high->commodity_24h` score `0.0368` n `43` status `ready` deltaP `13.1163` edge `-0.0046` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.0368` n `43` status `ready` deltaP `13.1163` edge `-0.0046` maxDD `-1.7154`
- `market_context_high->crypto_major_24h` score `-0.0122` n `76` status `ready` deltaP `-0.6853` edge `0.6127` maxDD `-35.1086`
- `risk_on_high->fx_4h` score `-0.0531` n `43` status `ready` deltaP `2.3078` edge `0.0066` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0531` n `43` status `ready` deltaP `2.3078` edge `0.0066` maxDD `-0.1126`
- `risk_on_high->fx_1h` score `-0.2427` n `43` status `ready` deltaP `0.6381` edge `-0.0007` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2427` n `43` status `ready` deltaP `0.6381` edge `-0.0007` maxDD `-0.1065`
- `market_context_high->metal_1h` score `-0.3471` n `80` status `ready` deltaP `-2.1557` edge `0.0049` maxDD `-0.4687`
- `market_context_high->fx_4h` score `-0.5052` n `77` status `ready` deltaP `-0.8031` edge `0.0043` maxDD `-0.7635`
- `risk_on_high->index_4h` score `-0.5687` n `43` status `ready` deltaP `5.3257` edge `0.0038` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.5687` n `43` status `ready` deltaP `5.3257` edge `0.0038` maxDD `-0.9359`
- `market_context_high->metal_4h` score `-0.5975` n `77` status `ready` deltaP `-0.5029` edge `0.049` maxDD `-0.7797`
- `market_context_high->fx_1h` score `-0.6454` n `80` status `ready` deltaP `-4.2747` edge `-0.0017` maxDD `-0.537`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
