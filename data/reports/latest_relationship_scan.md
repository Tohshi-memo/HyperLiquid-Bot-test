# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T16:37:35.998352+00:00`
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

- `news_risk_high->unknown_24h` score `740.2368` n `136` status `ready` deltaP `1.2153` edge `61.6783` maxDD `0.0`
- `market_context_high->unknown_1h` score `202.9747` n `34` status `ready` deltaP `9.7834` edge `16.854` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `57.9146` n `30` status `ready` deltaP `30.6945` edge `4.6567` maxDD `-2.4756`
- `market_context_high->equity_24h` score `31.1372` n `30` status `ready` deltaP `35.0348` edge `2.3926` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `26.5476` n `30` status `ready` deltaP `15.4167` edge `2.1475` maxDD `-2.7051`
- `market_context_high->index_24h` score `8.6421` n `30` status `ready` deltaP `32.9514` edge `0.5093` maxDD `-0.3705`
- `market_context_high->equity_4h` score `4.2488` n `34` status `ready` deltaP `24.4709` edge `0.2244` maxDD `-1.3444`
- `market_context_high->metal_24h` score `4.2372` n `30` status `ready` deltaP `37.4306` edge `0.1274` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.5501` n `34` status `ready` deltaP `38.5222` edge `0.0461` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `3.2132` n `34` status `ready` deltaP `18.7858` edge `0.1968` maxDD `-3.3417`
- `market_context_high->crypto_major_4h` score `1.7152` n `34` status `ready` deltaP `9.5678` edge `0.1696` maxDD `-5.2359`
- `market_context_high->equity_1h` score `1.6301` n `34` status `ready` deltaP `18.739` edge `0.0512` maxDD `-1.5564`
- `news_risk_high->index_24h` score `1.0467` n `136` status `ready` deltaP `17.1671` edge `0.0423` maxDD `-2.2287`
- `market_context_high->index_1h` score `0.8988` n `34` status `ready` deltaP `12.8567` edge `0.0087` maxDD `-0.2275`
- `market_context_high->metal_4h` score `0.734` n `34` status `ready` deltaP `14.1589` edge `0.0251` maxDD `-0.3647`
- `news_risk_high->metal_24h` score `0.583` n `136` status `ready` deltaP `16.6463` edge `0.1231` maxDD `-6.8392`
- `market_context_high->fx_1h` score `0.3821` n `34` status `ready` deltaP `11.571` edge `0.0075` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.2145` n `34` status `ready` deltaP `9.3695` edge `0.0412` maxDD `-4.8632`
- `news_risk_high->crypto_alt_1h` score `-0.0701` n `139` status `ready` deltaP `4.6224` edge `0.0544` maxDD `-4.2849`
- `news_risk_high->index_1h` score `-0.0875` n `139` status `ready` deltaP `2.7636` edge `0.0033` maxDD `-0.3214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
