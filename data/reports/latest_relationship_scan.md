# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T16:52:33.058193+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7080`

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

- `market_context_high->unknown_24h` score `1606.8751` n `134` status `ready` deltaP `-4.1797` edge `133.9771` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `155.9154` n `61` status `ready` deltaP `-1.1388` edge `13.0131` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `31.551` n `134` status `ready` deltaP `1.0261` edge `2.6357` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.3003` n `49` status `ready` deltaP `23.1645` edge `0.4936` maxDD `-1.5072`
- `market_context_high->equity_24h` score `4.2041` n `134` status `ready` deltaP `16.6589` edge `0.515` maxDD `-14.0571`
- `market_context_high->index_24h` score `3.4894` n `134` status `ready` deltaP `35.2638` edge `0.074` maxDD `-0.1315`
- `news_risk_high->crypto_alt_1h` score `1.2559` n `61` status `ready` deltaP `8.7391` edge `0.1175` maxDD `-3.3547`
- `news_risk_high->commodity_4h` score `0.6299` n `49` status `ready` deltaP `5.3478` edge `0.0506` maxDD `-0.7008`
- `market_context_high->metal_1h` score `0.3953` n `134` status `ready` deltaP `11.0533` edge `0.0149` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3811` n `134` status `ready` deltaP `15.9834` edge `0.0319` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.3565` n `134` status `ready` deltaP `5.53` edge `0.0804` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.2123` n `134` status `ready` deltaP `13.4806` edge `0.0497` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.0995` n `134` status `ready` deltaP `7.7643` edge `0.0593` maxDD `-5.2213`
- `market_context_high->equity_4h` score `0.0188` n `134` status `ready` deltaP `3.3059` edge `0.1388` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.101` n `134` status `ready` deltaP `3.5794` edge `-0.001` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3415` n `134` status `ready` deltaP `1.4948` edge `0.013` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.503` n `134` status `ready` deltaP `-0.3208` edge `-0.0025` maxDD `-0.4545`
- `news_risk_high->commodity_1h` score `-0.6323` n `61` status `ready` deltaP `-3.3499` edge `0.0199` maxDD `-0.6872`
- `news_risk_high->index_1h` score `-0.6848` n `61` status `ready` deltaP `-1.1264` edge `-0.0074` maxDD `-0.8305`
- `market_context_high->index_1h` score `-0.8162` n `134` status `ready` deltaP `-1.9461` edge `0.0008` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
