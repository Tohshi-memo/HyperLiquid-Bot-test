# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T11:07:26.297470+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `6933`

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

- `market_context_high->unknown_24h` score `137.136` n `57` status `ready` deltaP `-16.7306` edge `11.5759` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `43.1767` n `85` status `ready` deltaP `-7.8282` edge `3.7083` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.1165` n `57` status `ready` deltaP `34.9049` edge `0.5699` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `5.3534` n `57` status `ready` deltaP `3.0245` edge `0.981` maxDD `-17.8526`
- `market_context_high->index_24h` score `1.5992` n `57` status `ready` deltaP `24.6893` edge `0.1248` maxDD `-1.0829`
- `market_context_high->fx_4h` score `1.2676` n `85` status `ready` deltaP `18.6298` edge `0.0098` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.2844` n `85` status `ready` deltaP `10.2655` edge `0.0086` maxDD `-1.6002`
- `market_context_high->fx_24h` score `0.2663` n `57` status `ready` deltaP `14.3915` edge `0.0186` maxDD `-0.7657`
- `market_context_high->commodity_1h` score `0.2211` n `89` status `ready` deltaP `5.2093` edge `0.0088` maxDD `-0.3417`
- `market_context_high->fx_1h` score `0.0675` n `89` status `ready` deltaP `4.1614` edge `0.0021` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `-0.5081` n `89` status `ready` deltaP `-0.037` edge `0.024` maxDD `-3.7778`
- `market_context_high->metal_4h` score `-0.5712` n `85` status `ready` deltaP `-2.4839` edge `0.0156` maxDD `-1.1153`
- `market_context_high->metal_1h` score `-0.5861` n `89` status `ready` deltaP `-2.5836` edge `0.0015` maxDD `-0.7538`
- `market_context_high->crypto_alt_1h` score `-0.8192` n `89` status `ready` deltaP `-4.0806` edge `0.0256` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `-1.3305` n `85` status `ready` deltaP `-5.7317` edge `0.0782` maxDD `-11.1784`
- `market_context_high->index_4h` score `-1.371` n `85` status `ready` deltaP `-12.3529` edge `-0.0002` maxDD `-1.1242`
- `market_context_high->index_1h` score `-1.5719` n `89` status `ready` deltaP `-6.2538` edge `-0.0031` maxDD `-0.5627`
- `market_context_high->metal_24h` score `-1.5989` n `57` status `ready` deltaP `-11.7141` edge `0.0216` maxDD `-3.5466`
- `market_context_high->equity_1h` score `-1.6454` n `89` status `ready` deltaP `-6.3244` edge `-0.008` maxDD `-2.2898`
- `market_context_high->unknown_1h` score `-1.9938` n `89` status `ready` deltaP `-8.1797` edge `-0.078` maxDD `-1.0231`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
