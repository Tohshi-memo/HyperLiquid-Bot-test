# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T14:37:21.373436+00:00`
- Price records: `672`
- Market context records: `1851`
- Flow alert records: `7228`
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

- `market_context_high->crypto_alt_4h` score `6.5842` n `197` status `ready` deltaP `21.5172` edge `0.5197` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.0112` n `197` status `ready` deltaP `24.9652` edge `0.4591` maxDD `-4.9684`
- `market_context_high->metal_24h` score `5.8166` n `178` status `ready` deltaP `23.5975` edge `0.57` maxDD `-12.7414`
- `market_context_high->unknown_4h` score `4.4019` n `197` status `ready` deltaP `17.7626` edge `0.4508` maxDD `-9.8581`
- `market_context_high->index_24h` score `2.9187` n `178` status `ready` deltaP `15.2642` edge `0.2643` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `2.6252` n `178` status `ready` deltaP `14.3864` edge `0.6549` maxDD `-35.8966`
- `market_context_high->equity_4h` score `2.283` n `197` status `ready` deltaP `14.505` edge `0.203` maxDD `-5.0894`
- `market_context_high->equity_24h` score `0.8481` n `178` status `ready` deltaP `12.2425` edge `0.4789` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.5128` n `197` status `ready` deltaP `10.5492` edge `0.0813` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.2257` n `199` status `ready` deltaP `4.6987` edge `0.0861` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.2035` n `178` status `ready` deltaP `19.2065` edge `0.7475` maxDD `-62.3533`
- `market_context_high->fx_24h` score `0.0538` n `178` status `ready` deltaP `12.8239` edge `0.0239` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `0.0339` n `199` status `ready` deltaP `4.5595` edge `0.0838` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.1731` n `199` status `ready` deltaP `4.388` edge `0.0357` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.4425` n `199` status `ready` deltaP `3.5868` edge `0.0344` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.585` n `199` status `ready` deltaP `5.6826` edge `0.0207` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.6623` n `197` status `ready` deltaP `12.1348` edge `0.1331` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.6709` n `199` status `ready` deltaP `-0.4551` edge `0.0103` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7142` n `199` status `ready` deltaP `-4.1006` edge `-0.001` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0282` n `197` status `ready` deltaP `-5.641` edge `-0.0054` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
