# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T13:37:27.310564+00:00`
- Price records: `672`
- Market context records: `8626`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `5191.7058` n `60` status `ready` deltaP `34.2345` edge `432.456` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.2448` n `47` status `ready` deltaP `53.5345` edge `1.1199` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.2287` n `60` status `ready` deltaP `21.4735` edge `0.4356` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.4998` n `60` status `ready` deltaP `21.626` edge `0.0832` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.6868` n `60` status `ready` deltaP `14.9302` edge `0.0887` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.1813` n `60` status `ready` deltaP `7.5915` edge `0.1784` maxDD `-3.5385`
- `market_context_high->crypto_alt_4h` score `0.9133` n `58` status `ready` deltaP `11.5643` edge `0.1357` maxDD `-5.323`
- `news_risk_high->crypto_alt_1h` score `0.442` n `60` status `ready` deltaP `8.3333` edge `0.0538` maxDD `-1.8813`
- `news_risk_high->crypto_alt_4h` score `0.4393` n `60` status `ready` deltaP `11.2195` edge `0.1207` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `0.3287` n `60` status `ready` deltaP `6.2176` edge `0.0519` maxDD `-2.0972`
- `news_risk_high->fx_4h` score `0.3266` n `60` status `ready` deltaP `14.7561` edge `0.0246` maxDD `-0.6604`
- `market_context_high->fx_24h` score `0.2936` n `47` status `ready` deltaP `13.2343` edge `0.0432` maxDD `-2.1692`
- `news_risk_high->metal_4h` score `0.1202` n `60` status `ready` deltaP `4.2174` edge `0.0349` maxDD `-0.8085`
- `news_risk_high->fx_1h` score `0.1102` n `60` status `ready` deltaP `5.5988` edge `0.0049` maxDD `-0.2475`
- `market_context_high->commodity_24h` score `0.0937` n `47` status `ready` deltaP `18.8466` edge `0.1293` maxDD `-13.1007`
- `news_risk_high->metal_1h` score `0.044` n `60` status `ready` deltaP `5.3393` edge `0.0084` maxDD `-0.5599`
- `news_risk_high->index_1h` score `0.0087` n `60` status `ready` deltaP `3.523` edge `0.0093` maxDD `-0.5338`
- `market_context_high->fx_4h` score `-0.0005` n `58` status `ready` deltaP `9.7561` edge `0.0145` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `-0.1157` n `58` status `ready` deltaP `5.095` edge `0.0053` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.2681` n `58` status `ready` deltaP `2.3229` edge `0.0004` maxDD `-0.6874`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
