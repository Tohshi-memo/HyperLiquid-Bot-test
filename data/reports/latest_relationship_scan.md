# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T00:37:24.908288+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5392`

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

- `market_context_high->unknown_1h` score `101.1067` n `97` status `ready` deltaP `0.1389` edge `8.4661` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `96.053` n `97` status `ready` deltaP `2.7564` edge `8.0172` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `9.7336` n `65` status `ready` deltaP `33.9236` edge `0.6053` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `7.5644` n `48` status `ready` deltaP `26.9097` edge `0.5162` maxDD `-4.5519`
- `news_risk_high->crypto_alt_4h` score `6.7885` n `65` status `ready` deltaP `21.7683` edge `0.555` maxDD `-6.4195`
- `market_context_high->crypto_alt_24h` score `6.4607` n `48` status `ready` deltaP `20.8333` edge `0.5268` maxDD `-8.1838`
- `news_risk_high->equity_24h` score `5.1908` n `65` status `ready` deltaP `17.4573` edge `0.3262` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.0671` n `97` status `ready` deltaP `17.9046` edge `0.2899` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.5799` n `65` status `ready` deltaP `25.1736` edge `0.1305` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.1087` n `65` status `ready` deltaP `22.4062` edge `0.1707` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.0044` n `65` status `ready` deltaP `32.9808` edge `0.0567` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.7266` n `65` status `ready` deltaP `11.3634` edge `0.187` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.2251` n `65` status `ready` deltaP `20.1454` edge `0.0927` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1525` n `65` status `ready` deltaP `26.5154` edge `0.0176` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `1.9882` n `97` status `ready` deltaP `14.2818` edge `0.1155` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.5438` n `65` status `ready` deltaP `5.1681` edge `0.1461` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.4674` n `97` status `ready` deltaP `25.5831` edge `0.0274` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.4533` n `48` status `ready` deltaP `27.257` edge `0.1064` maxDD `-1.8102`
- `market_context_high->fx_1h` score `0.9791` n `97` status `ready` deltaP `15.166` edge `0.0069` maxDD `-0.113`
- `market_context_high->crypto_alt_4h` score `0.9017` n `97` status `ready` deltaP `3.624` edge `0.2299` maxDD `-7.6465`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
