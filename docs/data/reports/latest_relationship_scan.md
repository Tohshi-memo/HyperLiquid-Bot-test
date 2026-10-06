# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T00:52:38.444520+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7928`

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

- `market_context_high->crypto_major_24h` score `10.5125` n `78` status `ready` deltaP `27.5046` edge `0.7063` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.0513` n `65` status `ready` deltaP `31.4249` edge `0.5651` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `5.6851` n `78` status `ready` deltaP `25.9979` edge `0.3624` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.4615` n `65` status `ready` deltaP `18.965` edge `0.4631` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.3533` n `65` status `ready` deltaP `9.6538` edge `0.2251` maxDD `-0.1344`
- `news_risk_high->index_24h` score `3.2388` n `65` status `ready` deltaP `22.6804` edge `0.1187` maxDD `0.0`
- `news_risk_high->index_4h` score `2.567` n `65` status `ready` deltaP `28.6524` edge `0.0491` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4474` n `65` status `ready` deltaP `9.2676` edge `0.1777` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.9979` n `65` status `ready` deltaP `24.8687` edge `0.0157` maxDD `-0.1997`
- `market_context_high->crypto_major_4h` score `1.9419` n `117` status `ready` deltaP `10.9121` edge `0.1855` maxDD `-4.047`
- `news_risk_high->equity_4h` score `1.9406` n `65` status `ready` deltaP `16.7146` edge `0.1113` maxDD `-2.881`
- `news_risk_high->metal_4h` score `1.7298` n `65` status `ready` deltaP `16.415` edge `0.0763` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.4693` n `117` status `ready` deltaP `25.8167` edge `0.026` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.2935` n `117` status `ready` deltaP `17.1292` edge `0.0636` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.2213` n `65` status `ready` deltaP `3.8208` edge `0.1282` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9947` n `117` status `ready` deltaP `15.6866` edge `0.0067` maxDD `-0.271`
- `market_context_high->metal_24h` score `0.7604` n `78` status `ready` deltaP `24.7026` edge `0.0703` maxDD `-5.6663`
- `market_context_high->commodity_1h` score `0.7573` n `117` status `ready` deltaP `12.3548` edge `0.0204` maxDD `-0.5059`
- `market_context_high->equity_24h` score `0.7524` n `78` status `ready` deltaP `13.2435` edge `-0.0195` maxDD `-0.1536`
- `news_risk_high->commodity_24h` score `0.252` n `65` status `ready` deltaP `25.4005` edge `0.0661` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
