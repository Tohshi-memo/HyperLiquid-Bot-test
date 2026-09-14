# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T19:52:31.255487+00:00`
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

- `news_risk_high->unknown_4h` score `396.7664` n `78` status `ready` deltaP `-22.4554` edge `33.3029` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `23.9119` n `78` status `ready` deltaP `18.9236` edge `1.8665` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.9529` n `78` status `ready` deltaP `46.7281` edge `1.557` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `16.8446` n `78` status `ready` deltaP `34.0011` edge `1.3241` maxDD `-9.098`
- `news_risk_high->equity_24h` score `13.6305` n `78` status `ready` deltaP `41.1725` edge `1.0394` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7219` n `78` status `ready` deltaP `61.9391` edge `0.3315` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4181` n `78` status `ready` deltaP `37.7938` edge `0.3283` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `6.4159` n `120` status `ready` deltaP `36.4583` edge `0.2916` maxDD `0.0`
- `risk_on_high->commodity_24h` score `5.9011` n `51` status `ready` deltaP `36.4583` edge `0.2487` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.9011` n `51` status `ready` deltaP `36.4583` edge `0.2487` maxDD `0.0`
- `risk_on_high->fx_24h` score `4.5468` n `51` status `ready` deltaP `50.9906` edge `0.0432` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.5468` n `51` status `ready` deltaP `50.9906` edge `0.0432` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.176` n `120` status `ready` deltaP `47.9514` edge `0.0499` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.0911` n `52` status `ready` deltaP `26.8996` edge `0.0299` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.0911` n `52` status `ready` deltaP `26.8996` edge `0.0299` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8914` n `137` status `ready` deltaP `22.3095` edge `0.0507` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7958` n `137` status `ready` deltaP `12.9617` edge `0.0176` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6258` n `78` status `ready` deltaP `15.7442` edge `0.0381` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2803` n `52` status `ready` deltaP `7.3469` edge `0.0096` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2803` n `52` status `ready` deltaP `7.3469` edge `0.0096` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
