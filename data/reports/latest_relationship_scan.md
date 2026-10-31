# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T02:37:27.127868+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7100`

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

- `market_context_high->unknown_24h` score `1585.2012` n `134` status `ready` deltaP `-5.5685` edge `132.1802` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `141.5303` n `96` status `ready` deltaP `-2.6073` edge `11.8402` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `40.373` n `134` status `ready` deltaP `0.7212` edge `3.3729` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.7957` n `88` status `ready` deltaP `24.903` edge `0.5497` maxDD `-3.6198`
- `market_context_high->equity_24h` score `7.2179` n `134` status `ready` deltaP `18.9159` edge `0.7511` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.9039` n `134` status `ready` deltaP `37.5207` edge `0.0935` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.4791` n `96` status `ready` deltaP `11.0342` edge `0.1326` maxDD `-3.9659`
- `market_context_high->commodity_4h` score `0.4244` n `134` status `ready` deltaP `15.1574` edge `0.0562` maxDD `-1.0837`
- `market_context_high->metal_1h` score `0.3938` n `134` status `ready` deltaP `11.0533` edge `0.0147` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3256` n `134` status `ready` deltaP `14.9163` edge `0.0319` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.2306` n `134` status `ready` deltaP `4.6318` edge `0.0759` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.0336` n `134` status `ready` deltaP `7.3152` edge `0.0512` maxDD `-5.2213`
- `market_context_high->equity_4h` score `-0.0387` n `134` status `ready` deltaP `1.7815` edge `0.1416` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.1166` n `134` status `ready` deltaP `3.28` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.1834` n `134` status `ready` deltaP `3.1415` edge `0.0152` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.4721` n `134` status `ready` deltaP `0.289` edge `-0.0026` maxDD `-0.4545`
- `market_context_high->metal_24h` score `-0.6499` n `134` status `ready` deltaP `3.9257` edge `0.1552` maxDD `-10.5088`
- `market_context_high->index_1h` score `-0.8186` n `134` status `ready` deltaP `-1.9461` edge `0.0006` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.8253` n `96` status `ready` deltaP `2.2206` edge `-0.0036` maxDD `-1.3981`
- `news_risk_high->commodity_1h` score `-1.0001` n `96` status `ready` deltaP `-9.0631` edge `-0.0014` maxDD `-1.9789`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
