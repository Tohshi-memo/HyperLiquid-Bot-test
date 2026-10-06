# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T23:22:33.179952+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8730`

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

- `market_context_high->unknown_24h` score `1415.6836` n `117` status `ready` deltaP `11.3782` edge `117.9358` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `28.5695` n `117` status `ready` deltaP `-0.6632` edge `2.4391` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.3266` n `62` status `ready` deltaP `34.1611` edge `0.5698` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.4272` n `62` status `ready` deltaP `19.886` edge `0.4541` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.1477` n `62` status `ready` deltaP `22.3958` edge `0.113` maxDD `0.0`
- `news_risk_high->index_4h` score `2.7252` n `62` status `ready` deltaP `30.6304` edge `0.0491` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.5818` n `117` status `ready` deltaP `14.0205` edge `0.2181` maxDD `-4.047`
- `news_risk_high->equity_24h` score `2.2359` n `62` status `ready` deltaP `5.0067` edge `0.1629` maxDD `-0.1298`
- `news_risk_high->crypto_major_1h` score `1.9504` n `62` status `ready` deltaP `7.4802` edge `0.1482` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.9001` n `62` status `ready` deltaP `24.126` edge `0.0125` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.7298` n `62` status `ready` deltaP `17.1666` edge `0.0895` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.2262` n `62` status `ready` deltaP `17.7419` edge `0.0805` maxDD `-0.993`
- `news_risk_high->commodity_24h` score `1.0178` n `62` status `ready` deltaP `29.6259` edge `0.0896` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.958` n `117` status `ready` deltaP `20.2653` edge `0.0204` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.7384` n `117` status `ready` deltaP `12.6926` edge `0.0053` maxDD `-0.271`
- `news_risk_high->crypto_alt_1h` score `0.7376` n `62` status `ready` deltaP `2.4097` edge `0.0973` maxDD `-2.4854`
- `market_context_high->commodity_4h` score `0.591` n `117` status `ready` deltaP `12.6381` edge `0.035` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.3703` n `117` status `ready` deltaP `8.6123` edge `0.0131` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.3023` n `117` status `ready` deltaP `-1.0266` edge `0.2044` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `0.0334` n `62` status `ready` deltaP `5.8528` edge `0.0056` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
