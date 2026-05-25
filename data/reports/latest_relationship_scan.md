# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T23:07:16.154470+00:00`
- Price records: `672`
- Market context records: `1888`
- Flow alert records: `7335`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4510`

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

- `market_context_high->crypto_alt_4h` score `7.1475` n `199` status `ready` deltaP `22.8137` edge `0.558` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.7975` n `199` status `ready` deltaP `27.7148` edge `0.5063` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.3349` n `199` status `ready` deltaP `18.1104` edge `0.4429` maxDD `-9.8581`
- `market_context_high->metal_24h` score `3.0256` n `183` status `ready` deltaP `18.1552` edge `0.3737` maxDD `-12.7414`
- `market_context_high->equity_4h` score `2.343` n `199` status `ready` deltaP `14.4296` edge `0.2085` maxDD `-5.0894`
- `market_context_high->index_24h` score `1.7897` n `183` status `ready` deltaP `11.0372` edge `0.1984` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `1.6524` n `183` status `ready` deltaP `12.8756` edge `0.5839` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.5638` n `199` status `ready` deltaP `6.7945` edge `0.1003` maxDD `-3.2225`
- `market_context_high->index_4h` score `0.4243` n `199` status `ready` deltaP `9.7882` edge `0.079` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.3229` n `199` status `ready` deltaP `6.0565` edge `0.0979` maxDD `-4.9097`
- `market_context_high->fx_24h` score `0.2444` n `183` status `ready` deltaP `14.8309` edge `0.0264` maxDD `-1.3925`
- `market_context_high->equity_24h` score `0.0223` n `183` status `ready` deltaP `9.93` edge `0.4255` maxDD `-33.1875`
- `market_context_high->equity_1h` score `-0.1072` n `199` status `ready` deltaP `4.8371` edge `0.0382` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.3083` n `183` status `ready` deltaP `18.0584` edge `0.7125` maxDD `-62.3533`
- `market_context_high->metal_1h` score `-0.4876` n `199` status `ready` deltaP `6.8802` edge `0.0252` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-0.5624` n `199` status `ready` deltaP `2.8383` edge `0.0294` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-0.6206` n `199` status `ready` deltaP `12.0856` edge `0.1369` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.6529` n `199` status `ready` deltaP `-0.3054` edge `0.0108` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7259` n `199` status `ready` deltaP `-4.4` edge `-0.0005` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-0.9829` n `199` status `ready` deltaP `-5.0389` edge `-0.0036` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
