# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T14:52:17.850899+00:00`
- Price records: `672`
- Market context records: `1852`
- Flow alert records: `7231`
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

- `market_context_high->crypto_alt_4h` score `6.55` n `198` status `ready` deltaP `21.48` edge `0.5171` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `5.9681` n `198` status `ready` deltaP `24.8922` edge `0.456` maxDD `-4.9684`
- `market_context_high->metal_24h` score `5.7331` n `178` status `ready` deltaP `23.4239` edge `0.5642` maxDD `-12.7414`
- `market_context_high->unknown_4h` score `4.3058` n `198` status `ready` deltaP `17.4011` edge `0.4452` maxDD `-9.8581`
- `market_context_high->index_24h` score `2.8628` n `178` status `ready` deltaP `15.0905` edge `0.2608` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `2.5885` n `178` status `ready` deltaP `14.2127` edge `0.653` maxDD `-35.8966`
- `market_context_high->equity_4h` score `2.2368` n `198` status `ready` deltaP `14.4678` edge `0.1994` maxDD `-5.0894`
- `market_context_high->equity_24h` score `0.7658` n `178` status `ready` deltaP `12.0689` edge `0.4732` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.4913` n `198` status `ready` deltaP `10.5507` edge `0.0795` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.1945` n `199` status `ready` deltaP `4.549` edge `0.0845` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.1867` n `178` status `ready` deltaP `19.2065` edge `0.7461` maxDD `-62.3533`
- `market_context_high->fx_24h` score `0.0574` n `178` status `ready` deltaP `12.8239` edge `0.0242` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `0.0027` n `199` status `ready` deltaP `4.4098` edge `0.0822` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.2055` n `199` status `ready` deltaP `4.2383` edge `0.034` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.4629` n `199` status `ready` deltaP `3.4371` edge `0.0337` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.599` n `199` status `ready` deltaP `5.5329` edge `0.0199` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.67` n `198` status `ready` deltaP `12.1875` edge `0.1321` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.6793` n `199` status `ready` deltaP `-0.4551` edge `0.0096` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.722` n `199` status `ready` deltaP `-4.2503` edge `-0.001` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0138` n `198` status `ready` deltaP `-5.3923` edge `-0.0052` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
