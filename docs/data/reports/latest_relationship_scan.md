# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T06:07:31.544020+00:00`
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

- `market_context_high->unknown_1h` score `93.9982` n `111` status `ready` deltaP `0.9967` edge `7.868` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `66.9783` n `99` status `ready` deltaP `3.0272` edge `5.5925` maxDD `-0.4928`
- `market_context_high->crypto_major_24h` score `10.3686` n `68` status `ready` deltaP `29.0951` edge `0.6837` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.2841` n `65` status `ready` deltaP `32.3992` edge `0.578` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `7.5131` n `68` status `ready` deltaP `24.1728` edge `0.5269` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.9226` n `65` status `ready` deltaP `20.2439` edge `0.493` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.6445` n `65` status `ready` deltaP `13.6379` edge `0.2228` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `3.4294` n `99` status `ready` deltaP `14.839` edge `0.2572` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.3517` n `65` status `ready` deltaP `23.6111` edge `0.1219` maxDD `0.0`
- `news_risk_high->index_4h` score `2.8853` n `65` status `ready` deltaP `31.7613` edge `0.0549` maxDD `-0.4296`
- `news_risk_high->equity_4h` score `2.5782` n `65` status `ready` deltaP `20.4245` edge `0.1397` maxDD `-2.881`
- `news_risk_high->crypto_major_1h` score `2.5444` n `65` status `ready` deltaP `10.4652` edge `0.1778` maxDD `-1.5096`
- `news_risk_high->index_1h` score `2.0986` n `65` status `ready` deltaP `25.9166` edge `0.0171` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.9645` n `65` status `ready` deltaP `18.1637` edge `0.0842` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.3677` n `99` status `ready` deltaP `24.3071` edge `0.0276` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.2644` n `65` status `ready` deltaP `4.1202` edge `0.1298` maxDD `-2.4854`
- `market_context_high->equity_24h` score `0.5863` n `68` status `ready` deltaP `5.0858` edge `0.0352` maxDD `-0.6196`
- `market_context_high->fx_1h` score `0.5477` n `111` status `ready` deltaP `13.9505` edge `0.0056` maxDD `-0.271`
- `news_risk_high->commodity_24h` score `0.4994` n `65` status `ready` deltaP `24.2174` edge `0.1057` maxDD `-10.9169`
- `market_context_high->crypto_major_1h` score `0.4672` n `111` status `ready` deltaP `10.0772` edge `0.0816` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
