# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T14:37:23.039721+00:00`
- Price records: `672`
- Market context records: `1947`
- Flow alert records: `7500`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7547`

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

- `market_context_high->crypto_alt_4h` score `7.0653` n `232` status `ready` deltaP `21.9516` edge `0.5569` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.4886` n `232` status `ready` deltaP `25.4882` edge `0.4954` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.4613` n `232` status `ready` deltaP `13.845` edge `0.3152` maxDD `-9.8581`
- `market_context_high->equity_4h` score `1.9554` n `232` status `ready` deltaP `13.8606` edge `0.18` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `0.8301` n `199` status `ready` deltaP `15.3929` edge `0.4986` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.709` n `234` status `ready` deltaP `7.755` edge `0.106` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.5341` n `234` status `ready` deltaP `7.0475` edge `0.1089` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.2258` n `199` status `ready` deltaP `11.9871` edge `0.1815` maxDD `-12.7414`
- `market_context_high->index_24h` score `0.1333` n `199` status `ready` deltaP `4.1922` edge `0.106` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.1248` n `232` status `ready` deltaP `8.3403` edge `0.0637` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.2241` n `234` status `ready` deltaP `4.5` edge `0.0307` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2687` n `199` status `ready` deltaP `9.9323` edge `0.0163` maxDD `-1.3925`
- `market_context_high->equity_24h` score `-0.5819` n `199` status `ready` deltaP `9.6381` edge `0.3771` maxDD `-33.1875`
- `market_context_high->index_1h` score `-0.6029` n `234` status `ready` deltaP `0.6347` edge `0.0087` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6421` n `234` status `ready` deltaP `-2.8635` edge `0.0` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0407` n `232` status `ready` deltaP `-6.3305` edge `-0.0024` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.1752` n `234` status `ready` deltaP `3.5468` edge `0.012` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.4963` n `234` status `ready` deltaP `0.5093` edge `-0.0329` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-1.7403` n `232` status `ready` deltaP `7.0887` edge `0.0769` maxDD `-12.5349`
- `market_context_high->crypto_major_24h` score `-1.9554` n `199` status `ready` deltaP `14.1797` edge `0.6011` maxDD `-62.3533`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
