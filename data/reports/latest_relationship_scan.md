# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T00:22:26.678818+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7058`

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

- `market_context_high->unknown_24h` score `1585.5495` n `134` status `ready` deltaP `-6.0894` edge `132.2127` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `162.064` n `91` status `ready` deltaP `0.0888` edge `13.5173` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `40.3966` n `134` status `ready` deltaP `0.4163` edge `3.3769` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.1473` n `79` status `ready` deltaP `23.0531` edge `0.508` maxDD `-3.6198`
- `market_context_high->equity_24h` score `6.7444` n `134` status `ready` deltaP `17.527` edge `0.7209` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.7748` n `134` status `ready` deltaP `36.1318` edge `0.092` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.4108` n `91` status `ready` deltaP `10.2866` edge `0.1319` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.4546` n `134` status `ready` deltaP `15.3099` edge `0.0577` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.3541` n `134` status `ready` deltaP `10.3048` edge `0.0146` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.328` n `134` status `ready` deltaP `14.9163` edge `0.0322` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.1779` n `134` status `ready` deltaP `4.1827` edge `0.0745` maxDD `-2.3383`
- `market_context_high->equity_4h` score `-0.0095` n `134` status `ready` deltaP `2.0864` edge `0.1433` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.0925` n `134` status `ready` deltaP `3.7291` edge `-0.0009` maxDD `-0.1986`
- `market_context_high->crypto_major_1h` score `-0.1283` n `134` status `ready` deltaP `6.5667` edge `0.0483` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.1427` n `134` status `ready` deltaP `3.4409` edge `0.0166` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.48` n `134` status `ready` deltaP `0.1365` edge `-0.0026` maxDD `-0.4545`
- `market_context_high->metal_24h` score `-0.7303` n `134` status `ready` deltaP `3.9257` edge `0.1449` maxDD `-10.5088`
- `news_risk_high->commodity_1h` score `-0.8073` n `91` status `ready` deltaP `-6.6461` edge `0.0032` maxDD `-1.658`
- `market_context_high->index_1h` score `-0.8809` n `134` status `ready` deltaP `-2.6946` edge `0.0004` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.9168` n `91` status `ready` deltaP `1.1516` edge `-0.0041` maxDD `-1.3981`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
