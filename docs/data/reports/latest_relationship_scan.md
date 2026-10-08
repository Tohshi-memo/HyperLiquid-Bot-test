# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T00:07:29.288861+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8574`

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

- `market_context_high->unknown_4h` score `38.4814` n `90` status `ready` deltaP `-4.4749` edge `3.2905` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.9415` n `62` status `ready` deltaP `38.5818` edge `0.6749` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.0071` n `62` status `ready` deltaP `22.325` edge `0.5695` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `5.5089` n `62` status `ready` deltaP `13.4446` edge `0.3794` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.557` n `62` status `ready` deltaP `32.872` edge `0.1606` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `3.9772` n `90` status `ready` deltaP `10.0461` edge `0.7403` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.8328` n `62` status `ready` deltaP `31.2402` edge `0.054` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4635` n `62` status `ready` deltaP `10.1748` edge `0.173` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.4367` n `90` status `ready` deltaP `16.6463` edge `0.1885` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.0346` n `62` status `ready` deltaP `17.1666` edge `0.1149` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.8989` n `62` status `ready` deltaP `23.9763` edge `0.0134` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.4912` n `62` status `ready` deltaP `21.248` edge `0.0911` maxDD `-0.993`
- `news_risk_high->unknown_4h` score `1.261` n `62` status `ready` deltaP `-7.4499` edge `0.2793` maxDD `-5.6309`
- `market_context_high->metal_24h` score `1.105` n `90` status `ready` deltaP `20.0807` edge `0.1563` maxDD `-3.5466`
- `news_risk_high->crypto_alt_1h` score `1.0471` n `62` status `ready` deltaP `2.7091` edge `0.1211` maxDD `-2.4854`
- `market_context_high->equity_24h` score `1.0043` n `90` status `ready` deltaP `11.0073` edge `0.0532` maxDD `-1.0977`
- `market_context_high->fx_4h` score `0.9454` n `90` status `ready` deltaP `20.4539` edge `0.0171` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.6675` n `90` status `ready` deltaP `11.497` edge `0.0032` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1362` n `90` status `ready` deltaP `10.1031` edge `0.039` maxDD `-3.7778`
- `news_risk_high->metal_1h` score `0.1018` n `62` status `ready` deltaP `6.3019` edge `0.0083` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
