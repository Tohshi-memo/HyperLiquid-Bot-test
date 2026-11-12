# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T05:22:33.973775+00:00`
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

- `market_context_high->unknown_24h` score `163.8403` n `88` status `ready` deltaP `5.5128` edge `13.6307` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `88.575` n `88` status `ready` deltaP `7.2201` edge `7.3779` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `36.9909` n `48` status `ready` deltaP `31.4807` edge `2.8831` maxDD `-0.4983`
- `news_risk_high->crypto_major_24h` score `21.9962` n `48` status `ready` deltaP `42.5966` edge `1.7456` maxDD `-12.7247`
- `market_context_high->equity_24h` score `16.3917` n `88` status `ready` deltaP `16.5185` edge `1.495` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.1167` n `53` status `ready` deltaP `33.3438` edge `0.8163` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.7643` n `48` status `ready` deltaP `40.1384` edge `0.2961` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `5.6445` n `88` status `ready` deltaP `34.9638` edge `1.0` maxDD `-33.4213`
- `news_risk_high->index_24h` score `5.475` n `48` status `ready` deltaP `28.5395` edge `0.2713` maxDD `-0.0918`
- `market_context_high->metal_24h` score `4.8489` n `88` status `ready` deltaP `35.0071` edge `0.226` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.2527` n `53` status `ready` deltaP `40.9084` edge `0.1193` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.8678` n `53` status `ready` deltaP `20.5908` edge `0.3338` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5645` n `53` status `ready` deltaP `18.6137` edge `0.2442` maxDD `-3.6997`
- `market_context_high->index_24h` score `3.0754` n `88` status `ready` deltaP `16.9864` edge `0.1893` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.6964` n `53` status `ready` deltaP `24.5772` edge `0.0862` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `2.4498` n `48` status `ready` deltaP `12.6153` edge `0.5595` maxDD `-21.0291`
- `news_risk_high->crypto_alt_4h` score `2.1466` n `53` status `ready` deltaP `24.6692` edge `0.2746` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `2.1247` n `53` status `ready` deltaP `25.2909` edge `0.0339` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.0916` n `53` status `ready` deltaP `19.9839` edge `0.0847` maxDD `-0.8235`
- `news_risk_high->index_1h` score `1.3041` n `53` status `ready` deltaP `17.176` edge `0.0243` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
