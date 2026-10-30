# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T09:52:28.692193+00:00`
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

- `market_context_high->unknown_24h` score `1773.6806` n `134` status `ready` deltaP `-2.7908` edge `147.8683` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `304.5595` n `33` status `ready` deltaP `0.6034` edge `25.3885` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `34.7421` n `134` status `ready` deltaP `4.0749` edge `2.8813` maxDD `-0.3966`
- `market_context_high->index_24h` score `3.0942` n `134` status `ready` deltaP `33.3541` edge `0.0538` maxDD `-0.1315`
- `market_context_high->equity_24h` score `1.7848` n `134` status `ready` deltaP `16.3117` edge `0.3157` maxDD `-14.0571`
- `news_risk_high->index_1h` score `1.7351` n `33` status `ready` deltaP `22.9133` edge `0.006` maxDD `-0.1333`
- `news_risk_high->crypto_alt_1h` score `0.8521` n `33` status `ready` deltaP `9.1862` edge `0.0897` maxDD `-1.669`
- `market_context_high->metal_1h` score `0.3213` n `134` status `ready` deltaP `10.0054` edge `0.0124` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.2806` n `134` status `ready` deltaP `15.2212` edge `0.0241` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.1455` n `134` status `ready` deltaP `12.8708` edge `0.0482` maxDD `-1.0837`
- `market_context_high->equity_1h` score `0.0915` n `134` status `ready` deltaP `4.1827` edge `0.0673` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.0085` n `134` status `ready` deltaP `6.8661` edge `0.0577` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1135` n `134` status `ready` deltaP `3.4297` edge `-0.0016` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.314` n `134` status `ready` deltaP `1.7942` edge `0.0133` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.4715` n `134` status `ready` deltaP `0.8668` edge `0.0922` maxDD `-6.008`
- `news_risk_high->equity_1h` score `-0.6028` n `33` status `ready` deltaP `2.7128` edge `-0.0337` maxDD `-2.6`
- `news_risk_high->metal_1h` score `-0.6134` n `33` status `ready` deltaP `-2.7491` edge `-0.0066` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.6161` n `134` status `ready` deltaP `-2.15` edge `-0.0048` maxDD `-0.4545`
- `news_risk_high->fx_1h` score `-0.6889` n `33` status `ready` deltaP `-5.5934` edge `0.0004` maxDD `-0.1142`
- `market_context_high->crypto_alt_1h` score `-0.815` n `134` status `ready` deltaP `3.1482` edge `0.061` maxDD `-8.251`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
