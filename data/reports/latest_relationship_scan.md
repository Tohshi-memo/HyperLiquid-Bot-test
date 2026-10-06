# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T07:22:35.046611+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8632`

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

- `news_risk_high->crypto_major_4h` score `9.4304` n `62` status `ready` deltaP `33.7038` edge `0.5815` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.4551` n `62` status `ready` deltaP `20.1908` edge `0.4544` maxDD `-6.4195`
- `market_context_high->crypto_major_24h` score `3.6876` n `103` status `ready` deltaP `11.5705` edge `0.3902` maxDD `-8.8032`
- `news_risk_high->equity_24h` score `3.5002` n `62` status `ready` deltaP `10.7305` edge `0.2301` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.258` n `62` status `ready` deltaP `22.6804` edge `0.1203` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.6856` n `117` status `ready` deltaP `13.5632` edge `0.2298` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.5525` n `62` status `ready` deltaP `28.8012` edge `0.0469` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.0055` n `62` status `ready` deltaP `8.079` edge `0.1488` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.7923` n `62` status `ready` deltaP `22.9284` edge `0.0115` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.6382` n `62` status `ready` deltaP `16.8618` edge `0.0839` maxDD `-2.7837`
- `market_context_high->fx_4h` score `1.2829` n `117` status `ready` deltaP `23.7714` edge `0.0241` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.1993` n `117` status `ready` deltaP `16.2967` edge `0.0613` maxDD `-1.6002`
- `news_risk_high->metal_4h` score `1.1686` n `62` status `ready` deltaP `16.9797` edge `0.0782` maxDD `-0.993`
- `market_context_high->fx_1h` score `0.906` n `117` status `ready` deltaP `14.6387` edge `0.0063` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7897` n `117` status `ready` deltaP `12.5045` edge `0.0221` maxDD `-0.5059`
- `news_risk_high->commodity_24h` score `0.7632` n `62` status `ready` deltaP `27.0092` edge `0.0744` maxDD `-8.196`
- `news_risk_high->crypto_alt_1h` score `0.662` n `62` status `ready` deltaP `2.4097` edge `0.091` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `0.3303` n `117` status `ready` deltaP `-0.7218` edge `0.2047` maxDD `-7.1222`
- `market_context_high->metal_24h` score `0.1885` n `103` status `ready` deltaP `15.7441` edge `0.0567` maxDD `-5.6663`
- `news_risk_high->metal_1h` score `-0.1067` n `62` status `ready` deltaP `4.2061` edge `0.0049` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
