# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T02:37:29.020148+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11566`

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

- `market_context_high->unknown_24h` score `110.8512` n `88` status `ready` deltaP `4.9937` edge `9.2184` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `92.171` n `88` status `ready` deltaP `7.8298` edge `7.6735` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `40.6877` n `46` status `ready` deltaP `35.1211` edge `3.1565` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `23.8576` n `46` status `ready` deltaP `45.2234` edge `1.8832` maxDD `-12.7247`
- `market_context_high->equity_24h` score `18.0727` n `88` status `ready` deltaP `18.0756` edge `1.6247` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.2771` n `53` status `ready` deltaP `33.9536` edge `0.8256` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.562` n `46` status `ready` deltaP `39.9654` edge `0.2804` maxDD `0.0`
- `news_risk_high->index_24h` score `6.1815` n `46` status `ready` deltaP `31.8339` edge `0.3029` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.0611` n `88` status `ready` deltaP `34.9638` edge `1.0534` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.8585` n `88` status `ready` deltaP `35.0071` edge `0.2268` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.3571` n `53` status `ready` deltaP `41.823` edge `0.1219` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.9282` n `53` status `ready` deltaP `20.8957` edge `0.3368` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `3.8763` n `46` status `ready` deltaP `14.6081` edge `0.6781` maxDD `-17.615`
- `news_risk_high->equity_1h` score `3.4914` n `53` status `ready` deltaP `18.1646` edge `0.2411` maxDD `-3.6997`
- `market_context_high->index_24h` score `3.3799` n `88` status `ready` deltaP `18.1975` edge `0.2066` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.5726` n `53` status `ready` deltaP `23.5101` edge `0.083` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.2133` n `53` status `ready` deltaP `25.1265` edge `0.2801` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.1936` n `53` status `ready` deltaP `20.8985` edge `0.0871` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.0816` n `53` status `ready` deltaP `24.8418` edge `0.0333` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3185` n `53` status `ready` deltaP `17.3257` edge `0.0245` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
