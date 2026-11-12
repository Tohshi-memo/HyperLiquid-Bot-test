# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T10:22:31.169605+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11540`

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

- `market_context_high->unknown_24h` score `256.7115` n `88` status `ready` deltaP `6.0318` edge `21.3665` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `94.4106` n `88` status `ready` deltaP `7.2201` edge `7.8642` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `28.1327` n `53` status `ready` deltaP `21.0486` edge `2.2747` maxDD `-3.6503`
- `market_context_high->equity_24h` score `13.807` n `88` status `ready` deltaP `14.9379` edge `1.3069` maxDD `-16.8057`
- `news_risk_high->crypto_major_24h` score `11.7368` n `53` status `ready` deltaP `36.8969` edge `1.4553` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.4242` n `53` status `ready` deltaP `34.7158` edge `0.8336` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.9684` n `53` status `ready` deltaP `40.4844` edge `0.3108` maxDD `0.0`
- `market_context_high->metal_24h` score `4.9653` n `88` status `ready` deltaP `35.0071` edge `0.2357` maxDD `-1.4245`
- `market_context_high->crypto_alt_24h` score `4.9098` n `88` status `ready` deltaP `34.9638` edge `0.9058` maxDD `-33.4213`
- `news_risk_high->metal_4h` score `4.481` n `53` status `ready` deltaP `43.0425` edge `0.1241` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.0822` n `53` status `ready` deltaP `22.1152` edge `0.3415` maxDD `-9.2335`
- `news_risk_high->index_24h` score `3.6381` n `53` status `ready` deltaP `19.129` edge `0.206` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.5902` n `53` status `ready` deltaP `17.8652` edge `0.2431` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.8196` n `53` status `ready` deltaP `25.187` edge `0.0924` maxDD `-0.3611`
- `market_context_high->index_24h` score `2.7736` n `88` status `ready` deltaP `16.8134` edge `0.1653` maxDD `-2.3671`
- `news_risk_high->crypto_alt_4h` score `2.2498` n `53` status `ready` deltaP `25.8887` edge `0.2797` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.2471` n `53` status `ready` deltaP `21.5083` edge `0.0875` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.1307` n `53` status `ready` deltaP `25.2909` edge `0.0344` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3041` n `53` status `ready` deltaP `17.176` edge `0.0243` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7967` n `53` status `ready` deltaP `17.8934` edge `0.0808` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
