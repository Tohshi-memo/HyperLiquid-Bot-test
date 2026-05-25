# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T21:07:14.310887+00:00`
- Price records: `672`
- Market context records: `1879`
- Flow alert records: `7309`
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

- `market_context_high->crypto_alt_4h` score `6.8933` n `199` status `ready` deltaP `22.0515` edge `0.5419` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.6661` n `199` status `ready` deltaP `27.2575` edge `0.4984` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.3385` n `199` status `ready` deltaP `18.1104` edge `0.4432` maxDD `-9.8581`
- `market_context_high->metal_24h` score `3.763` n `181` status `ready` deltaP `19.3629` edge `0.4271` maxDD `-12.7414`
- `market_context_high->equity_4h` score `2.3899` n `199` status `ready` deltaP `14.582` edge `0.2114` maxDD `-5.0894`
- `market_context_high->index_24h` score `2.1239` n `181` status `ready` deltaP `12.2448` edge `0.2182` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `1.8282` n `181` status `ready` deltaP `12.7187` edge `0.5996` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.4835` n `199` status `ready` deltaP `6.3454` edge `0.0966` maxDD `-3.2225`
- `market_context_high->index_4h` score `0.4701` n `199` status `ready` deltaP `9.9407` edge `0.0818` maxDD `-3.7119`
- `market_context_high->equity_24h` score `0.298` n `181` status `ready` deltaP `10.857` edge `0.4423` maxDD `-33.1875`
- `market_context_high->fx_24h` score `0.2031` n `181` status `ready` deltaP `14.3598` edge `0.0261` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `0.1802` n `199` status `ready` deltaP `5.4577` edge `0.09` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `0.0692` n `181` status `ready` deltaP `18.9371` edge `0.7381` maxDD `-62.3533`
- `market_context_high->equity_1h` score `-0.2222` n `199` status `ready` deltaP `3.9389` edge `0.0346` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.4689` n `199` status `ready` deltaP `3.4371` edge `0.0332` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-0.5142` n `199` status `ready` deltaP `12.6953` edge `0.1417` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.5406` n `199` status `ready` deltaP `6.2814` edge `0.0224` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6932` n `199` status `ready` deltaP `-3.8012` edge `-0.0003` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.7236` n `199` status `ready` deltaP `-0.9042` edge `0.0089` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-0.9915` n `199` status `ready` deltaP `-5.0389` edge `-0.0047` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
