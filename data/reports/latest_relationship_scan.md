# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T19:52:31.026578+00:00`
- Price records: `672`
- Market context records: `5176`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5650`

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

- `market_context_high->unknown_24h` score `25.7088` n `74` status `ready` deltaP `32.4418` edge `1.9451` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `10.3262` n `74` status `ready` deltaP `22.9777` edge `1.0735` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `9.0191` n `74` status `ready` deltaP `24.2539` edge `0.9286` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `6.1088` n `149` status `ready` deltaP `20.5035` edge `0.4746` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.0507` n `149` status `ready` deltaP `15.5262` edge `0.4773` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.7561` n `149` status `ready` deltaP `14.4889` edge `0.529` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.7151` n `155` status `ready` deltaP `10.0357` edge `0.2235` maxDD `-2.7986`
- `market_context_high->equity_4h` score `1.4372` n `149` status `ready` deltaP `9.2445` edge `0.222` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.5696` n `155` status `ready` deltaP `4.5036` edge `0.1136` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.5668` n `155` status `ready` deltaP `6.7027` edge `0.1271` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.3723` n `155` status `ready` deltaP `8.6633` edge `0.0698` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0502` n `155` status `ready` deltaP `6.0827` edge `0.014` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0436` n `155` status `ready` deltaP `5.309` edge `0.0182` maxDD `-2.0682`
- `market_context_high->fx_24h` score `-0.1166` n `74` status `ready` deltaP `9.4079` edge `0.0171` maxDD `-0.8294`
- `market_context_high->fx_1h` score `-0.2246` n `155` status `ready` deltaP `2.4078` edge `0.0004` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.386` n `149` status `ready` deltaP `6.2213` edge `0.0381` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.578` n `149` status `ready` deltaP `3.3885` edge `0.0067` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6125` n `155` status `ready` deltaP `0.4259` edge `-0.0005` maxDD `-2.4692`
- `market_context_high->commodity_24h` score `-0.7786` n `74` status `ready` deltaP `11.036` edge `0.0727` maxDD `-11.3537`
- `market_context_high->metal_24h` score `-0.915` n `74` status `ready` deltaP `-4.7204` edge `0.1592` maxDD `-10.9367`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
