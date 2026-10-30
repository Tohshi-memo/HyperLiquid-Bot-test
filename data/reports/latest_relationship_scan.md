# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T09:37:38.114561+00:00`
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

- `market_context_high->unknown_24h` score `1770.2906` n `134` status `ready` deltaP `-2.7908` edge `147.5858` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `316.0288` n `32` status `ready` deltaP `0.3743` edge `26.3458` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `34.7829` n `134` status `ready` deltaP `4.0749` edge `2.8847` maxDD `-0.3966`
- `market_context_high->index_24h` score `3.0858` n `134` status `ready` deltaP `33.3541` edge `0.0531` maxDD `-0.1315`
- `news_risk_high->index_1h` score `1.9355` n `32` status `ready` deltaP `25.131` edge `0.0075` maxDD `-0.0996`
- `market_context_high->equity_24h` score `1.7284` n `134` status `ready` deltaP `16.3117` edge `0.311` maxDD `-14.0571`
- `news_risk_high->crypto_alt_1h` score `0.7736` n `32` status `ready` deltaP `7.7657` edge `0.0891` maxDD `-1.669`
- `market_context_high->metal_1h` score `0.3135` n `134` status `ready` deltaP `9.8557` edge `0.0124` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.2704` n `134` status `ready` deltaP `15.0688` edge `0.0238` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.1649` n `134` status `ready` deltaP `13.0233` edge `0.0488` maxDD `-1.0837`
- `market_context_high->equity_1h` score `0.0855` n `134` status `ready` deltaP `4.1827` edge `0.0668` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `-0.0107` n `134` status `ready` deltaP `6.7164` edge `0.0571` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1135` n `134` status `ready` deltaP `3.4297` edge `-0.0016` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.2996` n `134` status `ready` deltaP `1.9439` edge `0.0135` maxDD `-0.4475`
- `news_risk_high->equity_1h` score `-0.4097` n `32` status `ready` deltaP `4.3226` edge `-0.0221` maxDD `-2.4064`
- `market_context_high->equity_4h` score `-0.4676` n `134` status `ready` deltaP `0.8668` edge `0.0927` maxDD `-6.008`
- `news_risk_high->metal_1h` score `-0.5434` n `32` status `ready` deltaP `-1.4783` edge `-0.0061` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.6081` n `134` status `ready` deltaP `-1.9976` edge `-0.0048` maxDD `-0.4545`
- `news_risk_high->fx_1h` score `-0.7837` n `32` status `ready` deltaP `-7.2979` edge `-0.0004` maxDD `-0.1142`
- `market_context_high->crypto_alt_1h` score `-0.815` n `134` status `ready` deltaP `3.1482` edge `0.061` maxDD `-8.251`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
