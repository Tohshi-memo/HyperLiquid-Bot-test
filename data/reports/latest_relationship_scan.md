# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T17:07:25.221323+00:00`
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

- `news_risk_high->unknown_24h` score `737.6904` n `136` status `ready` deltaP `1.2153` edge `61.4661` maxDD `0.0`
- `market_context_high->unknown_1h` score `214.9204` n `32` status `ready` deltaP `9.5996` edge `17.8507` maxDD `-0.0395`
- `market_context_high->equity_4h` score `4.3543` n `32` status `ready` deltaP `23.7043` edge `0.2383` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `3.6044` n `32` status `ready` deltaP `20.9604` edge `0.2149` maxDD `-3.3417`
- `market_context_high->index_4h` score `3.5958` n `32` status `ready` deltaP `38.6433` edge `0.0491` maxDD `-0.2323`
- `market_context_high->crypto_major_4h` score `2.4255` n `32` status `ready` deltaP `13.7957` edge `0.2006` maxDD `-5.2359`
- `market_context_high->equity_1h` score `1.8481` n `32` status `ready` deltaP `20.2096` edge `0.0554` maxDD `-1.5564`
- `market_context_high->index_1h` score `1.2478` n `32` status `ready` deltaP `17.0846` edge `0.0096` maxDD `-0.2275`
- `news_risk_high->index_24h` score `1.0846` n `136` status `ready` deltaP `17.3407` edge `0.0443` maxDD `-2.2287`
- `market_context_high->metal_4h` score `0.9946` n `32` status `ready` deltaP `17.5305` edge `0.0277` maxDD `-0.3647`
- `market_context_high->crypto_major_1h` score `0.7117` n `32` status `ready` deltaP `13.0801` edge `0.0579` maxDD `-4.8632`
- `news_risk_high->metal_24h` score `0.5818` n `136` status `ready` deltaP `16.6463` edge `0.123` maxDD `-6.8392`
- `market_context_high->fx_1h` score `0.5567` n `32` status `ready` deltaP `14.7642` edge `0.0086` maxDD `-0.1854`
- `news_risk_high->index_1h` score `-0.0875` n `139` status `ready` deltaP `2.7636` edge `0.0033` maxDD `-0.3214`
- `news_risk_high->crypto_alt_1h` score `-0.0905` n `139` status `ready` deltaP `4.4727` edge `0.0537` maxDD `-4.2849`
- `news_risk_high->crypto_alt_24h` score `-0.163` n `136` status `ready` deltaP `13.9501` edge `0.2886` maxDD `-29.2814`
- `market_context_high->fx_4h` score `-0.2038` n `32` status `ready` deltaP `5.564` edge `0.0036` maxDD `-0.6787`
- `news_risk_high->equity_4h` score `-0.2089` n `139` status `ready` deltaP `15.5883` edge `0.0396` maxDD `-9.2079`
- `news_risk_high->equity_1h` score `-0.2893` n `139` status `ready` deltaP `2.7636` edge `0.0236` maxDD `-1.957`
- `market_context_high->metal_1h` score `-0.4703` n `32` status `ready` deltaP `-3.9858` edge `0.0109` maxDD `-0.215`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
