# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T21:37:17.359053+00:00`
- Price records: `672`
- Market context records: `1978`
- Flow alert records: `7586`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7584`

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

- `market_context_high->crypto_alt_4h` score `7.3892` n `234` status `ready` deltaP `22.5649` edge `0.5798` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.8142` n `234` status `ready` deltaP `26.1987` edge `0.5178` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.4757` n `234` status `ready` deltaP `13.5906` edge `0.3181` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.1943` n `234` status `ready` deltaP `13.9058` edge `0.1996` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.6309` n `199` status `ready` deltaP `16.7627` edge `0.5562` maxDD `-35.8966`
- `market_context_high->metal_24h` score `1.6215` n `199` status `ready` deltaP `15.7543` edge `0.2727` maxDD `-12.7414`
- `market_context_high->equity_24h` score `1.0137` n `199` status `ready` deltaP `14.4326` edge `0.4781` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `0.9836` n `234` status `ready` deltaP `9.1023` edge `0.1199` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.7416` n `234` status `ready` deltaP `7.796` edge `0.1212` maxDD `-4.9097`
- `market_context_high->index_24h` score `0.4465` n `199` status `ready` deltaP `4.1922` edge `0.1321` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.0723` n `234` status `ready` deltaP `7.0682` edge `0.0678` maxDD `-3.7119`
- `market_context_high->crypto_major_24h` score `0.0589` n `199` status `ready` deltaP `18.9742` edge `0.737` maxDD `-62.3533`
- `market_context_high->equity_1h` score `-0.1581` n `234` status `ready` deltaP `4.5` edge `0.0362` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.1856` n `199` status `ready` deltaP `10.446` edge `0.0198` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6496` n `234` status `ready` deltaP `0.0359` edge `0.0088` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6678` n `234` status `ready` deltaP `-3.3126` edge `-0.0003` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.1531` n `234` status `ready` deltaP `-8.2968` edge `-0.0037` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.3455` n `234` status `ready` deltaP `2.7983` edge `0.0028` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.47` n `234` status `ready` deltaP `0.9584` edge `-0.0337` maxDD `-3.6151`
- `market_context_high->commodity_1h` score `-1.8853` n `234` status `ready` deltaP `2.0088` edge `0.0007` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
