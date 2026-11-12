# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T04:22:26.225838+00:00`
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

- `market_context_high->unknown_24h` score `144.3084` n `88` status `ready` deltaP `4.9937` edge `12.0065` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `89.2902` n `88` status `ready` deltaP `7.2201` edge `7.4375` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `38.9348` n `47` status `ready` deltaP `33.91` edge `3.0185` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `22.8767` n `47` status `ready` deltaP `43.882` edge `1.8104` maxDD `-12.7247`
- `market_context_high->equity_24h` score `16.9414` n `88` status `ready` deltaP `16.8645` edge `1.5385` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.1191` n `53` status `ready` deltaP `33.3438` edge `0.8165` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.6832` n `47` status `ready` deltaP `39.9654` edge `0.2905` maxDD `0.0`
- `news_risk_high->index_24h` score `5.8914` n `47` status `ready` deltaP `30.6228` edge `0.2868` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `5.8013` n `88` status `ready` deltaP `34.9638` edge `1.0201` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.8609` n `88` status `ready` deltaP `35.0071` edge `0.227` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.2611` n `53` status `ready` deltaP `40.9084` edge `0.12` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.863` n `53` status `ready` deltaP `20.5908` edge `0.3334` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5645` n `53` status `ready` deltaP `18.6137` edge `0.2442` maxDD `-3.6997`
- `news_risk_high->crypto_alt_24h` score `3.1716` n `47` status `ready` deltaP `13.5905` edge `0.6169` maxDD `-19.0713`
- `market_context_high->index_24h` score `3.1438` n `88` status `ready` deltaP `16.9864` edge `0.195` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.6188` n `53` status `ready` deltaP `23.9675` edge `0.0838` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.1676` n `53` status `ready` deltaP `24.6692` edge `0.2773` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `2.1259` n `53` status `ready` deltaP `25.2909` edge `0.034` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.0964` n `53` status `ready` deltaP `19.9839` edge `0.0851` maxDD `-0.8235`
- `news_risk_high->index_1h` score `1.3185` n `53` status `ready` deltaP `17.3257` edge `0.0245` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
