# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T01:07:25.797467+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9622`

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

- `risk_on_high->commodity_24h` score `7.1002` n `54` status `ready` deltaP `39.3728` edge `0.3292` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.1002` n `54` status `ready` deltaP `39.3728` edge `0.3292` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `1.1309` n `172` status `ready` deltaP `13.1983` edge `0.3467` maxDD `-15.2359`
- `risk_on_high->crypto_major_4h` score `0.3838` n `91` status `ready` deltaP `14.9809` edge `0.1974` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.3838` n `91` status `ready` deltaP `14.9809` edge `0.1974` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.3461` n `172` status `ready` deltaP `3.6207` edge `0.0936` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.0058` n `172` status `ready` deltaP `7.0464` edge `0.1035` maxDD `-7.3329`
- `risk_on_high->index_1h` score `0.0008` n `91` status `ready` deltaP `4.8559` edge `0.0061` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0008` n `91` status `ready` deltaP `4.8559` edge `0.0061` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1698` n `172` status `ready` deltaP `7.1496` edge `0.0054` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2968` n `91` status `ready` deltaP `0.4472` edge `-0.003` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2968` n `91` status `ready` deltaP `0.4472` edge `-0.003` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.342` n `172` status `ready` deltaP `5.2047` edge `0.0084` maxDD `-0.9556`
- `risk_on_high->equity_1h` score `-0.4116` n `91` status `ready` deltaP `9.5585` edge `0.0316` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4116` n `91` status `ready` deltaP `9.5585` edge `0.0316` maxDD `-5.3696`
- `market_context_high->metal_4h` score `-0.4689` n `172` status `ready` deltaP `7.9091` edge `0.0419` maxDD `-1.6961`
- `risk_on_high->metal_1h` score `-0.4696` n `91` status `ready` deltaP `1.2946` edge `0.0043` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4696` n `91` status `ready` deltaP `1.2946` edge `0.0043` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.5125` n `172` status `ready` deltaP `-1.7826` edge `-0.0017` maxDD `-0.503`
- `market_context_high->equity_1h` score `-0.5775` n `172` status `ready` deltaP `9.5904` edge `0.0419` maxDD `-7.3168`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
