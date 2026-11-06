# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T09:52:28.263323+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4042`

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

- `news_risk_high->crypto_alt_4h` score `-0.4028` n `131` status `ready` deltaP `5.1154` edge `0.1779` maxDD `-14.0916`
- `news_risk_high->crypto_alt_1h` score `-0.5176` n `131` status `ready` deltaP `2.3129` edge `0.041` maxDD `-5.8225`
- `news_risk_high->fx_1h` score `-0.7409` n `131` status `ready` deltaP `-3.3608` edge `-0.0025` maxDD `-0.6065`
- `news_risk_high->index_1h` score `-0.769` n `131` status `ready` deltaP `2.1484` edge `-0.0001` maxDD `-1.2647`
- `news_risk_high->index_4h` score `-0.8504` n `131` status `ready` deltaP `4.9595` edge `0.0115` maxDD `-2.9538`
- `news_risk_high->fx_4h` score `-1.2042` n `131` status `ready` deltaP `-6.7841` edge `-0.0108` maxDD `-1.5348`
- `news_risk_high->index_24h` score `-1.2991` n `131` status `ready` deltaP `-7.7709` edge `0.0979` maxDD `-6.6786`
- `news_risk_high->metal_1h` score `-1.3815` n `131` status `ready` deltaP `-7.1171` edge `-0.019` maxDD `-2.5203`
- `news_risk_high->crypto_major_1h` score `-1.9534` n `131` status `ready` deltaP `-4.1231` edge `-0.0043` maxDD `-6.1465`
- `news_risk_high->fx_24h` score `-1.9629` n `131` status `ready` deltaP `-20.6133` edge `-0.0187` maxDD `-1.3096`
- `news_risk_high->equity_1h` score `-2.0919` n `131` status `ready` deltaP `-4.827` edge `-0.0009` maxDD `-13.8088`
- `news_risk_high->commodity_1h` score `-2.7086` n `131` status `ready` deltaP `-12.8948` edge `-0.0031` maxDD `-3.2657`
- `news_risk_high->equity_24h` score `-2.7752` n `131` status `ready` deltaP `16.3304` edge `0.8435` maxDD `-86.0244`
- `news_risk_high->crypto_major_4h` score `-2.8704` n `131` status `ready` deltaP `-5.4273` edge `0.0362` maxDD `-13.8038`
- `news_risk_high->metal_4h` score `-4.3602` n `131` status `ready` deltaP `-9.8422` edge `-0.0676` maxDD `-7.0775`
- `news_risk_high->commodity_4h` score `-4.5966` n `131` status `ready` deltaP `-20.5374` edge `-0.0107` maxDD `-9.5011`
- `news_risk_high->equity_4h` score `-6.0666` n `131` status `ready` deltaP `5.4168` edge `0.0563` maxDD `-38.17`
- `news_risk_high->metal_24h` score `-6.3366` n `131` status `ready` deltaP `-11.0158` edge `-0.2538` maxDD `-9.065`
- `news_risk_high->commodity_24h` score `-10.641` n `131` status `ready` deltaP `-21.8191` edge `0.0399` maxDD `-42.495`
- `news_risk_high->crypto_alt_24h` score `-12.4264` n `131` status `ready` deltaP `4.88` edge `0.0738` maxDD `-118.6236`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
