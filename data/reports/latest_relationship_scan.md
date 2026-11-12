# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T05:07:26.395300+00:00`
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

- `market_context_high->unknown_24h` score `159.0156` n `88` status `ready` deltaP `5.3398` edge `13.2298` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `88.5448` n `88` status `ready` deltaP `7.0676` edge `7.3764` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `38.5051` n `47` status `ready` deltaP `33.564` edge `2.985` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `22.5443` n `47` status `ready` deltaP `43.882` edge `1.7827` maxDD `-12.7247`
- `market_context_high->equity_24h` score `16.5117` n `88` status `ready` deltaP `16.5185` edge `1.505` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.1095` n `53` status `ready` deltaP `33.3438` edge `0.8157` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.7919` n `47` status `ready` deltaP `40.1384` edge `0.2984` maxDD `0.0`
- `news_risk_high->index_24h` score `5.8386` n `47` status `ready` deltaP `30.6228` edge `0.2824` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `5.6796` n `88` status `ready` deltaP `34.9638` edge `1.0045` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.8513` n `88` status `ready` deltaP `35.0071` edge `0.2262` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.2539` n `53` status `ready` deltaP `40.9084` edge `0.1194` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.8618` n `53` status `ready` deltaP `20.5908` edge `0.3333` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5573` n `53` status `ready` deltaP `18.6137` edge `0.2436` maxDD `-3.6997`
- `market_context_high->index_24h` score `3.091` n `88` status `ready` deltaP `16.9864` edge `0.1906` maxDD `-2.3671`
- `news_risk_high->crypto_alt_24h` score `3.0499` n `47` status `ready` deltaP `13.5905` edge `0.6013` maxDD `-19.0713`
- `news_risk_high->commodity_4h` score `2.6794` n `53` status `ready` deltaP `24.4248` edge `0.0858` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.152` n `53` status `ready` deltaP `24.6692` edge `0.2753` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `2.1259` n `53` status `ready` deltaP `25.2909` edge `0.034` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.0916` n `53` status `ready` deltaP `19.9839` edge `0.0847` maxDD `-0.8235`
- `news_risk_high->index_1h` score `1.3029` n `53` status `ready` deltaP `17.176` edge `0.0242` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
