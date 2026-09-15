# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T02:07:26.602105+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10882`

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

- `news_risk_high->unknown_4h` score `400.1432` n `78` status `ready` deltaP `-22.4554` edge `33.5843` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `24.3031` n `78` status `ready` deltaP `18.9236` edge `1.8991` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.0379` n `78` status `ready` deltaP `43.2559` edge `1.5039` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `15.5369` n `78` status `ready` deltaP `32.265` edge `1.2267` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.1726` n `78` status `ready` deltaP `44.1239` edge `1.0649` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.6019` n `78` status `ready` deltaP `60.7238` edge `0.3296` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.4493` n `78` status `ready` deltaP `37.7938` edge `0.3309` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.0799` n `52` status `ready` deltaP `38.8889` edge `0.2474` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.0799` n `52` status `ready` deltaP `38.8889` edge `0.2474` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.7829` n `137` status `ready` deltaP `31.5896` edge `0.2405` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `4.1505` n `52` status `ready` deltaP `46.8616` edge `0.0377` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.1505` n `52` status `ready` deltaP `46.8616` edge `0.0377` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.7535` n `137` status `ready` deltaP `43.6752` edge `0.0432` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9111` n `52` status `ready` deltaP `25.0703` edge `0.0271` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9111` n `52` status `ready` deltaP `25.0703` edge `0.0271` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7115` n `137` status `ready` deltaP `20.4802` edge `0.0479` maxDD `-0.345`
- `news_risk_high->index_4h` score `0.7269` n `78` status `ready` deltaP `17.2686` edge `0.0409` maxDD `-0.6935`
- `market_context_high->commodity_1h` score `0.6591` n `144` status `ready` deltaP `11.5228` edge `0.0158` maxDD `-0.3491`
- `risk_on_high->metal_1h` score `0.23` n `52` status `ready` deltaP `7.7614` edge `0.0083` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.23` n `52` status `ready` deltaP `7.7614` edge `0.0083` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
