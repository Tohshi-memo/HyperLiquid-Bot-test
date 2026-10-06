# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T13:52:35.160601+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8732`

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

- `market_context_high->unknown_24h` score `678.2326` n `117` status `ready` deltaP `11.0847` edge `56.4835` maxDD `-1.3748`
- `news_risk_high->crypto_major_4h` score `9.3858` n `62` status `ready` deltaP `33.5514` edge `0.5788` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.524` n `62` status `ready` deltaP `19.5811` edge `0.4642` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.2334` n `62` status `ready` deltaP `9.8714` edge `0.2136` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.1017` n `62` status `ready` deltaP `21.8213` edge `0.113` maxDD `0.0`
- `market_context_high->unknown_4h` score `2.8479` n `117` status `ready` deltaP `-0.3583` edge `0.2936` maxDD `-2.3109`
- `market_context_high->crypto_major_4h` score `2.641` n `117` status `ready` deltaP `13.4108` edge `0.2271` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.4759` n `62` status `ready` deltaP `28.039` edge `0.0456` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.0535` n `62` status `ready` deltaP `8.079` edge `0.1528` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8318` n `62` status `ready` deltaP `23.3775` edge `0.0118` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.6702` n `62` status `ready` deltaP `16.5569` edge `0.0886` maxDD `-2.7837`
- `market_context_high->commodity_4h` score `1.1555` n `117` status `ready` deltaP `15.8394` edge `0.0607` maxDD `-1.6002`
- `news_risk_high->metal_4h` score `1.1553` n `62` status `ready` deltaP `16.9797` edge `0.0765` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.9908` n `117` status `ready` deltaP `20.5702` edge `0.0211` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `0.8203` n `62` status `ready` deltaP `3.0085` edge `0.1002` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.7874` n `62` status `ready` deltaP `27.0092` edge `0.0775` maxDD `-8.196`
- `market_context_high->fx_1h` score `0.7408` n `117` status `ready` deltaP `12.6926` edge `0.0055` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.6507` n `117` status `ready` deltaP `11.1572` edge `0.0195` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.3991` n `117` status `ready` deltaP `-1.3315` edge `0.2145` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.0588` n `62` status `ready` deltaP `4.8049` edge `0.0049` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
