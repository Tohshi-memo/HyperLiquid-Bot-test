# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T01:07:21.358228+00:00`
- Price records: `672`
- Market context records: `2094`
- Flow alert records: `7921`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9146`

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

- `market_context_high->crypto_alt_4h` score `10.5459` n `187` status `ready` deltaP `30.8237` edge `0.7878` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `10.4443` n `187` status `ready` deltaP `36.9383` edge `0.6771` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.6779` n `187` status `ready` deltaP `24.0316` edge `0.4712` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.142` n `187` status `ready` deltaP `22.142` edge `0.307` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `3.6733` n `186` status `ready` deltaP `22.2979` edge `0.6895` maxDD `-35.8966`
- `market_context_high->index_4h` score `2.5228` n `187` status `ready` deltaP `18.5536` edge `0.1549` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `2.3013` n `187` status `ready` deltaP `16.2885` edge `0.1818` maxDD `-3.2225`
- `market_context_high->index_24h` score `2.122` n `186` status `ready` deltaP `11.2308` edge `0.2248` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `2.0635` n `187` status `ready` deltaP `13.4442` edge `0.1937` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.763` n `186` status `ready` deltaP `22.3593` edge `0.4877` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.8548` n `187` status `ready` deltaP `11.0499` edge `0.0764` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.7061` n `187` status `ready` deltaP `6.3002` edge `0.0888` maxDD `-3.0902`
- `market_context_high->index_1h` score `0.1734` n `187` status `ready` deltaP `6.3435` edge `0.0312` maxDD `-1.3898`
- `market_context_high->crypto_major_24h` score `0.11` n `186` status `ready` deltaP `21.1277` edge `0.7269` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.118` n `186` status `ready` deltaP `14.8752` edge `0.0303` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.1719` n `187` status `ready` deltaP `13.0918` edge `0.1529` maxDD `-11.3602`
- `market_context_high->metal_1h` score `-0.2534` n `187` status `ready` deltaP `6.8342` edge `0.0354` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8416` n `187` status `ready` deltaP `-1.3153` edge `0.0014` maxDD `-0.3548`
- `market_context_high->metal_24h` score `-1.2364` n `186` status `ready` deltaP `10.6783` edge `0.2159` maxDD `-23.2095`
- `market_context_high->fx_4h` score `-1.4326` n `187` status `ready` deltaP `-4.6857` edge `0.0` maxDD `-1.0513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
