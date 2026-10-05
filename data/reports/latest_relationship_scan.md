# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T16:07:30.873351+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8072`

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

- `market_context_high->crypto_major_24h` score `11.1378` n `78` status `ready` deltaP `30.5956` edge `0.7378` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.6312` n `65` status `ready` deltaP `33.6187` edge `0.5988` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.0384` n `65` status `ready` deltaP `20.7012` edge `0.4996` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `5.4559` n `78` status `ready` deltaP `26.0283` edge `0.3431` maxDD `-2.9571`
- `news_risk_high->index_24h` score `3.4494` n `65` status `ready` deltaP `24.6528` edge `0.1231` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.1877` n `65` status `ready` deltaP `9.8184` edge `0.2102` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.8771` n `65` status `ready` deltaP `31.9137` edge `0.0532` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.584` n `65` status `ready` deltaP `10.1658` edge `0.1831` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.5218` n `117` status `ready` deltaP `13.1059` edge `0.2192` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.446` n `65` status `ready` deltaP `20.272` edge `0.1297` maxDD `-2.881`
- `news_risk_high->index_1h` score `2.0015` n `65` status `ready` deltaP `24.8687` edge `0.016` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.9057` n `65` status `ready` deltaP `18.1637` edge `0.0793` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.6068` n `117` status `ready` deltaP `27.4299` edge `0.0267` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.2357` n `65` status `ready` deltaP `3.8208` edge `0.1294` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.0462` n `117` status `ready` deltaP `16.2854` edge `0.007` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.9786` n `117` status `ready` deltaP `14.4674` edge `0.0551` maxDD `-1.6002`
- `market_context_high->metal_24h` score `0.9025` n `78` status `ready` deltaP `26.7896` edge `0.0746` maxDD `-5.6663`
- `market_context_high->commodity_1h` score `0.6519` n `117` status `ready` deltaP `11.3069` edge `0.0186` maxDD `-0.5059`
- `market_context_high->equity_24h` score `0.5868` n `78` status `ready` deltaP `13.4081` edge `-0.0344` maxDD `-0.1536`
- `news_risk_high->commodity_24h` score `0.3701` n `65` status `ready` deltaP `24.9119` edge `0.0845` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
