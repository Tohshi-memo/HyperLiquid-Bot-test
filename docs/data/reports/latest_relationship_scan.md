# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T12:07:41.209456+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8372`

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

- `market_context_high->crypto_major_24h` score `10.8872` n `81` status `ready` deltaP `29.8032` edge `0.7222` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3489` n `65` status `ready` deltaP `32.3992` edge `0.5834` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `6.1566` n `81` status `ready` deltaP `25.3666` edge `0.4059` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.7982` n `65` status `ready` deltaP `19.6341` edge `0.4867` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.4981` n `112` status `ready` deltaP `15.9844` edge `0.2647` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.4573` n `65` status `ready` deltaP `24.8264` edge `0.1226` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.0818` n `65` status `ready` deltaP `10.3393` edge `0.1979` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.945` n `65` status `ready` deltaP `32.5235` edge `0.0548` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.5229` n `65` status `ready` deltaP `9.8664` edge `0.18` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.4812` n `65` status `ready` deltaP `20.5769` edge `0.1306` maxDD `-2.881`
- `news_risk_high->index_1h` score `2.0878` n `65` status `ready` deltaP `25.7669` edge `0.0172` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.7756` n `65` status `ready` deltaP `16.7918` edge `0.0776` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.6365` n `112` status `ready` deltaP `27.5915` edge `0.0281` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.2141` n `65` status `ready` deltaP `3.6711` edge `0.1286` maxDD `-2.4854`
- `market_context_high->commodity_4h` score `1.0156` n `112` status `ready` deltaP `15.2222` edge `0.0558` maxDD `-1.8118`
- `market_context_high->fx_1h` score `0.9808` n `122` status `ready` deltaP `15.5885` edge `0.0062` maxDD `-0.271`
- `market_context_high->crypto_alt_4h` score `0.8354` n `112` status `ready` deltaP `3.027` edge `0.2218` maxDD `-7.1222`
- `market_context_high->equity_24h` score `0.8335` n `81` status `ready` deltaP `11.5548` edge `0.0047` maxDD `-0.3151`
- `market_context_high->metal_24h` score `0.712` n `81` status `ready` deltaP `25.2315` edge `0.0656` maxDD `-6.0684`
- `news_risk_high->commodity_24h` score `0.4731` n `65` status `ready` deltaP `24.9119` edge `0.0977` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
