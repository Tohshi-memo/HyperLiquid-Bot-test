# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T15:07:31.439144+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11964`

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

- `news_risk_high->unknown_24h` score `755.1168` n `136` status `ready` deltaP `1.2153` edge `62.9183` maxDD `0.0`
- `market_context_high->unknown_1h` score `156.3744` n `40` status `ready` deltaP `10.2246` edge `12.9677` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `58.3353` n `36` status `ready` deltaP `30.2083` edge `4.695` maxDD `-2.4756`
- `market_context_high->equity_24h` score `31.0928` n `36` status `ready` deltaP `35.5903` edge `2.3852` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `30.1867` n `36` status `ready` deltaP `14.9305` edge `2.454` maxDD `-2.7051`
- `market_context_high->index_24h` score `8.6458` n `36` status `ready` deltaP `33.5069` edge `0.5059` maxDD `-0.3705`
- `market_context_high->crypto_alt_4h` score `5.3558` n `40` status `ready` deltaP `20.5183` edge `0.3638` maxDD `-3.3417`
- `market_context_high->metal_24h` score `4.477` n `36` status `ready` deltaP `40.2778` edge `0.1284` maxDD `-0.2401`
- `market_context_high->equity_4h` score `4.0929` n `40` status `ready` deltaP `25.7622` edge `0.2028` maxDD `-1.3444`
- `market_context_high->index_4h` score `3.2816` n `40` status `ready` deltaP `36.0061` edge `0.0405` maxDD `-0.2323`
- `market_context_high->crypto_major_4h` score `2.8577` n `40` status `ready` deltaP `11.1585` edge `0.2542` maxDD `-5.2359`
- `market_context_high->equity_1h` score `1.8497` n `40` status `ready` deltaP `20.2096` edge `0.0597` maxDD `-1.5564`
- `market_context_high->crypto_alt_1h` score `1.7403` n `40` status `ready` deltaP `11.9611` edge `0.1542` maxDD `-5.7799`
- `market_context_high->crypto_major_1h` score `1.5798` n `40` status `ready` deltaP `12.3054` edge `0.1354` maxDD `-4.8632`
- `market_context_high->index_1h` score `1.1158` n `40` status `ready` deltaP `15.3593` edge `0.0101` maxDD `-0.2275`
- `news_risk_high->index_24h` score `0.9771` n `136` status `ready` deltaP `17.1671` edge `0.0365` maxDD `-2.2287`
- `market_context_high->fx_1h` score `0.9377` n `40` status `ready` deltaP `15.8383` edge `0.0082` maxDD `-0.1854`
- `news_risk_high->metal_24h` score `0.4913` n `136` status `ready` deltaP `15.6046` edge `0.1224` maxDD `-6.8392`
- `market_context_high->metal_4h` score `0.4325` n `40` status `ready` deltaP `7.8354` edge `0.0217` maxDD `-0.3647`
- `news_risk_high->index_1h` score `-0.0755` n `139` status `ready` deltaP `2.9133` edge `0.0033` maxDD `-0.3214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
