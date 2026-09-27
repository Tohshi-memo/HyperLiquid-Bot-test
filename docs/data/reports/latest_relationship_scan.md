# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T02:53:02.071124+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11484`

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

- `news_risk_high->unknown_24h` score `2731.572` n `103` status `ready` deltaP `1.2153` edge `227.6229` maxDD `0.0`
- `market_context_high->unknown_1h` score `75.1623` n `44` status `ready` deltaP `10.1524` edge `6.2005` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `51.5532` n `44` status `ready` deltaP `28.4565` edge `4.1415` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `27.837` n `44` status `ready` deltaP `14.9148` edge `2.2583` maxDD `-2.7051`
- `market_context_high->equity_24h` score `27.7636` n `44` status `ready` deltaP `36.0954` edge `2.1044` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.7445` n `44` status `ready` deltaP `32.2759` edge `0.439` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.7424` n `44` status `ready` deltaP `32.6546` edge `0.118` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.3458` n `44` status `ready` deltaP `37.5277` edge `0.0357` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.9457` n `44` status `ready` deltaP `17.8215` edge `0.1643` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.234` n `44` status `ready` deltaP `8.8553` edge `0.1064` maxDD `-3.3417`
- `news_risk_high->index_24h` score `1.0531` n `103` status `ready` deltaP `16.102` edge `0.0416` maxDD `-2.2287`
- `market_context_high->equity_1h` score `1.0371` n `44` status `ready` deltaP `11.7175` edge `0.0486` maxDD `-1.5564`
- `market_context_high->crypto_major_1h` score `1.0364` n `44` status `ready` deltaP `8.669` edge `0.102` maxDD `-4.5405`
- `news_risk_high->metal_24h` score `0.9575` n `103` status `ready` deltaP `23.3431` edge `0.1319` maxDD `-6.8481`
- `market_context_high->crypto_major_4h` score `0.879` n `44` status `ready` deltaP `6.9152` edge `0.1176` maxDD `-5.2359`
- `market_context_high->index_1h` score `0.7864` n `44` status `ready` deltaP `12.0169` edge `0.0091` maxDD `-0.2275`
- `market_context_high->metal_1h` score `0.2336` n `44` status `ready` deltaP `6.0152` edge `0.011` maxDD `-0.1976`
- `market_context_high->fx_1h` score `0.1469` n `44` status `ready` deltaP `7.2128` edge `0.0064` maxDD `-0.1854`
- `market_context_high->crypto_alt_1h` score `-0.0077` n `44` status `ready` deltaP `3.8514` edge `0.0626` maxDD `-5.7799`
- `news_risk_high->index_1h` score `-0.1415` n `141` status `ready` deltaP `2.1362` edge `0.0031` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
