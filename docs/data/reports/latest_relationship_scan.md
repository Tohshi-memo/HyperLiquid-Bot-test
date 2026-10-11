# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T11:52:27.546992+00:00`
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

- `market_context_high->unknown_24h` score `300.2321` n `54` status `ready` deltaP `-16.3194` edge `25.1645` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `43.3402` n `85` status `ready` deltaP `-6.8041` edge `3.7151` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.014` n `54` status `ready` deltaP `34.0277` edge `0.5672` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `4.6882` n `54` status `ready` deltaP `-0.2894` edge `0.9178` maxDD `-17.8526`
- `market_context_high->index_24h` score `1.9668` n `54` status `ready` deltaP `28.588` edge `0.1316` maxDD `-0.9357`
- `market_context_high->fx_4h` score `1.2664` n `85` status `ready` deltaP `18.6298` edge `0.0097` maxDD `-0.2692`
- `market_context_high->fx_24h` score `0.552` n `54` status `ready` deltaP `17.4768` edge `0.0209` maxDD `-0.6646`
- `market_context_high->commodity_1h` score `0.3098` n `86` status `ready` deltaP `6.1238` edge `0.0101` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `0.1869` n `85` status `ready` deltaP `9.2414` edge `0.0073` maxDD `-1.6002`
- `market_context_high->fx_1h` score `-0.0466` n `86` status `ready` deltaP `2.7503` edge `0.002` maxDD `-0.271`
- `market_context_high->metal_1h` score `-0.5092` n `86` status `ready` deltaP `-1.1976` edge `0.0018` maxDD `-0.7275`
- `market_context_high->metal_4h` score `-0.5697` n `85` status `ready` deltaP `-2.4839` edge `0.0158` maxDD `-1.1153`
- `market_context_high->crypto_major_1h` score `-0.6562` n `86` status `ready` deltaP `-1.7616` edge `0.0165` maxDD `-3.7778`
- `market_context_high->crypto_alt_1h` score `-1.1074` n `86` status `ready` deltaP `-2.6946` edge `0.0291` maxDD `-4.9401`
- `market_context_high->unknown_1h` score `-1.165` n `86` status `ready` deltaP `-9.1596` edge `-0.0024` maxDD `-1.0231`
- `market_context_high->crypto_major_4h` score `-1.2616` n `85` status `ready` deltaP `-4.7076` edge `0.0802` maxDD `-11.1784`
- `market_context_high->index_4h` score `-1.4251` n `85` status `ready` deltaP `-13.377` edge `-0.0003` maxDD `-1.1242`
- `market_context_high->index_1h` score `-1.6956` n `86` status `ready` deltaP `-7.7252` edge `-0.0036` maxDD `-0.5627`
- `market_context_high->equity_1h` score `-1.7882` n `86` status `ready` deltaP `-7.8993` edge `-0.0094` maxDD `-2.2898`
- `market_context_high->metal_24h` score `-1.8742` n `54` status `ready` deltaP `-14.7569` edge `0.0066` maxDD `-3.5466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
