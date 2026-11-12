# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T06:07:29.633003+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11534`

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

- `market_context_high->unknown_24h` score `177.2755` n `88` status `ready` deltaP `5.5128` edge `14.7503` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `88.2174` n `88` status `ready` deltaP `7.2201` edge `7.3481` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `32.5116` n `51` status `ready` deltaP `25.7209` edge `2.5881` maxDD `-2.6885`
- `news_risk_high->crypto_major_24h` score `20.4867` n `51` status `ready` deltaP `39.0426` edge `1.6435` maxDD `-12.7247`
- `market_context_high->equity_24h` score `16.0629` n `88` status `ready` deltaP `16.5185` edge `1.4676` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.2167` n `53` status `ready` deltaP `33.6487` edge `0.8226` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.6767` n `51` status `ready` deltaP `40.1384` edge `0.2888` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `5.5377` n `88` status `ready` deltaP `34.9638` edge `0.9863` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.8501` n `88` status `ready` deltaP `35.0071` edge `0.2261` maxDD `-1.4245`
- `news_risk_high->index_24h` score `4.4587` n `51` status `ready` deltaP `22.7797` edge `0.2408` maxDD `-0.3551`
- `news_risk_high->metal_4h` score `4.2491` n `53` status `ready` deltaP `40.9084` edge `0.119` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.9368` n `53` status `ready` deltaP `21.0481` edge `0.3365` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5741` n `53` status `ready` deltaP `18.6137` edge `0.245` maxDD `-3.6997`
- `market_context_high->index_24h` score `3.0334` n `88` status `ready` deltaP `16.9864` edge `0.1858` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.7376` n `53` status `ready` deltaP `24.8821` edge `0.0876` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.1765` n `53` status `ready` deltaP `24.9741` edge `0.2764` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.1232` n `53` status `ready` deltaP `20.2888` edge `0.0853` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.0923` n `53` status `ready` deltaP `24.9915` edge `0.0332` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3029` n `53` status `ready` deltaP `17.176` edge `0.0242` maxDD `-0.4103`
- `news_risk_high->crypto_alt_24h` score `0.8414` n `51` status `ready` deltaP `9.9193` edge `0.4516` maxDD `-26.4555`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
