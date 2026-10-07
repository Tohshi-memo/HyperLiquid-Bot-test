# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T19:38:14.944581+00:00`
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

- `market_context_high->unknown_4h` score `38.3867` n `90` status `ready` deltaP `-5.4185` edge `3.2889` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.7787` n `62` status `ready` deltaP `37.5976` edge `0.6679` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.1091` n `62` status `ready` deltaP `22.7157` edge `0.5754` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `4.3898` n `62` status `ready` deltaP `10.3304` edge `0.3069` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.165` n `62` status `ready` deltaP `29.7578` edge `0.1487` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `3.0288` n `90` status `ready` deltaP `8.143` edge `0.6314` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.8983` n `62` status `ready` deltaP `32.0887` edge `0.0538` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.448` n `62` status `ready` deltaP `10.0251` edge `0.1727` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.2739` n `90` status `ready` deltaP `15.6621` edge `0.1815` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.1106` n `62` status `ready` deltaP `18.0267` edge `0.1155` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9888` n `62` status `ready` deltaP `25.0242` edge `0.0139` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.438` n `62` status `ready` deltaP `20.4055` edge `0.0899` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.2138` n `62` status `ready` deltaP `3.6073` edge `0.129` maxDD `-2.4854`
- `news_risk_high->unknown_4h` score `1.1663` n `62` status `ready` deltaP `-8.3935` edge `0.2777` maxDD `-5.6309`
- `market_context_high->fx_4h` score `0.9007` n `90` status `ready` deltaP `20.0609` edge `0.016` maxDD `-0.3077`
- `market_context_high->metal_24h` score `0.8931` n `90` status `ready` deltaP `19.2157` edge `0.1349` maxDD `-3.5466`
- `market_context_high->fx_1h` score `0.7154` n `90` status `ready` deltaP `12.0958` edge `0.0032` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1261` n `90` status `ready` deltaP `9.9534` edge `0.0387` maxDD `-3.7778`
- `news_risk_high->metal_1h` score `0.1101` n `62` status `ready` deltaP `6.4516` edge `0.008` maxDD `-1.0132`
- `market_context_high->commodity_1h` score `-0.0455` n `90` status `ready` deltaP `4.0818` edge `0.0066` maxDD `-0.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
