# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T04:37:28.455574+00:00`
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

- `market_context_high->unknown_24h` score `149.2122` n `88` status `ready` deltaP `5.1667` edge `12.414` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `88.918` n `88` status `ready` deltaP `7.0676` edge `7.4075` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `38.7842` n `47` status `ready` deltaP `33.737` edge `3.0071` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `22.7687` n `47` status `ready` deltaP `43.882` edge `1.8014` maxDD `-12.7247`
- `market_context_high->equity_24h` score `16.7908` n `88` status `ready` deltaP `16.6915` edge `1.5271` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.1155` n `53` status `ready` deltaP `33.3438` edge `0.8162` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.7108` n `47` status `ready` deltaP `39.9654` edge `0.2928` maxDD `0.0`
- `news_risk_high->index_24h` score `5.8722` n `47` status `ready` deltaP `30.6228` edge `0.2852` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `5.7654` n `88` status `ready` deltaP `34.9638` edge `1.0155` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.8573` n `88` status `ready` deltaP `35.0071` edge `0.2267` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.2575` n `53` status `ready` deltaP `40.9084` edge `0.1197` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.863` n `53` status `ready` deltaP `20.5908` edge `0.3334` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5549` n `53` status `ready` deltaP `18.6137` edge `0.2434` maxDD `-3.6997`
- `news_risk_high->crypto_alt_24h` score `3.1357` n `47` status `ready` deltaP `13.5905` edge `0.6123` maxDD `-19.0713`
- `market_context_high->index_24h` score `3.1246` n `88` status `ready` deltaP `16.9864` edge `0.1934` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.637` n `53` status `ready` deltaP `24.1199` edge `0.0843` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.1661` n `53` status `ready` deltaP `24.6692` edge `0.2771` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `2.1259` n `53` status `ready` deltaP `25.2909` edge `0.034` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.094` n `53` status `ready` deltaP `19.9839` edge `0.0849` maxDD `-0.8235`
- `news_risk_high->index_1h` score `1.3041` n `53` status `ready` deltaP `17.176` edge `0.0243` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
