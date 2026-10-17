# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T21:22:29.099533+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9616`

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

- `risk_on_high->commodity_24h` score `7.0659` n `54` status `ready` deltaP `39.1986` edge `0.3275` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0659` n `54` status `ready` deltaP `39.1986` edge `0.3275` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `1.0635` n `174` status `ready` deltaP `12.5368` edge `0.3344` maxDD `-14.6817`
- `risk_on_high->crypto_major_4h` score `0.4851` n `90` status `ready` deltaP `15.6402` edge `0.1949` maxDD `-10.6246`
- `risk_on_and_context->crypto_major_4h` score `0.4851` n `90` status `ready` deltaP `15.6402` edge `0.1949` maxDD `-10.6246`
- `market_context_high->crypto_major_1h` score `0.446` n `175` status `ready` deltaP `5.0342` edge `0.0925` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.0953` n `175` status `ready` deltaP `8.0008` edge `0.1046` maxDD `-7.3329`
- `risk_on_high->index_1h` score `0.0308` n `91` status `ready` deltaP `5.3064` edge `0.0056` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0308` n `91` status `ready` deltaP `5.3064` edge `0.0056` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1956` n `175` status `ready` deltaP `6.713` edge `0.005` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.2852` n `175` status `ready` deltaP `6.3413` edge `0.0081` maxDD `-0.9556`
- `risk_on_high->fx_1h` score `-0.289` n `91` status `ready` deltaP `0.5973` edge `-0.003` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.289` n `91` status `ready` deltaP `0.5973` edge `-0.003` maxDD `-0.376`
- `market_context_high->equity_1h` score `-0.3548` n `175` status `ready` deltaP `10.4667` edge `0.0387` maxDD `-7.3168`
- `risk_on_high->equity_1h` score `-0.4091` n `91` status `ready` deltaP `10.1591` edge `0.0278` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4091` n `91` status `ready` deltaP `10.1591` edge `0.0278` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.4564` n `91` status `ready` deltaP `1.594` edge `0.004` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4564` n `91` status `ready` deltaP `1.594` edge `0.004` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.573` n `174` status `ready` deltaP `6.1922` edge `0.0405` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.702` n `91` status `ready` deltaP `0.199` edge `0.0006` maxDD `-4.6876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
