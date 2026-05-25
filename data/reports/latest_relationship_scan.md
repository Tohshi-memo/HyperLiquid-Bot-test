# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T15:52:17.023255+00:00`
- Price records: `672`
- Market context records: `1856`
- Flow alert records: `7243`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4500`

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

- `market_context_high->crypto_alt_4h` score `6.4999` n `199` status `ready` deltaP `21.2893` edge `0.5142` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `5.9368` n `199` status `ready` deltaP `24.666` edge `0.4549` maxDD `-4.9684`
- `market_context_high->metal_24h` score `5.3955` n `178` status `ready` deltaP `22.7294` edge `0.5407` maxDD `-12.7414`
- `market_context_high->unknown_4h` score `4.1762` n `199` status `ready` deltaP `16.8909` edge `0.4378` maxDD `-9.8581`
- `market_context_high->index_24h` score `2.668` n `178` status `ready` deltaP `14.3961` edge `0.2492` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `2.413` n `178` status `ready` deltaP `13.5183` edge `0.643` maxDD `-35.8966`
- `market_context_high->equity_4h` score `2.13` n `199` status `ready` deltaP `13.9723` edge `0.1938` maxDD `-5.0894`
- `market_context_high->equity_24h` score `0.541` n `178` status `ready` deltaP `11.3744` edge `0.4591` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.4139` n `199` status `ready` deltaP `10.0931` edge `0.0761` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.2161` n `199` status `ready` deltaP `4.6987` edge `0.0853` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.1735` n `178` status `ready` deltaP `19.2065` edge `0.745` maxDD `-62.3533`
- `market_context_high->fx_24h` score `0.1171` n `178` status `ready` deltaP `13.3447` edge `0.0257` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `0.0003` n `199` status `ready` deltaP `4.4098` edge `0.082` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.2247` n `199` status `ready` deltaP `4.0886` edge `0.0334` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.5252` n `199` status `ready` deltaP `3.1377` edge `0.0305` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.6013` n `199` status `ready` deltaP `5.5329` edge `0.0196` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.6564` n `199` status `ready` deltaP `12.238` edge `0.1329` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.6916` n `199` status `ready` deltaP `-3.8012` edge `-0.0001` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.7116` n `199` status `ready` deltaP `-0.7545` edge `0.0089` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-0.9891` n `199` status `ready` deltaP `-5.0389` edge `-0.0044` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
