# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T01:07:27.278932+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7072`

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

- `market_context_high->unknown_24h` score `1585.2423` n `134` status `ready` deltaP `-6.0894` edge `132.1871` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `149.0384` n `94` status `ready` deltaP `-2.3029` edge `12.4565` maxDD `-0.7027`
- `market_context_high->unknown_4h` score `40.554` n `134` status `ready` deltaP `0.5688` edge `3.389` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.6701` n `82` status `ready` deltaP `23.933` edge `0.5457` maxDD `-3.6198`
- `market_context_high->equity_24h` score `6.9193` n `134` status `ready` deltaP `18.0478` edge `0.732` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.8261` n `134` status `ready` deltaP `36.6527` edge `0.0928` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.5551` n `94` status `ready` deltaP `11.6543` edge `0.1348` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.445` n `134` status `ready` deltaP `15.3099` edge `0.0569` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.3541` n `134` status `ready` deltaP `10.3048` edge `0.0146` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3264` n `134` status `ready` deltaP `14.9163` edge `0.032` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.1671` n `134` status `ready` deltaP `4.033` edge `0.0746` maxDD `-2.3383`
- `market_context_high->equity_4h` score `-0.0103` n `134` status `ready` deltaP `2.0864` edge `0.1432` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.1003` n `134` status `ready` deltaP `3.5794` edge `-0.0009` maxDD `-0.1986`
- `market_context_high->crypto_major_1h` score `-0.1259` n `134` status `ready` deltaP `6.5667` edge `0.0485` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.1427` n `134` status `ready` deltaP `3.4409` edge `0.0166` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4713` n `134` status `ready` deltaP `0.289` edge `-0.0025` maxDD `-0.4545`
- `market_context_high->metal_24h` score `-0.6998` n `134` status `ready` deltaP `3.9257` edge `0.1488` maxDD `-10.5088`
- `news_risk_high->index_1h` score `-0.8061` n `94` status `ready` deltaP `2.4748` edge `-0.0037` maxDD `-1.3981`
- `market_context_high->index_1h` score `-0.8929` n `134` status `ready` deltaP `-2.8443` edge `0.0004` maxDD `-1.1344`
- `news_risk_high->commodity_1h` score `-0.9132` n `94` status `ready` deltaP `-7.9437` edge `0.001` maxDD `-1.8766`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
