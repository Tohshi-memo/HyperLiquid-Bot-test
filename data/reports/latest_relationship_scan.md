# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T06:01:33.508816+00:00`
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

- `news_risk_high->unknown_24h` score `44.037` n `51` status `ready` deltaP `4.6875` edge `3.6385` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.8395` n `51` status `ready` deltaP `24.5636` edge `0.9108` maxDD `-0.0348`
- `news_risk_high->equity_24h` score `11.0488` n `51` status `ready` deltaP `39.5425` edge `0.7502` maxDD `-4.7801`
- `news_risk_high->index_24h` score `5.0211` n `51` status `ready` deltaP `48.6009` edge `0.1096` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.2779` n `51` status `ready` deltaP `15.8858` edge `0.1977` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2384` n `51` status `ready` deltaP `38.2353` edge `0.0284` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `3.0407` n `51` status `ready` deltaP `25.2511` edge `0.1621` maxDD `-2.164`
- `market_context_high->unknown_4h` score `1.9626` n `132` status `ready` deltaP `19.7062` edge `0.073` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1823` n `51` status `ready` deltaP `16.2469` edge `0.0072` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.8041` n `51` status `ready` deltaP `17.1451` edge `0.0252` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.6552` n `51` status `ready` deltaP `11.7198` edge `0.0162` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3741` n `51` status `ready` deltaP `10.0358` edge `-0.0049` maxDD `-0.4666`
- `news_risk_high->index_1h` score `0.0682` n `51` status `ready` deltaP `6.2786` edge `0.0022` maxDD `-0.1583`
- `market_context_high->unknown_1h` score `-0.1096` n `133` status `ready` deltaP `10.2246` edge `-0.0324` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1746` n `51` status `ready` deltaP `0.9951` edge `-0.0067` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.2837` n `51` status `ready` deltaP `5.996` edge `-0.0105` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4646` n `133` status `ready` deltaP `2.0497` edge `0.0` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.5628` n `51` status `ready` deltaP `21.6503` edge `-0.187` maxDD `-0.0053`
- `market_context_high->metal_4h` score `-0.5708` n `132` status `ready` deltaP `6.7535` edge `-0.0336` maxDD `-2.386`
- `market_context_high->index_1h` score `-1.0574` n `133` status `ready` deltaP `-4.4246` edge `-0.0048` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
