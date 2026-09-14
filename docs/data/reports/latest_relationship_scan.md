# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T17:07:28.990652+00:00`
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

- `news_risk_high->unknown_4h` score `395.0608` n `78` status `ready` deltaP `-21.8456` edge `33.1567` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `21.8701` n `78` status `ready` deltaP `46.7281` edge `1.5501` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `17.2737` n `78` status `ready` deltaP `34.1747` edge `1.3587` maxDD `-9.098`
- `news_risk_high->equity_24h` score `13.1885` n `78` status `ready` deltaP `39.2628` edge `1.0153` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7027` n `78` status `ready` deltaP `61.9391` edge `0.3299` maxDD `-0.075`
- `market_context_high->commodity_24h` score `6.8812` n `112` status `ready` deltaP `38.1944` edge `0.3188` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.3557` n `78` status `ready` deltaP `37.7938` edge `0.3231` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.1348` n `51` status `ready` deltaP `38.1944` edge `0.2566` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1348` n `51` status `ready` deltaP `38.1944` edge `0.2566` maxDD `0.0`
- `risk_on_high->fx_24h` score `4.7284` n `51` status `ready` deltaP `52.9003` edge `0.0456` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.7284` n `51` status `ready` deltaP `52.9003` edge `0.0456` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.3098` n `112` status `ready` deltaP `49.504` edge `0.0507` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9531` n `52` status `ready` deltaP `25.985` edge `0.0245` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9531` n `52` status `ready` deltaP `25.985` edge `0.0245` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7534` n `137` status `ready` deltaP `21.3949` edge `0.0453` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.749` n `137` status `ready` deltaP `12.5126` edge `0.0167` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6477` n `78` status `ready` deltaP `15.8966` edge `0.0399` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2336` n `52` status `ready` deltaP `6.8978` edge `0.0087` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2336` n `52` status `ready` deltaP `6.8978` edge `0.0087` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2186` n `137` status `ready` deltaP `10.1589` edge `0.0079` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
