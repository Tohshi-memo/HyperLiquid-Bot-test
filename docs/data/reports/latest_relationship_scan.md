# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T23:37:24.477189+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11748`

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

- `risk_on_high->crypto_alt_24h` score `21.8954` n `54` status `ready` deltaP `46.7592` edge `1.5341` maxDD `-1.3639`
- `risk_on_and_context->crypto_alt_24h` score `21.8954` n `54` status `ready` deltaP `46.7592` edge `1.5341` maxDD `-1.3639`
- `risk_on_high->unknown_4h` score `8.9811` n `84` status `ready` deltaP `30.6257` edge `0.5871` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `8.9811` n `84` status `ready` deltaP `30.6257` edge `0.5871` maxDD `-1.0945`
- `risk_on_high->crypto_major_24h` score `8.8172` n `54` status `ready` deltaP `27.2569` edge `0.661` maxDD `-6.6355`
- `risk_on_and_context->crypto_major_24h` score `8.8172` n `54` status `ready` deltaP `27.2569` edge `0.661` maxDD `-6.6355`
- `risk_on_high->fx_24h` score `6.1535` n `54` status `ready` deltaP `68.9236` edge `0.0533` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.1535` n `54` status `ready` deltaP `68.9236` edge `0.0533` maxDD `0.0`
- `market_context_high->unknown_4h` score `5.1773` n `149` status `ready` deltaP `21.054` edge `0.3381` maxDD `-1.0945`
- `risk_on_high->unknown_1h` score `4.4416` n `92` status `ready` deltaP `11.8915` edge `0.3153` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `4.4416` n `92` status `ready` deltaP `11.8915` edge `0.3153` maxDD `-0.2885`
- `risk_on_high->metal_24h` score `4.2873` n `54` status `ready` deltaP `39.8727` edge `0.1323` maxDD `-0.6006`
- `risk_on_and_context->metal_24h` score `4.2873` n `54` status `ready` deltaP `39.8727` edge `0.1323` maxDD `-0.6006`
- `market_context_high->crypto_major_24h` score `4.2419` n `117` status `ready` deltaP `17.4279` edge `0.4864` maxDD `-17.2607`
- `market_context_high->metal_24h` score `3.9878` n `117` status `ready` deltaP `31.6106` edge `0.2235` maxDD `-3.1535`
- `market_context_high->crypto_alt_24h` score `3.8663` n `117` status `ready` deltaP `18.6966` edge `0.79` maxDD `-27.517`
- `market_context_high->unknown_1h` score `2.944` n `161` status `ready` deltaP `9.8728` edge `0.2204` maxDD `-0.9372`
- `risk_on_high->equity_24h` score `1.7572` n `54` status `ready` deltaP `20.1968` edge `0.0754` maxDD `-2.7556`
- `risk_on_and_context->equity_24h` score `1.7572` n `54` status `ready` deltaP `20.1968` edge `0.0754` maxDD `-2.7556`
- `risk_on_high->index_24h` score `0.9908` n `54` status `ready` deltaP `18.6342` edge `-0.004` maxDD `-0.6798`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
