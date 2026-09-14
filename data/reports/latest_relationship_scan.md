# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T19:07:27.559428+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10692`

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

- `news_risk_high->unknown_4h` score `396.398` n `78` status `ready` deltaP `-22.4554` edge `33.2722` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `23.5879` n `78` status `ready` deltaP `18.9236` edge `1.8395` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.9739` n `78` status `ready` deltaP `46.9017` edge `1.5576` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `16.9917` n `78` status `ready` deltaP `34.1747` edge `1.3352` maxDD `-9.098`
- `news_risk_high->equity_24h` score `13.506` n `78` status `ready` deltaP `40.6517` edge `1.0325` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7159` n `78` status `ready` deltaP `61.9391` edge `0.331` maxDD `-0.075`
- `market_context_high->commodity_24h` score `6.4544` n `120` status `ready` deltaP `36.8056` edge `0.2925` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.4001` n `78` status `ready` deltaP `37.7938` edge `0.3268` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.9396` n `51` status `ready` deltaP `36.8056` edge `0.2496` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9396` n `51` status `ready` deltaP `36.8056` edge `0.2496` maxDD `0.0`
- `risk_on_high->fx_24h` score `4.5969` n `51` status `ready` deltaP `51.5114` edge `0.0439` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.5969` n `51` status `ready` deltaP `51.5114` edge `0.0439` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.2261` n `120` status `ready` deltaP `48.4722` edge `0.0506` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.0401` n `52` status `ready` deltaP `26.4423` edge `0.0287` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.0401` n `52` status `ready` deltaP `26.4423` edge `0.0287` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8404` n `137` status `ready` deltaP `21.8522` edge `0.0495` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8113` n `137` status `ready` deltaP `13.1114` edge `0.0179` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.636` n `78` status `ready` deltaP `15.8966` edge `0.0384` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2959` n `52` status `ready` deltaP `7.4966` edge `0.0099` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2959` n `52` status `ready` deltaP `7.4966` edge `0.0099` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
