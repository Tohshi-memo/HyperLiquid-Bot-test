# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T16:52:27.602324+00:00`
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

- `news_risk_high->unknown_24h` score `737.9112` n `136` status `ready` deltaP `1.2153` edge `61.4845` maxDD `0.0`
- `market_context_high->unknown_1h` score `208.9028` n `33` status `ready` deltaP `9.6943` edge `17.3486` maxDD `-0.0395`
- `market_context_high->equity_4h` score `4.3022` n `33` status `ready` deltaP `24.1778` edge `0.2308` maxDD `-1.3444`
- `market_context_high->index_4h` score `3.5744` n `33` status `ready` deltaP `38.5856` edge `0.0477` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `3.2186` n `33` status `ready` deltaP `18.4036` edge `0.1998` maxDD `-3.3417`
- `market_context_high->crypto_major_4h` score `2.0136` n `33` status `ready` deltaP `11.6177` edge `0.1808` maxDD `-5.2359`
- `market_context_high->equity_1h` score `1.5827` n `33` status `ready` deltaP `17.9369` edge `0.0526` maxDD `-1.5564`
- `market_context_high->index_1h` score `1.0664` n `33` status `ready` deltaP `14.9066` edge `0.009` maxDD `-0.2275`
- `news_risk_high->index_24h` score `1.0587` n `136` status `ready` deltaP `17.1671` edge `0.0433` maxDD `-2.2287`
- `market_context_high->metal_4h` score `0.8622` n `33` status `ready` deltaP `15.789` edge `0.0265` maxDD `-0.3647`
- `news_risk_high->metal_24h` score `0.5818` n `136` status `ready` deltaP `16.6463` edge `0.123` maxDD `-6.8392`
- `market_context_high->fx_1h` score `0.4678` n `33` status `ready` deltaP `13.1147` edge `0.0082` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.4278` n `33` status `ready` deltaP `11.0915` edge `0.0475` maxDD `-4.8632`
- `news_risk_high->crypto_alt_1h` score `-0.0761` n `139` status `ready` deltaP `4.6224` edge `0.0539` maxDD `-4.2849`
- `news_risk_high->index_1h` score `-0.0875` n `139` status `ready` deltaP `2.7636` edge `0.0033` maxDD `-0.3214`
- `market_context_high->fx_4h` score `-0.1079` n `33` status `ready` deltaP `7.3632` edge `0.0039` maxDD `-0.6787`
- `news_risk_high->equity_4h` score `-0.2089` n `139` status `ready` deltaP `15.5883` edge `0.0396` maxDD `-9.2079`
- `news_risk_high->crypto_alt_24h` score `-0.2789` n `136` status `ready` deltaP `13.7765` edge `0.2801` maxDD `-29.2814`
- `news_risk_high->equity_1h` score `-0.2893` n `139` status `ready` deltaP `2.7636` edge `0.0236` maxDD `-1.957`
- `market_context_high->metal_1h` score `-0.564` n `33` status `ready` deltaP `-5.0672` edge `0.0103` maxDD `-0.215`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
