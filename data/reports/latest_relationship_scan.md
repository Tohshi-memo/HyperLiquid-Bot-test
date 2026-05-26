# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T06:22:23.319665+00:00`
- Price records: `672`
- Market context records: `1920`
- Flow alert records: `7425`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6012`

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

- `market_context_high->crypto_alt_4h` score `7.6997` n `199` status `ready` deltaP `23.8808` edge `0.5969` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.2267` n `199` status `ready` deltaP `29.2392` edge `0.5319` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.0167` n `199` status `ready` deltaP `17.958` edge `0.4174` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.6569` n `199` status `ready` deltaP `15.954` edge `0.2245` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `0.9844` n `192` status `ready` deltaP `13.5416` edge `0.5238` maxDD `-35.8966`
- `market_context_high->metal_24h` score `0.8567` n `192` status `ready` deltaP `13.8889` edge `0.2214` maxDD `-12.7414`
- `market_context_high->crypto_major_1h` score `0.85` n `211` status `ready` deltaP `8.992` edge `0.1095` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.6878` n `211` status `ready` deltaP `8.1434` edge `0.1144` maxDD `-4.9097`
- `market_context_high->index_24h` score `0.5582` n `192` status `ready` deltaP `5.9028` edge `0.13` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.5103` n `199` status `ready` deltaP `10.398` edge `0.0821` maxDD `-3.7119`
- `market_context_high->fx_24h` score `-0.0636` n `192` status `ready` deltaP `11.8056` edge `0.0209` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1026` n `211` status `ready` deltaP `5.1487` edge `0.0365` maxDD `-2.6836`
- `market_context_high->metal_1h` score `-0.6051` n `211` status `ready` deltaP `5.4751` edge `0.0195` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.6165` n `211` status `ready` deltaP `0.4349` edge `0.0089` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6562` n `211` status `ready` deltaP `-3.2551` edge `0.0008` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-0.6628` n `199` status `ready` deltaP `11.9331` edge `0.1344` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-0.7869` n `199` status `ready` deltaP `-1.9901` edge `0.0012` maxDD `-1.1056`
- `market_context_high->equity_24h` score `-1.0228` n `192` status `ready` deltaP `7.2917` edge `0.356` maxDD `-33.1875`
- `market_context_high->unknown_1h` score `-1.1724` n `211` status `ready` deltaP `1.7077` edge `-0.0139` maxDD `-3.6151`
- `market_context_high->crypto_major_24h` score `-1.9055` n `192` status `ready` deltaP `13.8889` edge `0.6072` maxDD `-62.3533`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
