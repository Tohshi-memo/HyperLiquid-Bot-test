# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T03:52:26.460963+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5248`

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

- `market_context_high->unknown_1h` score `110.6569` n `102` status `ready` deltaP `-0.5137` edge `9.2663` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `71.632` n `95` status `ready` deltaP `2.4743` edge `5.984` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `11.0805` n `59` status `ready` deltaP `29.9847` edge `0.7371` maxDD `-0.423`
- `market_context_high->crypto_alt_24h` score `9.5038` n `59` status `ready` deltaP `25.462` edge `0.6842` maxDD `-2.9571`
- `news_risk_high->crypto_major_4h` score `9.3081` n `65` status `ready` deltaP `32.3992` edge `0.58` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.0954` n `65` status `ready` deltaP `20.2439` edge `0.5074` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `4.2171` n `65` status `ready` deltaP `15.2004` edge `0.2601` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.2008` n `95` status `ready` deltaP `17.9862` edge `0.3005` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.3889` n `65` status `ready` deltaP `23.6111` edge `0.125` maxDD `0.0`
- `news_risk_high->index_4h` score `2.8865` n `65` status `ready` deltaP `31.7613` edge `0.055` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.7102` n `65` status `ready` deltaP `20.4245` edge `0.1507` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.5636` n `65` status `ready` deltaP `10.4652` edge `0.1794` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0998` n `65` status `ready` deltaP `25.9166` edge `0.0172` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.9947` n `65` status `ready` deltaP `18.3162` edge `0.0857` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `1.7895` n `102` status `ready` deltaP `12.9389` edge `0.1079` maxDD `-2.2692`
- `market_context_high->fx_4h` score `1.5293` n `95` status `ready` deltaP `26.0864` edge `0.0292` maxDD `-0.3868`
- `market_context_high->equity_24h` score `1.3527` n `59` status `ready` deltaP `4.405` edge `0.1036` maxDD `-0.6196`
- `market_context_high->fx_24h` score `1.3085` n `59` status `ready` deltaP `17.5142` edge `0.0844` maxDD `-1.703`
- `news_risk_high->crypto_alt_1h` score `1.3016` n `65` status `ready` deltaP `4.1202` edge `0.1329` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `0.9752` n `95` status `ready` deltaP `3.4018` edge `0.2375` maxDD `-7.6465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
