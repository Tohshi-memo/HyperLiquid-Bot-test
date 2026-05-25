# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T12:22:18.480692+00:00`
- Price records: `672`
- Market context records: `1841`
- Flow alert records: `7200`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4489`

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

- `market_context_high->crypto_alt_4h` score `6.8574` n `196` status `ready` deltaP `22.7725` edge `0.5341` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.3784` n `178` status `ready` deltaP `25.16` edge `0.6064` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.2857` n `196` status `ready` deltaP `25.952` edge `0.4754` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.4147` n `196` status `ready` deltaP `17.5181` edge `0.4535` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.3041` n `178` status `ready` deltaP `16.8267` edge `0.286` maxDD `-4.1604`
- `market_context_high->equity_4h` score `2.7182` n `196` status `ready` deltaP `15.7603` edge `0.2309` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.7099` n `178` status `ready` deltaP `14.56` edge `0.6608` maxDD `-35.8966`
- `market_context_high->equity_24h` score `1.4891` n `178` status `ready` deltaP `13.805` edge `0.5219` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.7517` n `196` status `ready` deltaP `11.7658` edge `0.0931` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.3912` n `199` status `ready` deltaP `5.4472` edge `0.0949` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.3009` n `178` status `ready` deltaP `19.5537` edge `0.7533` maxDD `-62.3533`
- `market_context_high->crypto_alt_1h` score `0.2329` n `199` status `ready` deltaP `5.6074` edge `0.0934` maxDD `-4.9097`
- `market_context_high->fx_24h` score `-0.0413` n `178` status `ready` deltaP `12.1294` edge `0.0206` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.0591` n `199` status `ready` deltaP `4.5377` edge `0.0442` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.5013` n `199` status `ready` deltaP `3.2874` edge `0.0315` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-0.546` n `196` status `ready` deltaP `13.0476` edge `0.1367` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.5795` n `199` status `ready` deltaP `5.5329` edge `0.0224` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.6038` n `199` status `ready` deltaP `-0.006` edge `0.0129` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7383` n `199` status `ready` deltaP `-4.5497` edge `-0.0011` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-1.0593` n `196` status `ready` deltaP `-5.8922` edge `-0.0077` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
