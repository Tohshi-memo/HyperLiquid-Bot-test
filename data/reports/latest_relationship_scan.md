# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T04:52:26.395581+00:00`
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

- `market_context_high->unknown_24h` score `1167.7284` n `113` status `ready` deltaP `10.7731` edge `97.2769` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `30.4417` n `113` status `ready` deltaP `-0.8714` edge `2.5965` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.834` n `62` status `ready` deltaP `34.9233` edge `0.607` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.2641` n `62` status `ready` deltaP `21.2579` edge `0.5147` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.5745` n `113` status `ready` deltaP `17.3241` edge `0.2788` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.1446` n `62` status `ready` deltaP `22.2222` edge `0.1139` maxDD `0.0`
- `news_risk_high->index_4h` score `2.7288` n `62` status `ready` deltaP `30.6304` edge `0.0494` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.1147` n `62` status `ready` deltaP `7.7796` edge `0.1599` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.9133` n `62` status `ready` deltaP `24.2757` edge `0.0126` maxDD `-0.1997`
- `news_risk_high->equity_24h` score `1.9108` n `62` status `ready` deltaP `2.9234` edge `0.1497` maxDD `-0.1298`
- `news_risk_high->equity_4h` score `1.7204` n `62` status `ready` deltaP `16.4044` edge `0.0938` maxDD `-2.7837`
- `market_context_high->crypto_alt_4h` score `1.4491` n `113` status `ready` deltaP `1.5176` edge `0.283` maxDD `-7.1222`
- `market_context_high->crypto_major_24h` score `1.3416` n `113` status `ready` deltaP `7.0473` edge `0.3622` maxDD `-16.7906`
- `news_risk_high->metal_4h` score `1.275` n `62` status `ready` deltaP `18.3517` edge `0.0827` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `0.9847` n `62` status `ready` deltaP `2.7091` edge `0.1159` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.865` n `62` status `ready` deltaP `28.7579` edge `0.0758` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.8298` n `113` status `ready` deltaP `18.9632` edge `0.0184` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.7338` n `113` status `ready` deltaP `12.6954` edge `0.0049` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.4634` n `113` status `ready` deltaP `11.6124` edge `0.0312` maxDD `-1.6002`
- `market_context_high->crypto_major_1h` score `0.2861` n `113` status `ready` deltaP `9.6352` edge `0.0485` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
