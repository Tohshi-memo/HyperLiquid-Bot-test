# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T05:37:27.000085+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7022`

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

- `market_context_high->unknown_1h` score `97.7086` n `109` status `ready` deltaP `0.6826` edge `8.1793` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `70.313` n `97` status `ready` deltaP `2.7564` edge `5.8722` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `10.4696` n `66` status `ready` deltaP `29.3087` edge `0.6907` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.2745` n `65` status `ready` deltaP `32.3992` edge `0.5772` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `7.8327` n `66` status `ready` deltaP `24.1635` edge `0.5536` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.9538` n `65` status `ready` deltaP `20.2439` edge `0.4956` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.7706` n `65` status `ready` deltaP `13.9851` edge `0.231` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `3.7567` n `97` status `ready` deltaP `16.3802` edge `0.2742` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.3601` n `65` status `ready` deltaP `23.6111` edge `0.1226` maxDD `0.0`
- `news_risk_high->index_4h` score `2.8853` n `65` status `ready` deltaP `31.7613` edge `0.0549` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.6046` n `65` status `ready` deltaP `20.4245` edge `0.1419` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.5636` n `65` status `ready` deltaP `10.6149` edge `0.1784` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.1249` n `65` status `ready` deltaP `26.216` edge `0.0173` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.9645` n `65` status `ready` deltaP `18.1637` edge `0.0842` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.4907` n `97` status `ready` deltaP `25.6192` edge `0.0291` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.292` n `65` status `ready` deltaP `4.2699` edge `0.1311` maxDD `-2.4854`
- `market_context_high->equity_24h` score `0.7501` n `66` status `ready` deltaP `4.9874` edge `0.0495` maxDD `-0.6196`
- `market_context_high->fx_1h` score `0.5598` n `109` status `ready` deltaP `14.124` edge `0.006` maxDD `-0.271`
- `market_context_high->crypto_alt_4h` score `0.505` n `97` status `ready` deltaP `2.0996` edge `0.207` maxDD `-7.6465`
- `news_risk_high->commodity_24h` score `0.4696` n `65` status `ready` deltaP `23.8702` edge `0.1042` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
