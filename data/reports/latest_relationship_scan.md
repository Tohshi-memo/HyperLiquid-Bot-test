# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T10:22:28.212960+00:00`
- Price records: `672`
- Market context records: `6173`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11132`

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

- `news_risk_high->crypto_alt_24h` score `12.5654` n `32` status `ready` deltaP `42.3848` edge `0.7793` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.2289` n `32` status `ready` deltaP `63.4812` edge `0.1792` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.032` n `32` status `ready` deltaP `41.9845` edge `0.0607` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3336` n `32` status `ready` deltaP `28.1343` edge `0.0208` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.7139` n `194` status `ready` deltaP `0.9202` edge `0.2375` maxDD `-3.7317`
- `news_risk_high->crypto_major_24h` score `1.622` n `32` status `ready` deltaP `15.7956` edge `0.1806` maxDD `-4.2368`
- `news_risk_high->crypto_major_1h` score `1.197` n `32` status `ready` deltaP `12.7892` edge `0.1149` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6177` n `32` status `ready` deltaP `8.181` edge `0.0708` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.3719` n `194` status `ready` deltaP `-1.1368` edge `0.2918` maxDD `-11.925`
- `market_context_high->metal_24h` score `0.1193` n `194` status `ready` deltaP `20.3916` edge `0.1362` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.083` n `32` status `ready` deltaP `9.663` edge `0.0121` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.1785` n `194` status `ready` deltaP `2.392` edge `0.0609` maxDD `-2.671`
- `market_context_high->fx_1h` score `-0.2997` n `194` status `ready` deltaP `1.0724` edge `-0.001` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.5137` n `32` status `ready` deltaP `13.3852` edge `-0.1115` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6877` n `194` status `ready` deltaP `3.3872` edge `0.008` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7179` n `194` status `ready` deltaP `-1.7233` edge `-0.0037` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7912` n `32` status `ready` deltaP `-3.2836` edge `-0.0298` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8808` n `194` status `ready` deltaP `1.871` edge `-0.006` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.9861` n `194` status `ready` deltaP `2.9297` edge `0.0293` maxDD `-9.3536`
- `market_context_high->equity_1h` score `-1.0111` n `194` status `ready` deltaP `-2.8773` edge `0.0011` maxDD `-4.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
