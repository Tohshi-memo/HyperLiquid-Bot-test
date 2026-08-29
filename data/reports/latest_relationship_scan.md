# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T09:22:31.392714+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `news_risk_high->unknown_24h` score `50.5106` n `55` status `ready` deltaP `14.5202` edge `4.1581` maxDD `-1.9878`
- `news_risk_high->crypto_alt_24h` score `25.4463` n `55` status `ready` deltaP `37.7935` edge `2.061` maxDD `-13.0611`
- `market_context_high->unknown_24h` score `8.2379` n `117` status `ready` deltaP `16.7735` edge `0.6479` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.2529` n `80` status `ready` deltaP `10.8232` edge `0.5079` maxDD `-1.7183`
- `news_risk_high->crypto_major_24h` score `3.9174` n `55` status `ready` deltaP `20.4608` edge `0.4008` maxDD `-14.5272`
- `market_context_high->metal_24h` score `3.7405` n `117` status `ready` deltaP `30.6491` edge `0.2093` maxDD `-3.1535`
- `news_risk_high->equity_24h` score `2.7959` n `55` status `ready` deltaP `23.2386` edge `0.376` maxDD `-11.1316`
- `market_context_high->unknown_4h` score `2.6563` n `117` status `ready` deltaP `19.5839` edge `0.1315` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.6547` n `80` status `ready` deltaP `5.524` edge `0.2201` maxDD `-0.8558`
- `news_risk_high->fx_4h` score `2.3291` n `80` status `ready` deltaP `34.0549` edge `0.022` maxDD `-0.3953`
- `news_risk_high->metal_24h` score `1.8057` n `55` status `ready` deltaP `36.834` edge `0.045` maxDD `-3.0586`
- `news_risk_high->index_24h` score `1.462` n `55` status `ready` deltaP `19.5833` edge `0.0274` maxDD `-0.8895`
- `market_context_high->unknown_1h` score `1.266` n `119` status `ready` deltaP `9.4526` edge `0.0875` maxDD `-1.6015`
- `news_risk_high->fx_1h` score `0.6621` n `80` status `ready` deltaP `13.2934` edge `0.0054` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.4743` n `80` status `ready` deltaP `13.0988` edge `0.0055` maxDD `-0.5618`
- `market_context_high->metal_4h` score `-0.1805` n `117` status `ready` deltaP `8.8324` edge `0.0097` maxDD `-3.3377`
- `news_risk_high->index_1h` score `-0.3988` n `80` status `ready` deltaP `0.1572` edge `-0.0085` maxDD `-0.8275`
- `news_risk_high->index_4h` score `-0.561` n `80` status `ready` deltaP `1.311` edge `-0.0165` maxDD `-1.7996`
- `news_risk_high->commodity_4h` score `-0.5712` n `80` status `ready` deltaP `7.5` edge `0.0109` maxDD `-2.0635`
- `market_context_high->fx_1h` score `-0.5913` n `119` status `ready` deltaP `3.7136` edge `-0.0008` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
