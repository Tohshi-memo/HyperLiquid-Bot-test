# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T12:52:29.082187+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `7629`

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

- `market_context_high->unknown_24h` score `547.9601` n `50` status `ready` deltaP `-14.4444` edge `45.796` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `45.6784` n `82` status `ready` deltaP `-7.6219` edge `3.9154` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.9565` n `50` status `ready` deltaP `32.6944` edge `0.5713` maxDD `-1.0977`
- `market_context_high->index_24h` score `3.8641` n `50` status `ready` deltaP `33.9931` edge `0.1445` maxDD `-0.5956`
- `market_context_high->crypto_major_24h` score `3.8545` n `50` status `ready` deltaP `-5.3264` edge `0.8445` maxDD `-17.8526`
- `market_context_high->fx_24h` score `1.5003` n `50` status `ready` deltaP `22.2639` edge `0.0247` maxDD `-0.5146`
- `market_context_high->fx_4h` score `1.1847` n `82` status `ready` deltaP `17.6829` edge `0.0092` maxDD `-0.2692`
- `market_context_high->commodity_1h` score `0.2774` n `85` status `ready` deltaP `5.8084` edge `0.0095` maxDD `-0.3417`
- `market_context_high->commodity_4h` score `0.1377` n `82` status `ready` deltaP `8.5366` edge `0.0079` maxDD `-1.6002`
- `market_context_high->fx_1h` score `-0.179` n `85` status `ready` deltaP `1.2311` edge `0.0011` maxDD `-0.271`
- `market_context_high->metal_1h` score `-0.3231` n `85` status `ready` deltaP `2.3212` edge `0.0022` maxDD `-0.7275`
- `market_context_high->metal_4h` score `-0.489` n `82` status `ready` deltaP `-1.0671` edge `0.0167` maxDD `-1.1153`
- `market_context_high->crypto_alt_1h` score `-0.6795` n `85` status `ready` deltaP `0.8242` edge `0.0413` maxDD `-4.9401`
- `market_context_high->unknown_1h` score `-0.7497` n `85` status `ready` deltaP `-7.448` edge `0.0208` maxDD `-1.0231`
- `market_context_high->crypto_major_1h` score `-0.9372` n `85` status `ready` deltaP `-1.3367` edge `0.0197` maxDD `-3.7778`
- `market_context_high->index_1h` score `-1.137` n `85` status `ready` deltaP `-8.3956` edge `-0.0036` maxDD `-0.5627`
- `market_context_high->crypto_major_4h` score `-1.2298` n `82` status `ready` deltaP `-4.7256` edge `0.0844` maxDD `-11.1784`
- `market_context_high->index_4h` score `-1.3709` n `82` status `ready` deltaP `-13.567` edge `-0.0005` maxDD `-1.1178`
- `market_context_high->crypto_alt_4h` score `-1.799` n `82` status `ready` deltaP `-5.6402` edge `0.0628` maxDD `-13.8008`
- `market_context_high->equity_1h` score `-1.8148` n `85` status `ready` deltaP `-8.5012` edge `-0.0076` maxDD `-2.2898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
