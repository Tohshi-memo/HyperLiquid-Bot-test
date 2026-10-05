# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T07:52:32.817501+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6964`

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

- `market_context_high->unknown_1h` score `82.134` n `118` status `ready` deltaP `1.3143` edge `6.8772` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `56.5039` n `106` status `ready` deltaP `2.3125` edge `4.7244` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `10.6451` n `75` status `ready` deltaP `29.5069` edge `0.704` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3191` n `65` status `ready` deltaP `32.5516` edge `0.5799` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `7.1385` n `75` status `ready` deltaP `24.5764` edge `0.493` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.7996` n `65` status `ready` deltaP `19.7866` edge `0.4858` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.3433` n `65` status `ready` deltaP `23.6111` edge `0.1212` maxDD `0.0`
- `news_risk_high->equity_24h` score `3.3432` n `65` status `ready` deltaP `12.4226` edge `0.2058` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `3.0113` n `106` status `ready` deltaP `13.8288` edge `0.2385` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.8853` n `65` status `ready` deltaP `31.7613` edge `0.0549` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.5036` n `65` status `ready` deltaP `20.272` edge `0.1345` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.3993` n `65` status `ready` deltaP `9.567` edge `0.1717` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0471` n `65` status `ready` deltaP `25.3178` edge `0.0168` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.9258` n `65` status `ready` deltaP `17.8588` edge `0.083` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.2559` n `106` status `ready` deltaP `23.2685` edge `0.0252` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.0522` n `65` status `ready` deltaP `3.0723` edge `0.1191` maxDD `-2.4854`
- `market_context_high->crypto_major_1h` score `0.9833` n `118` status `ready` deltaP `11.2098` edge `0.0961` maxDD `-3.7778`
- `news_risk_high->commodity_24h` score `0.5718` n `65` status `ready` deltaP `25.0855` edge `0.1092` maxDD `-10.9169`
- `market_context_high->fx_1h` score `0.5102` n `118` status `ready` deltaP `13.3639` edge `0.0047` maxDD `-0.271`
- `market_context_high->equity_24h` score `0.2389` n `75` status `ready` deltaP `5.2431` edge `0.0052` maxDD `-0.6196`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
