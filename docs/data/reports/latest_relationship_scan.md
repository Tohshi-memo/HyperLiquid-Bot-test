# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T06:52:26.867266+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6958`

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

- `market_context_high->unknown_1h` score `88.8682` n `114` status `ready` deltaP `1.4471` edge `7.4375` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `62.3232` n `102` status `ready` deltaP `3.4134` edge `5.202` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `10.3835` n `71` status `ready` deltaP `29.2815` edge `0.6837` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3179` n `65` status `ready` deltaP `32.5516` edge `0.5798` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `7.1848` n `71` status `ready` deltaP `24.1491` edge `0.4997` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.8914` n `65` status `ready` deltaP `20.2439` edge `0.4904` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.4864` n `65` status `ready` deltaP `13.117` edge `0.2131` maxDD `-0.1344`
- `news_risk_high->index_24h` score `3.3457` n `65` status `ready` deltaP `23.6111` edge `0.1214` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.9008` n `102` status `ready` deltaP `12.7929` edge `0.2362` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.8853` n `65` status `ready` deltaP `31.7613` edge `0.0549` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.5314` n `65` status `ready` deltaP `20.4245` edge `0.1358` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.4772` n `65` status `ready` deltaP `10.0161` edge `0.1752` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0722` n `65` status `ready` deltaP `25.6172` edge `0.0169` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.9464` n `65` status `ready` deltaP `18.0113` edge `0.0837` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.1769` n `65` status `ready` deltaP `3.6711` edge `0.1255` maxDD `-2.4854`
- `market_context_high->crypto_major_1h` score `0.8364` n `114` status `ready` deltaP `10.529` edge `0.0884` maxDD `-3.7778`
- `market_context_high->fx_4h` score `0.7745` n `102` status `ready` deltaP `22.4354` edge `0.0254` maxDD `-0.3868`
- `news_risk_high->commodity_24h` score `0.5397` n `65` status `ready` deltaP `24.7383` edge `0.1074` maxDD `-10.9169`
- `market_context_high->fx_1h` score `0.4593` n `114` status `ready` deltaP `12.3857` edge `0.0047` maxDD `-0.271`
- `market_context_high->equity_24h` score `0.3988` n `71` status `ready` deltaP `5.1863` edge `0.0189` maxDD `-0.6196`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
