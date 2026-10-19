# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T14:07:33.045295+00:00`
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

- `market_context_high->commodity_24h` score `1.9159` n `76` status `ready` deltaP `17.9107` edge `0.1254` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.5413` n `43` status `ready` deltaP `14.1348` edge `0.0087` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.5413` n `43` status `ready` deltaP `14.1348` edge `0.0087` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.4512` n `43` status `ready` deltaP `10.2368` edge `-0.0003` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.4512` n `43` status `ready` deltaP `10.2368` edge `-0.0003` maxDD `-0.4273`
- `market_context_high->crypto_major_4h` score `0.1477` n `77` status `ready` deltaP `3.3873` edge `0.3368` maxDD `-15.2359`
- `risk_on_high->commodity_24h` score `0.0651` n `43` status `ready` deltaP `13.2902` edge `-0.0034` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.0651` n `43` status `ready` deltaP `13.2902` edge `-0.0034` maxDD `-1.7154`
- `market_context_high->crypto_major_1h` score `0.0299` n `81` status `ready` deltaP `2.5616` edge `0.0749` maxDD `-3.7178`
- `market_context_high->crypto_major_24h` score `-0.0532` n `76` status `ready` deltaP `-0.8589` edge `0.6086` maxDD `-35.1086`
- `risk_on_high->fx_4h` score `-0.0665` n `43` status `ready` deltaP `2.1552` edge `0.0065` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0665` n `43` status `ready` deltaP `2.1552` edge `0.0065` maxDD `-0.1126`
- `risk_on_high->fx_1h` score `-0.2427` n `43` status `ready` deltaP `0.6381` edge `-0.0007` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2427` n `43` status `ready` deltaP `0.6381` edge `-0.0007` maxDD `-0.1065`
- `market_context_high->metal_1h` score `-0.3877` n `81` status `ready` deltaP `-2.7113` edge `0.0034` maxDD `-0.4687`
- `market_context_high->fx_4h` score `-0.5139` n `77` status `ready` deltaP `-0.9557` edge `0.0042` maxDD `-0.7635`
- `risk_on_high->index_4h` score `-0.5687` n `43` status `ready` deltaP `5.3257` edge `0.0038` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.5687` n `43` status `ready` deltaP `5.3257` edge `0.0038` maxDD `-0.9359`
- `market_context_high->metal_4h` score `-0.5959` n `77` status `ready` deltaP `-0.5029` edge `0.0492` maxDD `-0.7797`
- `market_context_high->fx_1h` score `-0.6093` n `81` status `ready` deltaP `-3.6111` edge `-0.0015` maxDD `-0.537`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
