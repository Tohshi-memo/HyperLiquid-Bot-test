# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-07T10:37:30.339863+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8718`

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

- `market_context_high->unknown_24h` score `82.2373` n `96` status `ready` deltaP `7.6389` edge `6.8402` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `36.0482` n `96` status `ready` deltaP `-4.3191` edge `3.0867` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.255` n `62` status `ready` deltaP `35.6855` edge `0.637` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.9793` n `62` status `ready` deltaP `23.0872` edge `0.5621` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.5778` n `62` status `ready` deltaP `25.8681` edge `0.1257` maxDD `0.0`
- `news_risk_high->index_4h` score `2.8869` n `62` status `ready` deltaP `32.3073` edge `0.0514` maxDD `-0.4296`
- `news_risk_high->equity_24h` score `2.7348` n `62` status `ready` deltaP `6.7428` edge `0.1929` maxDD `-0.1298`
- `market_context_high->crypto_major_4h` score `2.4696` n `96` status `ready` deltaP `14.5833` edge `0.205` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `2.231` n `62` status `ready` deltaP `8.5281` edge `0.1646` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0079` n `62` status `ready` deltaP `25.3236` edge `0.0135` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `2.0047` n `62` status `ready` deltaP `18.2337` edge `0.1053` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.4311` n `62` status `ready` deltaP `20.3334` edge `0.0895` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.155` n `62` status `ready` deltaP `3.3079` edge `0.1261` maxDD `-2.4854`
- `market_context_high->crypto_major_24h` score `1.0698` n `96` status `ready` deltaP `5.5556` edge `0.3975` maxDD `-16.7906`
- `market_context_high->fx_1h` score `0.9322` n `96` status `ready` deltaP `14.5958` edge `0.0046` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.5811` n `96` status `ready` deltaP `16.5143` edge `0.014` maxDD `-0.3868`
- `news_risk_high->commodity_24h` score `0.4067` n `62` status `ready` deltaP `26.1537` edge `0.0344` maxDD `-8.196`
- `market_context_high->crypto_major_1h` score `0.2356` n `96` status `ready` deltaP `10.6787` edge `0.0479` maxDD `-3.7778`
- `market_context_high->metal_24h` score `0.2346` n `96` status `ready` deltaP `14.7569` edge `0.0802` maxDD `-3.5466`
- `market_context_high->crypto_alt_4h` score `0.1763` n `96` status `ready` deltaP `-3.8618` edge `0.2128` maxDD `-7.1222`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
