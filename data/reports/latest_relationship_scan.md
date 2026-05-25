# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T19:07:19.861134+00:00`
- Price records: `672`
- Market context records: `1870`
- Flow alert records: `7284`
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

- `market_context_high->crypto_alt_4h` score `6.6369` n `199` status `ready` deltaP `21.4418` edge `0.5246` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.3526` n `199` status `ready` deltaP `26.038` edge `0.4804` maxDD `-4.9684`
- `market_context_high->metal_24h` score `4.2958` n `178` status `ready` deltaP `20.4725` edge `0.4641` maxDD `-12.7414`
- `market_context_high->unknown_4h` score `4.2527` n `199` status `ready` deltaP `17.6531` edge `0.4391` maxDD `-9.8581`
- `market_context_high->index_24h` score `2.3433` n `178` status `ready` deltaP `13.0072` edge `0.2314` maxDD `-4.1604`
- `market_context_high->equity_4h` score `2.2346` n `199` status `ready` deltaP `14.1247` edge `0.2015` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.9852` n `178` status `ready` deltaP `12.4766` edge `0.6143` maxDD `-35.8966`
- `market_context_high->index_4h` score `0.4329` n `199` status `ready` deltaP `9.9407` edge `0.0787` maxDD `-3.7119`
- `market_context_high->equity_24h` score `0.4183` n `178` status `ready` deltaP `10.68` edge `0.4535` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `0.3204` n `199` status `ready` deltaP `5.4472` edge `0.089` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.2911` n `178` status `ready` deltaP `19.2065` edge `0.7548` maxDD `-62.3533`
- `market_context_high->fx_24h` score `0.2112` n `178` status `ready` deltaP `14.3864` edge `0.0266` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `0.0363` n `199` status `ready` deltaP `4.8589` edge `0.082` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.3098` n `199` status `ready` deltaP `3.4898` edge `0.0303` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.566` n `199` status `ready` deltaP `2.8383` edge `0.0291` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.5811` n `199` status `ready` deltaP `5.8323` edge `0.0202` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.6468` n `199` status `ready` deltaP `12.238` edge `0.1337` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.6924` n `199` status `ready` deltaP `-3.8012` edge `-0.0002` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.7871` n `199` status `ready` deltaP `-1.3533` edge `0.0066` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-0.9915` n `199` status `ready` deltaP `-5.0389` edge `-0.0047` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
