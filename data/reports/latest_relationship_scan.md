# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T13:56:54.119131+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8598`

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

- `market_context_high->unknown_4h` score `36.3628` n `90` status `ready` deltaP `-5.8468` edge `3.1231` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.6811` n `62` status `ready` deltaP `36.7526` edge `0.6654` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.5028` n `62` status `ready` deltaP `24.3067` edge `0.5976` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.9048` n `62` status `ready` deltaP `28.125` edge `0.1379` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.5045` n `62` status `ready` deltaP `8.9998` edge `0.242` maxDD `-0.1298`
- `news_risk_high->index_4h` score `3.1115` n `62` status `ready` deltaP `34.289` edge `0.0569` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.5008` n `62` status `ready` deltaP `10.0251` edge `0.1771` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.3935` n `62` status `ready` deltaP `20.063` edge `0.1255` maxDD `-2.7837`
- `market_context_high->crypto_major_4h` score `2.1763` n `90` status `ready` deltaP `14.8171` edge `0.179` maxDD `-4.047`
- `news_risk_high->index_1h` score `2.0822` n `62` status `ready` deltaP `26.0721` edge `0.0147` maxDD `-0.1997`
- `market_context_high->crypto_major_24h` score `1.9838` n `90` status `ready` deltaP `7.0833` edge `0.5045` maxDD `-16.7906`
- `news_risk_high->metal_4h` score `1.464` n `62` status `ready` deltaP `20.4858` edge `0.0927` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.3481` n `62` status `ready` deltaP `4.0564` edge `0.1372` maxDD `-2.4854`
- `market_context_high->fx_4h` score `0.7932` n `90` status `ready` deltaP `18.7771` edge `0.0156` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.7394` n `90` status `ready` deltaP `12.3952` edge `0.0032` maxDD `-0.271`
- `market_context_high->metal_24h` score `0.715` n `90` status `ready` deltaP `18.7152` edge `0.1154` maxDD `-3.5466`
- `news_risk_high->metal_1h` score `0.2204` n `62` status `ready` deltaP `7.4995` edge `0.0102` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `0.1604` n `90` status `ready` deltaP `9.9534` edge `0.0431` maxDD `-3.7778`
- `news_risk_high->commodity_24h` score `0.0324` n `62` status `ready` deltaP `24.0704` edge `0.0003` maxDD `-8.196`
- `market_context_high->crypto_alt_4h` score `-0.0068` n `90` status `ready` deltaP `-4.7256` edge `0.2033` maxDD `-7.1222`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
