# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T06:22:32.024549+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `44.0075` n `51` status `ready` deltaP `4.5139` edge `3.6372` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.8541` n `51` status `ready` deltaP `24.716` edge `0.911` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `10.9533` n `51` status `ready` deltaP `39.3689` edge `0.7434` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.9952` n `51` status `ready` deltaP `48.4273` edge `0.1086` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.2934` n `51` status `ready` deltaP `16.0355` edge `0.198` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2372` n `51` status `ready` deltaP `38.2353` edge `0.0283` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.9901` n `51` status `ready` deltaP `25.0986` edge `0.1589` maxDD `-2.164`
- `market_context_high->unknown_4h` score `1.8599` n `133` status `ready` deltaP `19.158` edge `0.0681` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1691` n `51` status `ready` deltaP `16.0972` edge `0.0071` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.8018` n `51` status `ready` deltaP `17.1451` edge `0.0249` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.637` n `51` status `ready` deltaP `11.5674` edge `0.0157` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3753` n `51` status `ready` deltaP `10.0358` edge `-0.0048` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.0682` n `51` status `ready` deltaP `6.2786` edge `0.0022` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `-0.094` n `133` status `ready` deltaP `10.3743` edge `-0.0321` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1909` n `51` status `ready` deltaP `0.6957` edge `-0.0068` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.2861` n `51` status `ready` deltaP `5.996` edge `-0.0107` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4732` n `133` status `ready` deltaP `1.9` edge `-0.0001` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.5736` n `51` status `ready` deltaP `21.6503` edge `-0.1879` maxDD `-0.0053`
- `market_context_high->metal_4h` score `-0.6739` n `133` status `ready` deltaP `6.2466` edge `-0.0341` maxDD `-2.4293`
- `market_context_high->index_1h` score `-1.0574` n `133` status `ready` deltaP `-4.4246` edge `-0.0048` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
