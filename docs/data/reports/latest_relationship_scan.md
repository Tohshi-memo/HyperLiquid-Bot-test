# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T11:37:25.312802+00:00`
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

- `market_context_high->unknown_24h` score `243.9736` n `55` status `ready` deltaP `-15.9154` edge `20.4736` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `43.2475` n `85` status `ready` deltaP `-7.8282` edge `3.7142` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.049` n `55` status `ready` deltaP `34.3308` edge `0.5681` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `4.8865` n `55` status `ready` deltaP `0.8554` edge `0.9356` maxDD `-17.8526`
- `market_context_high->index_24h` score `1.8404` n `55` status `ready` deltaP `27.2412` edge `0.1292` maxDD `-0.9887`
- `market_context_high->fx_4h` score `1.2664` n `85` status `ready` deltaP `18.6298` edge `0.0097` maxDD `-0.2692`
- `market_context_high->fx_24h` score `0.4554` n `55` status `ready` deltaP `16.4046` edge `0.0202` maxDD `-0.6944`
- `market_context_high->commodity_4h` score `0.2808` n `85` status `ready` deltaP `10.2655` edge `0.0083` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.2446` n `87` status `ready` deltaP `5.4288` edge `0.0093` maxDD `-0.3417`
- `market_context_high->fx_1h` score `-0.0081` n `87` status `ready` deltaP `3.2315` edge `0.002` maxDD `-0.271`
- `market_context_high->metal_1h` score `-0.5336` n `87` status `ready` deltaP `-1.6226` edge `0.0016` maxDD `-0.7358`
- `market_context_high->metal_4h` score `-0.5704` n `85` status `ready` deltaP `-2.4839` edge `0.0157` maxDD `-1.1153`
- `market_context_high->crypto_major_1h` score `-0.6101` n `87` status `ready` deltaP `-1.1735` edge `0.0185` maxDD `-3.7778`
- `market_context_high->crypto_alt_1h` score `-1.1642` n `87` status `ready` deltaP `-3.1196` edge `0.0272` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `-1.3336` n `85` status `ready` deltaP `-5.7317` edge `0.0778` maxDD `-11.1784`
- `market_context_high->index_4h` score `-1.3718` n `85` status `ready` deltaP `-12.3529` edge `-0.0003` maxDD `-1.1242`
- `market_context_high->unknown_1h` score `-1.4671` n `87` status `ready` deltaP `-8.8254` edge `-0.0298` maxDD `-1.0231`
- `market_context_high->index_1h` score `-1.6528` n `87` status `ready` deltaP `-7.22` edge `-0.0034` maxDD `-0.5627`
- `market_context_high->equity_1h` score `-1.734` n `87` status `ready` deltaP `-7.3112` edge `-0.0088` maxDD `-2.2898`
- `market_context_high->metal_24h` score `-1.7735` n `55` status `ready` deltaP `-13.6458` edge `0.0121` maxDD `-3.5466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
