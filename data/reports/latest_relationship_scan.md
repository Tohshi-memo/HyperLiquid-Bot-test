# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T01:07:26.113887+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12553`

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

- `market_context_high->unknown_24h` score `16580.693` n `59` status `ready` deltaP `12.0616` edge `1381.6492` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `379.5052` n `82` status `ready` deltaP `-5.8493` edge `31.7066` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `18.2469` n `82` status `ready` deltaP `33.1004` edge `1.3487` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `18.0958` n `82` status `ready` deltaP `39.8459` edge `1.3894` maxDD `-9.098`
- `market_context_high->equity_24h` score `10.3766` n `59` status `ready` deltaP `46.0069` edge `0.558` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `10.3484` n `59` status `ready` deltaP `23.055` edge `0.7914` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `6.1194` n `82` status `ready` deltaP `15.5191` edge `0.5845` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.0673` n `82` status `ready` deltaP `41.7852` edge `0.2447` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `5.0438` n `82` status `ready` deltaP `28.5654` edge `0.2753` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.2807` n `59` status `ready` deltaP `42.7083` edge `0.072` maxDD `0.0`
- `market_context_high->index_24h` score `3.9459` n `59` status `ready` deltaP `42.3847` edge `0.0855` maxDD `-0.1391`
- `market_context_high->metal_24h` score `0.3874` n `59` status `ready` deltaP `9.3632` edge `0.107` maxDD `-2.9132`
- `news_risk_high->index_4h` score `0.1333` n `82` status `ready` deltaP `7.7744` edge `0.0281` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.0542` n `53` status `ready` deltaP `5.5248` edge `0.0007` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `0.0542` n `53` status `ready` deltaP `5.5248` edge `0.0007` maxDD `-0.3081`
- `risk_on_high->index_1h` score `-0.0008` n `53` status `ready` deltaP `5.8553` edge `0.0005` maxDD `-0.1711`
- `risk_on_and_context->index_1h` score `-0.0008` n `53` status `ready` deltaP `5.8553` edge `0.0005` maxDD `-0.1711`
- `risk_on_high->crypto_alt_4h` score `-0.0198` n `51` status `ready` deltaP `6.274` edge `0.1231` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `-0.0198` n `51` status `ready` deltaP `6.274` edge `0.1231` maxDD `-6.7304`
- `risk_on_high->fx_1h` score `-0.1006` n `53` status `ready` deltaP `1.4518` edge `0.003` maxDD `-0.0464`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
