# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T14:07:27.706320+00:00`
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

- `news_risk_high->unknown_24h` score `770.688` n `136` status `ready` deltaP `1.2153` edge `64.2159` maxDD `0.0`
- `market_context_high->unknown_1h` score `156.4008` n `40` status `ready` deltaP `10.3743` edge `12.9689` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `57.7453` n `36` status `ready` deltaP `29.6875` edge `4.6493` maxDD `-2.4756`
- `market_context_high->equity_24h` score `30.8984` n `36` status `ready` deltaP `35.5903` edge `2.369` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `29.5066` n `36` status `ready` deltaP `14.4097` edge `2.4008` maxDD `-2.7051`
- `market_context_high->index_24h` score `8.5621` n `36` status `ready` deltaP `32.9861` edge `0.5024` maxDD `-0.3705`
- `market_context_high->crypto_alt_4h` score `5.0586` n `40` status `ready` deltaP `19.9085` edge `0.3431` maxDD `-3.3417`
- `market_context_high->metal_24h` score `4.4305` n `36` status `ready` deltaP `39.757` edge `0.128` maxDD `-0.2401`
- `market_context_high->equity_4h` score `4.0189` n `40` status `ready` deltaP `25.1524` edge `0.2007` maxDD `-1.3444`
- `market_context_high->index_4h` score `3.2281` n `40` status `ready` deltaP `35.3963` edge `0.0401` maxDD `-0.2323`
- `market_context_high->crypto_major_4h` score `2.6469` n `40` status `ready` deltaP `10.5488` edge `0.2407` maxDD `-5.2359`
- `market_context_high->equity_1h` score `1.7886` n `40` status `ready` deltaP `19.6108` edge `0.0586` maxDD `-1.5564`
- `market_context_high->crypto_alt_1h` score `1.6372` n `40` status `ready` deltaP `11.512` edge `0.1486` maxDD `-5.7799`
- `market_context_high->crypto_major_1h` score `1.4682` n `40` status `ready` deltaP `11.7066` edge `0.1301` maxDD `-4.8632`
- `market_context_high->index_1h` score `1.0787` n `40` status `ready` deltaP `14.9102` edge `0.01` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.9257` n `40` status `ready` deltaP `15.6886` edge `0.0082` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.8934` n `136` status `ready` deltaP `16.6463` edge `0.033` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.4448` n `136` status `ready` deltaP `15.0838` edge `0.122` maxDD `-6.8392`
- `market_context_high->metal_4h` score `0.4325` n `40` status `ready` deltaP `7.8354` edge `0.0217` maxDD `-0.3647`
- `news_risk_high->index_1h` score `-0.1127` n `139` status `ready` deltaP `2.4642` edge `0.0032` maxDD `-0.3214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
