# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T05:37:32.183211+00:00`
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

- `market_context_high->unknown_24h` score `167.7247` n `88` status `ready` deltaP `5.5128` edge `13.9544` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `88.2474` n `88` status `ready` deltaP `7.2201` edge `7.3506` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `35.5263` n `49` status `ready` deltaP `29.4824` edge `2.785` maxDD `-1.0156`
- `news_risk_high->crypto_major_24h` score `21.5088` n `49` status `ready` deltaP `41.3636` edge `1.7132` maxDD `-12.7247`
- `market_context_high->equity_24h` score `16.2765` n `88` status `ready` deltaP `16.5185` edge `1.4854` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.1517` n `53` status `ready` deltaP `33.4963` edge `0.8182` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.7307` n `49` status `ready` deltaP `40.1384` edge `0.2933` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `5.6063` n `88` status `ready` deltaP `34.9638` edge `0.9951` maxDD `-33.4213`
- `news_risk_high->index_24h` score `5.1286` n `49` status `ready` deltaP `26.5412` edge `0.2609` maxDD `-0.1698`
- `market_context_high->metal_24h` score `4.8489` n `88` status `ready` deltaP `35.0071` edge `0.226` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.2515` n `53` status `ready` deltaP `40.9084` edge `0.1192` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.8908` n `53` status `ready` deltaP `20.7433` edge `0.3347` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5729` n `53` status `ready` deltaP `18.6137` edge `0.2449` maxDD `-3.6997`
- `market_context_high->index_24h` score `3.061` n `88` status `ready` deltaP `16.9864` edge `0.1881` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.7146` n `53` status `ready` deltaP `24.7297` edge `0.0867` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.1489` n `53` status `ready` deltaP `24.6692` edge `0.2749` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `2.1115` n `53` status `ready` deltaP `25.1412` edge `0.0338` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.1062` n `53` status `ready` deltaP `20.1363` edge `0.0849` maxDD `-0.8235`
- `news_risk_high->crypto_alt_24h` score `1.9304` n `49` status `ready` deltaP `11.68` edge `0.5244` maxDD `-22.7155`
- `news_risk_high->index_1h` score `1.3041` n `53` status `ready` deltaP `17.176` edge `0.0243` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
