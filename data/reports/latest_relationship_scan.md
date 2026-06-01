# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T23:52:20.233992+00:00`
- Price records: `672`
- Market context records: `2610`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `8.0631` n `145` status `ready` deltaP `18.2627` edge `0.583` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.2735` n `146` status `ready` deltaP `25.0439` edge `0.5404` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.5019` n `146` status `ready` deltaP `14.7636` edge `0.3744` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.37` n `146` status `ready` deltaP `11.4306` edge `0.1567` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `0.9319` n `146` status `ready` deltaP `7.6846` edge `0.1314` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.7329` n `146` status `ready` deltaP `8.8631` edge `0.1214` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.7271` n `145` status `ready` deltaP `2.4185` edge `0.6823` maxDD `-39.0265`
- `market_context_high->index_24h` score `0.7055` n `145` status `ready` deltaP `8.6506` edge `0.0992` maxDD `-2.5127`
- `market_context_high->index_4h` score `0.2072` n `146` status `ready` deltaP `8.8227` edge `0.0426` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.0928` n `146` status `ready` deltaP `4.3905` edge `0.0124` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.4122` n `146` status `ready` deltaP `5.3523` edge `0.0178` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.4728` n `146` status `ready` deltaP `1.8005` edge `0.0149` maxDD `-2.6375`
- `market_context_high->metal_1h` score `-0.5889` n `146` status `ready` deltaP `1.5606` edge `0.0153` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.6377` n `146` status `ready` deltaP `-0.5352` edge `0.0039` maxDD `-0.278`
- `market_context_high->metal_4h` score `-0.6772` n `146` status `ready` deltaP `4.5021` edge `0.0523` maxDD `-4.7664`
- `market_context_high->equity_1h` score `-0.7797` n `146` status `ready` deltaP `-0.0779` edge `0.0194` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.8636` n `145` status `ready` deltaP `4.29` edge `-0.0012` maxDD `-1.6157`
- `market_context_high->fx_4h` score `-0.879` n `146` status `ready` deltaP `0.0793` edge `0.012` maxDD `-0.8621`
- `market_context_high->commodity_4h` score `-1.0906` n `146` status `ready` deltaP `3.1866` edge `0.0332` maxDD `-10.2078`
- `market_context_high->equity_4h` score `-1.3518` n `146` status `ready` deltaP `1.6497` edge `0.0168` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
