# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T02:52:16.008114+00:00`
- Price records: `672`
- Market context records: `1905`
- Flow alert records: `7382`
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

- `market_context_high->crypto_alt_4h` score `7.5843` n `199` status `ready` deltaP `23.7284` edge `0.5883` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.0359` n `199` status `ready` deltaP `28.3245` edge `0.5221` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.8561` n `199` status `ready` deltaP `17.1958` edge `0.4091` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.4646` n `199` status `ready` deltaP `14.7345` edge `0.2166` maxDD `-5.0894`
- `market_context_high->metal_24h` score `2.0327` n `185` status `ready` deltaP `16.9041` edge `0.2993` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `1.5074` n `185` status `ready` deltaP `13.0292` edge `0.5708` maxDD `-35.8966`
- `market_context_high->index_24h` score `1.2614` n `185` status `ready` deltaP `8.7838` edge `0.1694` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `0.6537` n `199` status `ready` deltaP `7.2436` edge `0.1048` maxDD `-3.2225`
- `market_context_high->index_4h` score `0.4619` n `199` status `ready` deltaP `10.0931` edge `0.0801` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.4548` n `199` status `ready` deltaP `6.6553` edge `0.1049` maxDD `-4.9097`
- `market_context_high->fx_24h` score `0.2221` n `185` status `ready` deltaP `14.6275` edge `0.0259` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.0652` n `199` status `ready` deltaP `5.2862` edge `0.0387` maxDD `-2.6836`
- `market_context_high->equity_24h` score `-0.3446` n `185` status `ready` deltaP `8.6139` edge `0.4037` maxDD `-33.1875`
- `market_context_high->metal_1h` score `-0.5258` n `199` status `ready` deltaP `6.4311` edge `0.0233` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6207` n `199` status `ready` deltaP `-2.6036` edge `0.001` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6793` n `199` status `ready` deltaP `-0.4551` edge `0.0096` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.736` n `199` status `ready` deltaP `11.9331` edge `0.1283` maxDD `-12.5349`
- `market_context_high->crypto_major_24h` score `-0.7499` n `185` status `ready` deltaP `16.9632` edge `0.683` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-0.8605` n `199` status `ready` deltaP `-3.2096` edge `-0.0001` maxDD `-1.1056`
- `market_context_high->unknown_1h` score `-0.8779` n `199` status `ready` deltaP `2.2395` edge `0.0071` maxDD `-3.6151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
