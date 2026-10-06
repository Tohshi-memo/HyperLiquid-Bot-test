# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T13:22:33.295977+00:00`
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

- `market_context_high->unknown_24h` score `566.8078` n `117` status `ready` deltaP `11.0847` edge `47.1981` maxDD `-1.3748`
- `news_risk_high->crypto_major_4h` score `9.4846` n `62` status `ready` deltaP `33.8562` edge `0.585` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.6168` n `62` status `ready` deltaP `19.886` edge `0.4699` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.3185` n `62` status `ready` deltaP `10.2151` edge `0.2184` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.1412` n `62` status `ready` deltaP `22.1649` edge `0.114` maxDD `0.0`
- `market_context_high->unknown_4h` score `2.7867` n `117` status `ready` deltaP `-0.3583` edge `0.2885` maxDD `-2.3109`
- `market_context_high->crypto_major_4h` score `2.7398` n `117` status `ready` deltaP `13.7156` edge `0.2333` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.5051` n `62` status `ready` deltaP `28.3438` edge `0.046` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.0463` n `62` status `ready` deltaP `8.079` edge `0.1522` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.8318` n `62` status `ready` deltaP `23.3775` edge `0.0118` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.7114` n `62` status `ready` deltaP `16.8618` edge `0.09` maxDD `-2.7837`
- `market_context_high->commodity_4h` score `1.1871` n `117` status `ready` deltaP `16.1442` edge `0.0613` maxDD `-1.6002`
- `news_risk_high->metal_4h` score `1.1592` n `62` status `ready` deltaP `16.9797` edge `0.077` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.0176` n `117` status `ready` deltaP `20.8751` edge `0.0213` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `0.8251` n `62` status `ready` deltaP `3.0085` edge `0.1006` maxDD `-2.4854`
- `news_risk_high->commodity_24h` score `0.7803` n `62` status `ready` deltaP `27.0092` edge `0.0766` maxDD `-8.196`
- `market_context_high->fx_1h` score `0.7276` n `117` status `ready` deltaP `12.5429` edge `0.0054` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.6866` n `117` status `ready` deltaP `11.4566` edge `0.0205` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `0.4919` n `117` status `ready` deltaP `-1.0266` edge `0.2202` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.0564` n `62` status `ready` deltaP `4.8049` edge `0.0051` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
