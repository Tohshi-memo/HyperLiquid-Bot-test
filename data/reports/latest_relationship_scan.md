# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T20:22:27.166500+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5036`

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

- `market_context_high->unknown_1h` score `97.622` n `97` status `ready` deltaP `-0.1605` edge `8.1777` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `78.7046` n `97` status `ready` deltaP `2.7564` edge `6.5715` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.3595` n `65` status `ready` deltaP `36.3626` edge `0.6412` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `8.6907` n `46` status `ready` deltaP `29.4082` edge `0.5934` maxDD `-4.5519`
- `market_context_high->crypto_alt_24h` score `8.2036` n `46` status `ready` deltaP `22.9695` edge `0.6578` maxDD `-8.1838`
- `news_risk_high->crypto_alt_4h` score `7.3493` n `65` status `ready` deltaP `23.9024` edge `0.5875` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `6.6341` n `65` status `ready` deltaP `20.4087` edge `0.4268` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.693` n `97` status `ready` deltaP `20.3436` edge `0.3258` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.8009` n `65` status `ready` deltaP `26.7361` edge `0.1385` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.7109` n `65` status `ready` deltaP `24.9976` edge `0.2036` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.2367` n `65` status `ready` deltaP `35.4198` edge `0.0598` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8238` n `65` status `ready` deltaP `11.8125` edge `0.1921` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.587` n `65` status `ready` deltaP `22.5845` edge `0.1066` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1956` n `65` status `ready` deltaP `26.9645` edge `0.0182` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `2.0853` n `97` status `ready` deltaP `14.7309` edge `0.1206` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.587` n `65` status `ready` deltaP `5.4675` edge `0.1477` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `1.4625` n `97` status `ready` deltaP `5.7581` edge `0.2624` maxDD `-7.6465`
- `market_context_high->fx_4h` score `1.3934` n `97` status `ready` deltaP `24.9733` edge `0.0253` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.3661` n `46` status `ready` deltaP `25.536` edge `0.1067` maxDD `-1.8102`
- `market_context_high->fx_1h` score `0.9372` n `97` status `ready` deltaP `14.7169` edge `0.0064` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
