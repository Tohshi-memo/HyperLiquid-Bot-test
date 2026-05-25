# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T22:52:19.598063+00:00`
- Price records: `672`
- Market context records: `1887`
- Flow alert records: `7332`
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

- `market_context_high->crypto_alt_4h` score `7.1319` n `199` status `ready` deltaP `22.8137` edge `0.5567` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.7951` n `199` status `ready` deltaP `27.7148` edge `0.5061` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.3349` n `199` status `ready` deltaP `18.1104` edge `0.4429` maxDD `-9.8581`
- `market_context_high->metal_24h` score `3.1115` n `183` status `ready` deltaP `18.3288` edge `0.3797` maxDD `-12.7414`
- `market_context_high->equity_4h` score `2.3514` n `199` status `ready` deltaP `14.4296` edge `0.2092` maxDD `-5.0894`
- `market_context_high->index_24h` score `1.83` n `183` status `ready` deltaP `11.2108` edge `0.2006` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `1.6572` n `183` status `ready` deltaP `12.8756` edge `0.5843` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.5482` n `199` status `ready` deltaP `6.6448` edge `0.1` maxDD `-3.2225`
- `market_context_high->index_4h` score `0.4327` n `199` status `ready` deltaP `9.7882` edge `0.0797` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.3001` n `199` status `ready` deltaP `5.9068` edge `0.097` maxDD `-4.9097`
- `market_context_high->fx_24h` score `0.2281` n `183` status `ready` deltaP `14.6573` edge `0.0262` maxDD `-1.3925`
- `market_context_high->equity_24h` score `0.0602` n `183` status `ready` deltaP `10.1036` edge `0.4275` maxDD `-33.1875`
- `market_context_high->equity_1h` score `-0.1263` n `199` status `ready` deltaP `4.6874` edge `0.0376` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.2752` n `183` status `ready` deltaP `18.232` edge `0.7141` maxDD `-62.3533`
- `market_context_high->metal_1h` score `-0.4884` n `199` status `ready` deltaP `6.8802` edge `0.0251` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-0.542` n `199` status `ready` deltaP `2.988` edge `0.0301` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-0.5868` n `199` status `ready` deltaP `12.238` edge `0.1387` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.6541` n `199` status `ready` deltaP `-0.3054` edge `0.0107` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7181` n `199` status `ready` deltaP `-4.2503` edge `-0.0005` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-0.9845` n `199` status `ready` deltaP `-5.0389` edge `-0.0038` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
