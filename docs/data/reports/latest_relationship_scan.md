# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T13:07:26.700693+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7245`

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

- `market_context_high->unknown_24h` score `2360.5452` n `111` status `ready` deltaP `-7.5028` edge `196.8051` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `93.8431` n `98` status `ready` deltaP `-5.9422` edge `7.8885` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `63.5288` n `111` status `ready` deltaP `1.1632` edge `5.2996` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `17.2515` n `46` status `ready` deltaP `45.6522` edge `1.1384` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.8151` n `111` status `ready` deltaP `27.1303` edge `0.9961` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `4.7292` n `98` status `ready` deltaP `17.571` edge `0.4156` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.6786` n `111` status `ready` deltaP `42.3142` edge `0.1261` maxDD `-0.1315`
- `market_context_high->metal_4h` score `1.0629` n `111` status `ready` deltaP `20.7826` edge `0.0402` maxDD `-0.7323`
- `market_context_high->equity_4h` score `1.0036` n `111` status `ready` deltaP `5.9946` edge `0.183` maxDD `-4.48`
- `news_risk_high->crypto_alt_1h` score `0.8073` n `98` status `ready` deltaP `7.3475` edge `0.1012` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.5876` n `111` status `ready` deltaP `13.2074` edge `0.0163` maxDD `-0.3209`
- `market_context_high->equity_1h` score `0.4628` n `111` status `ready` deltaP `5.5538` edge `0.0891` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.3289` n `111` status `ready` deltaP `8.5613` edge `0.0731` maxDD `-5.2213`
- `market_context_high->fx_1h` score `0.0969` n `111` status `ready` deltaP `6.011` edge `-0.0008` maxDD `-0.1476`
- `market_context_high->metal_24h` score `0.0913` n `111` status `ready` deltaP `13.049` edge `0.1894` maxDD `-10.5088`
- `market_context_high->commodity_4h` score `-0.04` n `111` status `ready` deltaP `9.833` edge `0.0512` maxDD `-1.0837`
- `market_context_high->fx_4h` score `-0.1171` n `111` status `ready` deltaP `4.6227` edge `-0.0008` maxDD `-0.1821`
- `market_context_high->crypto_major_4h` score `-0.341` n `111` status `ready` deltaP `15.4197` edge `0.1428` maxDD `-14.5879`
- `market_context_high->index_1h` score `-0.4368` n `111` status `ready` deltaP `2.7068` edge `0.0014` maxDD `-1.1344`
- `market_context_high->commodity_1h` score `-0.516` n `111` status `ready` deltaP `-0.7607` edge `0.0135` maxDD `-0.4475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
