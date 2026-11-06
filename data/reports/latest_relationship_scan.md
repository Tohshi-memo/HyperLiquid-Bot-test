# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-06T12:22:24.060798+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3915`

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

- `news_risk_high->equity_24h` score `-0.1833` n `121` status `ready` deltaP `21.4404` edge `0.9922` maxDD `-86.0244`
- `news_risk_high->index_4h` score `-0.3141` n `121` status `ready` deltaP `7.8512` edge `0.0114` maxDD `-2.3206`
- `news_risk_high->index_1h` score `-0.4213` n `121` status `ready` deltaP `5.5872` edge `0.0018` maxDD `-0.9325`
- `news_risk_high->fx_1h` score `-0.5064` n `121` status `ready` deltaP `-3.1016` edge `-0.0019` maxDD `-0.388`
- `news_risk_high->crypto_alt_4h` score `-0.5122` n `121` status `ready` deltaP `4.8263` edge `0.1658` maxDD `-14.0916`
- `news_risk_high->index_24h` score `-0.7241` n `121` status `ready` deltaP `-4.238` edge `0.1189` maxDD `-6.6786`
- `news_risk_high->crypto_alt_1h` score `-0.769` n `121` status `ready` deltaP `0.1794` edge `0.023` maxDD `-5.8225`
- `news_risk_high->fx_4h` score `-0.8346` n `121` status `ready` deltaP `-3.4456` edge `-0.0031` maxDD `-0.4745`
- `news_risk_high->metal_1h` score `-1.2187` n `121` status `ready` deltaP `-4.3958` edge `-0.0141` maxDD `-1.6521`
- `news_risk_high->fx_24h` score `-1.4453` n `121` status `ready` deltaP `-17.0623` edge `-0.0081` maxDD `-0.4086`
- `news_risk_high->equity_1h` score `-1.5496` n `121` status `ready` deltaP `-2.0661` edge `0.0121` maxDD `-10.7597`
- `news_risk_high->crypto_major_1h` score `-1.7269` n `121` status `ready` deltaP `-4.7075` edge `-0.0106` maxDD `-4.8205`
- `news_risk_high->crypto_major_4h` score `-1.8825` n `121` status `ready` deltaP `-4.3451` edge `0.0532` maxDD `-9.1553`
- `news_risk_high->commodity_1h` score `-2.8687` n `121` status `ready` deltaP `-14.2352` edge `-0.0075` maxDD `-3.2657`
- `news_risk_high->metal_4h` score `-2.9985` n `121` status `ready` deltaP `-7.7706` edge `-0.0516` maxDD `-3.7176`
- `news_risk_high->metal_24h` score `-3.5629` n `121` status `ready` deltaP `-6.2212` edge `-0.2257` maxDD `-8.5019`
- `news_risk_high->equity_4h` score `-3.5795` n `121` status `ready` deltaP `8.3085` edge `0.08` maxDD `-28.3612`
- `news_risk_high->commodity_4h` score `-4.6475` n `121` status `ready` deltaP `-21.1147` edge `-0.0111` maxDD `-9.5011`
- `news_risk_high->crypto_major_24h` score `-10.2301` n `121` status `ready` deltaP `-18.1332` edge `0.1187` maxDD `-50.6925`
- `news_risk_high->commodity_24h` score `-10.2634` n `121` status `ready` deltaP `-23.1076` edge `0.0164` maxDD `-40.0772`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
