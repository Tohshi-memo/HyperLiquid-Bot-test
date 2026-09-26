# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T23:52:32.838084+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11444`

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

- `news_risk_high->unknown_24h` score `3793.0836` n `91` status `ready` deltaP `1.2153` edge `316.0822` maxDD `0.0`
- `market_context_high->unknown_1h` score `70.3687` n `45` status `ready` deltaP `10.2029` edge `5.8007` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `49.7897` n `45` status `ready` deltaP `26.4236` edge `4.0081` maxDD `-2.4756`
- `market_context_high->equity_24h` score `27.1485` n `45` status `ready` deltaP `36.1459` edge `2.0528` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `26.9111` n `45` status `ready` deltaP `14.9653` edge `2.1808` maxDD `-2.7051`
- `market_context_high->index_24h` score `7.5248` n `45` status `ready` deltaP `31.2847` edge `0.4273` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.6699` n `45` status `ready` deltaP `31.9445` edge `0.1167` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.2958` n `45` status `ready` deltaP `37.0833` edge `0.0345` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.8602` n `45` status `ready` deltaP `17.9336` edge `0.1606` maxDD `-1.3444`
- `news_risk_high->index_24h` score `1.5206` n `91` status `ready` deltaP `19.2212` edge `0.0556` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.1809` n `91` status `ready` deltaP `26.6942` edge `0.1382` maxDD `-6.8481`
- `market_context_high->equity_1h` score `1.1697` n `45` status `ready` deltaP `13.0739` edge `0.0506` maxDD `-1.5564`
- `market_context_high->crypto_major_1h` score `1.07` n `45` status `ready` deltaP `8.2036` edge `0.1079` maxDD `-4.5405`
- `market_context_high->crypto_alt_4h` score `1.0698` n `45` status `ready` deltaP `8.7635` edge `0.0975` maxDD `-3.3417`
- `market_context_high->crypto_major_4h` score `0.7712` n `45` status `ready` deltaP `7.1273` edge `0.1072` maxDD `-5.2359`
- `market_context_high->index_1h` score `0.6312` n `45` status `ready` deltaP `10.7019` edge `0.0091` maxDD `-0.2275`
- `market_context_high->crypto_alt_1h` score `0.2186` n `45` status `ready` deltaP `4.9102` edge `0.0744` maxDD `-5.7799`
- `market_context_high->fx_1h` score `0.1966` n `45` status `ready` deltaP `8.1237` edge `0.0067` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.1646` n `45` status `ready` deltaP `5.153` edge `0.011` maxDD `-0.1976`
- `news_risk_high->equity_4h` score `-0.0861` n `139` status `ready` deltaP `16.4787` edge `0.0439` maxDD `-9.2079`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
