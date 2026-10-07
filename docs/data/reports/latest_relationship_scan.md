# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T17:07:35.595996+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8742`

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

- `market_context_high->unknown_4h` score `37.5322` n `90` status `ready` deltaP `-5.5994` edge `3.2189` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.8116` n `62` status `ready` deltaP `37.5282` edge `0.6711` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.4868` n `62` status `ready` deltaP `24.0171` edge `0.5982` maxDD `-6.4195`
- `news_risk_high->index_24h` score `4.12` n `62` status `ready` deltaP `29.5848` edge `0.1461` maxDD `0.0`
- `news_risk_high->equity_24h` score `4.02` n `62` status `ready` deltaP `9.6384` edge `0.2807` maxDD `-0.1298`
- `news_risk_high->index_4h` score `3.0506` n `62` status `ready` deltaP `33.5425` edge `0.0568` maxDD `-0.4296`
- `market_context_high->crypto_major_24h` score `2.6145` n `90` status `ready` deltaP `7.797` edge `0.5806` maxDD `-16.7906`
- `news_risk_high->crypto_major_1h` score `2.403` n `62` status `ready` deltaP `9.8076` edge `0.1704` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.3068` n `90` status `ready` deltaP `15.5927` edge `0.1847` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.2961` n `62` status `ready` deltaP `19.3402` edge `0.1222` maxDD `-2.7837`
- `news_risk_high->index_1h` score `2.0357` n `62` status `ready` deltaP `25.5509` edge `0.0143` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.4306` n `62` status `ready` deltaP `20.1735` edge `0.0905` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.2489` n `62` status `ready` deltaP `3.8358` edge `0.1304` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.8572` n `90` status `ready` deltaP `19.517` edge `0.016` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.8077` n `90` status `ready` deltaP `19.0426` edge `0.1251` maxDD `-3.5466`
- `market_context_high->fx_1h` score `0.7833` n `90` status `ready` deltaP `12.9148` edge `0.0034` maxDD `-0.271`
- `news_risk_high->unknown_4h` score `0.3118` n `62` status `ready` deltaP `-8.5744` edge `0.2077` maxDD `-5.6309`
- `news_risk_high->metal_1h` score `0.0994` n `62` status `ready` deltaP `6.3769` edge `0.0076` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `0.0969` n `90` status `ready` deltaP `9.7359` edge `0.0364` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `0.0214` n `90` status `ready` deltaP `4.7533` edge `0.0077` maxDD `-0.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
