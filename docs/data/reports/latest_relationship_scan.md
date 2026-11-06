# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T14:22:26.772587+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3932`

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

- `news_risk_high->equity_24h` score `0.7168` n `113` status `ready` deltaP `26.1797` edge `1.076` maxDD `-86.0244`
- `news_risk_high->index_4h` score `0.2073` n `113` status `ready` deltaP `11.0323` edge `0.0154` maxDD `-1.6566`
- `news_risk_high->index_1h` score `-0.2476` n `113` status `ready` deltaP `5.9416` edge `0.0021` maxDD `-0.8765`
- `news_risk_high->equity_4h` score `-0.311` n `113` status `ready` deltaP `11.3371` edge `0.1517` maxDD `-16.5894`
- `news_risk_high->index_24h` score `-0.4414` n `113` status `ready` deltaP `-0.9615` edge `0.1333` maxDD `-6.6786`
- `news_risk_high->fx_1h` score `-0.4496` n `113` status `ready` deltaP `0.2266` edge `0.001` maxDD `-0.1984`
- `news_risk_high->crypto_alt_1h` score `-0.4833` n `113` status `ready` deltaP `2.688` edge `0.0429` maxDD `-5.8225`
- `news_risk_high->crypto_alt_4h` score `-0.6882` n `113` status `ready` deltaP `2.7628` edge `0.157` maxDD `-14.0916`
- `news_risk_high->crypto_major_1h` score `-0.7842` n `113` status `ready` deltaP `-2.023` edge `0.0135` maxDD `-4.7103`
- `news_risk_high->metal_1h` score `-0.8054` n `113` status `ready` deltaP `-1.4771` edge `-0.0069` maxDD `-1.0293`
- `news_risk_high->crypto_major_4h` score `-1.0128` n `113` status `ready` deltaP `-1.971` edge `0.0644` maxDD `-9.1553`
- `news_risk_high->fx_4h` score `-1.0545` n `113` status `ready` deltaP `-0.862` edge `-0.0012` maxDD `-0.4745`
- `news_risk_high->fx_24h` score `-1.1941` n `113` status `ready` deltaP `-13.3126` edge `-0.0009` maxDD `-0.4086`
- `news_risk_high->equity_1h` score `-1.2847` n `113` status `ready` deltaP `-0.5922` edge `0.0209` maxDD `-9.5327`
- `news_risk_high->metal_4h` score `-2.0428` n `113` status `ready` deltaP `-4.588` edge `-0.0413` maxDD `-2.2008`
- `news_risk_high->commodity_1h` score `-2.8847` n `113` status `ready` deltaP `-14.3156` edge `-0.0083` maxDD `-3.2657`
- `news_risk_high->metal_24h` score `-3.2084` n `113` status `ready` deltaP `-1.7745` edge `-0.2099` maxDD `-8.5019`
- `news_risk_high->commodity_4h` score `-5.1577` n `113` status `ready` deltaP `-25.4371` edge `-0.0248` maxDD `-9.5011`
- `news_risk_high->crypto_major_24h` score `-6.0665` n `113` status `ready` deltaP `-16.0853` edge `0.1798` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-10.3785` n `113` status `ready` deltaP `-24.0821` edge `-0.0041` maxDD `-38.6848`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
