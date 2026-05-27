# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T07:37:17.209725+00:00`
- Price records: `672`
- Market context records: `2021`
- Flow alert records: `7710`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9091`

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

- `market_context_high->crypto_major_4h` score `8.9279` n `205` status `ready` deltaP `30.7927` edge `0.5917` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.4282` n `205` status `ready` deltaP `24.5427` edge `0.6532` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `5.9193` n `205` status `ready` deltaP `18.689` edge `0.4436` maxDD `-2.6599`
- `market_context_high->equity_4h` score `2.9721` n `205` status `ready` deltaP `17.1036` edge `0.2431` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `1.4853` n `205` status `ready` deltaP `12.0286` edge `0.1422` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.3762` n `205` status `ready` deltaP `12.622` edge `0.0989` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.1958` n `205` status `ready` deltaP `9.6334` edge `0.1468` maxDD `-4.9097`
- `market_context_high->unknown_24h` score `0.3821` n `191` status `ready` deltaP `16.1524` edge `0.4562` maxDD `-35.8966`
- `market_context_high->equity_1h` score `0.1984` n `205` status `ready` deltaP `6.9104` edge `0.0493` maxDD `-2.6402`
- `market_context_high->equity_24h` score `0.1643` n `191` status `ready` deltaP `15.0658` edge `0.4031` maxDD `-33.1875`
- `market_context_high->unknown_1h` score `0.029` n `205` status `ready` deltaP `3.7462` edge `0.0494` maxDD `-3.0902`
- `market_context_high->index_24h` score `-0.0699` n `191` status `ready` deltaP `3.3924` edge `0.0944` maxDD `-4.1604`
- `market_context_high->fx_24h` score `-0.2437` n `191` status `ready` deltaP `12.9321` edge `0.025` maxDD `-2.1887`
- `market_context_high->metal_24h` score `-0.3168` n `191` status `ready` deltaP `11.5362` edge `0.1603` maxDD `-14.4218`
- `market_context_high->index_1h` score `-0.3289` n `205` status `ready` deltaP `2.2543` edge `0.0166` maxDD `-1.3898`
- `market_context_high->fx_1h` score `-0.8637` n `205` status `ready` deltaP `-1.4415` edge `0.0004` maxDD `-0.3548`
- `market_context_high->metal_1h` score `-0.9462` n `205` status `ready` deltaP `3.3591` edge `0.0175` maxDD `-5.166`
- `market_context_high->metal_4h` score `-1.4636` n `205` status `ready` deltaP `7.5` edge `0.0903` maxDD `-11.9812`
- `market_context_high->fx_4h` score `-1.5537` n `205` status `ready` deltaP `-5.9756` edge `-0.0015` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.8044` n `205` status `ready` deltaP `3.354` edge `0.0021` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
