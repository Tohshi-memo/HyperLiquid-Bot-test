# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T13:07:25.310577+00:00`
- Price records: `672`
- Market context records: `3282`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10506`

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

- `risk_on_high->crypto_major_4h` score `15.8971` n `32` status `ready` deltaP `29.878` edge `1.2378` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8971` n `32` status `ready` deltaP `29.878` edge `1.2378` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `13.842` n `109` status `ready` deltaP `17.7705` edge `2.6403` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `11.9077` n `109` status `ready` deltaP `42.7099` edge `0.7504` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.2119` n `109` status `ready` deltaP `29.9408` edge `0.8235` maxDD `-16.1026`
- `risk_on_high->crypto_alt_4h` score `7.3169` n `32` status `ready` deltaP `10.8994` edge `0.7215` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.3169` n `32` status `ready` deltaP `10.8994` edge `0.7215` maxDD `-11.7537`
- `market_context_high->equity_24h` score `6.7027` n `109` status `ready` deltaP `19.8506` edge `1.5686` maxDD `-53.663`
- `risk_on_high->equity_4h` score `3.7514` n `32` status `ready` deltaP `15.0152` edge `0.4943` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.7514` n `32` status `ready` deltaP `15.0152` edge `0.4943` maxDD `-5.7426`
- `market_context_high->commodity_4h` score `2.6098` n `165` status `ready` deltaP `21.2103` edge `0.1719` maxDD `-3.9989`
- `risk_on_high->crypto_major_1h` score `2.0806` n `32` status `ready` deltaP `7.1669` edge `0.3259` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.0806` n `32` status `ready` deltaP `7.1669` edge `0.3259` maxDD `-5.8885`
- `risk_on_high->index_4h` score `1.13` n `32` status `ready` deltaP `1.1433` edge `0.196` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.13` n `32` status `ready` deltaP `1.1433` edge `0.196` maxDD `-1.7001`
- `market_context_high->crypto_major_24h` score `1.0513` n `109` status `ready` deltaP `18.6895` edge `2.0801` maxDD `-152.2601`
- `risk_on_high->commodity_4h` score `0.2837` n `32` status `ready` deltaP `9.0701` edge `0.0499` maxDD `-3.6044`
- `risk_on_and_context->commodity_4h` score `0.2837` n `32` status `ready` deltaP `9.0701` edge `0.0499` maxDD `-3.6044`
- `risk_on_high->metal_1h` score `0.2214` n `32` status `ready` deltaP `5.9506` edge `0.0572` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.2214` n `32` status `ready` deltaP `5.9506` edge `0.0572` maxDD `-1.4793`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
