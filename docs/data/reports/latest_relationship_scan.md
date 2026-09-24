# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T22:07:32.513940+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10665`

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

- `market_context_high->unknown_1h` score `84.6079` n `47` status `ready` deltaP `10.116` edge `6.9903` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `45.9821` n `47` status `ready` deltaP `30.4226` edge `3.6683` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.4684` n `47` status `ready` deltaP `24.782` edge `2.4118` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.3092` n `47` status `ready` deltaP `32.6795` edge `1.9268` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.9908` n `47` status `ready` deltaP `36.3253` edge `0.4367` maxDD `-0.3705`
- `news_risk_high->unknown_1h` score `6.5037` n `114` status `ready` deltaP `-4.0498` edge `0.5934` maxDD `-0.9543`
- `market_context_high->metal_24h` score `4.1832` n `47` status `ready` deltaP `35.4056` edge `0.1364` maxDD `-0.2401`
- `news_risk_high->crypto_alt_1h` score `3.4396` n `114` status `ready` deltaP `16.8847` edge `0.2231` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.8829` n `47` status `ready` deltaP `33.1117` edge `0.0349` maxDD `-0.2323`
- `news_risk_high->commodity_24h` score `2.7354` n `77` status `ready` deltaP `26.416` edge `0.095` maxDD `-1.7857`
- `news_risk_high->crypto_major_4h` score `2.5182` n `102` status `ready` deltaP `17.13` edge `0.3088` maxDD `-13.719`
- `news_risk_high->crypto_major_1h` score `2.4829` n `114` status `ready` deltaP `16.798` edge `0.1426` maxDD `-1.8141`
- `news_risk_high->crypto_alt_4h` score `2.36` n `102` status `ready` deltaP `8.5037` edge `0.3851` maxDD `-15.9436`
- `market_context_high->equity_4h` score `2.3285` n `47` status `ready` deltaP `16.6872` edge `0.1246` maxDD `-1.3444`
- `news_risk_high->metal_1h` score `1.5188` n `114` status `ready` deltaP `19.511` edge `0.025` maxDD `-0.6142`
- `news_risk_high->fx_4h` score `1.5076` n `102` status `ready` deltaP `22.4145` edge `0.0398` maxDD `-0.421`
- `market_context_high->index_1h` score `0.9739` n `47` status `ready` deltaP `14.7598` edge `0.0106` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9103` n `47` status `ready` deltaP `11.3167` edge `0.0407` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.6215` n `77` status `ready` deltaP `21.9765` edge `0.078` maxDD `-7.2536`
- `news_risk_high->fx_24h` score `0.5727` n `77` status `ready` deltaP `20.6011` edge `0.0992` maxDD `-1.7159`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
