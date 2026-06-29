# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T11:37:28.999081+00:00`
- Price records: `672`
- Market context records: `5140`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5596`

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

- `market_context_high->unknown_24h` score `27.1905` n `66` status `ready` deltaP `31.2342` edge `2.0919` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `7.0001` n `123` status `ready` deltaP `19.6138` edge `0.5548` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `6.7076` n `135` status `ready` deltaP `9.8425` edge `0.5575` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `4.9684` n `123` status `ready` deltaP `15.1423` edge `0.473` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.5925` n `123` status `ready` deltaP `13.0082` edge `0.4419` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `1.159` n `66` status `ready` deltaP `17.4242` edge `0.1335` maxDD `-4.0853`
- `market_context_high->equity_4h` score `0.9631` n `123` status `ready` deltaP `9.6037` edge `0.1801` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.7247` n `135` status `ready` deltaP `5.2872` edge `0.1213` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.6854` n `135` status `ready` deltaP `7.6902` edge `0.1304` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.6396` n `135` status `ready` deltaP `7.2023` edge `0.0646` maxDD `-2.745`
- `market_context_high->crypto_alt_24h` score `0.4486` n `66` status `ready` deltaP `17.4558` edge `0.5863` maxDD `-46.2794`
- `market_context_high->crypto_major_24h` score `0.0573` n `66` status `ready` deltaP `15.6881` edge `0.5841` maxDD `-48.0465`
- `market_context_high->index_1h` score `0.0158` n `135` status `ready` deltaP `5.5633` edge `0.0146` maxDD `-1.0296`
- `market_context_high->metal_24h` score `-0.0552` n `66` status `ready` deltaP `-0.7892` edge `0.1848` maxDD `-10.0641`
- `market_context_high->metal_1h` score `-0.0991` n `135` status `ready` deltaP `4.42` edge `0.0144` maxDD `-1.8592`
- `market_context_high->index_4h` score `-0.305` n `123` status `ready` deltaP `7.3679` edge `0.0372` maxDD `-2.9391`
- `market_context_high->fx_24h` score `-0.5129` n `66` status `ready` deltaP `3.63` edge `-0.0001` maxDD `-0.8549`
- `market_context_high->commodity_1h` score `-0.5217` n `135` status `ready` deltaP `1.4183` edge `0.0006` maxDD `-2.155`
- `market_context_high->fx_1h` score `-0.6235` n `135` status `ready` deltaP `-2.1357` edge `-0.0016` maxDD `-0.7944`
- `market_context_high->metal_4h` score `-0.8094` n `123` status `ready` deltaP `1.3211` edge `0.0437` maxDD `-5.8359`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
