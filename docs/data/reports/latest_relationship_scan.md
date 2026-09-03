# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-03T10:52:32.650679+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11581`

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

- `risk_on_high->unknown_4h` score `36.262` n `133` status `ready` deltaP `13.4192` edge `2.9942` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `36.262` n `133` status `ready` deltaP `13.4192` edge `2.9942` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `28.6896` n `164` status `ready` deltaP `11.5854` edge `2.3831` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `19.7426` n `133` status `ready` deltaP `2.6889` edge `1.685` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `19.7426` n `133` status `ready` deltaP `2.6889` edge `1.685` maxDD `-1.95`
- `market_context_high->unknown_1h` score `13.6549` n `176` status `ready` deltaP `1.4799` edge `1.1911` maxDD `-2.0446`
- `risk_on_high->equity_24h` score `3.8438` n `107` status `ready` deltaP `19.5353` edge `0.6046` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `3.8438` n `107` status `ready` deltaP `19.5353` edge `0.6046` maxDD `-19.828`
- `market_context_high->equity_24h` score `3.1809` n `136` status `ready` deltaP `20.0163` edge `0.5662` maxDD `-20.7654`
- `risk_on_high->crypto_alt_24h` score `1.8543` n `107` status `ready` deltaP `19.6943` edge `0.7968` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `1.8543` n `107` status `ready` deltaP `19.6943` edge `0.7968` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `1.8253` n `59` status `ready` deltaP `19.6151` edge `0.3967` maxDD `-19.4761`
- `news_risk_high->crypto_major_24h` score `1.1273` n `59` status `ready` deltaP `13.4799` edge `0.4424` maxDD `-30.7329`
- `market_context_high->crypto_alt_24h` score `0.9374` n `136` status `ready` deltaP `16.973` edge `0.7569` maxDD `-46.3234`
- `news_risk_high->equity_24h` score `0.844` n `59` status `ready` deltaP `5.4849` edge `0.2805` maxDD `-15.4056`
- `market_context_high->crypto_major_24h` score `0.5931` n `136` status `ready` deltaP `23.4375` edge `0.8662` maxDD `-61.3797`
- `risk_on_high->crypto_major_24h` score `0.5804` n `107` status `ready` deltaP `19.816` edge `0.8167` maxDD `-56.9519`
- `risk_on_and_context->crypto_major_24h` score `0.5804` n `107` status `ready` deltaP `19.816` edge `0.8167` maxDD `-56.9519`
- `news_risk_high->commodity_4h` score `0.2574` n `67` status `ready` deltaP `5.6425` edge `0.0313` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.079` n `133` status `ready` deltaP `11.6643` edge `0.0036` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
