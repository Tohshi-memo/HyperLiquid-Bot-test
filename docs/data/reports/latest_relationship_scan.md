# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T11:37:37.426932+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8312`

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

- `market_context_high->unknown_1h` score `39.6382` n `123` status `ready` deltaP `-1.3132` edge `3.3534` maxDD `-0.9839`
- `market_context_high->crypto_major_24h` score `10.886` n `81` status `ready` deltaP `29.8032` edge `0.7221` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3453` n `65` status `ready` deltaP `32.3992` edge `0.5831` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `6.3774` n `81` status `ready` deltaP `25.3666` edge `0.4243` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.8126` n `65` status `ready` deltaP `19.6341` edge `0.4879` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `3.5185` n `112` status `ready` deltaP `15.9844` edge `0.2664` maxDD `-4.047`
- `news_risk_high->index_24h` score `3.4271` n `65` status `ready` deltaP `24.4792` edge `0.1224` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.1005` n `65` status `ready` deltaP `10.5129` edge `0.1983` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.9498` n `65` status `ready` deltaP `32.5235` edge `0.0552` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.51` n `65` status `ready` deltaP `20.5769` edge `0.133` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.4965` n `65` status `ready` deltaP `9.8664` edge `0.1778` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0866` n `65` status `ready` deltaP `25.7669` edge `0.0171` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.7804` n `65` status `ready` deltaP `16.7918` edge `0.078` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.6317` n `112` status `ready` deltaP `27.5915` edge `0.0277` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.1781` n `65` status `ready` deltaP `3.6711` edge `0.1256` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.0041` n `123` status `ready` deltaP `15.895` edge `0.0061` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.8408` n `112` status `ready` deltaP `13.7412` edge `0.053` maxDD `-1.9634`
- `market_context_high->crypto_alt_4h` score `0.7682` n `112` status `ready` deltaP `3.027` edge `0.2162` maxDD `-7.1222`
- `market_context_high->equity_24h` score `0.7075` n `81` status `ready` deltaP `10.4939` edge `0.0023` maxDD `-0.3973`
- `market_context_high->metal_24h` score `0.538` n `81` status `ready` deltaP `23.1095` edge `0.0588` maxDD `-6.178`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
