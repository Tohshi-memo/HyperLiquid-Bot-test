# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T14:37:31.062654+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8252`

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

- `market_context_high->commodity_24h` score `1.9749` n `76` status `ready` deltaP `18.2585` edge `0.128` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.5473` n `43` status `ready` deltaP `14.1348` edge `0.0092` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.5473` n `43` status `ready` deltaP `14.1348` edge `0.0092` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.4512` n `43` status `ready` deltaP `10.2368` edge `-0.0003` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.4512` n `43` status `ready` deltaP `10.2368` edge `-0.0003` maxDD `-0.4273`
- `market_context_high->crypto_major_4h` score `0.1329` n `77` status `ready` deltaP `3.3873` edge `0.3349` maxDD `-15.2359`
- `risk_on_high->commodity_24h` score `0.1241` n `43` status `ready` deltaP `13.638` edge `-0.0008` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.1241` n `43` status `ready` deltaP `13.638` edge `-0.0008` maxDD `-1.7154`
- `risk_on_high->fx_4h` score `-0.0933` n `43` status `ready` deltaP `1.8498` edge `0.0063` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.0933` n `43` status `ready` deltaP `1.8498` edge `0.0063` maxDD `-0.1126`
- `market_context_high->crypto_major_24h` score `-0.1282` n `76` status `ready` deltaP `-1.2062` edge `0.6013` maxDD `-35.1086`
- `risk_on_high->fx_1h` score `-0.2427` n `43` status `ready` deltaP `0.6381` edge `-0.0007` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2427` n `43` status `ready` deltaP `0.6381` edge `-0.0007` maxDD `-0.1065`
- `market_context_high->crypto_major_1h` score `-0.2919` n `83` status `ready` deltaP `1.2229` edge `0.0561` maxDD `-4.8007`
- `market_context_high->metal_1h` score `-0.4798` n `83` status `ready` deltaP `-3.7822` edge `0.0007` maxDD `-0.6265`
- `market_context_high->fx_4h` score `-0.5313` n `77` status `ready` deltaP `-1.2611` edge `0.004` maxDD `-0.7635`
- `market_context_high->metal_4h` score `-0.5936` n `77` status `ready` deltaP `-0.5029` edge `0.0495` maxDD `-0.7797`
- `risk_on_high->index_4h` score `-0.5968` n `43` status `ready` deltaP `5.0204` edge `0.0035` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.5968` n `43` status `ready` deltaP `5.0204` edge `0.0035` maxDD `-0.9359`
- `market_context_high->fx_1h` score `-0.6711` n `83` status `ready` deltaP `-4.7416` edge `-0.0018` maxDD `-0.544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
